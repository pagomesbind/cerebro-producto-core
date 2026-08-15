# -*- coding: utf-8 -*-
"""
Pipeline de /dashboard_qa — ingesta del reporte de tiempo por estado de Jira
("Tiempo QA", CSV) y regeneración del dashboard "Performance de QA".

Uso (desde cualquier cwd):
    python pipeline.py inspect   # analiza el/los CSV de raw/ sin escribir nada
    python pipeline.py ingest    # ingesta completa: merge al log + regenera dashboard

Fuente de verdad acumulada (nunca se releen CSV históricos):
  - wiki/3_recursos/datos/log_performance_qa.md

CONTRATO DE ESCRITURA (pipeline multi-PM, 2026-08-15) — este script YA NO escribe el canon
directo. La ruta de arriba es un ESPEJO read-only en este install; el único que la escribe
es `/context_merge`, sobre el repo compartido CEREBRO_CORE. `ingest` siembra una copia de
trabajo en `wiki/1_proyectos/contexto_vivo/_staging_dashboard_qa/log_performance_qa.md` a
partir del espejo (o de un item `tipo: dato` pendiente sin mergear, si lo hay — verificar a
mano) y el resto del pipeline sigue leyendo/escribiendo ese log igual que antes, solo que
la constante ahora apunta ahí. Al terminar, la skill empaqueta ese archivo como un item
`tipo: dato` en `contexto_vivo/` con `destino_propuesto: 3_recursos/datos/log_performance_qa.md`
— el merge lo aplica por copia byte a byte. El dashboard HTML (`outputs/`) no es canon,
sigue escribiéndose directo. Ver SKILL.md, Paso de cierre.

A diferencia de /dashboard_delivery (que acumula agregados año×mes×espacio), este
log acumula **una fila por ticket** (`Clave`), con upsert por clave en cada ingesta.
Motivo: un ticket creado en un mes puede seguir en QA meses después — su tiempo en QA
cambia entre exports. Si el log guardara agregados mensuales ya cerrados, un export
incremental no podría corregir un mes ya "cerrado". Guardando el detalle por ticket,
cualquier export (completo o parcial) deja el estado acumulado correcto, y los
agregados mensuales se recalculan enteros desde ese detalle en cada corrida.

Formato de origen (export "Tiempo QA" de Jira, un único formato conocido — no hay
auto-detección de múltiples formatos como en dashboard_delivery):
  - Una fila por ticket de desarrollo (Historia/Error), con columnas de metadata
    (Clave, Tipo de Incidencia, Resumen, Estado, Creada, Proyecto, Persona asignada,
    Creador, Prioridad, Story Points, Resuelta) + una columna por CADA estado del
    workflow con el tiempo acumulado que el ticket pasó en ese estado ("-" si nunca
    pasó por ahí). El proveedor parte un mismo estado lógico en varias columnas según
    la variante de workflow del proyecto (ej. "EN QA", "EN QA-10269", "EN QA-10234"
    son las 3 variantes de "en QA" vistas hasta ahora) — se suman todas.
  - Duraciones en formato Jira "1M 2w 3d 4h 5m" (con signo opcional, ej. "-1w"), donde
    M=mes calendario (~30,44 días, calibrado contra Resuelta−Creada), w=semana de 7
    días, d=día de 24h — es decir, TIEMPO CALENDARIO, no horas hábiles.
  - "Resuelta" es opcional en el export (columna que Jira agrega solo si el usuario la
    selecciona al exportar): cuando falta, el dashboard degrada el toggle de eje X
    "por resolución" a solo los tickets que sí la traigan.

Métrica "tiempo hasta EN QA" (sesión 2026-07-27): además de medir cuánto tarda QA en
testear (tiempo EN QA), el pipeline calcula cuánto tarda el ticket en LLEGARLE a QA
= Creada + Σ(columnas pre-QA: Backlog/Asignado/Listo para desarrollo/En curso). Es
tiempo de desarrollo/Fintexa, no de QA — sirve para separar "el equipo tarda" de "le
llega tarde". Ver caveat del rebote a "Con defecto" en el docstring de COLS_PRE_QA.
"""
import csv
import re
import shutil
import statistics
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

if sys.stdout.encoding is None or sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

# --- Paths --------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parents[3]  # .claude/skills/dashboard_qa/scripts -> repo root
RAW_DIR = REPO / "raw"

# Espejo read-only del canon (input) -- NUNCA se escribe acá.
MIRROR_LOG_MD = REPO / "wiki" / "3_recursos" / "datos" / "log_performance_qa.md"

