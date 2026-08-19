---
id: 2026-08-15_dato_log_versiones_publicadas_tanda1
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — barrido incremental 2026-08-15, tanda 1/N (post backfill 2026-07-13)"
producto: transversal
tema: Filas nuevas para el log de control de versiones publicadas
tipo: dato
destino_propuesto: 3_recursos/datos/log_versiones_publicadas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9306bc6b7cffeb57db264f132b0e0e6a1ec53d8e
---

Append a la tabla "Versiones ingestadas" (insertar como filas nuevas, orden sugerido por espacio/fecha como el resto de la tabla). También actualizar la cabecera del archivo: "Último barrido: 2026-08-15 — barrido incremental vía API (tanda 1 de N; quedan pendientes 8 versiones WS + 2 versiones AD "Portal 2.0 V1/V2" detectadas como gap del backfill anterior — ver reporte `outputs/reportes_sync/2026-08-15_reporte_releases.md`)".

| Espacio | Versión | releaseDate | Fecha ingesta | Tickets ingestados (keys) | Destino / notas |
|---|---|---|---|---|---|
| AD | AD 71.2 FIX (PNET) | 2026-08-12 | 2026-08-15 | AD-1515, AD-1516, AD-1517, AD-1518, AD-1140, AD-861, AD-860, AD-774 | 4 nuevos (AD-1515/1516/1517/1518, mejoras al Monitor de carga masiva de deudas ProvinciaNET: carpeta Fallidos, zip/unzip, archivado histórico) → `botones_de_pago_y_qr.md` §"Carga masiva de deudas — cliente ProvinciaNET". AD-861/AD-860/AD-1140 ya documentados vía `/sync_meetings` (release v71.2 2026-08-10) y en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/` y `1_proyectos/proyecto-ministerio/prd-134_.../` — solo atribución de versión de publicación, sin merge nuevo. AD-774 (Serilog, Epic WS-564, infra) — ruido puro, sin merge de wiki. |
| ARD | ARDID V 1.18.2.1 HF | 2026-07-22 | 2026-08-15 | ARD-32 | Atribución: mismo hotfix de reintentos de SP ya documentado en `integracion_con_productos_bind.md` §11 (vía `/sync_meetings`, minuta 2026-07-17) — coincide fecha de despliegue y objeto del fix. Sin contenido técnico nuevo en Jira. **Espacio ARD nuevamente al día tras esta versión.** |

**Estado del backfill — corrección de campo (ver hallazgo del barrido 2026-08-15):** la fila "AD | ✅ COMPLETO" de la tabla "Estado del backfill histórico" queda desactualizada — el barrido incremental de esta corrida detectó 2 versiones AD publicadas el 2026-05-21 ("Portal 2.0 V1", "Portal 2.0 V2") que el backfill XML de 2026-07-13 no capturó, probablemente por nomenclatura no secuencial (no matchea el patrón `AD NN[.N]`). Pendiente de ingesta en la próxima tanda — no marcar el espacio como completo hasta procesarlas.
