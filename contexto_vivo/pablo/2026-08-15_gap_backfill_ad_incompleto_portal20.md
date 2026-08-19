---
id: 2026-08-15_gap_backfill_ad_incompleto_portal20
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — barrido incremental 2026-08-15"
producto: transversal
tema: Backfill de versiones AD marcado COMPLETO pero con 2 versiones sin capturar
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "3_recursos/datos/log_versiones_publicadas.md — fila 'AD | ✅ COMPLETO' de la tabla de estado del backfill, que afirma cierre de punta a punta del espacio"
confianza: alta
estado: capturado
merge_commit:
---

**Severidad: Media.** El backfill histórico de versiones publicadas del espacio AD (cerrado 2026-07-13 vía export XML, documentado como "✅ COMPLETO" en `log_versiones_publicadas.md`) no capturó 2 versiones: **"Portal 2.0 V1"** y **"Portal 2.0 V2"**, ambas publicadas el 2026-05-21 (detectado recién en el barrido incremental del 2026-08-15, vía JQL directa contra Jira).

**Hipótesis de causa:** el nombre de estas versiones no sigue el patrón secuencial `AD NN[.N] [HF/FIX]` que usa el resto del espacio AD — el proceso de backfill (que trabajaba con export XML + parsing por versión) probablemente asumió cobertura completa al llegar a la versión más antigua conocida en orden numérico, sin verificar cruzado por `releaseDate`. No se puede descartar que existan más versiones "fuera de patrón" en otros espacios (WS, OB, ARD, SER) que el mismo mecanismo haya saltado — no verificado en esta corrida, solo se confirmó para AD.

**Impacto:** un número no determinado de tickets `Bug`/`Story` de Adquirencia (relacionados al menos con Portal Web/Mayorista, a juzgar por los tickets vistos de pasada en la enumeración: AD-1316 "Pagos FX Portal", AD-1133 "Portal2.0 Mayorista") quedaron sin ingestar al canon (`detalle_productos/adquirencia/`) pese a estar en producción desde mayo.

**Actualización 2026-08-15 (misma sesión, tanda 2):** ambas versiones fueron procesadas — ver item `2026-08-15_portal_comercio_rollout_portal20` (20 tickets ingeridos) y la fila correspondiente en `2026-08-15_dato_log_versiones_publicadas_tanda2`. El gap de contenido queda **resuelto**; sigue abierta la recomendación de verificación cruzada por `releaseDate` sobre los demás espacios (WS/OB/ARD/SER) para descartar el mismo patrón — no se hizo en esta sesión.
