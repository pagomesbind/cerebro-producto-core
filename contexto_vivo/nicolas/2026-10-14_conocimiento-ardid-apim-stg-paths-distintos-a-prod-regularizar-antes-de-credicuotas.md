---
id: 2026-10-14_conocimiento-ardid-apim-stg-paths-distintos-a-prod-regularizar-antes-de-credicuotas
pm: nicolas
fecha_captura: 2026-10-14
fuente: "Mail \"Regularizar Path de los endpoint APIM STG\" (Hernán Clarich, 2026-10-09)"
producto: ardid
tema: Ardid — los paths del APIM en STG no coinciden con los de PROD y cada pase necesita arreglos; regularizarlos es prerrequisito para salir con Credicuotas
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/despliegues_y_operacion.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

**Qué se aprendió.**
- Los **paths de los endpoints de Ardid publicados en el APIM de STG no coinciden con los de producción**. Por eso cada pase a PROD de los micros o integraciones que consumen Ardid por APIM necesita arreglos puntuales.
- La diferencia **solo afecta a las integraciones que pasan por el APIM**. Las que llaman a Ardid directo al backend no se ven afectadas.
- Hernán Clarich propone igualar en STG los paths a los de PROD. Así se respeta la política del APIM y no hacen falta arreglos en cada pase.
- Es **prerrequisito para la salida de Credicuotas** (producto nuevo del APIM, ver `2026-10-06_conocimiento-ardid-apim-producto-ardidexternal-coto-y-extension-credicuotas`): primero en STG y después en producción, para no romper PROD.
- Le pide a Producto (Nicolás Colón) que identifique el **impacto del cambio de configuración de esos paths en STG** antes de aplicarlo (T-129).

**Pendiente (por eso la confianza es media):** el detalle está en dos adjuntos que no se descargaron. `APIM STG ARDID regularizar path de endpoint.docx` tiene los paths actuales de STG y el cambio propuesto. `ARDID consumo APIM-PROD.csv` tiene la estadística de consumo de PROD, con los paths de APIM y de backend. Cuando se lean, completar este item con la tabla de paths o capturar uno nuevo con `tipo_destino: actualizar`.

> Fuente: Mail "Regularizar Path de los endpoint APIM STG" — Hernán Clarich (2026-10-09), con copia a Matías Alzogaray, Emma Vignoles, Rocío Revelli, Marcelo Nadalin, Pablo Vargas y Osmel Mata (Fintexa).