# Copia de trabajo (donde el pipeline realmente lee/escribe) -- se siembra desde el
# espejo al arrancar `ingest`/`inspect`. Ver CONTRATO DE ESCRITURA en el docstring.
STAGING_DIR = REPO / "wiki" / "1_proyectos" / "contexto_vivo" / "_staging_dashboard_qa"
LOG_MD = STAGING_DIR / "log_performance_qa.md"

TEMPLATE = SCRIPT_DIR.parent / "assets" / "dashboard_template.html"
DASHBOARD = REPO / "outputs" / "dashboard_performance_qa.html"  # no es canon, directo


def seed_staging_from_mirror():
    """Siembra la copia de trabajo desde el espejo si todavia no existe. No pisa una
    copia ya sembrada en esta corrida -- si `ingest` corre dos veces sin pasar por
    /context_push, la segunda sigue mergeando sobre lo que la primera ya acumulo."""
    if LOG_MD.exists():
        return
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    if MIRROR_LOG_MD.exists():
        shutil.copy2(MIRROR_LOG_MD, LOG_MD)

# --- Equipo de QA (wiki/2_areas/overview_empresa/overview_equipo.md) ---------------------------------
# Analistas: Andrea Orsini, Bethania Tornari, Ana Moreno — nombres tal como aparecen
# en el export de Jira. Todo lo demás (Producto, PM de desarrollo, Unassigned, etc.)
# se agrupa en "Otros". Se usa tanto para "Persona asignada" como para "Creador"
# (decisión del usuario, sesión 2026-07-27): el dashboard mide al equipo de QA en
# ambos roles (quién testea / quién reporta observaciones).
QA_TEAM = ["Andrea ORSINI", "Bethania", "Ana"]

# Prefijos de observación de QA en staging (wiki/3_recursos/detalle_productos/
# transversal/gestion_jira.md §1.3): [OBS] lo rompió el desarrollo actual, [DEF] ya
# existía, [REQ] mala definición de la historia. Un ticket Error SIN estos prefijos
# es un bug reportado directamente en producción (por Soporte), no un hallazgo de QA.
OBS_TAGS = ("OBS", "DEF", "REQ")
OBS_RE = re.compile(r"\[(" + "|".join(OBS_TAGS) + r")\]", re.IGNORECASE)

# Columnas de tiempo-en-estado a sumar (variantes de workflow del mismo estado lógico).
COLS_QA = ["EN QA", "EN QA-10269", "EN QA-10234"]
COLS_DEFECTO = ["Con defecto", "CON DEFECTOS-10270"]
COLS_BLOQUEADO_TIME = ["Bloqueado"]

# Estados PRE-QA: todo lo que ocurre entre Creada y la primera llegada a EN QA
# (desarrollo/Fintexa, no responsabilidad de QA). Suma = "tiempo hasta asignación a
# QA" (decisión del usuario, sesión 2026-07-27). Válido por construcción: se verificó
# empíricamente que Σ(TODAS las columnas de tiempo) ≈ (fecha de export − Creada) para
# 839/853 tickets (error > 1 día en solo 14) — el estado terminal sigue acumulando
# tiempo hasta el momento del export, no se congela en Resuelta. Esto confirma que
# cada columna es una duración real y aditiva, no un valor arbitrario.
# ⚠️ CAVEAT (no resuelto): para tickets que pasaron por "Con defecto" (rebote QA→dev),
# el export no distingue transiciones — no hay forma de saber si el tiempo en "En
# curso"/"Asignado"/etc. ocurrió TODO antes de la primera llegada a EN QA, o si parte
# es retrabajo posterior al rebote. Evidencia indirecta de que sí puede haber mezcla:
# los tickets con tiempo en "Con defecto" > 0 (124 de 853, 14,5%) tienen más del doble
# de tiempo mediano en "En curso" que los que nunca rebotaron (9,1d vs 3,9d) — para
# esos, "tiempo hasta QA" puede estar sobreestimado. Se marca por ticket (`bounce`) y
# se advierte en el dashboard; no se resuelve con este export.
COLS_PRE_QA = [
    "Asignado", "ASIGNADO-10267", "Backlog", "Backlog-INF", "BACKLOG-10264", "BACKLOG-10231",
    "En curso", "EN CURSO-10232", "LISTO PARA DESARROLLO", "In Progress-10299",
    "In Progress-10265", "SELECCIONADO PARA DESARROLLO-10268", "Selected for Development-10040",
]

# Resto de columnas de tiempo-en-estado del export, conocidas pero irrelevantes para
# las métricas del dashboard (estados terminales cuyo "tiempo acumulado" corre hasta
# el export, no hasta un evento fijo — ver nota arriba) — cualquier columna de estado
# que aparezca y NO esté ni acá ni en las listas de arriba dispara [NUEVAS COLUMNAS].
KNOWN_UNUSED_STATUS_COLS = ["Finalizada", "HECHO-10266", "No aplica"]

