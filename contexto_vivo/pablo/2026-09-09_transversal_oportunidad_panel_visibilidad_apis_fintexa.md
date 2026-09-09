---
id: 2026-09-09_transversal_oportunidad_panel_visibilidad_apis_fintexa
pm: pablo
fecha_captura: 2026-09-09
fuente: "Assessment de auditoría del banco tras el fraude de Transferencias Pull (raw/BIND PSP- Assessment 14052026.xlsx, hoja 'Aspectos Identificados', área 'Implementaciones', PRIORIDAD Media). Remediación liderada por Hernán Clarich y Mariana Nadalin."
producto: transversal
tema: Dependencia funcional con Fintexa para credenciales/homologación de APIs — Bind PSP no tiene visibilidad ni administración propia de qué APIs consume cada cliente
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 4b0d3d1e684ff33256a33a29f86746dfd5c7cc9a
---

## Qué encontró el banco

"La generación de credenciales, homologación y producción, es realizada por Fintexa. Asimismo, desde BIND PSP no tienen acceso a la administración o consulta de las api que consume el cliente. En estos casos, desde el área de implementaciones realizan la consulta a Fintexa [...] BIND PSP debería tener esa tarea." Riesgo declarado: "de continuidad de negocio. Si el proveedor falla, la PSP no tiene capacidad de reacción ni auditoría (Lock-in tecnológico)." Además, las credenciales hoy no están divididas por API permitida sino por vertical/producto completo — más superficie de exposición que la necesaria.

## Mitigante propuesta por el propio equipo de Implementaciones (en el assessment)

"Disponer de un archivo con la información de usuarios y endpoints habilitados por cliente generado por Fintexa" y, idealmente, "un panel consultivo (preferentemente administrativo) de Fintexa con las apis habilitadas por usuario cliente, para actualización y consulta" — con la aclaración de que esto "colisiona con Seg Info" y que Bind PSP "sólo debería tener visualización" (no administración plena), al menos en una primera etapa.

## Por qué es una oportunidad de Producto, no solo de Implementaciones

Sin visibilidad propia de qué API consume cada cliente, Producto tampoco puede evaluar con precisión el impacto de deprecar/migrar un endpoint (ver el patrón ya vivido en `getnet_oauth2_resolve/` — depender de que Fintexa confirme volumen y aceptadores activos) ni auditar exposición de superficie de ataque por cliente. Es candidato a un proyecto propio de Producto/Plataforma (panel de solo lectura, alimentado por un archivo o API que hoy no existe), no solo un pedido de proceso hacia Fintexa.

## Qué haría falta para avanzar

- Confirmar con Seg Info hasta dónde puede llegar Bind PSP en visibilidad (dato ya señalado como fricción en el propio assessment).
- Definir con Implementaciones/Integraciones el alcance mínimo: ¿alcanza con un archivo/reporte periódico de Fintexa, o hace falta un panel interactivo?
- Evaluar si conviene atarlo a la migración de credenciales por API (en vez de por vertical/producto completo) que menciona el mismo punto del assessment.

Ver tarea relacionada `T-077` en `tareas.md`.
