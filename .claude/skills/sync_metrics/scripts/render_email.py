# -*- coding: utf-8 -*-
"""
Renderer del email ejecutivo de /sync_metrics — "el pipeline mide, Claude interpreta, el
renderer maqueta". No hace ningún cálculo de negocio: todo lo numérico sale del JSON de
`pipeline.py palancas`, que ya viene medido (incluida la tendencia de ventana móvil).

Uso:
    python pipeline.py palancas [SemanaId] > palancas.json
    # Claude escribe hallazgos.json: su lectura de negocio de los candidatos de palancas.json
    # (3 a 6 items, priorizados), en esta forma:
    #   [{"severidad": "Alta", "tipo": "Concentración", "titulo": "...", "texto": "...",
    #     "palanca_id": "nsm1_tac" | null}, ...]
    python render_email.py palancas.json hallazgos.json --email > email.html
    python render_email.py palancas.json hallazgos.json --md    > tablas.md

Diseño (rediseño 2026-08-04, iterado en 9 rondas con el usuario):
- Cards SOLO para las dos NSM raíz, tituladas con su significado ("NSM#1: Volumen en API
  Bank" / "NSM#2: Volumen en Payway") — nadie recuerda qué es "NSM1" a secas.
- El resto de las palancas va como ÁRBOL JERÁRQUICO con viñetas e indentación, no cards
  individuales — mucho más compacto para leer de un vistazo.
- Protagonista: TENDENCIA de ventana móvil de 4 semanas (últimas 4 cerradas vs. las 4
  previas) — reemplaza al "MoM" mensual-calendario. Decisión del usuario (2026-08-04): el
  tramo mensual se congelaba en meses de 5 semanas ISO y el nombre de mes ("julio") se
  prestaba a leerse como un cierre contable exacto, cuando era una aproximación — con
  riesgo real de que alguien (ej. el CEO) lo malinterprete. La ventana móvil no tiene
  nombre de mes, se actualiza todas las semanas, y lleva una nota de metodología explícita
  en el email para que quede claro que es una señal de ritmo, no un cierre mensual.
- WoW: dato SECUNDARIO — chico, sin negrita, coloreado según signo (igual que la tendencia,
  pero subordinado en tamaño/peso), entre paréntesis, solo el %.
- Un solo renglón por palanca del árbol, con la tendencia en columna de ANCHO FIJO alineada
  a la izquierda de su columna (todas las flechas quedan alineadas verticalmente) — no
  justificado a la derecha del todo, decisión explícita del usuario.
- Leading indicators (altas de cuentas/comercios, categoria="leading_indicator"): no suman
  volumen, se formatean como cantidad entera (`p["formato"] == "entero"`), no como pesos.

Restricciones de Gmail/Outlook (sin cambios): todo el CSS inline, layout con <table>, sin
flex/grid, sin imágenes externas, sin JS, sin <details>/colapsables.
"""
import html
import json
import sys

try:  # la consola de Windows no es UTF-8 y se come acentos/flechas del reporte
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:  # pragma: no cover
    pass

# --- Paleta -------------------------------------------------------------
VERDE, ROJO, GRIS, GRIS_CLARO = "#1e7e46", "#c0392b", "#5b6b7f", "#b9c1cd"
AZUL_OSCURO = "#0b2545"
TINTE_POR_NSM = {"NSM#1": ("#eff8ff", "#cfe0f5"), "NSM#2": ("#f3f0ff", "#d9d0ff")}

CATEGORIA_LABEL = {
    "componente_nsm1": "Componente de NSM#1", "split_in_out": "Entrante / Saliente",
    "sin_clasificar": "Sin clasificar", "tipo_operacion_wallet": "Tipo de operación (Wallet)",
    "tipo_tac": "Tipo (Agente de Cobros)", "split_in_out_tac": "Entrante / Saliente (TAC)",
    "palanca_indirecta": "Palanca indirecta de NSM#1", "canal_nsm2": "Canal (Payway)",
    "medio_pago_nsm2": "Medio de pago (Payway)", "fuera_payway": "Fuera de Payway",
    "leading_indicator": "Leading indicator",
}

NSM_TITULO = {"NSM#1": "NSM#1: Volumen en API Bank", "NSM#2": "NSM#2: Volumen en Payway"}