REQUIRED_META_COLS = ["Clave", "Tipo de Incidencia", "Resumen", "Estado", "Creada",
                      "Proyecto", "Persona asignada", "Creador"]
OPTIONAL_META_COLS = ["Resuelta", "Story Points", "Prioridad"]

MONTH_MIN = 30.44 * 24 * 60  # calibrado contra (Resuelta − Creada) real, ver SKILL.md
WEEK_MIN = 7 * 24 * 60
DAY_MIN = 24 * 60
DUR_RE = re.compile(r"(-?)(\d+)([Mwdhm])")


def fnum(x):
    v = round(float(x), 2)
    if v == int(v):
        return str(int(v))
    return f"{v:.2f}".rstrip("0").rstrip(".")


def team_group(name):
    name = (name or "").strip()
    return name if name in QA_TEAM else "Otros"


def parse_duration(v):
    """'1M 2w 3d 4h 5m' (con signo opcional por token) -> minutos. '-'/vacío -> 0."""
    v = (v or "").strip()
    if v in ("", "-"):
        return 0.0
    total = 0.0
    for sign, n, unit in DUR_RE.findall(v):
        n = int(n) * (-1 if sign == "-" else 1)
        mult = {"M": MONTH_MIN, "w": WEEK_MIN, "d": DAY_MIN, "h": 60, "m": 1}[unit]
        total += n * mult
    return total


def parse_dt(v):
    v = (v or "").strip()
    if not v:
        return None
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(v, fmt)
        except ValueError:
            continue
    return None


def find_csvs():
    if not RAW_DIR.exists():
        return []
    files = [p for p in RAW_DIR.glob("*.csv") if not p.name.startswith("~$")]
    return sorted(files)


# --- Lectura del CSV ----------------------------------------------------------
def read_qa_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        missing_req = [c for c in REQUIRED_META_COLS if c not in fieldnames]
        qa_cols = [c for c in COLS_QA if c in fieldnames]
        if missing_req or not qa_cols:
            sys.exit(
                f"[ABORT] {path.name}: no matchea el formato conocido de 'Tiempo QA'. "
                f"Faltan columnas obligatorias: {missing_req or '(ninguna)'}"
                f"{'; ninguna columna EN QA* presente' if not qa_cols else ''}. "
                f"Columnas del archivo: {fieldnames}. "
                f"No se adivina el mapeo — revisar el archivo con el usuario."
            )
        has_resuelta = "Resuelta" in fieldnames
        has_sp = "Story Points" in fieldnames
        defecto_cols = [c for c in COLS_DEFECTO if c in fieldnames]
        bloqueado_cols = [c for c in COLS_BLOQUEADO_TIME if c in fieldnames]
        pre_qa_cols = [c for c in COLS_PRE_QA if c in fieldnames]

        known = (set(REQUIRED_META_COLS) | set(OPTIONAL_META_COLS) | set(COLS_QA)
                 | set(COLS_DEFECTO) | set(COLS_BLOQUEADO_TIME) | set(COLS_PRE_QA)
                 | set(KNOWN_UNUSED_STATUS_COLS))
        extras = [c for c in fieldnames if c not in known]

        tickets = {}
        n_rows = 0
        bad_dates, sin_sp, clamped, obs_count = [], [], [], 0
        for row in reader:
            clave = (row.get("Clave") or "").strip()
            if not clave:
                continue
            n_rows += 1
            creada = parse_dt(row.get("Creada"))
            if creada is None:
                bad_dates.append(clave)
                continue
            resuelta = parse_dt(row.get("Resuelta")) if has_resuelta else None

            qa_min = sum(parse_duration(row.get(c)) for c in qa_cols)
            defecto_min = sum(parse_duration(row.get(c)) for c in defecto_cols)
            bloqueado_min = sum(parse_duration(row.get(c)) for c in bloqueado_cols)
            pre_qa_min = sum(parse_duration(row.get(c)) for c in pre_qa_cols)

            if resuelta and qa_min > 0:
                lag_min = (resuelta - creada).total_seconds() / 60
                if qa_min > lag_min + 1:  # +1min de margen por redondeo de "M"
                    clamped.append(clave)
                    qa_min = max(lag_min, 0.0)

            sp = None
            if has_sp:
                sp_raw = (row.get("Story Points") or "").strip()
                if sp_raw:
                    try:
                        sp = float(sp_raw)
                    except ValueError:
                        sin_sp.append(clave)
                else:
                    sin_sp.append(clave)

            resumen = row.get("Resumen") or ""
            tags = sorted({m.upper() for m in OBS_RE.findall(resumen)})
            if tags:
                obs_count += 1

            asignado_raw = (row.get("Persona asignada") or "").strip() or "Unassigned"
            creador_raw = (row.get("Creador") or "").strip()
            estado = (row.get("Estado") or "").strip()

            tickets[clave] = {
                "clave": clave,
                "proyecto": (row.get("Proyecto") or "").strip(),
                "tipo": (row.get("Tipo de Incidencia") or "").strip(),
                "estado": estado,
                "creada": creada.strftime("%Y-%m-%d"),
                "resuelta": resuelta.strftime("%Y-%m-%d") if resuelta else None,
                "asignado": asignado_raw,
                "creador": creador_raw,
                "sp": sp,
                "min_qa": round(qa_min, 1),
                "min_defecto": round(defecto_min, 1),
                "min_bloqueado": round(bloqueado_min, 1),
                "min_pre_qa": round(pre_qa_min, 1),
                "bounce": defecto_min > 0,
                "obs_tags": tags,
            }

    warnings = []
    if not has_resuelta:
        warnings.append("Sin columna 'Resuelta': el toggle de eje X 'por resolución' del dashboard no va a tener datos de este lote.")
    if not has_sp:
        warnings.append("Sin columna 'Story Points': la métrica 'tiempo por SP' no va a tener datos de este lote.")
    if bad_dates:
        warnings.append(f"{len(bad_dates)} ticket(s) con 'Creada' ilegible, EXCLUIDOS: {', '.join(bad_dates[:10])}" + (" …" if len(bad_dates) > 10 else ""))
    if sin_sp:
        warnings.append(f"{len(sin_sp)} ticket(s) sin Story Points (quedan fuera de la métrica 'tiempo por SP'): {', '.join(sin_sp[:10])}" + (" …" if len(sin_sp) > 10 else ""))
    if clamped:
        warnings.append(f"{len(clamped)} ticket(s) con tiempo en QA mayor al lag Creada→Resuelta total — recortado al lag (redondeo de 'M'): {', '.join(clamped[:10])}" + (" …" if len(clamped) > 10 else ""))

    meta = {"file": path.name, "rows": n_rows, "extras": extras, "warnings": warnings,
            "has_resuelta": has_resuelta, "has_sp": has_sp, "obs_count": obs_count}
    return tickets, meta


