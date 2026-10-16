---
id: 2026-10-15_adquirencia_gap_titularidad_tarjeta_sin_proyecto_trackeado
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — detectado al procesar la reunión 'Análisis COBRO' (2026-10-15) contra `1_proyectos/index.md` y `detalle_productos/adquirencia/index.md`"
producto: adquirencia
tema: PRD-25/titularidad_tarjeta no existe en la tabla maestra de 1_proyectos/index.md pese a tener diseño técnico avanzado en curso
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "wiki/3_recursos/detalle_productos/adquirencia/index.md (actualización 2026-09-23) afirma que el reenvío de una propuesta de MODO 'fue el disparador confirmado del discovery del proyecto activo titularidad_tarjeta (PRD-25)' — pero ni PRD-25 ni ninguna carpeta titularidad_tarjeta/ existen en wiki/1_proyectos/index.md §2, ni hay carpeta física en 1_proyectos/, ni aparece en la lista de IDEAs Finalizadas de §3."
confianza: media
estado: en_cola
merge_commit:
---

## Qué se encontró

El canon de Adquirencia (`detalle_productos/adquirencia/index.md`) documenta desde el 2026-09-23 que existe un "proyecto activo `titularidad_tarjeta` (PRD-25)". Al procesar la reunión "Análisis COBRO" del 2026-10-15 — donde Nicolás Colón presentó un diseño técnico completo y maduro de la integración con MODO para esta misma funcionalidad (ver item `2026-10-15_adquirencia_conocimiento_diseno_validacion_titularidad_modo`) — se buscó la carpeta/fila correspondiente en `wiki/1_proyectos/index.md` §2 (tabla maestra, resolver de rutas) para actualizarla directamente, como corresponde a `1_proyectos/` (escritura directa, sin pasar por `contexto_vivo/`).

**No se encontró ninguna fila ni carpeta**: ni `PRD-25` en la tabla maestra, ni `titularidad_tarjeta/` como carpeta física bajo `1_proyectos/`, ni en la lista de IDEAs Finalizadas de §3 (que tampoco lo incluye).

## Posibles explicaciones (sin confirmar)

1. El proyecto nunca llegó a crearse formalmente como carpeta en `1_proyectos/` pese a que el canon de `3_recursos/` ya lo da por "activo" desde hace más de tres semanas — posible salto de paso en el flujo `/idea_start`.
2. El proyecto se creó y se trabajó fuera de este Cerebro (otra sesión, otro PM) y nunca se sincronizó a este índice.
3. El proyecto cambió de nombre/IDEA de Jira y el canon de `3_recursos/` quedó con la referencia vieja.

## Impacto

Sin una carpeta de proyecto, el trabajo de diseño sustancial hecho en la reunión del 15/10 (reglas de negocio completas, manejo de errores, arquitectura de servicio externo, caché) queda **solo como conocimiento de producto en `contexto_vivo/` y luego en `detalle_productos/`**, sin decisiones/gaps/riesgos propios de proyecto, sin tabla de IDEA en Jira verificada desde este Cerebro, y sin que `1_proyectos/index.md` refleje que hay trabajo activo en curso sobre esto.

## Qué falta decidir

Confirmar con el usuario (Pablo Gomes) si PRD-25 existe realmente en Jira y en qué estado, y si corresponde crear la carpeta `titularidad_tarjeta/` en `1_proyectos/` retroactivamente (vía `/idea_start` o similar) para que el trabajo futuro sobre esta integración tenga dónde aterrizar.

> Fuente: cruce entre `detalle_productos/adquirencia/index.md` y `1_proyectos/index.md`, detectado 2026-10-16 al procesar la reunión "Análisis COBRO" del 2026-10-15.