# Estructura del árbol de palancas que SUMAN al total — jerarquía de negocio explícita, no
# se puede derivar genéricamente del campo "padre" del JSON (los tipos de Wallet tienen
# padre=nsm1_wallet, no nsm1_out/nsm1_in — el anidado OUT/IN de acá es solo visual, para
# que el árbol se lea como negocio). GOTCHA: si algún día se agrega un tipo nuevo a
# NSM1_TIPOS/TAC_TIPOS/NSM2_TIPOS/NSM2_FORMAS en pipeline.py, hay que sumarlo acá también
# — no hay forma automática de que este árbol se entere de un id nuevo.
ARBOL_CORE_NSM1 = [
    ("nsm1_wallet", 0), ("nsm1_out", 1), ("nsm1_tipo_1", 2), ("nsm1_tipo_3", 2),
    ("nsm1_tipo_8", 2), ("nsm1_in", 1), ("nsm1_tipo_2", 2), ("nsm1_tipo_14", 2),
    ("nsm1_tipo_6", 2), ("nsm1_sin_clasificar", 1),
    ("nsm1_tac", 0), ("tac_lado_saliente", 1), ("tac_lado_entrante", 1),
    ("tac_tipo_transfer.cvu.received", 2), ("tac_tipo_transfer.cbu.received", 2),
]
ARBOL_CORE_NSM2 = [
    ("nsm2_canal_6", 1), ("nsm2_canal_7", 1),
    ("nsm2_medio_90", 1), ("nsm2_medio_80", 1), ("nsm2_medio_60", 1), ("nsm2_medio_10", 1),
]
# Categorías de contexto (no suman): orden dinámico por volumen, no hardcodeado por id.
CONTEXTO_CATEGORIAS = {
    "NSM#1": ("palanca_indirecta", "leading_indicator"),
    "NSM#2": ("fuera_payway", "leading_indicator"),
}


def _color(v):
    return GRIS if v is None else (VERDE if v >= 0 else ROJO)


def _flecha(v):
    return "&bull;" if v is None else ("&#9650;" if v >= 0 else "&#9660;")


def _pct(v):
    if v is None:
        return "s/d"
    return "{:+.1f}%".format(v).replace(".", ",")


def _monto(v):
    if v is None:
        return "s/d"
    m = v / 1_000_000.0
    dec = 0 if abs(m) >= 100 else (1 if abs(m) >= 1 else 2)
    s = "{:,.{}f}".format(m, dec).replace(",", "\x00").replace(".", ",").replace("\x00", ".")
    return "$" + s + " M"


def _entero(v):
    if v is None:
        return "s/d"
    return "{:,.0f}".format(v).replace(",", ".")


def _valor(v, formato):
    return _entero(v) if formato == "entero" else _monto(v)


def _esc(s):
    return html.escape(str(s or ""), quote=True)


# --- Cards de NSM (solo las 2 raíz) ---------------------------------------
def _card_nsm(p):
    """Card de una NSM raíz: 'últimas 4 semanas' como headline (NO acumulado de mes
    calendario — ver nota de metodología del email), tendencia móvil protagonista, WoW
    chico y subordinado en paréntesis."""
    bg, borde = TINTE_POR_NSM.get(p["nsm"], TINTE_POR_NSM["NSM#1"])
    ventana = p.get("tendencia_ventana")
    tend_pct = p.get("tendencia_pct")
    tend_prev = p.get("tendencia_acumulado_previo")
    wow = p.get("wow")
    return (
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
        'style="background:{bg};border:1px solid {borde};border-radius:10px;">'
        '<tr><td style="padding:16px 18px;">'
        '<div style="font-size:12px;font-weight:700;color:{azul};">{titulo}</div>'
        '<div style="font-size:10px;color:{gris};margin-top:2px;">Últimas {ventana} semanas cerradas</div>'
        '<div style="font-size:26px;font-weight:700;color:{azul};margin-top:6px;">{acumulado}</div>'
        '<div style="font-size:13px;margin-top:8px;">'
        '<span style="color:{c_tend};font-weight:700;">{f_tend} Tendencia {tend}</span> '
        '<span style="color:{gris};">({ventana} sem. previas: {prev})</span></div>'
        '<div style="font-size:10.5px;color:{c_wow};font-weight:400;margin-top:4px;">(WoW {wow})</div>'
        '</td></tr></table>'
    ).format(bg=bg, borde=borde, azul=AZUL_OSCURO, gris=GRIS, titulo=_esc(NSM_TITULO.get(p["nsm"], p["nombre"])),
             ventana=ventana or "?", acumulado=_monto(p.get("tendencia_acumulado")),
             c_tend=_color(tend_pct), f_tend=_flecha(tend_pct), tend=_pct(tend_pct), prev=_monto(tend_prev),
             c_wow=_color(wow), wow=_pct(wow))


