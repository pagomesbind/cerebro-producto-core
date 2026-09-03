---
id: 2026-09-02_iniciativa_prd116_lista15_servicio_ya_existe
pm: pablo
fecha_captura: 2026-09-02
fuente: "conversación del PM con Juan M. Rodríguez Acquarone (sistemas Banco Industrial) + captura de flujo legado de onboarding del banco, aportadas directamente en sesión"
producto: onboarding
tema: PRD-116 — hallazgo que redefine el alcance (servicio ya integrado, no requiere build nuevo)
tipo: iniciativa
proyecto: PRD-116
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Novedad a anteponer en la fila de PRD-116 (Validar lista 15 del banco industrial)

El PM confirmó con sistemas de Banco Industrial que la validación de lista 15 (mandato de PLD del grupo) **no requiere integración nueva**: el servicio SOAP de Listas Negras que consulta esa lista ya está integrado y en producción en el onboarding de personas físicas de BIND 24 — solo falta incluir ese paso, ya existente, en los flujos de alta de CVU. Reduce significativamente el esfuerzo estimado de la IDEA. Detalle completo y decisiones asociadas en `1_proyectos/proyecto-onboarding-estrategico/prd-116_validar_lista15_banco/proyecto.md` §5 y `decisiones.md`.