# --- Log md: parseo y escritura -------------------------------------------------
DETAIL_HEADER = ["Clave", "Proyecto", "Tipo", "Estado", "Creada", "Resuelta",
                 "Asignado", "Creador", "SP", "Horas QA", "Horas Defecto",
                 "Horas pre-QA", "Rebote", "Obs"]


def parse_log():
    """Devuelve (tickets: {clave: dict}, lots: list) desde el log actual; ({}, []) si no existe.

    Reconoce tanto el formato viejo (12 columnas, sin Horas pre-QA/Rebote — sesión
    2026-07-27 inicial) como el nuevo (14 columnas, suma "tiempo hasta EN QA"): las
    filas viejas quedan con min_pre_qa=0.0/bounce=False hasta la próxima ingesta real
    (que las recalcula desde el CSV), no se pierde nada del resto del detalle.
    """
    if not LOG_MD.exists():
        return {}, []
    text = LOG_MD.read_text(encoding="utf-8")
    tickets, lots = {}, []
    section = None
    for line in text.splitlines():
        if line.startswith("## "):
            if "Registro de lotes" in line:
                section = "lots"
            elif line.startswith("## Datos"):
                section = "data"
            else:
                section = None
            continue
        if not line.startswith("|") or line.startswith("|---") or section is None:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if section == "lots" and len(cells) == 5 and cells[0] != "Fecha ingesta":
            lots.append(cells)
        elif section == "data" and cells[0] not in ("Clave",) and len(cells) in (12, 14):
            if len(cells) == 14:
                (clave, proyecto, tipo, estado, creada, resuelta, asignado, creador,
                 sp, horas_qa, horas_defecto, horas_pre_qa, rebote, obs) = cells
                min_pre_qa = round(float(horas_pre_qa) * 60, 1)
                bounce = rebote == "Sí"
            else:
                (clave, proyecto, tipo, estado, creada, resuelta, asignado, creador,
                 sp, horas_qa, horas_defecto, obs) = cells
                min_pre_qa, bounce = 0.0, False
            tickets[clave] = {
                "clave": clave, "proyecto": proyecto, "tipo": tipo, "estado": estado,
                "creada": creada, "resuelta": None if resuelta == "—" else resuelta,
                "asignado": asignado, "creador": creador,
                "sp": None if sp == "—" else float(sp),
                "min_qa": round(float(horas_qa) * 60, 1),
                "min_defecto": round(float(horas_defecto) * 60, 1),
                "min_bloqueado": 0.0,
                "min_pre_qa": min_pre_qa,
                "bounce": bounce,
                "obs_tags": [] if obs == "—" else obs.split("/"),
            }
    return tickets, lots


