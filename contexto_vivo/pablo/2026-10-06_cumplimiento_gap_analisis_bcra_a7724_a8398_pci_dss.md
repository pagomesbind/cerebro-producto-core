---
id: 2026-10-06_cumplimiento_gap_analisis_bcra_a7724_a8398_pci_dss
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_mails — mail \"GAP Análisis BIND-PSP\" de Hernán Clarich (Fintexa, hernan.clarich-ext@bind.com.ar) a Eugenia Blanco (Auditoría, Banco Industrial), 2026-10-06, threadId 1a110c40e55f3709, cc Emma Vignoles/Mariana Nadalin/Pablo Gomes"
producto: transversal
tema: GAP Analysis consolidado de cumplimiento tecnológico/seguridad (A7724/A7777/A7783/A8398) y PCI-DSS entregado a Auditoría del banco
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/gestion_riesgo_tecnologia_seguridad_a7724.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Hernán Clarich (Fintexa, vía cuenta `hernan.clarich-ext@bind.com.ar`) envió el 2026-10-06 a Eugenia Blanco (Auditoría, Banco Industrial) el **GAP Analysis de la PCP** (adjunto `34257-gap-analisis-bcra-psp-v12.xlsx`), con copia a Emma Vignoles, Mariana Nadalin y Pablo Gomes.

Puntos relevantes del cuerpo del mail:

- El archivo **consolida 4 comunicaciones BCRA: A7724, A7777, A7783 y A8398**, siempre analizadas **desde el enfoque PSP y PSP como servicio** (no desde el enfoque de entidad financiera tradicional). Esto es la primera evidencia concreta en el Cerebro de que existe un GAP Analysis que efectivamente trata la aplicabilidad específica a PSP de estas comunicaciones — incluida la A7783, que `gestion_riesgo_tecnologia_seguridad_a7724.md` menciona como "citada en la tabla de correlaciones de otra norma pero no conseguida" (ver sección "Por qué se había marcado como duda de aplicabilidad"). Este mail confirma que la A7783 sí fue trabajada en el análisis de gap, aunque el contenido del Excel no se leyó automáticamente.
- **Algunas adecuaciones del GAP están alineadas con puntos de PCI-DSS**, dado que ambas normativas exigen la existencia de políticas y procedimientos — Hernán marca esto como un punto de cruce entre ambos frentes normativos (A7724/8398 de un lado, PCI-DSS del otro), relevante para no duplicar esfuerzo de adecuación entre `gestion_riesgo_tecnologia_seguridad_a7724.md` y `pci_dss_recertificacion.md`.
- **Las fechas de implementación de algunas adecuaciones están "un poco ajustadas" a un inicio desde fines de julio de 2026** — sin fecha límite explícita en el cuerpo del mail, pero marca que el plan de adecuación ya tiene cronograma en marcha, no solo diagnóstico.
- Formato: Excel, adjunto al mail, no leído automáticamente por esta skill (ver nota de adjuntos pendientes).

**Relevancia directa para el Anexo B:** el `gestion_riesgo_tecnologia_seguridad_a7724.md` ya documenta (sección "Anexo B — Comités...") que la auditora del banco (Eugenia Blanco) indicó el 2026-09-30 que *"la base para contestar el Anexo B debe ser el GAP Analysis y los Planes de Adecuación"*. Este mail es la entrega concreta de ese GAP Analysis a la propia Eugenia Blanco — cierra (o al menos avanza fuerte) ese prerrequisito. Vale la pena que el PM confirme si este GAP Analysis es insumo directo para las planillas B1a-B1h del Anexo B que tiene asignadas (ver T-165 en `tareas.md`).

**Pendiente de lectura manual:** el adjunto `34257-gap-analisis-bcra-psp-v12.xlsx` (GAP Analysis completo, por norma/punto/estado/fecha) no se leyó — si el PM lo abre, vale la pena volcar su detalle en un item de seguimiento o directamente actualizar este archivo con el estado adecuación por adecuación.