def _fila_2(cards):
    return ('<tr>' + "".join('<td width="50%" style="padding:6px;vertical-align:top;">{}</td>'
                             .format(c) for c in cards) + '</tr>')


# --- Árbol de palancas ------------------------------------------------------
WOW_COL_W, TEND_COL_W = 92, 200


def _fila_arbol(p, nivel, contexto=False):
    """Un renglón del árbol: nombre (izquierda, indentado por nivel) | columna WoW (ancho
    fijo, alineada a la izquierda de su columna, chica/gris/coloreada, subordinada) |
    columna Tendencia (ancho fijo, alineada a la izquierda de su columna, protagonista,
    negrita, coloreada, con flecha y valor de referencia). Todo en UNA fila — decisión
    explícita del usuario (2026-08-04) para que se lea rápido y las flechas queden
    alineadas verticalmente entre renglones, sin importar el nivel de indentación."""
    formato = p.get("formato", "monto")
    tend_pct, tend_prev, wow = p.get("tendencia_pct"), p.get("tendencia_acumulado_previo"), p.get("wow")
    indent = 20 * nivel
    peso = "700" if nivel <= 1 else "600"
    tam_nombre = "13.5px" if nivel == 0 else ("13px" if nivel == 1 else "12.5px")
    op = "1" if not contexto else "0.72"
    borde = "2px solid #dde3ea;" if nivel > 0 else "none;"
    bullet = "&bull;&nbsp;" if nivel > 0 else ""
    return (
        '<tr><td style="padding:7px 0 7px {indent}px;border-left:{borde}opacity:{op};">'
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
        '<td style="font-size:{tam};font-weight:{peso};color:{azul};padding-right:8px;vertical-align:middle;">'
        '{bullet}{nombre}</td>'
        '<td width="{wow_w}" style="width:{wow_w}px;text-align:left;vertical-align:middle;white-space:nowrap;">'
        '<span style="font-size:10.5px;font-weight:400;color:{c_wow};">(WoW {wow})</span></td>'
        '<td width="{tend_w}" style="width:{tend_w}px;text-align:left;vertical-align:middle;white-space:nowrap;">'
        '<span style="font-size:13px;font-weight:700;color:{c_tend};">{f_tend} Tend. {tend}</span>'
        '<span style="font-size:11px;color:{gris};"> (prev. {prev})</span></td>'
        '</tr></table>'
        '{nota}'
        '</td></tr>'
    ).format(indent=indent, borde=borde, op=op, tam=tam_nombre, peso=peso, azul=AZUL_OSCURO,
             bullet=bullet, nombre=_esc(p["nombre"]), wow_w=WOW_COL_W, c_wow=_color(wow), wow=_pct(wow),
             tend_w=TEND_COL_W, c_tend=_color(tend_pct), f_tend=_flecha(tend_pct), tend=_pct(tend_pct),
             gris=GRIS, prev=_valor(tend_prev, formato),
             nota='<div style="font-size:10px;color:{};font-style:italic;padding:2px 0 0 {}px;">{}</div>'
                 .format(GRIS, indent, _esc(p["nota"])) if p.get("nota") else "")


def _titulo_seccion(txt):
    return ('<tr><td style="padding:16px 0 4px 0;font-size:11px;font-weight:700;color:{};'
           'text-transform:uppercase;letter-spacing:.6px;border-top:1px solid #eef0f3;">{}</td></tr>'
           ).format(GRIS, _esc(txt))


