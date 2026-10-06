---
id: 2026-10-05_onboarding_conocimiento_rechazada_borra_datos_parametrizable_por_entidad
pm: pablo
fecha_captura: 2026-10-05
fuente: "sesión de trabajo del proyecto bcra_anexo_b — definición de Onboarding aportada por el PM (texto pegado) mientras se redactaba P-04 (Procedimiento de Altas No Concretadas); el PM indicó que se definió en su momento y está en producción"
producto: onboarding
tema: Al pasar una solicitud a RECHAZADA el sistema borra los datos y conserva solo un registro mínimo; el proceso es parametrizable por entidad y solo debe aplicarse a las entidades del banco
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md y `proyecto-onboarding-estrategico/gaps.md` (2026-07-20) — registran que Fintexa confirmó que los archivos en Onboarding son temporales y que no existe limpieza automática (tarea T-036 en `2_areas/tareas.md` pidiendo construirla). El PM indica que el borrado al pasar a rechazada ya está definido y en producción. Confirmar el alcance real: ¿es solo la solicitud rechazada, y los archivos temporales de otras solicitudes siguen sin limpieza?"
confianza: media
estado: en_cola
merge_commit:
---

Definición de Onboarding, aportada por el PM el 2026-10-05, que según el PM está en producción:

> Al pasar alguien a RECHAZADO, borrar datos. Dejar sólo: identificador, fecha, hora, gestor, historial, vista de validaciones y vista de timeline. Este proceso debe ser parametrizable por ENTIDAD, porque sólo debería hacerse en las entidades del banco y no en todas (por ejemplo, RIPSA).

## Cómo se usa en los procedimientos

- Se refleja en P-04 (Procedimiento de Altas No Concretadas), sección de conservación y disposición final: las solicitudes rechazadas de las entidades con el proceso activado conservan solo ese registro mínimo; en las demás entidades se conservan con las medidas de protección habituales.
- Para las altas no concretadas que no son rechazadas (vencidas, pendientes) no hay eliminación automática ni plazo de conservación definidos; sigue siendo una brecha (B-06 de `1_proyectos/bcra_anexo_b/brechas_cumplimiento.md`).
- Es relevante para el requisito de "disposición final de las altas no concretadas" del requerimiento del BCRA.

## Por verificar

- Qué entidades tienen activado el borrado hoy (las del banco, según el PM).
- Si el borrado alcanza también a los archivos (imágenes de DNI y selfie) de la solicitud rechazada.
- Si aplica a la solicitud rechazada por validación manual y a las de persona jurídica.