def coverage_str(tickets):
    if not tickets:
        return "sin datos"
    meses = sorted({t["creada"][:7] for t in tickets})
    rango = meses[0] if meses[0] == meses[-1] else f"{meses[0]} – {meses[-1]}"
    proys = sorted({t["proyecto"] for t in tickets})
    return f"{rango}, {' + '.join(proys)}"


def build_resumen_mensual(tickets):
    """Tabla de sanity check por mes de creación: no alimenta el dashboard (que
    recalcula todo del detalle en JS), es para que un humano audite de un vistazo."""
    by_mes = defaultdict(list)
    for t in tickets:
        by_mes[t["creada"][:7]].append(t)
    out = ["| Mes (creación) | Tickets creados | Con QA cerrado | Mediana días en QA (equipo) | Mediana días hasta EN QA | Observaciones | Aún en QA | Sin paso por QA |",
           "|---|---|---|---|---|---|---|---|"]
    for mes in sorted(by_mes):
        rows = by_mes[mes]
        cerrados = [t for t in rows if t["estado"] != "EN QA" and t["min_qa"] > 0]
        dias = [t["min_qa"] / DAY_MIN for t in cerrados]
        mediana = f"{fnum(statistics.median(dias))}" if dias else "—"
        alcanzo_qa = [t for t in rows if t["min_qa"] > 0]
        dias_pre = [t["min_pre_qa"] / DAY_MIN for t in alcanzo_qa]
        mediana_pre = f"{fnum(statistics.median(dias_pre))}" if dias_pre else "—"
        obs = sum(1 for t in rows if t["obs_tags"])
        en_qa = sum(1 for t in rows if t["estado"] == "EN QA")
        sin_qa = sum(1 for t in rows if t["estado"] != "EN QA" and t["min_qa"] == 0)
        out.append(f"| {mes} | {len(rows)} | {len(cerrados)} | {mediana} | {mediana_pre} | {obs} | {en_qa} | {sin_qa} |")
    return out