def _arbol_nsm(byid, nsm, arbol_core):
    filas = []
    for pid, nivel in arbol_core:
        p = byid.get(pid)
        if not p or not p.get("visible", True):
            continue
        filas.append(_fila_arbol(p, nivel))

    for categoria in CONTEXTO_CATEGORIAS[nsm]:
        items = sorted(
            [p for p in byid.values() if p["nsm"] == nsm and p["categoria"] == categoria
            and p.get("visible", True)],
            key=lambda p: -(p["volumen"] or 0))
        if not items:
            continue
        etiqueta = "Leading indicator — no suma directo al volumen, pero su crecimiento " \
                  "antecede el de la NSM" if categoria == "leading_indicator" else \
                  CATEGORIA_LABEL.get(categoria, categoria) + " — no suman al total"
        filas.append(_titulo_seccion(etiqueta))
        for p in items:
            filas.append(_fila_arbol(p, 1, contexto=True))
    return "".join(filas)


def _hallazgo_html(h):
    sev = h.get("severidad", "Media")
    color = {"Alta": ROJO, "Media": "#d68910", "Baja": GRIS}.get(sev, GRIS)
    titulo = h.get("titulo") or h.get("texto", "")[:80]
    return (
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
        'style="margin-bottom:12px;"><tr>'
        '<td width="4" style="background:{color};border-radius:2px;"></td>'
        '<td style="padding:2px 0 2px 14px;">'
        '<div style="font-size:11px;font-weight:700;color:{color};text-transform:uppercase;'
        'letter-spacing:.8px;">{sev} &middot; {tipo}</div>'
        '<div style="font-size:14px;font-weight:700;color:{azul};margin-top:3px;">{titulo}</div>'
        '<div style="font-size:13px;color:#42546a;line-height:1.55;margin-top:4px;">{texto}</div>'
        '</td></tr></table>'
    ).format(color=color, azul=AZUL_OSCURO, sev=_esc(sev), tipo=_esc(h.get("tipo", "")),
             titulo=_esc(titulo), texto=_esc(h.get("texto", "")))


def render_email(doc, hallazgos):
    palancas = doc["palancas"]
    byid = {p["id"]: p for p in palancas}
    nsm1, nsm2 = byid["nsm1"], byid["nsm2"]

    kpis = _fila_2([_card_nsm(nsm1), _card_nsm(nsm2)])
    arbol1 = _arbol_nsm(byid, "NSM#1", ARBOL_CORE_NSM1)
    arbol2 = _arbol_nsm(byid, "NSM#2", ARBOL_CORE_NSM2)
    hallazgos_html = "".join(_hallazgo_html(h) for h in hallazgos) or \
        '<div style="font-size:13px;color:#5b6b7f;">Sin hallazgos materiales esta semana.</div>'
    ventana = nsm1.get("tendencia_ventana") or 4

    return """<div style="margin:0;padding:0;background:#f4f5f7;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f5f7;padding:24px 12px;">
<tr><td align="center">
<table role="presentation" width="640" cellpadding="0" cellspacing="0" style="max-width:640px;width:100%;background:#ffffff;border-radius:10px;overflow:hidden;box-shadow:0 1px 3px rgba(16,24,40,.08);">

  <tr><td style="background:{azul};padding:22px 28px;">
    <div style="color:#8fb8e8;font-size:11px;letter-spacing:1.6px;text-transform:uppercase;font-weight:700;">Bind PSP &middot; North Star Metrics</div>
    <div style="color:#ffffff;font-size:22px;font-weight:700;margin-top:6px;">Reporte semanal &mdash; Semana {semana}</div>
    <div style="color:#a9c4e4;font-size:13px;margin-top:4px;">{rango}</div>
  </td></tr>

  <tr><td style="padding:14px 20px 4px 20px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6fa;border-radius:8px;">
      <tr><td style="padding:10px 14px;font-size:11px;color:{gris};line-height:1.5;">
        <b style="color:{azul};">Cómo leer este reporte:</b> "Tendencia" compara las <b>últimas {ventana} semanas cerradas</b> contra las
        <b>{ventana} semanas previas</b> &mdash; es un indicador de si estamos acelerando o desacelerando, actualizado cada semana.
        <b>No es el acumulado del mes calendario</b> ni una cifra de facturación mensual exacta.
      </td></tr>
    </table>
  </td></tr>

  <tr><td style="padding:16px 20px 4px 20px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0">{kpis}</table>
  </td></tr>

  <tr><td style="padding:24px 20px 4px 20px;">
    <div style="font-size:15px;font-weight:700;color:{azul};border-bottom:2px solid {azul};padding-bottom:6px;">Cómo se mueve {t1}</div>
  </td></tr>
  <tr><td style="padding:4px 20px 4px 20px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0">{arbol1}</table>
  </td></tr>

  <tr><td style="padding:24px 20px 4px 20px;">
    <div style="font-size:15px;font-weight:700;color:{azul};border-bottom:2px solid {azul};padding-bottom:6px;">Cómo se mueve {t2}</div>
  </td></tr>
  <tr><td style="padding:4px 20px 4px 20px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0">{arbol2}</table>
  </td></tr>

  <tr><td style="padding:24px 28px 4px 28px;">
    <div style="font-size:15px;font-weight:700;color:{azul};border-bottom:2px solid {azul};padding-bottom:6px;">Hallazgos</div>
  </td></tr>
  <tr><td style="padding:14px 24px 8px 24px;">{hallazgos_html}</td></tr>

  <tr><td style="padding:16px 28px 24px 28px;border-top:1px solid #eef0f3;">
    <div style="font-size:12px;color:{gris};line-height:1.6;">
      Reporte generado automáticamente el {generado}. La tendencia de {ventana} semanas móviles es un
      indicador aproximado de ritmo, no un cierre contable mensual. El objetivo de mercado (top 2 en
      volumen API BANK / top 6 en volumen Payway) todavía no tiene un valor de referencia cargado.
    </div>
  </td></tr>

</table>
</td></tr>
</table>
</div>""".format(azul=AZUL_OSCURO, gris=GRIS, semana=_esc(doc["semana"]), rango=_esc(doc["rango"]),
                  ventana=ventana, kpis=kpis, t1=_esc(NSM_TITULO["NSM#1"]), t2=_esc(NSM_TITULO["NSM#2"]),
                  arbol1=arbol1, arbol2=arbol2, hallazgos_html=hallazgos_html,
                  generado=_esc(doc["generado"]))


