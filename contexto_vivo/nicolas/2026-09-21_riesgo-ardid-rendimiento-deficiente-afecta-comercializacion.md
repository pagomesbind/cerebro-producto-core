---
id: 2026-09-21_riesgo-ardid-rendimiento-deficiente-afecta-comercializacion
pm: nicolas
fecha_captura: 2026-09-21
fuente: "Reunión 'Weekly - Producto / Operaciones' (2026-09-21)"
producto: ardid
tema: Deficiencias de rendimiento de Ardid (demoras, fallas en reportes) afectan la comercialización a Coto y Grupo Desa
tipo: riesgo
destino_propuesto: 3_recursos/arquitectura_sistema/relacion_con_fintexa.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

En la reunión "Weekly - Producto / Operaciones" (2026-09-21), Mariana Nadalin y Pablo Gomes reportaron deficiencias de rendimiento en Ardid: demoras y fallas en la generación de reportes ("tirás un reporte y no trae datos, etc."). El problema es relevante porque Bind está **comercializando/ofreciendo el servicio de Ardid a clientes externos** — Coto ya lo tiene y a **Grupo Desa** se le ofreció la semana anterior (reunión comercial) — y la deficiencia de performance compromete esa oferta.

Al buscar responsable, Mariana Nadalin describió un **desvío de responsabilidad circular entre Fintexa y Penta**: "del lado de Fintexa nos dicen que es Penta, Penta nos dice que es Fintexa, y así damos vueltas". Propuso revisar si la infraestructura/recursos de los servidores efectivamente soportan el servicio antes de seguir comercializándolo, y escalar el reclamo conjuntamente a Fintexa, Hernán y Penta. Se mencionó también que parte del problema puede estar relacionado con cómo están paginadas las consultas en las distintas versiones que gestiona Matias Alzogaray — sin conclusión técnica cerrada en la reunión.

No hay todavía un caso puntual documentado (ticket, incidente con cliente) más allá de la mención genérica a Coto y Grupo Desa — a confirmar si ya generó un reclamo formal o sigue siendo una preocupación preventiva de Mariana Nadalin.

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-09-21), minuta Gemini.