def write_log(tickets_by_clave, lots, today):
    tickets = sorted(tickets_by_clave.values(), key=lambda t: (t["creada"], t["clave"]))
    resumen = build_resumen_mensual(tickets)
    detalle = ["| " + " | ".join(DETAIL_HEADER) + " |", "|" + "---|" * len(DETAIL_HEADER)]
    for t in tickets:
        obs_cell = "/".join(t["obs_tags"]) if t["obs_tags"] else "—"
        detalle.append(
            f"| {t['clave']} | {t['proyecto']} | {t['tipo']} | {t['estado']} | {t['creada']} | "
            f"{t['resuelta'] or '—'} | {t['asignado']} | {t['creador']} | "
            f"{fnum(t['sp']) if t['sp'] is not None else '—'} | {fnum(t['min_qa'] / 60)} | "
            f"{fnum(t['min_defecto'] / 60)} | {fnum(t['min_pre_qa'] / 60)} | "
            f"{'Sí' if t['bounce'] else 'No'} | {obs_cell} |"
        )
    lots_tbl = ["| Fecha ingesta | Archivo fuente | Cobertura | Tickets tocados | Destino histórico |",
                "|---|---|---|---|---|"] + ["| " + " | ".join(l) + " |" for l in lots]
    last_lot = lots[-1] if lots else ["—"] * 5

    en_qa_now = sum(1 for t in tickets if t["estado"] == "EN QA")
    sin_qa = sum(1 for t in tickets if t["estado"] != "EN QA" and t["min_qa"] == 0)
    obs_tot = sum(1 for t in tickets if t["obs_tags"])
    alcanzo_qa = [t for t in tickets if t["min_qa"] > 0]
    alcanzo_qa_tot = len(alcanzo_qa)
    bounce_tot = sum(1 for t in tickets if t["bounce"])
    mediana_pre_qa_global = fnum(statistics.median([t["min_pre_qa"] / DAY_MIN for t in alcanzo_qa])) if alcanzo_qa else "—"

    md = f"""# Log de Performance de QA — Base de datos del dashboard "Performance de QA"

> **Última ingesta:** {today} — {last_lot[1]} ({last_lot[2]}, {last_lot[3]}).
>
> Este archivo es la **base de datos acumulada**, por ticket, del dashboard [`outputs/dashboard_performance_qa.html`](../../outputs/dashboard_performance_qa.html), mantenida por la skill [`/dashboard_qa`](../../.claude/skills/dashboard_qa/SKILL.md). El usuario deja en `raw/` un export de Jira "Tiempo QA" (una fila por ticket, tiempo acumulado por estado). Cada ingesta hace **upsert por `Clave`**: el ticket que reaparece se actualiza con el dato fresco (su tiempo en QA puede haber cambiado si seguía abierto), el que no aparece en el export nuevo se conserva tal cual. Los agregados del dashboard se recalculan enteros desde este detalle en cada corrida — **no hace falta releer los CSV históricos**.

## Metodología / criterios de agregación

- **Equipo de QA** (`wiki/2_areas/overview_empresa/overview_equipo.md`): Andrea Orsini, Bethania Tornari, Ana Moreno. Todo lo demás (Producto, PM de desarrollo, Unassigned) se agrupa como "Otros" — tanto para "Persona asignada" (quién testeó) como para "Creador" (quién reportó una observación).
- **Tiempo en QA** = suma de todas las variantes de columna "EN QA*" del export (el proveedor las parte por variante de workflow). Es **tiempo calendario** (24h/día, 7d/semana), no horas hábiles — el export no trae las fechas de transición necesarias para descontar fines de semana.
- **Universo de las métricas de tiempo (tiempo en QA / tiempo por SP):** tickets con tiempo en QA > 0 y estado ≠ `EN QA` (su reloj ya paró, sea `Finalizada` o `Bloqueado`). Los tickets hoy en `EN QA` ({en_qa_now}) se excluyen de esas métricas — su tiempo sigue corriendo, promediarlo no mide nada — y se reportan aparte como "aún en QA". Los tickets que nunca pasaron por QA ({sin_qa}) se reportan como "sin paso por QA".
- **Observación** = ticket con prefijo `[OBS]`/`[DEF]`/`[REQ]` en el Resumen (`gestion_jira.md` §1.3), no todo ticket tipo Error. Total histórico: {obs_tot}.
- **Story Points nulos:** el ticket queda fuera de la métrica "tiempo por SP" (no computa 0 — sesgaría el ratio a la baja).
- **Eje X — 3 anclas posibles, "por asignación a QA" es la default (decisión del usuario, 2026-07-27):**
  - **Por asignación a QA (default):** ubica el ticket en el mes en que **entró por primera vez a `EN QA`** = `Creada` + Σ de todas las columnas de tiempo previas a `EN QA` (`Backlog`/`Asignado`/`Listo para desarrollo`/`En curso`, todas sus variantes). Es la ancla más representativa de "qué estaba testeando el equipo ese mes": el desfasaje entre creación y entrada a QA (mediana {mediana_pre_qa_global} días) es mucho mayor que el desfasaje entre entrada a QA y cierre — agrupar por creación arrastra ese desfasaje largo al gráfico, agrupar por asignación a QA casi no. Validado empíricamente antes de construir: Σ(todas las columnas de tiempo del export) ≈ (fecha de export − `Creada`) en 839/853 tickets (error > 1 día en solo 14) — confirma que cada columna es una duración real y aditiva, y que el estado terminal (`Finalizada`) sigue corriendo hasta el export, no se congela en `Resuelta`. Solo definido para tickets que alguna vez llegaron a `EN QA` ({alcanzo_qa_tot} de {len(tickets)}) — a diferencia de "por creación", acá **no hay** censura por tickets que todavía no llegaron a QA (simplemente no aparecen en el eje bajo este modo).
    - **⚠️ Caveat sin resolver — rebote a "Con defecto":** el export no trae la secuencia de transiciones, solo totales acumulados por estado. Para los {bounce_tot} tickets que alguna vez pasaron por `Con defecto` (columna `Rebote = Sí` en el detalle), no se puede distinguir si el tiempo en `En curso`/`Asignado`/etc. ocurrió TODO antes de la primera llegada a `EN QA`, o si una parte es retrabajo posterior al rebote — de ser así, esos tickets podrían quedar ubicados en un mes posterior al real. Evidencia indirecta de que puede haber mezcla: los tickets con rebote tienen más del doble de tiempo mediano en "En curso" que los que nunca rebotaron (9,1d vs 3,9d). El dashboard expone un KPI aparte ("Con rebote"), no oculta los tickets.
  - **Por creación:** ubica el ticket en su mes de `Creada`. Como el tiempo en QA se mide solo sobre tickets ya cerrados, los meses recientes muestran únicamente los tickets que cerraron rápido — los lentos siguen abiertos. Esto hace que los últimos 2-3 meses del gráfico se vean sistemáticamente más veloces de lo que realmente son (censura estadística fuerte, porque el desfasaje pre-QA es largo), no por mejora real. Se mantiene como toggle secundario, útil para ver "cuándo entró el trabajo" en vez de "cuándo se testeó".
  - **Por resolución:** ubica el ticket en su mes de `Resuelta` (si el export la trae). Mezcla tickets creados en distintos meses que cerraron el mismo mes — útil como segundo cruce independiente para detectar si el sesgo de otro modo es real.
  - En los 3 modos, los meses con cohorte incompleta se marcan en itálica en el eje X (criterio según la pestaña: tickets aún en `EN QA` para Tiempo en QA/Tiempo por SP; no aplica a Observaciones).
- **Recorte de consistencia:** si el tiempo en QA de un ticket supera el lag total `Resuelta − Creada` (posible por el redondeo de "M" a 30,44 días), se recorta a ese lag y se advierte en la ingesta.

## Registro de lotes ingeridos

{chr(10).join(lots_tbl)}

## Resumen mensual (sanity check — el dashboard recalcula todo del detalle)

{chr(10).join(resumen)}

## Datos — detalle por ticket

{chr(10).join(detalle)}
"""
    LOG_MD.write_text(md, encoding="utf-8")


