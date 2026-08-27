---
id: 2026-08-26_wallet_authexternal_v2_etapa3_cierre_migracion
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión AD 71.3 (publicada 2026-08-24), ticket AD-1528"
producto: wallet
tema: Pasaje a PROD de AuthExternal V2 — etapa 3/3, cierre de la migración
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md §7 — el párrafo vigente (ingerido de WS-1429/WS-1444, W 71.4 FIX/W 71.6 FIX) dice explícitamente 'Sin detalle de qué etapas ya pasaron ni cuántas faltan — gap de visibilidad del roadmap completo de esta migración'. Este ticket resuelve ese gap: la migración tiene 3 etapas en total y esta es la última (3/3), publicada del lado Adquirencia."
confianza: alta
estado: en_cola
merge_commit:
---

**Se cierra la migración de AuthExternal V2** (autenticación externa por microservicios) con la etapa 3 de 3, publicada en **AD 71.3** (2026-08-24, ticket [AD-1528](https://bindpsp.atlassian.net/browse/AD-1528)).

Contexto acumulado de las 3 etapas (las 2 primeras ya estaban en la wiki, del lado Wallet/WS):
- **Etapa 1/3** — [WS-1429](https://bindpsp.atlassian.net/browse/WS-1429), W 71.4 FIX (2026-07-30): relevamiento/soporte técnico.
- **Etapa 2/3** — [WS-1444](https://bindpsp.atlassian.net/browse/WS-1444), W 71.6 FIX (2026-08-06): migra **Wallet.BIND** y **SharedDebin**.
- **Etapa 3/3** — AD-1528, AD 71.3 (2026-08-24): migra el apuntado a AuthExternal V2 de tres microservicios compartidos usados por Adquirencia — **Shared.Cvu**, **Shared.Debin** y **Shared.Coelsa.Alias**. El ticket, del espacio AD (Historia "[US] Pasaje a PROD AuthE V2 3 3"), aclara que es la continuación por etapas de la migración de autenticación externa. Comentario de cierre (Andrea Orsini, 2026-08-24): "Se efectuaran validaciones en PROD. Paso el ticket a finalizado."

**Nota:** `SharedDebin` aparece nombrado tanto en la etapa 2 (WS-1444) como en la 3 (AD-1528) — no hay aclaración en Jira de por qué se repite (¿alcance parcial en la etapa 2, o dos migraciones de microservicios con nombre similar?). No es una contradicción bloqueante, pero vale dejarlo explícito por si un PM necesita precisión técnica a futuro.

**Al mergear:** reemplazar la frase de gap de §7 ("Sin detalle de qué etapas ya pasaron ni cuántas faltan") por la confirmación de que la migración de AuthExternal V2 quedó completa en 3 etapas al 2026-08-24, agregando la etapa 3/3 con el detalle de arriba.
