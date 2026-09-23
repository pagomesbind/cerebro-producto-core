---
id: 2026-09-21_ardid_riesgo_performance_afecta_ventas_coto_desa
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_meetings — reunión \"Weekly - Producto / Operaciones\" (14:58, con Mariana Nadalin, Pablo Gomes, Matías Alzogaray), 2026-09-21"
producto: ardid
tema: Problemas de performance/confiabilidad de Ardid (demoras y fallas al generar reportes) están afectando la venta del servicio a Coto y Grupo DESA, con desvío de responsabilidad Fintexa↔Penta sin resolver
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "posible actualización de un riesgo ya capturado sobre Grupo DESA (id 2026-09-14_clientes_grupo_desa_riesgo_continuidad_escalado_dir, régimen: 'en_cola' según contexto_vivo/index.md) — el archivo correspondiente no se encontró en disco al momento de esta captura (ver nota de anomalía en el cuerpo); no se pudo verificar ni completar in place"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

**⚠️ Nota de anomalía de integridad, no del contenido de este item:** `contexto_vivo/index.md` lista el item `2026-09-14_clientes_grupo_desa_riesgo_continuidad_escalado_dir` (riesgo, adquirencia — "Grupo DESA amenaza con dar de baja el servicio, reclamo escalado a dirección") como `en_cola`, pero el archivo `wiki/1_proyectos/contexto_vivo/2026-09-14_clientes_grupo_desa_riesgo_continuidad_escalado_dir.md` **no existe en disco** — junto con una veintena más de items listados como `en_cola`/`capturado` en el índice de fechas 2026-09-16 a 2026-09-21 (ej. todo el lote `2026-09-18_*`, varios `2026-09-21_*`). Este barrido de `/sync_meetings` no investigó la causa (está fuera de su alcance) — se señala para que el usuario lo revise: puede ser una pérdida real de contenido capturado y nunca subido a `CEREBRO_CORE`, o un desfasaje entre el índice y el estado real de la carpeta. Por las dudas, este hallazgo se captura como item **nuevo** (no como edición in place del item de 09-14, que no se pudo localizar), citando el contenido conocido del item anterior por lo que registra el índice.

**Hallazgo nuevo (reunión "Weekly - Producto / Operaciones", 2026-09-21):** Mariana Nadalin reportó que **Ardid está "andando para atrás" en cuanto a performance** — reportes que no se generan, o que se generan sin datos, entre otros síntomas (no se detalló una lista completa en la minuta). El punto de negocio: Bind PSP está comercializando/ofreciendo Ardid como servicio a clientes — ya lo tiene **Coto** y se le ofreció **la semana pasada (semana del 14/09) a Grupo DESA también** — sin haber confirmado antes que la infraestructura soporte la carga.

**Desvío de responsabilidad sin resolver:** según Mariana Nadalin, Fintexa dice que el problema es de Penta (el proveedor de infraestructura/hosting), y Penta dice que es de Fintexa — "así damos vueltas y vueltas". Se acordó escalar el reclamo conjuntamente a Fintexa, Hernán (Clarich, Arquitectura) y Penta, y evaluar si el problema tiene que ver con cómo están paginadas las consultas en las versiones que gestiona Matías Alzogaray.

**Conexión con Grupo DESA (según lo ya capturado el 2026-09-14, sin poder verificar el archivo original — ver anomalía arriba):** el índice de `contexto_vivo/` registra que Grupo DESA (cliente de mayor volumen de Botón Simple 1.0, también protagonista del problem statement de `rechazos_bines_payway`/PRD-251) amenaza con dar de baja el servicio y que el reclamo ya escaló a dirección. Si la oferta de Ardid a Grupo DESA mencionada hoy es parte de la negociación para retenerlo, un Ardid con problemas de performance conocidos podría jugar en contra de esa negociación — conexión razonable pero no confirmada explícitamente en ninguna de las dos fuentes.

**Estado:** riesgo en escalamiento activo (Mariana Nadalin/Pablo Gomes acordaron elevarlo a Fintexa/Hernán/Penta en esta misma reunión) — sin ticket, sin fecha de resolución, sin dueño único confirmado todavía por el desvío de responsabilidad entre proveedores.