# --- Dashboard ------------------------------------------------------------------
def to_dashboard_record(t):
    en_qa_now = t["estado"] == "EN QA"
    # Mes de asignación a QA (decisión del usuario, 2026-07-27): Creada + tiempo pre-QA
    # = mes en que el ticket llegó por primera vez a EN QA. Solo definido para tickets
    # que alguna vez llegaron a QA (min_qa > 0) — un ticket sin ese dato simplemente no
    # aparece en el eje cuando el usuario elige agrupar "por asignación a QA".
    mes_asignacion_qa = None
    if t["min_qa"] > 0:
        creada_dt = datetime.strptime(t["creada"], "%Y-%m-%d")
        asignacion_dt = creada_dt + timedelta(minutes=t["min_pre_qa"])
        mes_asignacion_qa = asignacion_dt.strftime("%Y-%m")
    return {
        "clave": t["clave"],
        "proyecto": t["proyecto"],
        "tipo": t["tipo"],
        "estado": t["estado"],
        "mes_creada": t["creada"][:7],
        "mes_resuelta": t["resuelta"][:7] if t["resuelta"] else None,
        "mes_asignacion_qa": mes_asignacion_qa,
        "asignado": t["asignado"],
        "asignado_grupo": team_group(t["asignado"]),
        "creador": t["creador"],
        "creador_grupo": team_group(t["creador"]),
        "sp": t["sp"],
        "horas_qa": round(t["min_qa"] / 60, 2),
        "horas_pre_qa": round(t["min_pre_qa"] / 60, 2),
        "bounce": t["bounce"],
        "en_qa_now": en_qa_now,
        "obs": bool(t["obs_tags"]),
    }


def write_dashboard(tickets_by_clave, today_ddmmyyyy):
    tpl = TEMPLATE.read_text(encoding="utf-8")
    tickets = sorted(tickets_by_clave.values(), key=lambda t: (t["creada"], t["clave"]))
    records = [to_dashboard_record(t) for t in tickets]
    subtitle = (f"Tiempo en QA, observaciones y tiempo por Story Point del equipo de QA de Bind PSP · "
                f"Fuente: export de Jira “Tiempo QA” · "
                f"Última ingesta: {today_ddmmyyyy} ({coverage_str(tickets)})")
    import json
    out = tpl.replace("__DATA_JSON__", json.dumps(records, ensure_ascii=False, separators=(",", ":")))
    out = out.replace("__SUBTITLE__", subtitle)
    assert "__DATA_JSON__" not in out and "__SUBTITLE__" not in out
    DASHBOARD.parent.mkdir(parents=True, exist_ok=True)
    DASHBOARD.write_text(out, encoding="utf-8")


# --- Comandos --------------------------------------------------------------------
def report_meta(meta):
    print(f"  filas: {meta['rows']} · observaciones [OBS]/[DEF]/[REQ]: {meta['obs_count']}")
    if not meta["has_resuelta"]:
        print("  [INFO] sin columna 'Resuelta'")
    if not meta["has_sp"]:
        print("  [INFO] sin columna 'Story Points'")
    if meta["extras"]:
        print(f"  [NUEVAS COLUMNAS no contempladas — evaluar si son variantes de estado a sumar]: {meta['extras']}")
    for w in meta["warnings"]:
        print(f"  [WARN] {w}")


