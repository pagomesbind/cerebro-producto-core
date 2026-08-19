---
id: 2026-08-15_dato_log_versiones_publicadas_tanda2
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — barrido incremental 2026-08-15, tanda 2/2 (cierre completo del delta detectado)"
producto: transversal
tema: Filas nuevas para el log de control — cierre completo del barrido 2026-08-15
tipo: dato
destino_propuesto: 3_recursos/datos/log_versiones_publicadas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Append a la tabla "Versiones ingestadas" (tras las filas de la tanda 1). Actualizar también la cabecera: "Último barrido: 2026-08-15 — barrido incremental completo vía API, todo el delta detectado desde el backfill de 2026-07-13 quedó ingerido (12 versiones nuevas: 3 AD, 8 WS, 1 ARD)." Y en la tabla "Estado del backfill histórico", la fila de AD pasa de "✅ COMPLETO" a **"✅ COMPLETO (corregido 2026-08-15)"** con nota: "backfill original de 2026-07-13 saltó 2 versiones con nomenclatura no secuencial ('Portal 2.0 V1'/'Portal 2.0 V2', ambas 2026-05-21) — cerradas en este barrido incremental. Ver gap `2026-08-15_gap_backfill_ad_incompleto_portal20` (ya resuelto)."

| Espacio | Versión | releaseDate | Fecha ingesta | Tickets ingestados (keys) | Destino / notas |
|---|---|---|---|---|---|
| AD | Portal 2.0 V1 | 2026-05-21 | 2026-08-15 | AD-1133, AD-1132, AD-1131, AD-1130, AD-1129, AD-1121, AD-1120, AD-1119, AD-1118, AD-1117, AD-1114, AD-988, AD-845, AD-841, AD-839, AD-838, AD-837, AD-593 | 18 tickets, rollout de Portal 2.0 (Entidad + Mayorista) → `portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md`. AD-839 ya documentado vía `/sync_meetings` (impuestos QRI, DAD-2235) — solo atribución. |
| AD | Portal 2.0 V2 | 2026-05-21 | 2026-08-15 | AD-1316, AD-1262 | 2 tickets, Pagos FX Portal (etiqueta IBAN/BAN, filtro de países pegado) → `portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md`. |
| WS | W 71 | 2026-07-15 | 2026-08-15 | 25 tickets: WS-1324, WS-1311, WS-1309, WS-1306, WS-1305, WS-1304, WS-1303, WS-1300, WS-1296, WS-1292, WS-1284, WS-1280, WS-1277, WS-1252, WS-1249, WS-1232, WS-1217, WS-1206, WS-1078, WS-1077, WS-1050, WS-1044, WS-816, WS-730, WS-614 | 19 nuevos + 6 atribución (WS-1296/730/1306/1305/1304/1303, ya documentados vía `/sync_meetings`). Destinos: `dolar_ccl.md` §3.6 (WS-1217), `debin_y_fondeo.md` "Contracargos DEBIN" (WS-1252, WS-816), `cuenta_remunerada_fci.md` (WS-1284 + atribución), `conciliacion_y_totalizadores.md` §4 (WS-1277), `pedidos_de_clientes_y_hallazgos_operativos.md` "Operación de Wallet" (WS-1077/1078/1324/1292/1249/1232/1300/1044/1050/1206). Ruido sin merge: WS-614 (descripción corrupta). |
| WS | W 71.1 FIX | 2026-07-16 | 2026-08-15 | WS-1387, WS-1388 | Migración EasyNet del evento de transferencia entrante + HttpClient factory → `historial_confiabilidad_transferencias_y_comprobantes.md` §10. |
| WS | W 71.2 FIX | 2026-07-23 | 2026-08-15 | WS-1417, WS-1413, WS-1395, WS-1394, WS-1389, WS-1364, WS-1298 | Anti-affinity WalletOperaciones + relevamiento WebhookSender a PROD (.NET 8, colas Quorum latentes) → `historial_confiabilidad_transferencias_y_comprobantes.md` §10; CodigoPSP=0 en reportes, transferencias sin datos contraparte, PagosQR en Auditar sin resolver → `pedidos_de_clientes_y_hallazgos_operativos.md`; API Feriados por IP interna → `historial_confiabilidad...` §10 (ruido técnico). |
| WS | W 71.3 FIX | 2026-07-28 | 2026-08-15 | WS-1432, WS-1431 | Altas de organización (HAPSA org 62, demo app org 64) → `organizaciones_y_configuracion.md` §7. |
| WS | W 71.4 FIX | 2026-07-30 | 2026-08-15 | WS-1429, WS-1427, WS-1285 | AuthExternal V2 pasaje a PROD etapa 1/3 → `organizaciones_y_configuracion.md` §7; correcciones Dólar CCL (montoObtenido, IDs de comprobante de cargo) → `dolar_ccl.md` §3.6. |
| WS | W 71.5 FIX | 2026-07-31 | 2026-08-15 | WS-1445 | Cambio de nombre de app de demo en BFF de onboarding (DEMO → APKD) — config puntual, sin merge de wiki. |
| WS | W 71.6 FIX | 2026-08-06 | 2026-08-15 | WS-1444 | AuthExternal V2 pasaje a PROD etapa 2/3 (Wallet.BIND + SharedDebin) → `organizaciones_y_configuracion.md` §7. |
| WS | W 71.7 FIX | 2026-08-10 | 2026-08-15 | WS-1470 | Alta de organización 66 (PAFX) en WalletBFF PROD → `organizaciones_y_configuracion.md` §7. |
| ARD | (ya cerrado en tanda 1) | — | — | — | Ver `2026-08-15_dato_log_versiones_publicadas_tanda1`. |

**Pendiente menor:** la fecha exacta de `W 71.1 FIX` y `W 71.3 FIX` no se resolvió en este barrido (no se consultó `releaseDate` puntual para esas dos) — quedan como "a confirmar" en la tabla; no bloquea la ingesta de contenido, solo la precisión de la línea de tiempo. Completar en el próximo barrido con una consulta `key in (WS-1387, WS-1432)`, `fields=["fixVersions"]`.