def render_md(doc):
    """Bloques de tabla Markdown por sección de palancas — para pegar en
    wiki/2_areas/datasets/metricas_semanales.md sin transcribir las cifras a mano."""
    palancas = doc["palancas"]
    out = ["# Palancas — semana {} ({})\n".format(doc["semana"], doc["rango"])]
    for nsm in ("NSM#1", "NSM#2"):
        out.append("\n## {}\n".format(nsm))
        items = [p for p in palancas if p["nsm"] == nsm and p["categoria"] != "nsm"
                and p.get("visible", True)]
        items.sort(key=lambda p: (not p["suma"], -(p["volumen"] or 0)))
        out.append("| Palanca | Categoría | Volumen | % del padre | WoW | Tendencia | Prev. tendencia |")
        out.append("|---|---|---:|---:|---:|---:|---:|")
        for p in items:
            formato = p.get("formato", "monto")
            out.append("| {} | {} | {} | {} | {} | {} | {} |".format(
                p["nombre"], CATEGORIA_LABEL.get(p["categoria"], p["categoria"]),
                _valor(p["volumen"], formato),
                "{:.1f}%".format(p["share_padre"]) if p.get("share_padre") is not None else "s/d",
                _pct(p.get("wow")), _pct(p.get("tendencia_pct")),
                _valor(p.get("tendencia_acumulado_previo"), formato)))
    return "\n".join(out) + "\n"


def main():
    if len(sys.argv) < 3 or sys.argv[-1] not in ("--email", "--md"):
        print(__doc__)
        return 1
    modo = sys.argv[-1]
    with open(sys.argv[1], encoding="utf-8") as fh:
        doc = json.load(fh)
    hallazgos = []
    if len(sys.argv) > 3:
        with open(sys.argv[2], encoding="utf-8") as fh:
            hallazgos = json.load(fh)
    if modo == "--email":
        sys.stdout.write(render_email(doc, hallazgos))
    else:
        sys.stdout.write(render_md(doc))
    return 0


if __name__ == "__main__":
    sys.exit(main())
