# -*- coding: utf-8 -*-
"""
Pipeline de /sync_metrics — ingesta semanal de los CSV agregados que el PM exporta de la
base y medición de las dos North Star Metrics de Bind PSP.

Uso (desde cualquier cwd):
    python pipeline.py inspect            # lee raw/ y reporta, sin escribir NADA
    python pipeline.py ingest             # mergea raw/ contra una COPIA DE TRABAJO del store
    python pipeline.py analyze [SEMANA]   # calcula NSM + palancas + hallazgos, texto
    python pipeline.py palancas [SEMANA]  # mismo cálculo que analyze, en JSON — insumo
                                           # del renderer de email/reporte (render_email.py)

CONTRATO DE ESCRITURA (pipeline multi-PM, 2026-08-15) — este script YA NO escribe el canon
directo. `2_areas/`/`3_recursos/` son espejo read-only en este install; el único que las
escribe es `/context_merge`, sobre el repo compartido CEREBRO_CORE. Por eso:

  - INPUT: el store real vive en `wiki/3_recursos/datos/datos_metricas_semanales/*.csv`
    (espejo). `ingest` arranca SEMBRANDO una copia de trabajo en
    `wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/` a partir de ese espejo — o, si
    ya hay un item `tipo: dato` con `destino_propuesto: 3_recursos/datos/datos_metricas_semanales`
    todavía sin mergear en `contexto_vivo/`, a partir de ESE (gana el pendiente más nuevo
    sobre el espejo desactualizado — ver CLAUDE.md, "Items tipo: dato"). Verificá esto a
    mano antes de correr `ingest` si sabés que hubo una corrida sin mergear.
  - Todo el pipeline (merge, `semanas.csv`, `log_metricas_semanales.md`) sigue leyendo y
    escribiendo `STORE`/`LOG_MD` exactamente igual que antes — solo que esas constantes
    ahora apuntan a la copia de trabajo, no al canon.
  - OUTPUT: al terminar `ingest`, la skill (no este script) empaqueta el contenido de
    `_staging_sync_metrics/` como UN item `tipo: dato` en `contexto_vivo/`, con
    `destino_propuesto: 3_recursos/datos/datos_metricas_semanales` — `/context_merge` lo
    aplica por copia byte a byte, sin redactarlo. Ver SKILL.md, Paso de cierre.

Los CSV del store son agregados puros (cantidades y volúmenes por dimensión de negocio),
sin una sola fila de PII — por eso viven en la wiki y se versionan en git, a diferencia de
los datasets crudos regulados por `datasets_locales/` (gitignored).

Detección de formato: por FIRMA DE HEADER, nunca por nombre de archivo. El PM puede
renombrar o partir los exports en N archivos (la query de operaciones/transacciones no
siempre entra en una sola corrida) y el pipeline los concatena igual.

Excepción (usuario, 2026-08-11): su herramienta de export nunca incluye la fila de header.
Para ese caso hay un fallback posicional (COLUMN_ORDER_HEADERLESS + _sniff_headerless) que
asume el orden exacto de columnas de las queries de SKILL.md — y, solo para desambiguar
cuentas/comercios (misma forma exacta), sí mira el nombre de archivo. Cada asunción se
imprime como [ASUMIDO] en inspect/ingest para que quede a la vista.
"""
import csv
import hashlib
import io
import json
import shutil
import statistics
import sys
import unicodedata
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

try:  # la consola de Windows no es UTF-8 y se come los acentos del reporte
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:  # pragma: no cover
    pass

# --- Paths ------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parents[3]  # .claude/skills/sync_metrics/scripts -> repo root
RAW_DIR = REPO / "raw"

# Espejo read-only del canon (input) -- NUNCA se escribe acá.
MIRROR_STORE = REPO / "wiki" / "3_recursos" / "datos" / "datos_metricas_semanales"
MIRROR_LOG_MD = REPO / "wiki" / "3_recursos" / "datos" / "log_metricas_semanales.md"

# Copia de trabajo (donde el pipeline realmente lee/escribe) -- se siembra desde el
# espejo (o desde un item tipo:dato pendiente, ver docstring) al arrancar `ingest`.
STAGING_DIR = REPO / "wiki" / "1_proyectos" / "contexto_vivo" / "_staging_sync_metrics"
STORE = STAGING_DIR / "datos_metricas_semanales"
LOG_MD = STAGING_DIR / "log_metricas_semanales.md"


def seed_staging_from_mirror():
    """Siembra la copia de trabajo desde el espejo si todavia no existe o esta vacia.

    No pisa una copia de trabajo ya sembrada en esta corrida -- si `ingest` se corre
    dos veces sin pasar por /context_push, la segunda sigue mergeando sobre lo que la
    primera ya acumulo (no vuelve a partir del espejo, que quedo atras)."""
    if STORE.exists() and any(STORE.iterdir()):
        return  # ya sembrada -- puede tener merges pendientes de una corrida anterior
    STORE.parent.mkdir(parents=True, exist_ok=True)
    if MIRROR_STORE.exists():
        shutil.copytree(MIRROR_STORE, STORE, dirs_exist_ok=True)
    else:
        STORE.mkdir(parents=True, exist_ok=True)
    if MIRROR_LOG_MD.exists() and not LOG_MD.exists():
        shutil.copy2(MIRROR_LOG_MD, LOG_MD)

# --- Definición de las NSM (confirmada por el usuario, 2026-07-21) ----------
# NSM #1 — volumen operado por API BANK (Banco Industrial). Solo los tipos de operación
# que efectivamente se cursan contra la API del banco. El resto (dólar, cripto, FX, PIX,
# cash-in con tarjeta, internas) impacta indirectamente y se reporta aparte.
NSM1_OUT = {1: "Transferencia Saliente", 3: "Pago con QR", 8: "Transf. Pull Débito"}
NSM1_IN = {2: "Transferencia Entrante", 6: "Transf. Pull Crédito", 14: "Debin Recurrente Crédito"}
NSM1_TIPOS = dict(list(NSM1_OUT.items()) + list(NSM1_IN.items()))
# GOTCHA: el opportunity tree de wiki/2_areas/direccion/north_star.md agrupa "transferencias
# pull" entero bajo IN. El usuario precisó (2026-07-21) que Pull Débito es OUT (debita la
# cuenta de la wallet) y solo Pull Crédito es IN. Manda esta definición, no el tree.

EST_APROBADA = 2
EST_RECHAZADA = 3
EST_DEVUELTA = {6, 7}  # Devuelta / Devuelta parcial

# NSM #2 — volumen operado con el gateway Payway (=Decidir=Prisma). Hoy solo cobro NO
# presente: tarjeta por Botón Simple y Botón 2.0. El POS presente (MPOS) todavía no pasa
# por Payway — ese proyecto no se shippeó — así que se reporta como contexto, no como NSM.
NSM2_TIPOS = {6: "Botón Simple", 7: "Botón 2.0"}
NSM2_FORMAS = {80: "Tarjeta de Crédito", 90: "Tarjeta de Débito",
               60: "Tarjeta Prepaga", 10: "Tarjeta de Crédito Cuotas"}
EST_ACREDITADO = "ACREDITADO"
EST_RECHAZADA_ADQ = "RECHAZADA"
EST_DEVUELTA_ADQ = "DEVUELTA"

# Palanca directa adicional a NSM #1 (usuario, 2026-07-23): transferencias entrantes a CVU,
# entrantes a CBU y salientes del producto Agente de Cobros y Pagos — se cursan contra la
# misma API BANK que las Operaciones de Wallet, así que mueven el volumen de NSM#1
# directamente. Viven en una tabla propia (Transferences/Collectors), no en Operaciones.
# DECISIÓN DEL USUARIO (2026-07-23): esta palanca SE SUMA al total oficial de NSM#1, tanto
# para todo el histórico ya ingerido como hacia adelante — no es un bloque aparte, es parte
# del número que se reporta como "NSM#1". Ver Datos.nsm1_oficial() / nsm1_oficial_out() /
# nsm1_oficial_in() más abajo, que hacen la fusión con Operaciones de Wallet.
TAC_OUT = {"TRANSFER": "Saliente (Agente de Cobro)"}
TAC_IN = {"transfer.cvu.received": "Entrante CVU", "transfer.cbu.received": "Entrante CBU"}
TAC_TIPOS = dict(list(TAC_OUT.items()) + list(TAC_IN.items()))
# "NULL" (Type vacío) apareció en el backfill del 2026-07-23 (~1.506 filas, ~0,5% del
# volumen del lote): el usuario confirmó que es probablemente un bug/error de la fuente,
# pero que de todas formas SUMA al volumen de NSM#1 aunque no se sepa a qué lado (IN/OUT)
# cae — se reporta como bucket "Sin clasificar" dentro del total, nunca se le asigna un
# lado por analogía. Ver ../../../../wiki/2_areas/gaps_y_preguntas.md.
TAC_TIPOS_TODOS = set(TAC_TIPOS) | {"NULL"}
TAC_EST_OK = {"COMPLETED"}  # único estado que suma volumen (confirmado por el usuario,
                            # 2026-07-23) — el resto es "no exitoso", se mide como anomalía
DIM_TAC_STATUS = {"COMPLETED", "FAILED", "PENDING", "UNKNOWN", "CREDIT_ERROR",
                   "DATA_ERROR", "IN_PROGRESS", "NO_WARRANTY"}

# Dimensiones estables (referencia del usuario). Si aparece un Id fuera de estas tablas,
# el pipeline avisa y hay que pedirle el dato al usuario — nunca se adivina.
DIM_TIPO_TRANSACCION = {
    0: "Desconocido", 1: "TransferenciasEntranteCvu", 2: "Liquidador", 3: "EcoCerrado",
    4: "MPOS", 6: "BotonSimple", 7: "Boton20", 9: "Transferencia30", 12: "TAP2PHONE",
}
DIM_FORMA_PAGO = {
    80: "Tarjeta de Crédito", 90: "Tarjeta de Débito", 20: "QR", 60: "Tarjeta Prepaga",
    40: "RxT", 50: "Liquidador", 10: "Tarjeta de Crédito Cuotas", 70: "Eco Cerrado",
}
DIM_ESTADO_ADQ = {"ACREDITADO", "RECHAZADA", "DEVUELTA", "ENPROCESO"}

# Palancas indirectas de NSM#1 (no suman, alimentan el saldo que después opera contra el
# banco) y categorías de Adquirencia fuera del scope de NSM#2 hoy (el POS presente todavía
# no pasa por Payway). A nivel de módulo porque las usa tanto el desglose de `analyze` como
# el detector de hallazgos `_palancas_secundarias` — una sola fuente de verdad para las dos.
INDIRECTAS_NSM1 = {9: "Compra Dólar CCL", 10: "Venta Dólar CCL", 11: "Compra Cripto",
                   12: "Venta Cripto", 16: "Pago FX", 15: "Pago QR Pix",
                   13: "Ingreso con tarjeta", 7: "Viaje QR",
                   4: "Transf. interna saliente", 5: "Transf. interna entrante"}
FUERA_PAYWAY_NSM2 = {1: "Transf. Entrante CVU", 2: "Liquidador", 3: "EcoCerrado",
                      4: "MPOS / POS", 9: "Transferencia 3.0", 12: "TAP2PHONE"}

# --- Recursos: firma de header -> esquema del store -------------------------
# 'sig' son columnas que identifican unívocamente al recurso; 'key' es la clave de merge
# (un combo que llega de nuevo REEMPLAZA al viejo, nunca se suma); 'val' son las medidas.
RESOURCES = {
    "operaciones": {
        "sig": {"semanaid", "organizacionid", "tipooperacionid", "estadoid", "volumen"},
        "key": ["SemanaId", "OrganizacionId", "TipoOperacionId", "EstadoId"],
        "val": ["Cantidad", "Volumen"],
        "file": "fact_operaciones.csv",
        "semanal": True,
    },
    "transacciones": {
        "sig": {"semanaid", "entidadidentificador", "tipotransaccion", "formadepago", "estado"},
        "key": ["SemanaId", "EntidadIdentificador", "TipoTransaccion", "FormadePago", "Estado"],
        "val": ["Cantidad", "Volumen"],
        "file": "fact_transacciones.csv",
        "semanal": True,
    },
    "cuentas": {
        "sig": {"semanaid", "organizacionid", "cantidad"},
        "key": ["SemanaId", "OrganizacionId"],
        "val": ["Cantidad"],
        "file": "fact_cuentas.csv",
        "semanal": True,
    },
    "comercios": {
        "sig": {"semanaid", "entidadid", "cantidad"},
        "key": ["SemanaId", "EntidadId"],
        "val": ["Cantidad"],
        "file": "fact_comercios.csv",
        "semanal": True,
    },
    "transferencias_agente_cobro": {
        "sig": {"semanaid", "type", "collectorid", "status", "volumen"},
        "key": ["SemanaId", "Type", "CollectorId", "Status"],
        "val": ["Cantidad", "Volumen"],
        "file": "fact_transferencias_agente_cobro.csv",
        "semanal": True,
    },
    "dim_collectors": {
        "sig": {"id", "collectaccountid", "name", "cuit", "psp", "cbu", "codigo", "bankid"},
        "key": ["Id"],
        "val": ["Name", "Cuit", "Codigo", "BankId"],
        "file": "dim_collectors.csv",
        "semanal": False,
    },
    "dim_organizaciones": {
        "sig": {"id", "nombre", "codigo", "billeteraid"},
        "key": ["Id"],
        "val": ["Nombre", "Codigo", "FechaAlta", "FechaBaja", "CodigoEntidad"],
        "file": "dim_organizaciones.csv",
        "semanal": False,
    },
    "dim_entidades": {
        "sig": {"id", "nombre", "cuit", "codigo", "dominioadquirente"},
        "key": ["Id"],
        "val": ["Nombre", "Cuit", "Codigo", "AdministradorNombre"],
        "file": "dim_entidades.csv",
        "semanal": False,
    },
    "dim_tipos_operacion": {
        "sig": {"id", "nombre", "codigotipocomprobante"},
        "key": ["Id"],
        "val": ["Nombre", "Codigo"],
        "file": "dim_tipos_operacion.csv",
        "semanal": False,
    },
    "dim_estados_operacion": {
        "sig": {"id", "nombre", "descripcion"},
        "key": ["Id"],
        "val": ["Nombre"],
        "file": "dim_estados_operacion.csv",
        "semanal": False,
    },
}
# --- Fallback para exports SIN fila de encabezado (usuario, 2026-08-11: "Save Results As
# csv" de su herramienta nunca incluye headers y las queries de SKILL.md no van a cambiar)
# -----------------------------------------------------------------------------
# Orden posicional de columnas, calcado 1:1 del SELECT de cada query en SKILL.md. Si el día
# de mañana se edita una query ahí, hay que editar la lista correspondiente acá también —
# no hay forma de derivarlo del archivo en sí porque no trae nombres de columna.
COLUMN_ORDER_HEADERLESS = {
    "operaciones": ["SemanaId", "FechaInicioCorte", "FechaFinCorte", "OrganizacionId",
                     "TipoOperacionId", "EstadoId", "Cantidad", "Volumen"],
    "transacciones": ["SemanaId", "FechaInicioCorte", "FechaFinCorte", "EntidadIdentificador",
                       "TipoTransaccion", "FormadePago", "Estado", "Cantidad", "Volumen"],
    "cuentas": ["SemanaId", "FechaInicioCorte", "FechaFinCorte", "OrganizacionId", "Cantidad"],
    "comercios": ["SemanaId", "FechaInicioCorte", "FechaFinCorte", "EntidadId", "Cantidad"],
    "transferencias_agente_cobro": ["SemanaId", "FechaInicioCorte", "FechaFinCorte", "Type",
                                     "CollectorId", "Status", "Cantidad", "Volumen"],
    # dim_entidades/dim_organizaciones headerless = volcado "SELECT *" de la tabla completa.
    # Orden confirmado por el usuario (2026-08-11) contrastando contra el store ya ingerido
    # (wiki/2_areas/control/datos_metricas_semanales/dim_entidades.csv y dim_organizaciones.csv):
    # las columnas _cN no se usan (no aparecen en RESOURCES[...]["val"]), se listan solo para
    # que la posición de las columnas que sí importan (AdministradorNombre, CodigoEntidad)
    # quede correcta.
    "dim_entidades": ["Id", "Nombre", "Cuit", "Codigo", "_c4", "_c5", "_c6",
                       "AdministradorNombre", "_c8", "_c9"],
    "dim_organizaciones": ["Id", "Nombre", "Codigo", "FechaAlta", "FechaBaja", "_c5", "_c6",
                            "_c7", "_c8", "_c9", "CodigoEntidad"],
}
# Filas de igual largo son ambiguas por forma sola (operaciones/transferencias_agente_cobro
# comparten 8 columnas; cuentas/comercios comparten 5) — se desambigua por contenido (texto
# vs. numérico en la columna 4) o, si eso tampoco alcanza, por palabra clave en el nombre de
# archivo. Es la única excepción a "nunca por nombre de archivo": sin fila de encabezado no
# queda otra señal.
_NCOLS_AMBIGUOS = {8: ["operaciones", "transferencias_agente_cobro"], 5: ["cuentas", "comercios"]}
_FILENAME_HINTS = {
    "cuentas": ("cuent",), "comercios": ("comercio",),
    "operaciones": ("operacion",), "transferencias_agente_cobro": ("transferenc",),
}