def print_summary(tickets_by_clave):
    tickets = list(tickets_by_clave.values())
    n = len(tickets)
    en_qa_now = [t for t in tickets if t["estado"] == "EN QA"]
    con_qa = [t for t in tickets if t["estado"] != "EN QA" and t["min_qa"] > 0]
    sin_qa = [t for t in tickets if t["estado"] != "EN QA" and t["min_qa"] == 0]
    con_sp = [t for t in con_qa if t["sp"]]
    obs = [t for t in tickets if t["obs_tags"]]
    alcanzo_qa = [t for t in tickets if t["min_qa"] > 0]
    bounce = [t for t in tickets if t["bounce"]]
    proys = defaultdict(int)
    for t in tickets:
        proys[t["proyecto"]] += 1

    print(f"\n  Tickets totales: {n}")
    print(f"  Con tiempo en QA cerrado (universo métricas 1/3): {len(con_qa)}")
    print(f"    de esos, con Story Points (universo métrica 3): {len(con_sp)}")
    print(f"  Aún en EN QA (excluidos de métricas de tiempo): {len(en_qa_now)}")
    print(f"  Sin paso por QA (min_qa=0): {len(sin_qa)}")
    print(f"  Observaciones [OBS]/[DEF]/[REQ]: {len(obs)}")
    print(f"  Alcanzaron EN QA alguna vez (universo métrica 'tiempo hasta EN QA'): {len(alcanzo_qa)}")
    if alcanzo_qa:
        dias_pre = [t["min_pre_qa"] / DAY_MIN for t in alcanzo_qa]
        print(f"  Tiempo hasta EN QA (días) — mediana global: {fnum(statistics.median(dias_pre))} · promedio: {fnum(sum(dias_pre)/len(dias_pre))}")
    print(f"  Con rebote a 'Con defecto' (dato de tiempo-hasta-QA menos confiable): {len(bounce)}")
    print(f"  Por proyecto: {dict(sorted(proys.items(), key=lambda kv: -kv[1]))}")

    if con_qa:
        dias = [t["min_qa"] / DAY_MIN for t in con_qa]
        print(f"  Tiempo en QA (días calendario) — mediana global: {fnum(statistics.median(dias))} · promedio: {fnum(sum(dias)/len(dias))}")
    equipo_asig = defaultdict(int)
    equipo_creador = defaultdict(int)
    for t in tickets:
        equipo_asig[team_group(t["asignado"])] += 1
    for t in obs:
        equipo_creador[team_group(t["creador"])] += 1
    print(f"  Tickets por grupo (asignado): {dict(equipo_asig)}")
    print(f"  Observaciones por grupo (creador): {dict(equipo_creador)}")


def cmd_inspect():
    seed_staging_from_mirror()
    csvs = find_csvs()
    if not csvs:
        sys.exit("[ABORT] No hay .csv en raw/. Nada que ingestar.")
    existing, _ = parse_log()
    merged = dict(existing)
    for p in csvs:
        print(f"== {p.name} ==")
        tickets, meta = read_qa_csv(p)
        report_meta(meta)
        overlap = set(tickets) & set(existing)
        changed = sum(1 for c in overlap if existing[c].get("min_qa") != tickets[c]["min_qa"]
                      or existing[c].get("estado") != tickets[c]["estado"])
        nuevos = len(set(tickets) - set(existing))
        print(f"  {nuevos} tickets nuevos respecto del log · {len(overlap)} ya existían ({changed} con cambios de estado/tiempo)")
        merged.update(tickets)
    print("\n== Estado si se ingesta ahora (acumulado) ==")
    print_summary(merged)


def cmd_ingest():
    seed_staging_from_mirror()
    csvs = find_csvs()
    if not csvs:
        sys.exit("[ABORT] No hay .csv en raw/. Nada que ingestar.")
    today = date.today().isoformat()
    today_dd = date.today().strftime("%d/%m/%Y")

    existing, lots = parse_log()
    merged = dict(existing)
    for p in csvs:
        print(f"== Ingesta: {p.name} ==")
        tickets, meta = read_qa_csv(p)
        report_meta(meta)
        merged.update(tickets)
        dest = f"`4_archivos/historial_raw/{today[:7]}_reporte_tiempo_qa/`"
        lot_row = [today, f"`{p.name}`", coverage_str(list(tickets.values())), f"{len(tickets)} tickets", dest]
        lots = [l for l in lots if l[1] != lot_row[1]] + [lot_row]

    write_log(merged, lots, today)
    write_dashboard(merged, today_dd)

    print("\n== Estado acumulado post-ingesta ==")
    print_summary(merged)
    print(f"\nOK -> {LOG_MD.relative_to(REPO)}")
    print(f"OK -> {DASHBOARD.relative_to(REPO)}")
    print("PENDIENTE PARA CLAUDE: verificar dashboard, rotar raw/ -> historial, changelog, gaps si hubo warnings, git push.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "inspect":
        cmd_inspect()
    elif cmd == "ingest":
        cmd_ingest()
    else:
        sys.exit("uso: python pipeline.py [inspect|ingest]")