FACTS = ["operaciones", "transacciones", "cuentas", "comercios"]
# Palanca directa adicional a NSM#1 (transferencias Agente de Cobros y Pagos, usuario
# 2026-07-23): se mide semanalmente igual que los FACTS, pero NO bloquea el ingest si falta
# — es una métrica complementaria, no una de las dos NSM, y forzar su presencia impediría
# backfills o correcciones puntuales de esta sola tabla sin tener que resubir operaciones/
# transacciones/cuentas/comercios de nuevo.
FACTS_PALANCA = ["transferencias_agente_cobro"]
NSM_FACTS = ["operaciones", "transacciones"]  # sin estos dos no hay NSM que medir


# --- Utilidades -------------------------------------------------------------
def norm(s):
    s = unicodedata.normalize("NFD", str(s or "").strip().lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def to_num(x):
    """Tolera decimal con coma y separador de miles, y celdas vacías/NULL."""
    s = str(x or "").strip()
    if not s or s.upper() == "NULL":
        return 0.0
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return 0.0


def to_int(x):
    try:
        return int(float(str(x).strip()))
    except (ValueError, TypeError):
        return None


def fmt_m(v):
    """Volúmenes en millones de ARS — la unidad con la que se habla del negocio.
    Precisión variable: un cliente chico no puede quedar reportado como '$0 M'."""
    m = v / 1_000_000.0
    dec = 0 if abs(m) >= 100 else (1 if abs(m) >= 1 else 2)
    return "$" + _sep_es("{:,.{}f}".format(m, dec)) + " M"


def fmt_n(v, dec=0):
    """Entero con separador de miles a la española (1.234.567)."""
    return _sep_es("{:,.{}f}".format(v, dec))


def fmt_valor(v, formato="monto"):
    """Despacha a fmt_m (default, pesos) o fmt_n (formato="entero" — leading indicators como
    altas de cuentas/comercios, que son una cantidad, no un monto en pesos)."""
    if v is None:
        return "s/d"
    return fmt_n(v) if formato == "entero" else fmt_m(v)


def _sep_es(s):
    return s.replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def fmt_pct(v, signo=True):
    if v is None:
        return "s/d"
    return ("{:+.1f}%" if signo else "{:.1f}%").format(v)


def pct_change(nuevo, viejo):
    if not viejo:
        return None
    return (nuevo - viejo) / viejo * 100.0


def _share(parte, total):
    return (parte / total * 100.0) if total else 0.0


def read_csv_any(path):
    """Lee un CSV tolerando BOM y separador ; o , . Devuelve (headers_norm, filas dict)."""
    with io.open(path, encoding="utf-8-sig", newline="") as fh:
        sample = fh.read(4096)
        fh.seek(0)
        sep = ";" if sample.count(";") >= sample.count(",") else ","
        rdr = csv.DictReader(fh, delimiter=sep)
        rows = [r for r in rdr if any((v or "").strip() for v in r.values())]
        heads = [h for h in (rdr.fieldnames or []) if h]
    return {norm(h) for h in heads}, heads, rows


def _leer_filas_crudas(path):
    """Lee el CSV como filas de texto planas, SIN tratar la primera línea como header."""
    with io.open(path, encoding="utf-8-sig", newline="") as fh:
        sample = fh.read(4096)
        fh.seek(0)
        sep = ";" if sample.count(";") >= sample.count(",") else ","
        rdr = csv.reader(fh, delimiter=sep)
        return [r for r in rdr if any((v or "").strip() for v in r)]


def _sniff_headerless(path):
    """Fallback posicional para exports sin fila de encabezado (usuario, 2026-08-11).
    Devuelve (recurso, rows, nota) o (None, None, None) si no se puede resolver."""
    filas = _leer_filas_crudas(path)
    if not filas:
        return None, None, None
    ncols = len(filas[0])
    candidatos = [r for r, cols in COLUMN_ORDER_HEADERLESS.items() if len(cols) == ncols]
    if ncols in _NCOLS_AMBIGUOS:
        candidatos = list(_NCOLS_AMBIGUOS[ncols])
        if ncols == 8:
            # operaciones: 4ta columna (OrganizacionId) numérica.
            # transferencias_agente_cobro: 4ta columna (Type) es texto (TRANSFER, ...).
            val4 = filas[0][3].strip() if len(filas[0]) > 3 else ""
            candidatos = ["operaciones"] if val4.lstrip("-").isdigit() else \
                ["transferencias_agente_cobro"]
        else:
            # cuentas vs. comercios: misma forma exacta, sin señal de contenido —
            # única excepción a "detección por firma de header, nunca por nombre de archivo".
            nombre = path.name.lower()
            candidatos = [r for r in candidatos
                          if any(h in nombre for h in _FILENAME_HINTS[r])]
    if len(candidatos) != 1:
        return None, None, None
    recurso = candidatos[0]
    cols = COLUMN_ORDER_HEADERLESS[recurso]
    if len(cols) != ncols:
        return None, None, None
    rows = [dict(zip(cols, fila)) for fila in filas]
    nota = ("'{}' sin fila de encabezado -> asumido como '{}' por forma/contenido "
            "({} columnas). Verificá que sea correcto.".format(path.name, recurso, ncols))
    return recurso, rows, nota


def sniff(path):
    """Identifica el recurso por firma de header. None si no matchea ninguno conocido."""
    try:
        hnorm, heads, rows = read_csv_any(path)
    except Exception as e:  # noqa: BLE001 - queremos el motivo textual en el reporte
        return None, None, str(e), None
    mejor = None
    for nombre, spec in RESOURCES.items():
        if spec["sig"] <= hnorm:
            # gana la firma más específica (evita que cuentas/comercios se pisen)
            if mejor is None or len(spec["sig"]) > len(RESOURCES[mejor]["sig"]):
                mejor = nombre
    if mejor is None:
        recurso_hl, rows_hl, nota = _sniff_headerless(path)
        if recurso_hl is not None:
            return recurso_hl, rows_hl, None, nota
        primera = (heads[0] if heads else "").strip()
        if primera.isdigit() and len(primera) == 6:
            return None, None, ("este export vino SIN fila de encabezado (la primera celda, "
                                 "'{}', es un SemanaId, no un nombre de columna) y no se pudo "
                                 "resolver por forma/contenido — re-exportalo incluyendo los "
                                 "headers".format(primera)), None
        return None, None, "header no reconocido: " + ", ".join(heads), None
    return mejor, rows, None, None


def col(row, nombre):
    """Acceso a columna tolerante a acentos/mayúsculas."""
    objetivo = norm(nombre)
    for k, v in row.items():
        if norm(k) == objetivo:
            return v
    return None


# --- Store ------------------------------------------------------------------
def store_path(recurso):
    return STORE / RESOURCES[recurso]["file"]


def load_store(recurso):
    p = store_path(recurso)
    if not p.exists():
        return {}
    spec = RESOURCES[recurso]
    _, _, rows = read_csv_any(p)
    out = {}
    for r in rows:
        k = tuple((col(r, c) or "").strip() for c in spec["key"])
        out[k] = {c: (col(r, c) or "") for c in spec["key"] + spec["val"]}
    return out


def write_store(recurso, data):
    spec = RESOURCES[recurso]
    cols = spec["key"] + spec["val"]
    STORE.mkdir(parents=True, exist_ok=True)
    with io.open(store_path(recurso), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter=";", lineterminator="\n")
        w.writerow(cols)
        for k in sorted(data, key=_sort_key):
            w.writerow([data[k].get(c, "") for c in cols])


def _sort_key(k):
    return tuple((0, to_int(x), "") if to_int(x) is not None else (1, 0, str(x)) for x in k)


def load_semanas():
    p = STORE / "semanas.csv"
    if not p.exists():
        return {}
    _, _, rows = read_csv_any(p)
    return {(col(r, "SemanaId") or "").strip(): {
        "inicio": col(r, "FechaInicio"), "fin": col(r, "FechaFin"),
        "completa": (col(r, "Completa") or "").strip() == "1",
        "fuentes": col(r, "Fuentes") or "", "lote": col(r, "Lote") or ""} for r in rows}


def write_semanas(sem):
    STORE.mkdir(parents=True, exist_ok=True)
    with io.open(STORE / "semanas.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter=";", lineterminator="\n")
        w.writerow(["SemanaId", "FechaInicio", "FechaFin", "Completa", "Fuentes", "Lote"])
        for s in sorted(sem):
            d = sem[s]
            w.writerow([s, d["inicio"], d["fin"], "1" if d["completa"] else "0",
                        d["fuentes"], d["lote"]])


def semanas_completas():
    return sorted(s for s, d in load_semanas().items() if d["completa"])


# --- Lectura de raw/ --------------------------------------------------------
def scan_raw():
    """Devuelve (lotes, sin_reconocer, dup_files, asumidos).
    lotes[recurso] = {'rows': [...], 'files': [...]}
    asumidos = [nota, ...] — exports sin header resueltos por forma/contenido (ver sniff).

    Un archivo cuyo contenido byte-a-byte ya se leyó se descarta: la única forma de que
    eso pase es que el PM haya dejado el mismo export dos veces, y sumarlo duplicaría el
    volumen (ver agregar_lote, que suma los fragmentos de un export partido)."""
    lotes = defaultdict(lambda: {"rows": [], "files": []})
    sin_rec, dup_files, asumidos, hashes = [], [], [], {}
    if not RAW_DIR.exists():
        return lotes, sin_rec, dup_files, asumidos
    for p in sorted(RAW_DIR.glob("*.csv")):
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if h in hashes:
            dup_files.append((p.name, hashes[h]))
            continue
        hashes[h] = p.name
        recurso, rows, err, nota = sniff(p)
        if recurso is None:
            sin_rec.append((p.name, err))
            continue
        if nota:
            asumidos.append(nota)
        lotes[recurso]["rows"].extend(rows)
        lotes[recurso]["files"].append(p.name)
    return lotes, sin_rec, dup_files, asumidos


def agregar_lote(recurso, rows):
    """Colapsa el lote a una fila por clave. Devuelve (data, n_fragmentos).

    GOTCHA CENTRAL DE ESTA SKILL: cuando la query no entra en una sola corrida, el PM la
    parte en varios archivos cortando por FECHA, no por semana — así que las semanas del
    borde llegan en dos pedazos (verificado en el backfill 2026-07-21: 202601 y 202610
    aparecen en dos archivos cada una, con cantidades distintas y complementarias).
    Esos fragmentos se SUMAN. Pisar uno con otro perdería medio volumen de esa semana.
    El merge contra el store, en cambio, sí REEMPLAZA: ahí un combo repetido es una
    reingesta o una corrección de la misma semana, no un pedazo nuevo."""
    spec = RESOURCES[recurso]
    suma = spec.get("semanal", False)
    data, frags = {}, 0
    for r in rows:
        k = tuple((col(r, c) or "").strip() for c in spec["key"])
        if not all(k):
            continue
        fila = {c: (col(r, c) or "").strip() for c in spec["key"]}
        for c in spec["val"]:
            v = col(r, c)
            fila[c] = _fmt_val(v) if c in ("Cantidad", "Volumen") else (v or "").strip()
        if k in data and suma:
            frags += 1
            for c in spec["val"]:
                if c in ("Cantidad", "Volumen"):
                    fila[c] = _fmt_val(to_num(data[k][c]) + to_num(fila[c]))
        data[k] = fila
    return data, frags


def cortes_de(rows):
    """SemanaId -> (FechaInicio, FechaFin) tal como vienen del export."""
    out = {}
    for r in rows:
        s = (col(r, "SemanaId") or "").strip()
        if s:
            out.setdefault(s, ((col(r, "FechaInicioCorte") or "")[:10],
                               (col(r, "FechaFinCorte") or "")[:10]))
    return out


def es_completa(fin_str):
    """Una semana está cerrada solo si su corte final ya pasó. Un export tomado a mitad
    de semana trae una semana parcial que arruinaría cualquier serie si se computa."""
    try:
        return datetime.strptime(fin_str[:10], "%Y-%m-%d").date() <= date.today()
    except (ValueError, TypeError):
        return False


def _rango_iso_real(semana_id):
    """Rango [lunes, lunes+7) que le corresponde a un SemanaId (YYYYWW) según ISO-8601."""
    s = int(semana_id)
    anio, semana = divmod(s, 100)
    ini = date.fromisocalendar(anio, semana, 1)  # día 1 = lunes
    fin = ini + timedelta(days=7)
    return ini.isoformat(), fin.isoformat()


def _validar_alineacion_iso(cortes):
    """Compara el rango que trae el export (FechaInicioCorte/FechaFinCorte) contra el rango
    ISO real de su SemanaId. Si no coinciden, la query se corrió un día que no es lunes — el
    `DECLARE @FechaFin = CAST(GETDATE() AS DATE)` original solo produce la semana ISO correcta
    si se corre un lunes; cualquier otro día, la ventana de 7 días queda corrida: sobra un día
    de la semana siguiente y falta el mismo día de la semana que se está midiendo (verificado
    en la corrida del 2026-08-04, corrida un martes: SemanaId=202631 vino con ventana
    2026-07-28→2026-08-04 en vez de la real 2026-07-27→2026-08-03 — faltaba el lunes 27 y
    sobraba el lunes 3 de agosto, que pertenece a la semana siguiente).

    Como el export ya viene agregado por SUM/COUNT en el motor, no queda grano diario para
    corregir esto en el pipeline: no se puede "restar" el día de más ni "completar" el que
    falta. La corrección es en el origen — ver el `DECLARE` corregido en SKILL.md, que ancla
    @FechaFin al lunes de la semana en curso (DATEADD(week, DATEDIFF(week,0,GETDATE()),0))
    en vez de a GETDATE() — y por eso este chequeo aborta en vez de solo avisar.

    Devuelve lista de dicts con el detalle, uno por SemanaId desalineado."""
    fuera = []
    for s, (ini, fin) in cortes.items():
        try:
            ini_real, fin_real = _rango_iso_real(s)
        except (ValueError, TypeError):
            continue  # SemanaId no numérico o inválido: no es este chequeo el que lo atrapa
        if (ini, fin) != (ini_real, fin_real):
            fuera.append({"semana": s, "ini_export": ini, "fin_export": fin,
                          "ini_real": ini_real, "fin_real": fin_real})
    return fuera


def _imprimir_desalineadas(fuera):
    print("\n[ABORT] {} semana(s) con ventana desalineada del calendario ISO:"
          .format(len(fuera)))
    for x in fuera:
        print("    SemanaId {}: export trae {} -> {}  (real: {} -> {})"
              .format(x["semana"], x["ini_export"], x["fin_export"],
                      x["ini_real"], x["fin_real"]))
    print("    La query se corrió un día que no es lunes. Corregí el DECLARE de @FechaFin en")
    print("    SKILL.md a:  DATEADD(week, DATEDIFF(week, 0, GETDATE()), 0)")
    print("    y volvé a exportar — no se puede arreglar esto desde el pipeline, el export ya")
    print("    viene agregado (SUM/COUNT), no queda grano diario para corregir la ventana.")
    print("    Si de verdad querés ingerir esta ventana corrida tal cual (no recomendado),")
    print("    corré con --forzar-desalineadas.")


# --- Comando: inspect -------------------------------------------------------
def cmd_inspect(forzar_desalineadas=False):
    seed_staging_from_mirror()
    lotes, sin_rec, dup_files, asumidos = scan_raw()
    warns, faltan = [], []

    print("=" * 78)
    print("INSPECT — lectura de raw/ (no se escribe nada)")
    print("=" * 78)

    for nota in asumidos:
        print("[ASUMIDO] " + nota)
    if asumidos:
        print()

    for nombre, original in dup_files:
        warns.append("'{}' es byte-a-byte idéntico a '{}': se descarta para no duplicar "
                     "volumen. Confirmá con el usuario que no era otro período."
                     .format(nombre, original))
    for nombre, err in sin_rec:
        print("[ABORT] '{}' no matchea ninguna firma conocida -> {}".format(nombre, err))
    if sin_rec:
        print("        No inventes un mapeo: registrá el caso en ../../../../wiki/2_areas/gaps_y_preguntas.md y")
        print("        consultá al usuario antes de tocar RESOURCES en pipeline.py.\n")

    # 1) Insumos obligatorios — pero solo si el lote toca al menos uno de los 4 FACTS
    # core: un raw/ que trae SOLO recursos nuevos (ej. un backfill puntual de la palanca
    # TAC + su dimensión) no tiene por qué resubir operaciones/transacciones/cuentas/
    # comercios de semanas que el store ya tiene.
    if any(r in lotes for r in FACTS):
        for rec in FACTS:
            if rec not in lotes:
                faltan.append(rec)
    if faltan:
        print("[FALTA] Insumos obligatorios ausentes en raw/: " + ", ".join(faltan))
        print("        Pedile al usuario que los exporte (las queries están en SKILL.md)")
        print("        y frená acá: no corras ingest con el lote incompleto.\n")

    # Dimensiones: obligatorias solo si el store todavía no las tiene
    for rec in ("dim_organizaciones", "dim_entidades", "dim_collectors"):
        if rec not in lotes and not store_path(rec).exists():
            print("[FALTA] {} — primera corrida sin la dimensión. Pedila al usuario.".format(rec))
            faltan.append(rec)

    if not lotes:
        print("\nraw/ no tiene CSVs procesables. Nada que inspeccionar.")
        return 1

    # 2) Resumen por recurso
    print("\n--- Recursos detectados ---")
    for rec in sorted(lotes):
        L = lotes[rec]
        print("  {:<22} {:>6} filas   <- {}".format(rec, len(L["rows"]), ", ".join(L["files"])))

    # 3) Semanas y completitud
    sem_store = load_semanas()
    cortes, por_rec = {}, {}
    for rec in FACTS + FACTS_PALANCA:
        if rec in lotes:
            c = cortes_de(lotes[rec]["rows"])
            por_rec[rec] = set(c)
            cortes.update(c)
    if any(f in lotes for f in FACTS) and "transferencias_agente_cobro" not in lotes \
            and store_path("transferencias_agente_cobro").exists():
        warns.append("no llegó transferencias_agente_cobro esta semana (la palanca TAC de "
                     "NSM#1). No bloquea el ingest, pero confirmá con el usuario si se "
                     "olvidó el export o si de verdad no hubo movimiento.")

    # Ventana ISO: aborta ANTES de mostrar semanas/completitud — una semana desalineada no
    # debería ni sugerir que está lista para 'ingest'. Ver _validar_alineacion_iso.
    desalineadas = _validar_alineacion_iso(cortes)
    if desalineadas and not forzar_desalineadas:
        _imprimir_desalineadas(desalineadas)
        faltan.append("(ventana ISO desalineada — ver arriba)")
    elif desalineadas and forzar_desalineadas:
        warns.append("{} semana(s) con ventana ISO desalineada, ingeridas igual por "
                     "--forzar-desalineadas: {}"
                     .format(len(desalineadas), ", ".join(x["semana"] for x in desalineadas)))

    todas = sorted(cortes)
    if todas:
        print("\n--- Semanas en el lote: {} ({} .. {}) ---".format(len(todas), todas[0], todas[-1]))
        parciales = [s for s in todas if not es_completa(cortes[s][1])]
        for s in parciales:
            print("  [PARCIAL] {} ({} -> {}) todavía abierta: se guarda pero NO se computa."
                  .format(s, cortes[s][0], cortes[s][1]))
        for rec in NSM_FACTS:
            if rec in por_rec:
                falt = [s for s in todas if s not in por_rec[rec] and es_completa(cortes[s][1])]
                if falt:
                    warns.append("semanas sin datos de {}: {}".format(rec, ", ".join(falt)))
        # huecos en la serie acumulada
        union = sorted(set(todas) | set(sem_store))
        huecos = _huecos(union)
        if huecos:
            warns.append("huecos en la serie histórica (semanas nunca ingeridas): "
                         + ", ".join(huecos))
        # overlaps
        pisa = [s for s in todas if s in sem_store]
        if pisa:
            print("  [OVERLAP] {} semana(s) ya en el store se van a pisar: {}"
                  .format(len(pisa), ", ".join(pisa[:12]) + (" ..." if len(pisa) > 12 else "")))
            print("            Normal en un backfill o una corrección; sospechoso si el PM")
            print("            subió la semana de siempre y aparecen meses viejos.")

    # 4) Dimensiones desconocidas
    warns += _chequear_dimensiones(lotes)

    # 5) Fragmentos de un export partido (misma clave en dos archivos -> se SUMAN)
    for rec in FACTS + FACTS_PALANCA:
        if rec in lotes:
            data, frags = agregar_lote(rec, lotes[rec]["rows"])
            if frags:
                print("\n  [SPLIT] {}: {} fila(s) llegaron partidas entre archivos y se SUMAN "
                      "\n          ({} filas crudas -> {} combos). Esperable cuando la query no "
                      "\n          entra en una sola corrida y el corte cae dentro de una semana."
                      .format(rec, frags, len(lotes[rec]["rows"]), len(data)))

    print("\n--- Warnings ---")
    for w in warns:
        print("  [WARN] " + w)
    if not warns:
        print("  (ninguno)")

    print("\nListo para 'ingest'." if not faltan else "\nNO corras 'ingest': faltan insumos.")
    return 0 if not faltan else 1


def _huecos(semanas):
    """Semanas ISO ausentes entre la primera y la última de la serie."""
    if not semanas:
        return []
    ints = sorted(int(s) for s in semanas)
    esperadas, y, w = [], ints[0] // 100, ints[0] % 100
    while y * 100 + w <= ints[-1]:
        esperadas.append(y * 100 + w)
        w += 1
        if w > _semanas_iso(y):
            y, w = y + 1, 1
    return [str(s) for s in esperadas if s not in set(ints)]


def _semanas_iso(anio):
    d = date(anio, 12, 28)  # el 28-dic siempre cae en la última semana ISO del año
    return d.isocalendar()[1]


def _chequear_dimensiones(lotes):
    """Todo Id que aparece en los hechos tiene que existir en su dimensión. Si no, se pide
    el dato al usuario: imputar por analogía sería inventar negocio."""
    warns = []
    orgs = _ids_dim("dim_organizaciones", lotes, "Id")
    ents_cod = _ids_dim("dim_entidades", lotes, "Codigo")
    ents_id = _ids_dim("dim_entidades", lotes, "Id")
    collectors = _ids_dim("dim_collectors", lotes, "Id")

    def desconocidos(rec, campo, universo, label):
        if rec not in lotes or not universo:
            return
        vistos = {(col(r, campo) or "").strip() for r in lotes[rec]["rows"]}
        falt = sorted(v for v in vistos if v and v not in universo)
        if falt:
            warns.append("{}: {} {} sin fila en la dimensión ({}). Pedile al usuario el "
                         "refresh de la tabla antes de reportar."
                         .format(rec, len(falt), label, ", ".join(falt[:10])))

    desconocidos("operaciones", "OrganizacionId", orgs, "OrganizacionId")
    desconocidos("cuentas", "OrganizacionId", orgs, "OrganizacionId")
    desconocidos("transacciones", "EntidadIdentificador", ents_cod, "EntidadIdentificador")
    desconocidos("comercios", "EntidadId", ents_id, "EntidadId")
    desconocidos("transferencias_agente_cobro", "CollectorId", collectors, "CollectorId")

    if "transferencias_agente_cobro" in lotes:
        tipos_tac = {(col(r, "Type") or "").strip() for r in lotes["transferencias_agente_cobro"]["rows"]}
        estados_tac = {(col(r, "Status") or "").strip().upper() for r in lotes["transferencias_agente_cobro"]["rows"]}
        falt_tipo = sorted(t for t in tipos_tac if t and t not in TAC_TIPOS)
        if falt_tipo:
            warns.append("transferencias_agente_cobro: Type desconocido(s) -> {}. Tabla nueva "
                         "(usuario, 2026-07-23): preguntá qué significan antes de sumarlos a IN/OUT."
                         .format(falt_tipo))
        falt_est = sorted(e for e in estados_tac if e and e not in DIM_TAC_STATUS)
        if falt_est:
            warns.append("transferencias_agente_cobro: Status desconocido(s) -> {}. Confirmá con "
                         "el usuario si suman al volumen (hoy solo COMPLETED cuenta)."
                         .format(falt_est))

    if "transacciones" in lotes:
        tt = {to_int(col(r, "TipoTransaccion")) for r in lotes["transacciones"]["rows"]}
        fp = {to_int(col(r, "FormadePago")) for r in lotes["transacciones"]["rows"]}
        es = {(col(r, "Estado") or "").strip().upper() for r in lotes["transacciones"]["rows"]}
        for vals, dim, label in ((tt, DIM_TIPO_TRANSACCION, "TipoTransaccion"),
                                 (fp, DIM_FORMA_PAGO, "FormadePago")):
            falt = sorted(v for v in vals if v is not None and v not in dim)
            if falt:
                warns.append("transacciones: {} desconocido(s) -> {}. Es una tabla estable: "
                             "pedile el significado al usuario, no lo deduzcas."
                             .format(label, falt))
        falt = sorted(v for v in es if v and v not in DIM_ESTADO_ADQ)
        if falt:
            warns.append("transacciones: Estado desconocido(s) -> {}. Idem: preguntá qué "
                         "significan y si suman al volumen.".format(falt))

    if "operaciones" in lotes:
        tipos = _ids_dim("dim_tipos_operacion", lotes, "Id")
        estados = _ids_dim("dim_estados_operacion", lotes, "Id")
        for campo, universo, label in (("TipoOperacionId", tipos, "TipoOperacionId"),
                                       ("EstadoId", estados, "EstadoId")):
            if not universo:
                continue
            vistos = {(col(r, campo) or "").strip() for r in lotes["operaciones"]["rows"]}
            falt = sorted(v for v in vistos if v and v not in universo)
            if falt:
                warns.append("operaciones: {} desconocido(s) -> {}. Pedile la tabla al usuario."
                             .format(label, ", ".join(falt)))
    return warns


def _ids_dim(recurso, lotes, campo):
    """Universo de valores de una dimensión: lo que llegó en el lote + lo que ya hay en el
    store (el PM no manda las dimensiones todas las semanas)."""
    vals = set()
    if recurso in lotes:
        vals |= {(col(r, campo) or "").strip() for r in lotes[recurso]["rows"]}
    for row in load_store(recurso).values():
        v = (row.get(campo) or "").strip()
        if v:
            vals.add(v)
    return {v for v in vals if v}


# --- Comando: ingest --------------------------------------------------------
def cmd_ingest(forzar_desalineadas=False):
    seed_staging_from_mirror()
    lotes, sin_rec, dup_files, asumidos = scan_raw()
    for nota in asumidos:
        print("  [ASUMIDO] " + nota)
    for nombre, original in dup_files:
        print("  [WARN] '{}' descartado: idéntico a '{}'".format(nombre, original))
    if sin_rec:
        print("[ABORT] Hay archivos no reconocidos en raw/. Corré 'inspect' primero.")
        return 1
    faltan = [r for r in FACTS if r not in lotes] if any(r in lotes for r in FACTS) else []
    if faltan:
        print("[ABORT] Faltan insumos obligatorios: {}. Pedíselos al usuario (queries en "
              "SKILL.md) y no escribas nada hasta tenerlos.".format(", ".join(faltan)))
        return 1

    # Ventana ISO: se valida ANTES de escribir una sola fila al store — mismo chequeo que
    # 'inspect' (ver _validar_alineacion_iso), pero acá el costo de no frenar es peor: ya
    # habría datos corridos mezclados con el store acumulado.
    cortes = {}
    for rec in FACTS + FACTS_PALANCA:
        cortes.update(cortes_de(lotes[rec]["rows"]) if rec in lotes else {})
    desalineadas = _validar_alineacion_iso(cortes)
    if desalineadas and not forzar_desalineadas:
        _imprimir_desalineadas(desalineadas)
        return 1
    if desalineadas:
        print("[WARN] {} semana(s) con ventana ISO desalineada, ingeridas igual por "
              "--forzar-desalineadas: {}"
              .format(len(desalineadas), ", ".join(x["semana"] for x in desalineadas)))

    lote_id = date.today().isoformat()
    resumen = []

    for rec in sorted(lotes):
        # 1) colapsar el lote sumando fragmentos de exports partidos
        lote, frags = agregar_lote(rec, lotes[rec]["rows"])
        # 2) mergear contra el store REEMPLAZANDO el combo (reingesta / corrección)
        data = load_store(rec)
        antes = len(data)
        pisados = sum(1 for k in lote if k in data)
        data.update(lote)
        write_store(rec, data)
        nuevos = len(lote) - pisados
        resumen.append((rec, antes, len(data), nuevos, pisados, len(lotes[rec]["files"])))
        print("  {:<22} {:>6} -> {:>6} filas  (+{} nuevas, {} pisadas{})"
              .format(rec, antes, len(data), nuevos, pisados,
                      ", {} fragmentos sumados".format(frags) if frags else ""))

    # Semanas (reusa `cortes`, ya validado más arriba)
    sem = load_semanas()
    presencia = defaultdict(set)
    for rec in FACTS + FACTS_PALANCA:
        for s in cortes_de(lotes[rec]["rows"]) if rec in lotes else ():
            presencia[s].add(rec)
    nuevas_completas = []
    for s, (ini, fin) in cortes.items():
        # "Fuentes" ACUMULA entre corridas (una semana puede recibir sus recursos en
        # lotes distintos, ej. un backfill puntual de una sola tabla nueva) — nunca
        # reemplaza lo que ya se sabía de esa semana, o un ingest parcial le borraría
        # la completitud a una semana que ya estaba cerrada.
        previas = set((sem.get(s, {}).get("fuentes") or "").split("+")) - {""}
        totales = previas | presencia[s]
        completa = es_completa(fin) and {"operaciones", "transacciones"} <= totales
        if completa and (s not in sem or not sem[s]["completa"]):
            nuevas_completas.append(s)
        sem[s] = {"inicio": ini, "fin": fin, "completa": completa,
                  "fuentes": "+".join(sorted(totales)), "lote": lote_id}
    write_semanas(sem)

    comp = [s for s in sem if sem[s]["completa"]]
    print("\nSemanas en el store: {} ({} completas, {} parciales)"
          .format(len(sem), len(comp), len(sem) - len(comp)))
    print("Semanas nuevas cerradas en esta corrida: "
          + (", ".join(sorted(nuevas_completas)) or "(ninguna)"))
    _append_log(lote_id, lotes, resumen, sorted(cortes), nuevas_completas)
    return 0


def _fmt_val(v):
    x = to_num(v)
    return str(int(x)) if x == int(x) else "{:.2f}".format(x)


def _append_log(lote_id, lotes, resumen, semanas, nuevas):
    LOG_MD.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_MD.exists():
        LOG_MD.write_text(
            "# Log de control — /sync_metrics\n\n"
            "> Ledger de máquina. Una fila por corrida de la skill: qué archivos entraron,\n"
            "> qué semanas cubrieron y cuántas filas quedaron en el store acumulado\n"
            "> (`datos_metricas_semanales/`). Se consulta para auditar qué hizo la skill,\n"
            "> no para razonar sobre el negocio — eso vive en\n"
            "> [`metricas_semanales.md`](metricas_semanales.md).\n\n"
            "| Fecha corrida | Semanas del lote | Semanas cerradas | Recurso | Archivos | Filas lote | Filas store | Nuevas | Pisadas |\n"
            "|---|---|---|---|---|---|---|---|---|\n", encoding="utf-8")
    rango = "{}–{}".format(semanas[0], semanas[-1]) if semanas else "—"
    filas = []
    for rec, antes, despues, nuevos, pisados, nfiles in resumen:
        filas.append("| {} | {} | {} | {} | {} | {} | {} | {} | {} |\n".format(
            lote_id, rango, len(nuevas), rec, nfiles, len(lotes[rec]["rows"]),
            despues, nuevos, pisados))
    with io.open(LOG_MD, "a", encoding="utf-8") as fh:
        fh.writelines(filas)


# --- Carga analítica desde el store ----------------------------------------
class Datos(object):
    """Vista tipada del store, ya filtrada a semanas cerradas."""

    def __init__(self):
        self.sem = load_semanas()
        self.semanas = sorted(s for s, d in self.sem.items() if d["completa"])
        self.orgs = {k[0]: v.get("Nombre", k[0]) for k, v in load_store("dim_organizaciones").items()}
        ents = load_store("dim_entidades")
        self.ent_por_cod = {(v.get("Codigo") or "").strip(): v.get("Nombre", "") for v in ents.values()}
        self.ent_por_id = {k[0]: v.get("Nombre", "") for k, v in ents.items()}
        self.collectors = {k[0]: v.get("Name", k[0]) for k, v in load_store("dim_collectors").items()}
        self.ops = self._ops()
        self.trx = self._trx()
        self.tac_rows = self._tac_data()
        self.cuentas = self._simple("cuentas", "OrganizacionId")
        self.comercios = self._simple("comercios", "EntidadId")

    def _ops(self):
        out = []
        for r in load_store("operaciones").values():
            s = r["SemanaId"]
            if s not in self.sem or not self.sem[s]["completa"]:
                continue
            out.append((s, r["OrganizacionId"], to_int(r["TipoOperacionId"]),
                        to_int(r["EstadoId"]), to_num(r["Cantidad"]), to_num(r["Volumen"])))
        return out

    def _trx(self):
        out = []
        for r in load_store("transacciones").values():
            s = r["SemanaId"]
            if s not in self.sem or not self.sem[s]["completa"]:
                continue
            out.append((s, r["EntidadIdentificador"], to_int(r["TipoTransaccion"]),
                        to_int(r["FormadePago"]), (r["Estado"] or "").upper().strip(),
                        to_num(r["Cantidad"]), to_num(r["Volumen"])))
        return out

    def _tac_data(self):
        out = []
        for r in load_store("transferencias_agente_cobro").values():
            s = r["SemanaId"]
            if s not in self.sem or not self.sem[s]["completa"]:
                continue
            out.append((s, r["CollectorId"], (r["Type"] or "").strip(),
                        (r["Status"] or "").upper().strip(),
                        to_num(r["Cantidad"]), to_num(r["Volumen"])))
        return out

    def _simple(self, rec, campo):
        out = []
        for r in load_store(rec).values():
            s = r["SemanaId"]
            if s not in self.sem or not self.sem[s]["completa"]:
                continue
            out.append((s, r[campo], to_num(r["Cantidad"])))
        return out

    def org(self, i):
        return self.orgs.get(str(i), "org {}".format(i))

    def ent(self, cod):
        return self.ent_por_cod.get(str(cod)) or "entidad {}".format(cod)

    def entid(self, i):
        return self.ent_por_id.get(str(i)) or "entidad #{}".format(i)

    def collector(self, i):
        return self.collectors.get(str(i)) or "collector #{}".format(i)

    def rango(self, s):
        d = self.sem.get(s, {})
        return "{} → {}".format(d.get("inicio", "?"), d.get("fin", "?"))

    # --- series NSM ---
    def nsm1(self, tipos=None, estados=(EST_APROBADA,)):
        tipos = tipos or set(NSM1_TIPOS)
        vol, cant = defaultdict(float), defaultdict(float)
        for s, _o, t, e, c, v in self.ops:
            if t in tipos and e in estados:
                vol[s] += v
                cant[s] += c
        return vol, cant

    def nsm1_por_org(self, semana, tipos=None):
        tipos = tipos or set(NSM1_TIPOS)
        out = defaultdict(float)
        for s, o, t, e, _c, v in self.ops:
            if s == semana and t in tipos and e == EST_APROBADA:
                out[o] += v
        return out

    def nsm2(self, tipos=None, formas=None, estados=(EST_ACREDITADO,)):
        tipos = tipos or set(NSM2_TIPOS)
        formas = formas or set(NSM2_FORMAS)
        vol, cant = defaultdict(float), defaultdict(float)
        for s, _e, t, f, est, c, v in self.trx:
            if t in tipos and f in formas and est in estados:
                vol[s] += v
                cant[s] += c
        return vol, cant

    def nsm2_por_entidad(self, semana):
        out = defaultdict(float)
        for s, e, t, f, est, _c, v in self.trx:
            if s == semana and t in NSM2_TIPOS and f in NSM2_FORMAS and est == EST_ACREDITADO:
                out[e] += v
        return out

    # --- transferencias Agente de Cobros y Pagos (se funden a NSM#1, ver nsm1_oficial) ---
    def tac(self, tipos=None, estados=TAC_EST_OK):
        """Por default incluye TODOS los Type (clasificados + 'NULL' sin clasificar) — el
        usuario confirmó (2026-07-23) que el volumen sin clasificar igual suma al total."""
        tipos = tipos or TAC_TIPOS_TODOS
        vol, cant = defaultdict(float), defaultdict(float)
        for s, _cid, t, est, c, v in self.tac_rows:
            if t in tipos and est in estados:
                vol[s] += v
                cant[s] += c
        return vol, cant

    def tac_por_collector(self, semana, tipos=None):
        tipos = tipos or TAC_TIPOS_TODOS
        out = defaultdict(float)
        for s, cid, t, est, _c, v in self.tac_rows:
            if s == semana and t in tipos and est in TAC_EST_OK:
                out[cid] += v
        return out

    # --- NSM#1 oficial = Operaciones de Wallet + transferencias Agente de Cobros ---
    # Decisión del usuario (2026-07-23): la palanca TAC se funde al número oficial de NSM#1,
    # todo el histórico y hacia adelante. `nsm1()` de arriba sigue siendo Operaciones-only
    # (se usa para el desglose "por tipo de operación" y el análisis por Organizacion, que
    # no tienen equivalente en la tabla de Collectors) — estos métodos son la fusión.
    def nsm1_oficial(self, estados=(EST_APROBADA,)):
        return _merge_series(self.nsm1(estados=estados), self.tac())

    def nsm1_oficial_out(self):
        return _merge_series(self.nsm1(tipos=set(NSM1_OUT)), self.tac(tipos=set(TAC_OUT)))

    def nsm1_oficial_in(self):
        return _merge_series(self.nsm1(tipos=set(NSM1_IN)), self.tac(tipos=set(TAC_IN)))

    def nsm1_sin_clasificar(self):
        return self.tac(tipos={"NULL"})

    # --- Altas — leading indicators (usuario, 2026-08-04): no suman al volumen de la NSM,
    # pero su crecimiento antecede el de la NSM correspondiente. `vol` y `cant` son iguales
    # acá a propósito (no hay concepto de "monto" en una alta) — el registro de palancas las
    # marca con formato="entero" para no imprimirlas como si fueran pesos.
    def altas_cuentas(self):
        vol, cant = defaultdict(float), defaultdict(float)
        for s, _org, c in self.cuentas:
            vol[s] += c
            cant[s] += c
        return vol, cant

    def altas_comercios(self):
        vol, cant = defaultdict(float), defaultdict(float)
        for s, _ent, c in self.comercios:
            vol[s] += c
            cant[s] += c
        return vol, cant


def _merge_series(*pares):
    """Suma N pares (vol, cant) semana a semana. Usado para fundir Operaciones de Wallet
    con transferencias Agente de Cobros en el total oficial de NSM#1."""
    vol, cant = defaultdict(float), defaultdict(float)
    for v, c in pares:
        for s, x in v.items():
            vol[s] += x
        for s, x in c.items():
            cant[s] += x
    return vol, cant


# --- Registro de palancas ----------------------------------------------------
# Pedido del usuario (2026-08-04): el reporte y el email tratan a cada palanca del árbol de
# oportunidades con el mismo rigor que a las dos NSM — WoW, MoM y detectores — en vez de
# líneas de texto sueltas con solo volumen y WoW. Este registro es la ÚNICA fuente de verdad:
# de acá comen el desglose impreso de `analyze`, `_detectar_palancas` y el JSON de
# `cmd_palancas` (insumo del renderer de cards del email). Antes cada uno de esos tres
# caminos recalculaba su propia serie por su cuenta y podían divergir.
def registro_palancas():
    """Devuelve la lista de todas las palancas de las dos NSM, construida programáticamente
    desde los dicts de negocio que ya existen arriba (NSM1_TIPOS, TAC_TIPOS, NSM2_TIPOS,
    NSM2_FORMAS, INDIRECTAS_NSM1, FUERA_PAYWAY_NSM2) — cero duplicación de definiciones de
    negocio. Se reconstruye una vez por corrida (barata: solo arma closures).

    Cada entrada:
      id                slug estable — clave del JSON y de los detectores
      nombre            display, ya en español
      nsm               NSM padre: "NSM#1" | "NSM#2"
      categoria         agrupador para impresión/filtrado (ver tabla en SKILL.md)
      suma              ¿este volumen está DENTRO del número que se reporta como la NSM?
                         None para las 2 entradas raíz (nsm1/nsm2), que no "suman a sí mismas"
      eje                partición: las palancas del mismo eje son mutuamente excluyentes y
                         suman el 100% de su `padre` — evita doble conteo (ver gotcha abajo)
      padre             id de la palanca/NSM contra la que se calcula el share (NO siempre es
                         la NSM — ver gotcha abajo)
      serie             callable(d) -> (vol, cant)
      ocultar_si_vacia  no imprimir/tarjetear si no tuvo volumen ni en la semana actual ni en
                        las últimas 8 (palancas de contexto que a veces están en $0)
      nota              sufijo textual para el hallazgo/card (contexto de por qué no suma, etc.)

    GOTCHA — doble conteo por `eje`: canal_nsm2 y medio_pago_nsm2 son DOS particiones
    INDEPENDIENTES del mismo total de NSM#2 (cada una suma el 100% por su cuenta). Sumar
    "todas las palancas con suma=True" de una NSM sin agrupar por `eje` cuenta el volumen dos
    veces. Ídem NSM#1 con componente_nsm1 (Wallet vs. TAC) vs. split_in_out vs.
    sin_clasificar+lado — son tres cortes distintos del mismo número oficial.

    GOTCHA — `padre` no siempre es la NSM: los tipos de Wallet se reportan como % de
    Operaciones (no del total oficial fusionado) y los tipos de TAC como % de TAC — así está
    impreso desde el 2026-07-23 y el usuario lee esos % como "composición de esta fuente", no
    "peso sobre la NSM". No cambiarlo sin preguntarle."""
    reg = []

    # nombre_hallazgo: los 3 agregados que YA tenían detector antes del registro (2026-07-27
    # y anteriores) usan estos strings literales en el texto del hallazgo — se preservan acá
    # para no romper la paridad con lo que el usuario ya viene leyendo cada semana.
    reg.append({"id": "nsm1", "nombre": "NSM#1", "nombre_hallazgo": "NSM#1 API BANK (oficial)",
               "nsm": "NSM#1", "categoria": "nsm", "suma": None, "eje": None, "padre": None,
               "serie": lambda d: d.nsm1_oficial(), "ocultar_si_vacia": False, "nota": ""})
    reg.append({"id": "nsm2", "nombre": "NSM#2", "nombre_hallazgo": "NSM#2 Payway",
               "nsm": "NSM#2", "categoria": "nsm", "suma": None, "eje": None, "padre": None,
               "serie": lambda d: d.nsm2(), "ocultar_si_vacia": False, "nota": ""})

    reg.append({"id": "nsm1_wallet", "nombre": "Operaciones (Wallet)", "nsm": "NSM#1",
               "categoria": "componente_nsm1", "suma": True, "eje": "nsm1_fuente",
               "padre": "nsm1", "serie": lambda d: d.nsm1(),
               "ocultar_si_vacia": False, "nota": ""})
    reg.append({"id": "nsm1_tac", "nombre": "Transferencias Agente de Cobros",
               "nombre_hallazgo": "TAC Agente de Cobros (componente)", "nsm": "NSM#1",
               "categoria": "componente_nsm1", "suma": True, "eje": "nsm1_fuente",
               "padre": "nsm1", "serie": lambda d: d.tac(),
               "ocultar_si_vacia": False, "nota": ""})

    reg.append({"id": "nsm1_out", "nombre": "OUT", "nsm": "NSM#1", "categoria": "split_in_out",
               "suma": True, "eje": "nsm1_lado", "padre": "nsm1",
               "serie": lambda d: d.nsm1_oficial_out(), "ocultar_si_vacia": False, "nota": ""})
    reg.append({"id": "nsm1_in", "nombre": "IN", "nsm": "NSM#1", "categoria": "split_in_out",
               "suma": True, "eje": "nsm1_lado", "padre": "nsm1",
               "serie": lambda d: d.nsm1_oficial_in(), "ocultar_si_vacia": False, "nota": ""})
    reg.append({"id": "nsm1_sin_clasificar", "nombre": "Sin clasificar", "nsm": "NSM#1",
               "categoria": "sin_clasificar", "suma": True, "eje": "nsm1_lado", "padre": "nsm1",
               "serie": lambda d: d.nsm1_sin_clasificar(), "ocultar_si_vacia": True,
               "nota": "Type=NULL, probable error de origen; suma al total oficial de todas "
                       "formas (decisión del usuario, 2026-07-23) — ver ../../../../wiki/2_areas/gaps_y_preguntas.md"})

    for t, nom in sorted(NSM1_TIPOS.items()):
        reg.append({"id": "nsm1_tipo_{}".format(t), "nombre": nom, "nsm": "NSM#1",
                   "categoria": "tipo_operacion_wallet", "suma": True, "eje": "nsm1_tipo",
                   "padre": "nsm1_wallet", "serie": lambda d, t=t: d.nsm1(tipos={t}),
                   "ocultar_si_vacia": False, "nota": ""})

    for t, nom in sorted(TAC_TIPOS.items()):
        reg.append({"id": "tac_tipo_{}".format(t), "nombre": nom, "nsm": "NSM#1",
                   "categoria": "tipo_tac", "suma": True, "eje": "tac_tipo",
                   "padre": "nsm1_tac", "serie": lambda d, t=t: d.tac(tipos={t}),
                   "ocultar_si_vacia": False, "nota": ""})

    for etiqueta, tipos in (("Saliente", TAC_OUT), ("Entrante", TAC_IN)):
        reg.append({"id": "tac_lado_{}".format(etiqueta.lower()), "nombre": etiqueta,
                   "nsm": "NSM#1", "categoria": "split_in_out_tac", "suma": True,
                   "eje": "tac_lado", "padre": "nsm1_tac",
                   "serie": lambda d, tipos=set(tipos): d.tac(tipos=tipos),
                   "ocultar_si_vacia": False, "nota": ""})

    for t, nom in sorted(INDIRECTAS_NSM1.items()):
        # nota_corta: el hallazgo de TENDENCIA de esta categoría venía con el sufijo corto
        # desde _palancas_secundarias (solo "no suma a NSM#1"); el de CAMBIO DE NIVEL siempre
        # tuvo la frase completa. Se preservan los dos literales para no romper la paridad.
        reg.append({"id": "indirecta_{}".format(t), "nombre": nom, "nsm": "NSM#1",
                   "categoria": "palanca_indirecta", "suma": False, "eje": None,
                   "padre": "nsm1", "serie": lambda d, t=t: d.nsm1(tipos={t}),
                   "ocultar_si_vacia": True, "nota_corta": "no suma a NSM#1",
                   "nota": "no suma a NSM#1, pero alimenta el saldo que después opera "
                           "contra el banco"})

    for t, nom in sorted(NSM2_TIPOS.items()):
        reg.append({"id": "nsm2_canal_{}".format(t), "nombre": nom, "nsm": "NSM#2",
                   "categoria": "canal_nsm2", "suma": True, "eje": "nsm2_canal",
                   "padre": "nsm2", "serie": lambda d, t=t: d.nsm2(tipos={t}),
                   "ocultar_si_vacia": False, "nota": ""})

    for f, nom in sorted(NSM2_FORMAS.items()):
        reg.append({"id": "nsm2_medio_{}".format(f), "nombre": nom, "nsm": "NSM#2",
                   "categoria": "medio_pago_nsm2", "suma": True, "eje": "nsm2_medio",
                   "padre": "nsm2", "serie": lambda d, f=f: d.nsm2(formas={f}),
                   "ocultar_si_vacia": False, "nota": ""})

    for t, nom in sorted(FUERA_PAYWAY_NSM2.items()):
        reg.append({"id": "fuera_payway_{}".format(t), "nombre": nom, "nsm": "NSM#2",
                   "categoria": "fuera_payway", "suma": False, "eje": None, "padre": "nsm2",
                   "serie": lambda d, t=t: d.nsm2(tipos={t}, formas=set(DIM_FORMA_PAGO)),
                   "ocultar_si_vacia": True, "nota": "fuera del scope de NSM#2 hoy"})

    # Leading indicators (usuario, 2026-08-04): no suman al volumen — son cantidad de altas,
    # no pesos — pero su crecimiento antecede el de la NSM correspondiente (más cuentas/
    # comercios activos hoy = más volumen mañana). "formato": "entero" evita que se impriman
    # como si fueran montos en pesos (fmt_m dividiría por 1.000.000 y mostraría "$0,03 M" en
    # vez de "30.075").
    reg.append({"id": "altas_cuentas", "nombre": "Cuentas de Wallet creadas", "nsm": "NSM#1",
               "categoria": "leading_indicator", "suma": False, "eje": None, "padre": "nsm1",
               "serie": lambda d: d.altas_cuentas(), "ocultar_si_vacia": False,
               "formato": "entero",
               "nota": "no suma directo al volumen, pero su crecimiento antecede el de NSM#1"})
    reg.append({"id": "altas_comercios", "nombre": "Comercios de Adquirencia creados",
               "nsm": "NSM#2", "categoria": "leading_indicator", "suma": False, "eje": None,
               "padre": "nsm2", "serie": lambda d: d.altas_comercios(),
               "ocultar_si_vacia": False, "formato": "entero",
               "nota": "no suma directo al volumen, pero su crecimiento antecede el de NSM#2"})

    return reg


# --- Métricas derivadas -----------------------------------------------------
def serie(vol, semanas):
    return [vol.get(s, 0.0) for s in semanas]


def tendencia(vals):
    """Pendiente relativa (%/semana) de una regresión lineal simple sobre la ventana."""
    n = len(vals)
    if n < 3 or not any(vals):
        return None
    mx = (n - 1) / 2.0
    my = sum(vals) / n
    den = sum((i - mx) ** 2 for i in range(n))
    if not den or not my:
        return None
    b = sum((i - mx) * (v - my) for i, v in enumerate(vals)) / den
    return b / my * 100.0


def zscore(actual, previos):
    if len(previos) < 4:
        return None
    mu = statistics.mean(previos)
    sd = statistics.pstdev(previos)
    if not sd:
        return None
    return (actual - mu) / sd


def bloque_nsm(nombre, vol, cant, semanas, actual):
    i = semanas.index(actual)
    hist = serie(vol, semanas[: i + 1])
    v = hist[-1]
    prev = hist[-2] if len(hist) > 1 else None
    m4 = statistics.mean(hist[-5:-1]) if len(hist) >= 5 else None
    m13 = statistics.mean(hist[-14:-1]) if len(hist) >= 14 else None
    mx = max(hist)
    return {
        "nombre": nombre, "volumen": v, "cantidad": cant.get(actual, 0.0),
        "wow": pct_change(v, prev) if prev else None,
        "vs_m4": pct_change(v, m4) if m4 else None,
        "vs_m13": pct_change(v, m13) if m13 else None,
        "max": mx, "vs_max": pct_change(v, mx) if mx else None,
        "semana_max": semanas[hist.index(mx)],
        "tendencia6": tendencia(hist[-6:]),
        "z": zscore(v, hist[-9:-1]),
        "ticket": (v / cant[actual]) if cant.get(actual) else 0.0,
        "baseline13": m13, "serie": hist,
    }


# --- Vista mensual (MoM) -----------------------------------------------------
# La NSM se sigue reportando semana a semana (WoW) como KPI principal — es el número más
# cercano y el que más importa mirar. La vista mensual (MoM) es contexto adicional, porque
# el objetivo de mercado de ambas NSM se va a expresar en volumen mensual (usuario,
# 2026-07-22).
#
# MoM se mide SIEMPRE "en el mismo punto del mes anterior en semanas" (decisión del
# usuario, 2026-07-22): si el mes en curso lleva 3 semanas cerradas, se compara la suma de
# esas 3 semanas contra la suma de las primeras 3 semanas del mes anterior — nunca mes
# completo contra mes completo, que compararía cosas de distinto tamaño. Para simplificar,
# un mes nunca aporta más de 4 semanas a esta comparación (1 mes = 4 semanas), aunque el
# calendario real a veces le asigne una quinta.
#
# Una semana se asigna al mes que contiene su JUEVES (misma convención que ISO usa para
# asignar una semana a un año: el jueves es el día "central" de una semana Lunes-Domingo,
# así que "el mes que tiene más días de esa semana" y "el mes del jueves" coinciden). Esto
# solo importa para AGRUPAR y ETIQUETAR ("junio", "julio") — la comparación en sí siempre
# es por tramo de semanas, nunca por mes calendario completo.
TRAMO_MAX = 4  # "1 mes = 4 semanas para simplificar" (decisión del usuario, 2026-07-22)


# Cache de módulo: con el registro de palancas, `mes_de` pasa de llamarse ~1 vez por semana
# a ~1 vez por semana POR PALANCA (medir_palancas llama bloque_mensual para cada una). El
# mapa semana->mes es inmutable dentro de una corrida (`sem` sale del store una sola vez, en
# Datos.__init__), así que cachear por SemanaId es seguro y evita repetir el strptime.
_MES_CACHE = {}


def mes_de(semana_id, sem):
    if semana_id not in _MES_CACHE:
        d = datetime.strptime(sem[semana_id]["inicio"][:10], "%Y-%m-%d").date() + timedelta(days=3)
        _MES_CACHE[semana_id] = "{:04d}-{:02d}".format(d.year, d.month)
    return _MES_CACHE[semana_id]


def a_mensual(vol_semanal, cant_semanal, semanas_scope, sem):
    """Agrupa las series semanales (ya recortadas a las semanas que corresponda — hasta la
    semana `actual` de la corrida, no necesariamente todo el store) por mes calendario.
    Devuelve meses ordenados, volumen y cantidad por mes (mes completo, para la serie
    histórica del anexo), y qué semanas componen cada mes en orden cronológico (para
    poder recortar cualquier mes al mismo tramo de N semanas)."""
    por_mes = defaultdict(list)
    for s in semanas_scope:
        por_mes[mes_de(s, sem)].append(s)
    for m in por_mes:
        por_mes[m].sort(key=int)
    meses = sorted(por_mes)
    vol_mes = {m: sum(vol_semanal.get(s, 0.0) for s in por_mes[m]) for m in meses}
    cant_mes = {m: sum(cant_semanal.get(s, 0.0) for s in por_mes[m]) for m in meses}
    return meses, vol_mes, cant_mes, por_mes


def _tramo(vol_semanal, por_mes, m, k):
    """Suma de las primeras k semanas (cronológicas) del mes m. None si ese mes no tiene
    al menos k semanas — no tiene sentido comparar un tramo que no existe."""
    sems = por_mes[m][:k]
    if len(sems) < k:
        return None
    return sum(vol_semanal.get(s, 0.0) for s in sems)


def bloque_mensual(nombre, vol_semanal, cant_semanal, semanas_scope, sem):
    meses, vol_mes, cant_mes, por_mes = a_mensual(vol_semanal, cant_semanal, semanas_scope, sem)
    if len(meses) < 2:
        return None
    actual, anterior = meses[-1], meses[-2]
    k = min(TRAMO_MAX, len(por_mes[actual]))  # semanas informadas del mes en curso

    tramo_actual = _tramo(vol_semanal, por_mes, actual, k)
    tramo_anterior = _tramo(vol_semanal, por_mes, anterior, k)
    mom = pct_change(tramo_actual, tramo_anterior) if tramo_anterior else None

    # Baseline y máximo también se miden por tramo de k semanas (mismo criterio de
    # comparación: nunca mes completo contra un recorte parcial) sobre los meses previos
    # al actual — el actual todavía puede estar en curso, no cuenta como "histórico".
    historicos = meses[:-1]
    tramos_hist = [(m, _tramo(vol_semanal, por_mes, m, k)) for m in historicos]
    tramos_hist = [(m, v) for m, v in tramos_hist if v is not None]
    vals_hist = [v for _, v in tramos_hist]
    baseline = statistics.mean(vals_hist[-3:]) if len(vals_hist) >= 3 else \
        (statistics.mean(vals_hist) if vals_hist else None)
    maximo = max(vals_hist) if vals_hist else None
    mes_max = tramos_hist[vals_hist.index(maximo)][0] if maximo is not None else None

    return {
        "nombre": nombre,
        "mes_actual": actual, "mes_anterior": anterior, "k": k,
        "es_mes_en_curso": len(por_mes[actual]) < TRAMO_MAX,
        # Acotado a las mismas k semanas que el resto del bloque — si no, "acumulado a la
        # fecha" y el MoM de abajo mostrarían dos recortes distintos del mismo mes y el
        # reporte se leería inconsistente (ej. un mes real de 5 semanas mezclando un
        # acumulado de 5 con una comparación de 4).
        "volumen_acumulado": tramo_actual,
        "cantidad_acumulada": _tramo(cant_semanal, por_mes, actual, k),
        "tramo_actual": tramo_actual, "tramo_anterior": tramo_anterior,
        "mom": mom,
        "baseline3": baseline, "vs_baseline3": pct_change(tramo_actual, baseline) if baseline else None,
        "maximo": maximo, "mes_max": mes_max,
        "vs_max": pct_change(tramo_actual, maximo) if maximo else None,
        "serie_meses": [(m, vol_mes[m]) for m in meses],
        "meses_en_curso": {actual},  # el último mes de la serie siempre puede sumar más semanas
    }


# --- Tendencia de ventana móvil (reemplaza al "MoM" mensual-calendario como protagonista) --
# Decisión del usuario, 2026-08-04: comparar "julio vs. junio" mezclaba mal la ETIQUETA (mes
# calendario) con el CÁLCULO real (un tramo de hasta TRAMO_MAX semanas, capado) — un mes de 5
# semanas ISO (como julio 2026, con la 202631) dejaba el número "congelado" varias semanas
# seguidas porque la 5ª semana no entraba al tramo, y alguien mirando el reporte sin conocer
# ese detalle podía leer "$1.070.467 M" como si fuera la facturación real y cerrada de julio
# — no lo es. Se reemplaza por una VENTANA MÓVIL pura, sin relación a mes calendario: compara
# las últimas `ventana` semanas cerradas contra las `ventana` semanas anteriores a esas. Se
# actualiza todas las semanas (nunca se congela) y no necesita ningún nombre de mes — es
# "últimas N semanas" vs. "N semanas previas", que no se puede confundir con un cierre
# contable mensual. `bloque_mensual` no se elimina: sigue alimentando la serie mensual
# completa del anexo (magnitud absoluta por mes, mes completo vs. mes completo), que es
# información histórica de contexto, no el número protagonista.
VENTANA_TENDENCIA = 4  # semanas por bloque de la ventana móvil


def bloque_movil(nombre, vol, semanas, actual, ventana=VENTANA_TENDENCIA):
    """Ventana móvil de `ventana` semanas: suma las últimas `ventana` semanas cerradas hasta
    `actual` (inclusive) y la compara contra las `ventana` semanas inmediatamente anteriores.
    None si no hay historia suficiente para dos ventanas completas (2*ventana semanas)."""
    i = semanas.index(actual)
    if i + 1 < ventana * 2:
        return None
    semanas_actual = semanas[i + 1 - ventana: i + 1]
    semanas_previa = semanas[i + 1 - ventana * 2: i + 1 - ventana]
    v_actual = sum(vol.get(s, 0.0) for s in semanas_actual)
    v_previa = sum(vol.get(s, 0.0) for s in semanas_previa)
    return {
        "nombre": nombre, "ventana": ventana,
        "semanas_actual": semanas_actual, "semanas_previa": semanas_previa,
        "acumulado": v_actual, "acumulado_previo": v_previa,
        "tendencia": pct_change(v_actual, v_previa) if v_previa else None,
    }


def medir_palancas(d, actual):
    """Una sola pasada por `registro_palancas()`: para cada palanca calcula el bloque semanal
    (WoW, z, tendencia6, vs. baseline, ...) Y el mensual (MoM por tramo), más su share contra
    `padre`. Es la ÚNICA fuente de verdad de la que comen el desglose impreso de `analyze`,
    `_detectar_palancas` y el JSON de `cmd_palancas` — antes cada camino recalculaba su propia
    serie por su cuenta y podían divergir. Devuelve un dict ordenado id -> registro (el orden
    es el de `registro_palancas()`, que ya es el orden de impresión/tarjeteo deseado).

    `scope` = d.semanas[:i+1], NUNCA d.semanas completo: un `analyze`/`palancas` de una semana
    vieja no puede mostrar meses que en ese momento todavía no habían pasado — mismo gotcha
    que ya tenía `bloque_mensual` para las dos NSM (2026-07-22, línea de cmd_analyze), ahora
    aplica a todas las palancas y el recorte se hace acá una sola vez.

    Nota de performance: esto BAJA el trabajo total, no lo sube. Antes cada palanca se
    recalculaba 2 o 3 veces (desglose impreso + detector, a veces + `_mix`); ahora se mide
    una sola vez y todo lo demás lee de este dict."""
    i = d.semanas.index(actual)
    scope = d.semanas[: i + 1]
    recs = {}
    for p in registro_palancas():
        vol, cant = p["serie"](d)
        b = bloque_nsm(p["nombre"], vol, cant, d.semanas, actual)
        bm = bloque_mensual(p["nombre"], vol, cant, scope, d.sem)
        bmov = bloque_movil(p["nombre"], vol, d.semanas, actual)
        rec = {k: v for k, v in p.items() if k != "serie"}
        rec["semanal"], rec["mensual"], rec["movil"] = b, bm, bmov
        rec["vol_semanal"], rec["cant_semanal"] = vol, cant
        recs[p["id"]] = rec
    # segunda pasada: los padres ya están medidos, ahora se puede calcular el share
    for rec in recs.values():
        padre = rec.get("padre")
        rec["share"] = _share(rec["semanal"]["volumen"], recs[padre]["semanal"]["volumen"]) \
            if padre and padre in recs else None
    return recs


def print_bloque_movil(m):
    if m is None:
        print("  Todavía no hay {} semanas de historia previa — tendencia disponible más "
              "adelante.".format(VENTANA_TENDENCIA * 2))
        return
    print("  Últimas {} semanas ({} → {}) . {}".format(
        m["ventana"], m["semanas_actual"][0], m["semanas_actual"][-1], fmt_m(m["acumulado"])))
    print("  {} semanas previas ({} → {}) . {}".format(
        m["ventana"], m["semanas_previa"][0], m["semanas_previa"][-1], fmt_m(m["acumulado_previo"])))
    print("  Tendencia ............... {}".format(fmt_pct(m["tendencia"])))
    print("  NOTA: esto NO es un cierre de mes calendario — es una ventana móvil de {} "
          "semanas cerradas.".format(m["ventana"]))


def print_bloque_mensual(b):
    if b is None:
        print("  Todavía no hay al menos 2 meses con datos — vista mensual disponible")
        print("  más adelante (necesita más historia).")
        return
    curso = " (en curso, {} de ~4 semanas)".format(b["k"]) if b["es_mes_en_curso"] else ""
    print("  Mes actual .............. {}{}".format(b["mes_actual"], curso))
    print("  Acumulado a la fecha .... {}".format(fmt_m(b["volumen_acumulado"])))
    print("  Operaciones acumuladas .. {}".format(fmt_n(b["cantidad_acumulada"])))
    print("  MoM ({} sem. vs. mismas {} sem. de {}) . {}  (esas semanas de {} sumaron {})"
          .format(b["k"], b["k"], b["mes_anterior"], fmt_pct(b["mom"]), b["mes_anterior"],
                  fmt_m(b["tramo_anterior"]) if b["tramo_anterior"] else "s/d"))
    print("  vs. baseline 3 meses .... {}  (baseline {}, tramo de {} semanas)"
          .format(fmt_pct(b["vs_baseline3"]),
                  fmt_m(b["baseline3"]) if b["baseline3"] else "s/d", b["k"]))
    print("  vs. máximo histórico .... {}  (máx {} en {}, mismo tramo)"
          .format(fmt_pct(b["vs_max"]), fmt_m(b["maximo"]) if b["maximo"] else "s/d",
                  b["mes_max"] or "s/d"))
    print("  Objetivo ................ PENDIENTE — cuando el usuario aporte el volumen")
    print("                            mensual de mercado, esta fila pasa a ser el % real")
    print("                            de avance hacia top 2 / top 6.")


def print_serie_mensual(b):
    print("  {:<9} {:>16}  {:>9}".format("Mes", "Volumen total", "MoM*"))
    serie = b["serie_meses"]
    for i, (m, v) in enumerate(serie):
        mom = pct_change(v, serie[i - 1][1]) if i else None
        etiqueta = m + ("**" if m in b.get("meses_en_curso", ()) else "")
        print("  {:<9} {:>16}  {:>9}".format(etiqueta, fmt_m(v), fmt_pct(mom)))
    print("  (*) esta columna es mes completo vs. mes completo, solo para ver la magnitud")
    print("      absoluta de cada mes — el MoM de la vista principal de arriba es por")
    print("      tramo de semanas, más preciso para el mes en curso.")
    if b.get("meses_en_curso"):
        print("  (**) mes en curso, todavía no cerraron todas sus semanas")


def print_bloque(b):
    print("  Volumen semana ......... {}".format(fmt_m(b["volumen"])))
    print("  Operaciones ............ {}".format(fmt_n(b["cantidad"])))
    print("  Ticket promedio ........ ${}".format(fmt_n(b["ticket"])))
    print("  WoW .................... {}".format(fmt_pct(b["wow"])))
    print("  vs. promedio 4 semanas . {}".format(fmt_pct(b["vs_m4"])))
    print("  vs. baseline 13 semanas  {}  (baseline {})"
          .format(fmt_pct(b["vs_m13"]), fmt_m(b["baseline13"]) if b["baseline13"] else "s/d"))
    print("  vs. máximo histórico ... {}  (máx {} en {})"
          .format(fmt_pct(b["vs_max"]), fmt_m(b["max"]), b["semana_max"]))
    print("  Tendencia 6 semanas .... {} por semana"
          .format(fmt_pct(b["tendencia6"]) if b["tendencia6"] is not None else "s/d"))
    print("  z-score vs. 8 previas .. {}"
          .format("{:+.2f}".format(b["z"]) if b["z"] is not None else "s/d"))
    print("  Objetivo ............... PENDIENTE — el valor de mercado (top 2 API BANK /")
    print("                           top 6 Payway) todavía no se conoce; ver north_star.md")


# --- Detectores de hallazgos ------------------------------------------------
def detectar(d, actual, recs=None):
    """Emite CANDIDATOS a hallazgo con reglas explícitas. El pipeline detecta; la lectura
    de negocio (por qué pasó, qué hacer) la pone Claude — nunca al revés, y nunca se
    inventa la causa: si no hay explicación en la wiki, va a ../../../../wiki/2_areas/gaps_y_preguntas.md.

    `recs` es opcional (medir_palancas(d, actual) si no se pasa) para que un caller que ya
    los tiene medidos —cmd_analyze y cmd_palancas— no los recalcule dos veces."""
    h = []
    sems = d.semanas
    i = sems.index(actual)
    prev = sems[max(0, i - 8): i]
    if recs is None:
        recs = medir_palancas(d, actual)

    # 1) Cambio de nivel y tendencia sobre TODO el registro de palancas — las dos NSM, sus
    # componentes (Wallet/TAC), el núcleo (tipos de operación, tipos de TAC, IN/OUT, canales
    # y formas de pago de NSM#2) y las palancas de contexto (indirectas de NSM#1, fuera de
    # Payway). Monitoreo total, reporte selectivo (usuario, 2026-07-27 — ampliado al núcleo
    # 2026-08-04): el pipeline corre esto sobre cada palanca en cada `analyze`, pero solo
    # entra al reporte/email la que cruza su piso de materialidad. Silencio es la respuesta
    # esperada la semana que no hay nada raro.
    h += _detectar_palancas(d, actual, prev, recs)

    # 2) Mix IN/OUT (NSM#1) y Botón Simple vs 2.0 (NSM#2)
    h += _mix(d, actual, prev)

    # 3) Churn y activación de clientes
    h += _churn(d, actual, prev)

    # 4) Concentración de riesgo
    h += _concentracion(d, actual)

    # 5) Calidad: rechazos y devoluciones
    h += _calidad(d, actual, prev)

    # 6) Altas de cuentas y comercios
    h += _altas(d, actual, prev)

    orden = {"Alta": 0, "Media": 1, "Baja": 2}
    return sorted(h, key=lambda x: orden[x["severidad"]])


def _h(sev, tipo, texto, palanca_id=None):
    return {"severidad": sev, "tipo": tipo, "texto": texto, "palanca_id": palanca_id}


def _mix(d, actual, prev):
    h = []
    out_v, _ = d.nsm1_oficial_out()
    in_v, _ = d.nsm1_oficial_in()
    tot = out_v.get(actual, 0) + in_v.get(actual, 0)
    sh_now = _share(out_v.get(actual, 0), tot)
    prev_sh = [_share(out_v.get(s, 0), out_v.get(s, 0) + in_v.get(s, 0)) for s in prev
               if (out_v.get(s, 0) + in_v.get(s, 0))]
    if prev_sh and abs(sh_now - statistics.mean(prev_sh)) >= 5:
        h.append(_h("Media", "Mix shift",
                    "NSM#1 (oficial): el OUT pasó a ser {:.1f}% del volumen (media 8 semanas "
                    "{:.1f}%) — se movió el balance IN/OUT".format(sh_now, statistics.mean(prev_sh))))
    bs, _ = d.nsm2(tipos={6})
    b20, _ = d.nsm2(tipos={7})
    tot2 = bs.get(actual, 0) + b20.get(actual, 0)
    sh20 = _share(b20.get(actual, 0), tot2)
    prev20 = [_share(b20.get(s, 0), bs.get(s, 0) + b20.get(s, 0)) for s in prev
              if (bs.get(s, 0) + b20.get(s, 0))]
    if prev20 and abs(sh20 - statistics.mean(prev20)) >= 5:
        h.append(_h("Media", "Mix shift",
                    "NSM#2: Botón 2.0 es el {:.1f}% del volumen Payway (media 8 semanas "
                    "{:.1f}%) — migración desde Botón Simple".format(sh20, statistics.mean(prev20))))
    tot_nsm2, _ = d.nsm2()
    for fp, nom in sorted(NSM2_FORMAS.items()):
        v, _ = d.nsm2(formas={fp})
        sh = _share(v.get(actual, 0), tot_nsm2.get(actual, 0))
        prv = [_share(v.get(s, 0), tot_nsm2.get(s, 0)) for s in prev if tot_nsm2.get(s, 0)]
        if prv and abs(sh - statistics.mean(prv)) >= 8:
            h.append(_h("Media", "Mix shift",
                        "NSM#2: {} pasó a {:.1f}% del volumen (media 8 semanas {:.1f}%)"
                        .format(nom, sh, statistics.mean(prv))))
    tac_out, _ = d.tac(tipos=set(TAC_OUT))
    tac_in, _ = d.tac(tipos=set(TAC_IN))
    tot_tac = tac_out.get(actual, 0) + tac_in.get(actual, 0)
    sh_tac_now = _share(tac_out.get(actual, 0), tot_tac)
    prev_tac_sh = [_share(tac_out.get(s, 0), tac_out.get(s, 0) + tac_in.get(s, 0)) for s in prev
                   if (tac_out.get(s, 0) + tac_in.get(s, 0))]
    if prev_tac_sh and abs(sh_tac_now - statistics.mean(prev_tac_sh)) >= 5:
        h.append(_h("Media", "Mix shift",
                    "TAC Agente de Cobros: el saliente pasó a ser {:.1f}% del volumen "
                    "(media 8 semanas {:.1f}%) — se movió el balance entrante/saliente"
                    .format(sh_tac_now, statistics.mean(prev_tac_sh))))
    return h


# Piso de materialidad: un cliente tiene que pesar al menos esto sobre el volumen semanal
# de su NSM para que su movimiento sea un hallazgo. Sin este piso, cada semana escupe una
# decena de "caídas del 99%" de organizaciones de test o de cuentas con $3.000 de volumen,
# y el ruido tapa la señal que sí importa.
PISO_MATERIALIDAD = 0.001   # 0,1% del volumen NSM típico: debajo de esto no es negocio
MATERIAL_ALTA = 0.02        # a partir de 2% del volumen, el movimiento del cliente es Alta


def _churn(d, actual, prev):
    """Un cliente que venía operando y se apaga es la señal más cara del negocio (contexto
    Astropay). La inversa —primera semana con volumen— es una activación que hay que
    entender: puede ser el pipeline comercial empezando a operar."""
    h = []
    ult4 = prev[-4:]
    if not ult4:
        return h
    for label, actual_map, hist_fn, nombrador in (
            ("NSM#1", d.nsm1_por_org(actual), d.nsm1_por_org, d.org),
            ("NSM#2", d.nsm2_por_entidad(actual), d.nsm2_por_entidad, d.ent),
            ("TAC", d.tac_por_collector(actual), d.tac_por_collector, d.collector)):
        hist = {s: hist_fn(s) for s in ult4}
        # el piso se calcula sobre el volumen típico de la NSM, no sobre el de esta semana:
        # si la semana se derrumbó, el piso no tiene que derrumbarse con ella
        tipico = statistics.mean([sum(hist[s].values()) for s in ult4] + [sum(actual_map.values())])
        piso = tipico * PISO_MATERIALIDAD
        activos_antes = {k for s in ult4 for k, v in hist[s].items() if v > 0}
        for k in sorted(activos_antes):
            semanas_activo = sum(1 for s in ult4 if hist[s].get(k, 0) > 0)
            v_prev = statistics.mean([hist[s].get(k, 0) for s in ult4])
            if v_prev < piso:
                continue
            # la severidad la da el peso del cliente, no el % de caída: perder el 90% de
            # alguien que mueve el 0,2% del volumen no es lo mismo que perder al top-1
            sev = "Alta" if v_prev >= tipico * MATERIAL_ALTA else "Media"
            if semanas_activo == len(ult4) and actual_map.get(k, 0) == 0:
                h.append(_h(sev, "Churn",
                            "{}: {} operó las 4 semanas previas ({} promedio, {:.1f}% del "
                            "volumen) y esta semana quedó en CERO"
                            .format(label, nombrador(k), fmt_m(v_prev), _share(v_prev, tipico))))
            elif semanas_activo >= 3 and actual_map.get(k, 0):
                caida = pct_change(actual_map[k], v_prev)
                if caida is not None and caida <= -60:
                    h.append(_h(sev, "Caída de cliente",
                                "{}: {} cayó {} vs. su promedio de 4 semanas ({} -> {}, "
                                "{:.1f}% del volumen)"
                                .format(label, nombrador(k), fmt_pct(caida), fmt_m(v_prev),
                                        fmt_m(actual_map[k]), _share(v_prev, tipico))))
        nuevos = [k for k, v in actual_map.items()
                  if v >= piso and k not in activos_antes]
        for k in sorted(nuevos, key=lambda x: -actual_map[x])[:3]:
            h.append(_h("Media", "Activación",
                        "{}: {} generó volumen por primera vez en 5 semanas ({}, {:.1f}% "
                        "del volumen)".format(label, nombrador(k), fmt_m(actual_map[k]),
                                              _share(actual_map[k], tipico))))
    return h


def _concentracion(d, actual):
    h = []
    for label, mapa, nombrador in (("NSM#1", d.nsm1_por_org(actual), d.org),
                                   ("NSM#2", d.nsm2_por_entidad(actual), d.ent),
                                   ("TAC", d.tac_por_collector(actual), d.collector)):
        tot = sum(mapa.values())
        if not tot:
            continue
        top = sorted(mapa.items(), key=lambda kv: -kv[1])
        s1 = _share(top[0][1], tot)
        s3 = _share(sum(v for _, v in top[:3]), tot)
        sev = "Alta" if s1 >= 40 else "Media"
        if s1 >= 30:
            h.append(_h(sev, "Concentración",
                        "{}: {} concentra el {:.1f}% del volumen y el top-3 el {:.1f}% — "
                        "riesgo de dependencia de un solo cliente"
                        .format(label, nombrador(top[0][0]), s1, s3)))
    return h


def _calidad(d, actual, prev):
    """Un salto en la tasa de rechazo suele ser un problema técnico o de procesador antes
    que un problema comercial — por eso se mira separado del volumen."""
    h = []

    def tasa_ops(s, estados):
        num = sum(c for ss, _o, t, e, c, _v in d.ops
                  if ss == s and t in NSM1_TIPOS and e in estados)
        den = sum(c for ss, _o, t, e, c, _v in d.ops if ss == s and t in NSM1_TIPOS)
        return _share(num, den)

    def tasa_trx(s, estados, formas=None):
        formas = formas or set(NSM2_FORMAS)
        num = sum(c for ss, _e, t, f, est, c, _v in d.trx
                  if ss == s and t in NSM2_TIPOS and f in formas and est in estados)
        den = sum(c for ss, _e, t, f, est, c, _v in d.trx
                  if ss == s and t in NSM2_TIPOS and f in formas)
        return _share(num, den)

    def tasa_tac(s, estados):
        num = sum(c for ss, _cid, t, est, c, _v in d.tac_rows
                  if ss == s and t in TAC_TIPOS_TODOS and est in estados)
        den = sum(c for ss, _cid, t, est, c, _v in d.tac_rows if ss == s and t in TAC_TIPOS_TODOS)
        return _share(num, den)

    for label, fn, estados, concepto in (
            ("NSM#1", tasa_ops, {EST_RECHAZADA}, "rechazo"),
            ("NSM#1", tasa_ops, EST_DEVUELTA, "devolución"),
            ("NSM#2", tasa_trx, {EST_RECHAZADA_ADQ}, "rechazo"),
            ("NSM#2", tasa_trx, {EST_DEVUELTA_ADQ}, "devolución"),
            ("TAC", tasa_tac, DIM_TAC_STATUS - TAC_EST_OK, "falla (no COMPLETED)")):
        act = fn(actual, estados)
        base = [fn(s, estados) for s in prev]
        if not base:
            continue
        mu = statistics.mean(base)
        if abs(act - mu) >= 5:
            h.append(_h("Alta", "Calidad",
                        "{}: tasa de {} en {:.1f}% (media 8 semanas {:.1f}%, {:+.1f} pp)"
                        .format(label, concepto, act, mu, act - mu)))
    for fp, nom in sorted(NSM2_FORMAS.items()):
        act = tasa_trx(actual, {EST_RECHAZADA_ADQ}, {fp})
        base = [tasa_trx(s, {EST_RECHAZADA_ADQ}, {fp}) for s in prev]
        if base and act and abs(act - statistics.mean(base)) >= 8:
            h.append(_h("Media", "Calidad",
                        "NSM#2 / {}: rechazo en {:.1f}% (media 8 semanas {:.1f}%)"
                        .format(nom, act, statistics.mean(base))))
    # Detalle por Status individual de TAC (anomalías, aunque solo COMPLETED sume volumen —
    # pedido explícito del usuario, 2026-07-23: "considerar otros estados para reportar
    # anomalías"). Un salto puntual en CREDIT_ERROR/DATA_ERROR/NO_WARRANTY, por ejemplo, no
    # se ve en la tasa agregada "no COMPLETED" de arriba si el resto compensa.
    for est in sorted(DIM_TAC_STATUS - TAC_EST_OK):
        act = tasa_tac(actual, {est})
        base = [tasa_tac(s, {est}) for s in prev]
        if base and act and abs(act - statistics.mean(base)) >= 3:
            h.append(_h("Media", "Calidad",
                        "TAC / Status {}: {:.1f}% de las operaciones (media 8 semanas {:.1f}%)"
                        .format(est, act, statistics.mean(base))))
    return h


def _altas(d, actual, prev):
    """Las altas son el leading indicator del volumen: conectan con el foco Onboarding."""
    h = []
    i_actual = d.semanas.index(actual)
    for label, datos, nombrador in (("Cuentas de wallet", d.cuentas, d.org),
                                    ("Comercios de adquirencia", d.comercios, d.entid)):
        tot = defaultdict(float)
        for s, _k, c in datos:
            tot[s] += c
        act = tot.get(actual, 0)
        base = [tot.get(s, 0) for s in prev]
        if not base:
            continue
        z = zscore(act, base)
        if z is not None and abs(z) >= 2:
            h.append(_h("Alta" if abs(z) >= 3 else "Media", "Altas",
                        "{}: {} altas en la semana (media 8 semanas {}, z={:+.2f})"
                        .format(label, fmt_n(act), fmt_n(statistics.mean(base)), z)))
        # El z-score se cae cuando la ventana tiene un outlier fuerte: un pico aislado
        # infla el desvío y esconde una caída sostenida posterior. La mediana no.
        med = statistics.median(base)
        delta = pct_change(act, med)
        if med and delta is not None and abs(delta) >= 40 and (z is None or abs(z) < 2):
            h.append(_h("Media", "Altas",
                        "{}: {} altas vs. mediana de 8 semanas {} ({}) — el z-score no lo "
                        "marca porque la ventana tiene un pico que infla el desvío"
                        .format(label, fmt_n(act), fmt_n(med), fmt_pct(delta))))
        # Deriva estructural: las altas son el leading indicator del volumen, y una caída
        # sostenida de trimestre no se ve en ninguna ventana de 8 semanas.
        largo = [tot.get(s, 0) for s in d.semanas[max(0, i_actual - 13): i_actual + 1]]
        if len(largo) >= 10:
            reciente = statistics.mean(largo[-4:])
            viejo = statistics.mean(largo[:4])
            drift = pct_change(reciente, viejo)
            if drift is not None and abs(drift) >= 35:
                h.append(_h("Alta" if abs(drift) >= 50 else "Media", "Deriva de altas",
                            "{}: promedio de las últimas 4 semanas {} vs. {} trece semanas "
                            "atrás ({}) — cambio estructural, no ruido semanal"
                            .format(label, fmt_n(reciente), fmt_n(viejo), fmt_pct(drift))))
    return h


# Piso de materialidad por categoría de palanca (usado por _detectar_palancas). Se calcula
# como % del volumen típico de la NSM de referencia (NSM#1 para todo lo que cuelga de ella,
# NSM#2 para lo que cuelga de Payway) — no un número fijo, así una palanca chica pero
# relevante para su familia sí dispara, y el ruido de fondo (unos pocos miles de pesos) no
# infla z-scores sin sentido.
PISO_PALANCA_CORE = 0.001         # 0,1% — palancas que SUMAN al número de la NSM
PISO_PALANCA_SECUNDARIA = 0.005   # 0,5% — palancas de contexto (indirectas / fuera de Payway)
# Los agregados (las 2 NSM y sus 2 componentes, Wallet/TAC) no tienen piso: si se mueven, la
# NSM se movió, punto — no hace falta que superen ningún umbral de tamaño para ser candidato.
PISO_POR_CATEGORIA = {"nsm": 0.0, "componente_nsm1": 0.0}

# Sufijo que se agrega al tipo de hallazgo ("Cambio de nivel" / "Tendencia") para identificar
# de qué familia de palanca se trata. Las categorías ausentes de este dict (nsm, componente_
# nsm1) no llevan sufijo — son los 3 agregados que ya tenían detector desde antes del
# registro y su texto se preserva literal.
_TIPO_SUFIJO_POR_CATEGORIA = {
    "palanca_indirecta": " (palanca indirecta)",
    "fuera_payway": " (fuera de Payway)",
}


def _piso_de(rec):
    """Piso de materialidad, en % del volumen típico de la NSM de referencia. 0,1% para
    palancas que SUMAN al número de la NSM (si se mueven, la NSM se movió, así que son
    materiales por construcción aunque sean chicas); 0,5% para las de contexto (indirectas /
    fuera de Payway), que no forman parte del número reportado y necesitan un volumen mínimo
    para no ser puro ruido. No se baja del todo el piso del núcleo porque TAC_TIPOS tiene
    ramas que arrancaron en $0 y el bucket "Sin clasificar" es errático por definición (es un
    bug de origen) — una serie EXACTAMENTE en $0 ya se auto-silencia (zscore devuelve None
    con sd=0), así que Pull Débito/Crédito, en $0 desde el incidente de marzo 2026, no genera
    ruido, y el día que se reactiven la primera semana con volumen dispara sola, que es justo
    lo que pide este piso."""
    if rec["categoria"] in PISO_POR_CATEGORIA:
        return PISO_POR_CATEGORIA[rec["categoria"]]
    return PISO_PALANCA_CORE if rec["suma"] else PISO_PALANCA_SECUNDARIA


def _detectar_palancas(d, actual, prev, recs):
    """Cambio de nivel (z-score) y tendencia sobre TODO `registro_palancas()` — reemplaza al
    bucle viejo de los 3 agregados (NSM#1, NSM#2, TAC) que vivía en `detectar` y a
    `_palancas_secundarias` (unificada acá el 2026-08-04). Recibe `recs`, ya medidos por
    `medir_palancas` — no recalcula ningún bloque, a diferencia de la versión vieja que
    llamaba `bloque_nsm` una segunda vez por palanca.

    Antes solo los 3 agregados y las palancas indirectas/fuera-de-Payway tenían detector; los
    6 tipos de operación de Wallet, los 3 tipos de TAC, el split IN/OUT (de Wallet y de TAC),
    "Sin clasificar", los 2 canales y las 4 formas de pago de NSM#2 —el NÚCLEO de las dos
    NSM— no tenían ninguno: una caída fuerte en un tipo individual solo aparecía como
    candidato si arrastraba al agregado por encima de z=2. Pedido del usuario (2026-08-04)."""
    h = []
    if not prev:
        return h
    ref_por_nsm = {"NSM#1": recs["nsm1"]["vol_semanal"], "NSM#2": recs["nsm2"]["vol_semanal"]}
    for rec in recs.values():
        piso_pct = _piso_de(rec)
        ref = ref_por_nsm[rec["nsm"]]
        piso_abs = statistics.mean([ref.get(s, 0) for s in prev]) * piso_pct
        base = statistics.mean([rec["vol_semanal"].get(s, 0) for s in prev])
        if base < piso_abs:
            continue

        b = rec["semanal"]
        nombre = rec.get("nombre_hallazgo") or rec["nombre"]
        tipo_sufijo = "" if rec["categoria"] in PISO_POR_CATEGORIA else \
            _TIPO_SUFIJO_POR_CATEGORIA.get(rec["categoria"], " (palanca {})".format(rec["nsm"]))
        texto_sufijo = " — {}".format(rec["nota"]) if rec["nota"] else ""
        # Las palancas de contexto conservan el texto CORTO de tendencia (sin vs. baseline
        # 13s) que ya tenían en _palancas_secundarias — es el que el usuario ya lee cada
        # semana. Los agregados y las palancas nuevas del núcleo llevan la forma larga, que
        # ya usaban los 3 agregados desde antes.
        forma_corta = rec["categoria"] in ("palanca_indirecta", "fuera_payway")

        if b["z"] is not None and abs(b["z"]) >= 2:
            h.append(_h("Alta" if abs(b["z"]) >= 3 else "Media",
                        "Cambio de nivel" + tipo_sufijo,
                        "{}: {} vs. media de 8 semanas (z={:+.2f}, WoW {}){}".format(
                            nombre, fmt_m(b["volumen"]), b["z"], fmt_pct(b["wow"]), texto_sufijo),
                        palanca_id=rec["id"]))
        umbral_tend = 8 if rec["suma"] is False else 5
        if b["tendencia6"] is not None and abs(b["tendencia6"]) >= umbral_tend:
            if forma_corta:
                # Palancas de contexto: la tendencia usa `nota_corta` si existe (palanca
                # indirecta) — el hallazgo de tendencia históricamente no llevaba la frase
                # completa que sí lleva el de cambio de nivel. fuera_payway no define
                # nota_corta porque su nota ya es igual de corta en los dos casos.
                nota_tend = rec.get("nota_corta", rec["nota"])
                sufijo_tend = " — {}".format(nota_tend) if nota_tend else ""
                texto = "{}: tendencia de 6 semanas {} por semana{}".format(
                    nombre, fmt_pct(b["tendencia6"]), sufijo_tend)
            else:
                texto = ("{}: tendencia de 6 semanas en {} por semana (acumulado {} vs. "
                         "baseline 13s){}".format(nombre, fmt_pct(b["tendencia6"]),
                                                  fmt_pct(b["vs_m13"]), texto_sufijo))
            h.append(_h("Media", "Tendencia" + tipo_sufijo, texto, palanca_id=rec["id"]))
    return h


def _visible_palanca(d, rec):
    """Mismo filtro que ya usaban los desgloses de palancas indirectas/fuera-de-Payway antes
    del registro: no mostrar una palanca de contexto que está en $0 y no tuvo nada en las
    últimas 8 semanas — evita que la sección de palancas liste dos docenas de líneas en $0."""
    if not rec.get("ocultar_si_vacia"):
        return True
    if rec["semanal"]["volumen"]:
        return True
    return any(rec["vol_semanal"].get(s) for s in d.semanas[-8:])


def _resolver_semana(d, semana=None):
    """Resuelve qué SemanaId analizar: la pedida (validando que esté cerrada) o la última
    cerrada del store. Compartida por cmd_analyze y cmd_palancas para que las dos elijan
    exactamente la misma semana por default. Devuelve (semana_id, error) — error es None si
    todo salió bien."""
    if not d.semanas:
        return None, "El store no tiene ninguna semana cerrada. Corré 'ingest' primero."
    actual = semana or d.semanas[-1]
    if actual not in d.semanas:
        return None, ("La semana {} no está cerrada en el store. Cerradas: {} .. {}"
                      .format(actual, d.semanas[0], d.semanas[-1]))
    return actual, None


# --- Comando: analyze -------------------------------------------------------
def cmd_analyze(semana=None):
    seed_staging_from_mirror()  # lee la copia de trabajo si hay una corrida de ingest sin
                                 # mergear todavia; si no existe, la siembra desde el espejo
    d = Datos()
    actual, err = _resolver_semana(d, semana)
    if err:
        print("[ABORT] " + err)
        return 1
    i = d.semanas.index(actual)

    print("=" * 78)
    print("ANALYZE — semana {}  ({})".format(actual, d.rango(actual)))
    print("historia disponible: {} semanas cerradas ({} .. {})"
          .format(len(d.semanas), d.semanas[0], d.semanas[-1]))
    parciales = sorted(s for s, x in d.sem.items() if not x["completa"])
    if parciales:
        print("semanas parciales EXCLUIDAS de todo cálculo: " + ", ".join(parciales))
    print("=" * 78)

    v1, c1 = d.nsm1_oficial()
    v2, c2 = d.nsm2()

    print("\n" + "=" * 78)
    print("DETALLE SEMANAL (WoW) — KPI principal: qué pasó esta semana vs. la anterior")
    print("=" * 78)

    # --- NSM #1 (total OFICIAL = Operaciones de Wallet + Transferencias Agente de Cobros,
    # fusión confirmada por el usuario 2026-07-23, ver Datos.nsm1_oficial)
    b1 = bloque_nsm("NSM#1", v1, c1, d.semanas, actual)
    print("\n### NSM #1 — Volumen operado por API BANK (Banco Industrial)")
    print("    Operaciones tipos {} | estado Aprobada  +  Transferencias Agente de Cobros"
          " | estado COMPLETED".format(sorted(NSM1_TIPOS)))
    print_bloque(b1)

    print("\n  Composición del total oficial:")
    v_ops_only, c_ops_only = d.nsm1()
    b_ops = bloque_nsm("Operaciones (Wallet)", v_ops_only, c_ops_only, d.semanas, actual)
    v_tac_only, c_tac_only = d.tac()
    b_tac = bloque_nsm("Transferencias Agente de Cobros", v_tac_only, c_tac_only, d.semanas, actual)
    for bb in (b_ops, b_tac):
        print("    {:<32} {:>16}  ({:5.1f}% del total)  WoW {:>8}"
              .format(bb["nombre"], fmt_m(bb["volumen"]), _share(bb["volumen"], b1["volumen"]),
                      fmt_pct(bb["wow"])))

    print("\n  Desglose IN / OUT (total oficial):")
    for etiqueta, fn in (("OUT", d.nsm1_oficial_out), ("IN", d.nsm1_oficial_in)):
        vv, cc = fn()
        bb = bloque_nsm(etiqueta, vv, cc, d.semanas, actual)
        print("    {:<4} {:>16}  ({:5.1f}% del total)  WoW {:>8}  tend6 {:>8}"
              .format(etiqueta, fmt_m(bb["volumen"]), _share(bb["volumen"], b1["volumen"]),
                      fmt_pct(bb["wow"]), fmt_pct(bb["tendencia6"])))
    vv_nc, cc_nc = d.nsm1_sin_clasificar()
    if vv_nc.get(actual):
        bb_nc = bloque_nsm("Sin clasificar", vv_nc, cc_nc, d.semanas, actual)
        print("    {:<4} {:>16}  ({:5.1f}% del total)  WoW {:>8}  -- TAC Type=NULL, ver "
              "../../../../wiki/2_areas/gaps_y_preguntas.md".format("N/C", fmt_m(bb_nc["volumen"]),
                                            _share(bb_nc["volumen"], b1["volumen"]),
                                            fmt_pct(bb_nc["wow"])))

    print("\n  Por tipo de operación (Wallet — no incluye la palanca TAC, ver detalle abajo):")
    for t, nom in sorted(NSM1_TIPOS.items()):
        vv, cc = d.nsm1(tipos={t})
        bb = bloque_nsm(nom, vv, cc, d.semanas, actual)
        print("    {:<26} {:>16}  ({:5.1f}%)  WoW {:>8}  ops {:>10}"
              .format(nom, fmt_m(bb["volumen"]), _share(bb["volumen"], b_ops["volumen"]),
                      fmt_pct(bb["wow"]), fmt_n(bb["cantidad"])))
    _top(d, "  Top 8 organizaciones (Operaciones/Wallet):", d.nsm1_por_org(actual),
         d.nsm1_por_org(d.semanas[i - 1]) if i else {}, d.org, b_ops["volumen"])

    print("\n  Palancas indirectas (NO suman a la NSM, alimentan el saldo que después opera):")
    for t, nom in sorted(INDIRECTAS_NSM1.items()):
        vv, cc = d.nsm1(tipos={t})
        if not vv.get(actual) and not any(vv.get(s) for s in d.semanas[-8:]):
            continue
        bb = bloque_nsm(nom, vv, cc, d.semanas, actual)
        print("    {:<26} {:>16}  WoW {:>8}  ops {:>10}"
              .format(nom, fmt_m(bb["volumen"]), fmt_pct(bb["wow"]), fmt_n(bb["cantidad"])))

    print("\n  Detalle de Transferencias Agente de Cobros y Pagos (YA incluida en el total")
    print("  oficial de arriba — esto es su desglose interno):")
    print_bloque(b_tac)
    print("\n    Entrante / Saliente:")
    for etiqueta, tipos in (("Saliente", TAC_OUT), ("Entrante", TAC_IN)):
        vv, cc = d.tac(tipos=set(tipos))
        bb = bloque_nsm(etiqueta, vv, cc, d.semanas, actual)
        print("    {:<10} {:>16}  ({:5.1f}% del total)  WoW {:>8}"
              .format(etiqueta, fmt_m(bb["volumen"]), _share(bb["volumen"], b_tac["volumen"]),
                      fmt_pct(bb["wow"])))
    print("\n    Por tipo:")
    for t, nom in sorted(TAC_TIPOS.items()):
        vv, cc = d.tac(tipos={t})
        bb = bloque_nsm(nom, vv, cc, d.semanas, actual)
        print("    {:<26} {:>16}  ({:5.1f}%)  WoW {:>8}  ops {:>10}"
              .format(nom, fmt_m(bb["volumen"]), _share(bb["volumen"], b_tac["volumen"]),
                      fmt_pct(bb["wow"]), fmt_n(bb["cantidad"])))
    if vv_nc.get(actual):
        print("    {:<26} {:>16}  Type=NULL — probable error de origen, pero SUMA al total"
              .format("(sin clasificar)", fmt_m(vv_nc[actual])))
        print("                                          (decisión del usuario, 2026-07-23) — ver ../../../../wiki/2_areas/gaps_y_preguntas.md")
    _top(d, "    Top 8 collectors (TAC):", d.tac_por_collector(actual),
         d.tac_por_collector(d.semanas[i - 1]) if i else {}, d.collector, b_tac["volumen"])

    # --- NSM #2
    v2, c2 = d.nsm2()
    b2 = bloque_nsm("NSM#2", v2, c2, d.semanas, actual)
    print("\n### NSM #2 — Volumen operado con el gateway Payway (cobro NO presente)")
    print("    tipos {} | formas {} | estado ACREDITADO"
          .format(sorted(NSM2_TIPOS), sorted(NSM2_FORMAS)))
    print_bloque(b2)
    print("\n  Por canal:")
    for t, nom in sorted(NSM2_TIPOS.items()):
        vv, cc = d.nsm2(tipos={t})
        bb = bloque_nsm(nom, vv, cc, d.semanas, actual)
        print("    {:<26} {:>16}  ({:5.1f}%)  WoW {:>8}  trx {:>10}"
              .format(nom, fmt_m(bb["volumen"]), _share(bb["volumen"], b2["volumen"]),
                      fmt_pct(bb["wow"]), fmt_n(bb["cantidad"])))
    print("\n  Por medio de pago:")
    for f, nom in sorted(NSM2_FORMAS.items()):
        vv, cc = d.nsm2(formas={f})
        bb = bloque_nsm(nom, vv, cc, d.semanas, actual)
        print("    {:<26} {:>16}  ({:5.1f}%)  WoW {:>8}  trx {:>10}"
              .format(nom, fmt_m(bb["volumen"]), _share(bb["volumen"], b2["volumen"]),
                      fmt_pct(bb["wow"]), fmt_n(bb["cantidad"])))
    _top(d, "  Top 8 entidades (NSM#2):", d.nsm2_por_entidad(actual),
         d.nsm2_por_entidad(d.semanas[i - 1]) if i else {}, d.ent, b2["volumen"])

    print("\n  Adquirencia FUERA de Payway (contexto — el POS presente todavía no pasa por el gateway):")
    for t, nom in sorted(FUERA_PAYWAY_NSM2.items()):
        vv, cc = d.nsm2(tipos={t}, formas=set(DIM_FORMA_PAGO))
        if not vv.get(actual) and not any(vv.get(s) for s in d.semanas[-8:]):
            continue
        bb = bloque_nsm(nom, vv, cc, d.semanas, actual)
        print("    {:<26} {:>16}  WoW {:>8}  trx {:>10}"
              .format(nom, fmt_m(bb["volumen"]), fmt_pct(bb["wow"]), fmt_n(bb["cantidad"])))

    # --- Palancas — cada una atada a su NSM. Protagonista: tendencia de ventana móvil de
    # VENTANA_TENDENCIA semanas (últimas N cerradas vs. las N previas) — reemplaza al "MoM"
    # mensual-calendario (decisión del usuario, 2026-08-04: el tramo mensual se congelaba en
    # meses de 5 semanas ISO y el nombre de mes se prestaba a leerse como cifra de cierre
    # contable exacta, cuando es un tramo capado). El WoW queda como dato secundario. Se mide
    # UNA vez acá con medir_palancas() y se reusa abajo para los hallazgos.
    recs = medir_palancas(d, actual)
    print("\n" + "=" * 78)
    print("PALANCAS — cada una atada a su NSM (tendencia de {} semanas móviles; WoW como dato "
          "secundario)".format(VENTANA_TENDENCIA))
    print("=" * 78)
    for nsm in ("NSM#1", "NSM#2"):
        core = [r for r in recs.values() if r["nsm"] == nsm and r["categoria"] != "nsm"
               and r["suma"] and _visible_palanca(d, r)]
        contexto = [r for r in recs.values() if r["nsm"] == nsm and r["categoria"] != "nsm"
                   and not r["suma"] and _visible_palanca(d, r)]
        print("\n### {}".format(nsm))
        for grupo, etiqueta in ((core, "que suman al total"), (contexto, "de contexto")):
            if not grupo:
                continue
            print("\n  Palancas {}:".format(etiqueta))
            for r in sorted(grupo, key=lambda r: -r["semanal"]["volumen"]):
                padre_nom = recs[r["padre"]]["nombre"] if r["padre"] in recs else "-"
                fmt = r.get("formato", "monto")
                mv = r["movil"]
                tend_txt = fmt_pct(mv["tendencia"]) if mv else "s/d"
                tend_ant = fmt_valor(mv["acumulado_previo"], fmt) if mv else "s/d"
                print("    {:<32} {:>14}  ({:5.1f}% de {})  Tend {:>8} (prev. {})  WoW {:>8}"
                      .format(r["nombre"][:32], fmt_valor(r["semanal"]["volumen"], fmt),
                              r["share"] or 0.0, padre_nom, tend_txt, tend_ant,
                              fmt_pct(r["semanal"]["wow"])))
                if r["nota"]:
                    print("        {}".format(r["nota"]))

    # --- Salud y altas
    print("\n### Métricas de salud (no suman al volumen NSM)")
    _salud(d, actual, i)

    print("\n### Altas (leading indicator del volumen)")
    _altas_print(d, actual, i)

    # --- Tendencia de ventana móvil — protagonista (reemplaza a "VISTA MENSUAL (MoM)",
    # decisión del usuario 2026-08-04, ver comentario de bloque_movil). Sin nombre de mes: no
    # se puede confundir con un cierre contable exacto.
    mv1, mv2 = recs["nsm1"]["movil"], recs["nsm2"]["movil"]
    print("\n" + "=" * 78)
    print("TENDENCIA — ventana móvil de {} semanas (últimas {} cerradas vs. las {} previas; "
          "NO es un cierre mensual, ver nota de metodología)".format(
              VENTANA_TENDENCIA, VENTANA_TENDENCIA, VENTANA_TENDENCIA))
    print("=" * 78)
    print("\n### NSM #1 · Volumen API BANK")
    print_bloque_movil(mv1)
    print("\n### NSM #2 · Volumen Payway")
    print_bloque_movil(mv2)

    # --- Serie mensual completa (mes completo vs. mes completo) — SOLO contexto histórico de
    # magnitud absoluta, ya no es la base del número protagonista.
    semanas_hasta_actual = d.semanas[: i + 1]
    bm1 = bloque_mensual("NSM#1", v1, c1, semanas_hasta_actual, d.sem)
    bm2 = bloque_mensual("NSM#2", v2, c2, semanas_hasta_actual, d.sem)
    print("\n--- Serie mensual completa (mes completo vs. mes completo, solo contexto histórico"
          " — NO es la base de la tendencia de arriba) — NSM #1 ---")
    if bm1:
        print_serie_mensual(bm1)
    print("\n--- Serie mensual completa (mes completo vs. mes completo, solo contexto histórico"
          " — NO es la base de la tendencia de arriba) — NSM #2 ---")
    if bm2:
        print_serie_mensual(bm2)

    # --- Serie completa para graficar/narrar
    print("\n### Serie semanal completa (volumen NSM, millones ARS)")
    print("    {:<9} {:>14} {:>9} {:>14} {:>9}".format("Semana", "NSM#1", "WoW", "NSM#2", "WoW"))
    for j, s in enumerate(d.semanas):
        w1 = pct_change(v1.get(s, 0), v1.get(d.semanas[j - 1], 0)) if j else None
        w2 = pct_change(v2.get(s, 0), v2.get(d.semanas[j - 1], 0)) if j else None
        print("    {:<9} {:>14} {:>9} {:>14} {:>9}".format(
            s, fmt_m(v1.get(s, 0)), fmt_pct(w1), fmt_m(v2.get(s, 0)), fmt_pct(w2)))

    # --- Hallazgos
    print("\n### Candidatos a hallazgo (detección automática — la lectura de negocio la pone el PM)")
    hs = detectar(d, actual, recs=recs)
    if not hs:
        print("    (ninguna regla disparó: semana dentro de los rangos habituales)")
    for x in hs:
        print("    [{}] {}: {}".format(x["severidad"], x["tipo"], x["texto"]))
    return 0


# --- Comando: palancas (JSON) ------------------------------------------------
def cmd_palancas(semana=None):
    """Mismo cálculo que 'analyze' (NSM + palancas + hallazgos), en JSON puro a stdout — es
    el insumo de render_email.py (cards del email) y de las tablas Markdown de la wiki.

    Subcomando aparte en vez de 'analyze --json': 'analyze' imprime ~200 líneas de texto que
    el usuario ya lee cada semana; esconder cada print detrás de un flag hubiera sido mucho
    más riesgo de romper esa salida que agregar un comando nuevo que no la toca."""
    seed_staging_from_mirror()
    d = Datos()
    actual, err = _resolver_semana(d, semana)
    if err:
        print(json.dumps({"error": err}, ensure_ascii=False))
        return 1

    recs = medir_palancas(d, actual)
    hallazgos = detectar(d, actual, recs=recs)

    palancas_json = []
    for r in recs.values():
        b, mv = r["semanal"], r["movil"]
        palancas_json.append({
            "id": r["id"], "nombre": r["nombre"], "nsm": r["nsm"], "categoria": r["categoria"],
            "suma": r["suma"], "eje": r["eje"], "padre": r["padre"], "nota": r["nota"],
            "formato": r.get("formato", "monto"),
            "share_padre": r["share"], "visible": _visible_palanca(d, r),
            "volumen": b["volumen"], "cantidad": b["cantidad"], "ticket": b["ticket"],
            "wow": b["wow"], "vs_m4": b["vs_m4"], "vs_m13": b["vs_m13"], "vs_max": b["vs_max"],
            "maximo": b["max"], "semana_max": b["semana_max"], "tendencia6": b["tendencia6"],
            "z": b["z"], "serie_semanal": b["serie"],
            "volumen_semana_anterior": b["serie"][-2] if len(b["serie"]) > 1 else None,
            # Tendencia de ventana móvil (protagonista, reemplaza al "MoM" mensual — usuario,
            # 2026-08-04): compara las últimas VENTANA_TENDENCIA semanas cerradas contra las
            # VENTANA_TENDENCIA previas. Sin relación a mes calendario — ver bloque_movil().
            "tendencia_ventana": mv["ventana"] if mv else None,
            "tendencia_pct": mv["tendencia"] if mv else None,
            "tendencia_acumulado": mv["acumulado"] if mv else None,
            "tendencia_acumulado_previo": mv["acumulado_previo"] if mv else None,
            "tendencia_semanas_actual": mv["semanas_actual"] if mv else None,
            "tendencia_semanas_previa": mv["semanas_previa"] if mv else None,
        })

    doc = {"semana": actual, "rango": d.rango(actual), "generado": date.today().isoformat(),
          "palancas": palancas_json, "hallazgos": hallazgos}
    print(json.dumps(doc, ensure_ascii=False, indent=2))
    return 0


def _top(d, titulo, mapa, mapa_prev, nombrador, total):
    print("\n" + titulo)
    top = sorted(mapa.items(), key=lambda kv: -kv[1])[:8]
    for k, v in top:
        w = pct_change(v, mapa_prev.get(k, 0)) if mapa_prev.get(k) else None
        print("    {:<34} {:>16}  ({:5.1f}%)  WoW {:>9}"
              .format(nombrador(k)[:34], fmt_m(v), _share(v, total),
                      fmt_pct(w) if w is not None else "nuevo"))


def _salud(d, actual, i):
    prev = d.semanas[max(0, i - 8): i]

    def linea(label, num_fn, den_fn):
        act = _share(num_fn(actual), den_fn(actual))
        base = [_share(num_fn(s), den_fn(s)) for s in prev]
        mu = statistics.mean(base) if base else None
        print("  {:<42} {:5.1f}%   media 8 semanas {}"
              .format(label, act, "{:5.1f}%".format(mu) if mu is not None else "  s/d"))

    ops_t = lambda s, est: sum(c for ss, _o, t, e, c, _v in d.ops  # noqa: E731
                               if ss == s and t in NSM1_TIPOS and (est is None or e in est))
    trx_t = lambda s, est: sum(c for ss, _e, t, f, e2, c, _v in d.trx  # noqa: E731
                               if ss == s and t in NSM2_TIPOS and f in NSM2_FORMAS
                               and (est is None or e2 in est))
    linea("NSM#1 — tasa de rechazo (ops)", lambda s: ops_t(s, {EST_RECHAZADA}),
          lambda s: ops_t(s, None))
    linea("NSM#1 — tasa de devolución (ops)", lambda s: ops_t(s, EST_DEVUELTA),
          lambda s: ops_t(s, None))
    linea("NSM#2 — tasa de rechazo (trx)", lambda s: trx_t(s, {EST_RECHAZADA_ADQ}),
          lambda s: trx_t(s, None))
    tac_t = lambda s, est: sum(c for ss, _cid, t, e2, c, _v in d.tac_rows  # noqa: E731
                               if ss == s and t in TAC_TIPOS and (est is None or e2 in est))
    linea("TAC Agente de Cobros — tasa de falla (no COMPLETED)",
          lambda s: tac_t(s, DIM_TAC_STATUS - TAC_EST_OK), lambda s: tac_t(s, None))
    linea("NSM#2 — tasa de devolución (trx)", lambda s: trx_t(s, {EST_DEVUELTA_ADQ}),
          lambda s: trx_t(s, None))
    for f, nom in sorted(NSM2_FORMAS.items()):
        t_f = lambda s, est, ff=f: sum(  # noqa: E731
            c for ss, _e, t, fp, e2, c, _v in d.trx
            if ss == s and t in NSM2_TIPOS and fp == ff and (est is None or e2 in est))
        if t_f(actual, None):
            linea("NSM#2 / {} — tasa de rechazo".format(nom),
                  lambda s, tt=t_f: tt(s, {EST_RECHAZADA_ADQ}), lambda s, tt=t_f: tt(s, None))


def _altas_print(d, actual, i):
    prev = d.semanas[max(0, i - 8): i]
    for label, datos, nombrador in (("Cuentas de wallet", d.cuentas, d.org),
                                    ("Comercios de adquirencia", d.comercios, d.entid)):
        tot = defaultdict(float)
        por_k = defaultdict(float)
        for s, k, c in datos:
            tot[s] += c
            if s == actual:
                por_k[k] += c
        base = [tot.get(s, 0) for s in prev]
        print("  {}: {} en la semana  (media 8 semanas {}, WoW {})"
              .format(label, fmt_n(tot.get(actual, 0)),
                      fmt_n(statistics.mean(base) if base else 0),
                      fmt_pct(pct_change(tot.get(actual, 0), tot.get(d.semanas[i - 1], 0))
                              if i else None)))
        for k, v in sorted(por_k.items(), key=lambda kv: -kv[1])[:5]:
            print("      {:<34} {:>9}  ({:4.1f}%)"
                  .format(nombrador(k)[:34], fmt_n(v), _share(v, tot.get(actual, 0))))


# --- Main -------------------------------------------------------------------
def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    args = sys.argv[2:]
    forzar = "--forzar-desalineadas" in args
    args = [a for a in args if a != "--forzar-desalineadas"]
    if cmd == "inspect":
        return cmd_inspect(forzar_desalineadas=forzar)
    if cmd == "ingest":
        return cmd_ingest(forzar_desalineadas=forzar)
    if cmd == "analyze":
        return cmd_analyze(args[0] if args else None)
    if cmd == "palancas":
        return cmd_palancas(args[0] if args else None)
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
