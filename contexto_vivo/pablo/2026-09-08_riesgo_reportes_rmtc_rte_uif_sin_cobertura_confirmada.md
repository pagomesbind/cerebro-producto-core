---
id: 2026-09-08_riesgo_reportes_rmtc_rte_uif_sin_cobertura_confirmada
pm: pablo
fecha_captura: 2026-09-08
fuente: "Consulta directa al Boletín Oficial (aviso 318446, 19/12/2024 — RESOL-2024-200-APN-UIF#MJ, Resolución UIF 200/2024) hecha por el usuario durante una auditoría de cumplimiento del proyecto Onboarding Estratégico, cruzada contra un barrido exhaustivo del Cerebro (sub-agente de exploración, misma sesión) sobre reportería UIF/BCRA ya documentada."
producto: transversal
tema: Dos reportes sistemáticos obligatorios de la Resolución UIF 200/2024 (RMTC y RTE) sin ninguna mención en el Cerebro
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no — es una ausencia, no una contradicción. Lo más cercano ya documentado es 3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md (reportería diaria a Worldsys/BCRA, LAVADOOPERACIONES/LAVADOCLIENTES) y limites_operativos_uif_ros.md (topes mensuales para decidir generación de ROS) — ninguno de los dos es RMTC ni RTE."
confianza: media
estado: ingestado
merge_commit: d7e1ccf
---

## Qué se detectó

Al pedir a WebFetch el contenido oficial del aviso del Boletín Oficial que resuelve a la Resolución UIF 200/2024, el resumen devuelto incluye, entre los "Reportes Sistemáticos" que la norma exige a los sujetos obligados del art. 20 incisos 5 y 6 de la Ley 25.246 (que incluye a emisores de tarjetas y a operadores/proveedores de servicios de cobro y/o pago — la categoría de Bind PSP):

- **RMTC — Reporte Mensual de Tarjetas de Crédito:** para transacciones iguales o superiores a 13 SMVM (Salario Mínimo Vital y Móvil).
- **RTE — Reporte de Transacciones en Efectivo:** para depósitos iguales o superiores a 20 SMVM, identificando al depositante.

Un barrido dedicado del Cerebro completo (sub-agente de exploración, en la misma sesión que capturó este item) no encontró **ninguna** mención de "RMTC", "reporte mensual de tarjetas", "transacciones en efectivo" ni "reporte de efectivo" en ningún archivo de `wiki/`. Lo más cercano que existe es la reportería diaria a Worldsys/BCRA (`3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md`, tipos `LAVADOOPERACIONES`/`LAVADOCLIENTES`, entre otros) y los topes operativos mensuales para decidir cuándo pedir documentación de respaldo antes de generar un ROS (`limites_operativos_uif_ros.md`, $25M PF/$300M PJ) — ninguno de los dos es, ni parece ser, el mecanismo técnico de RMTC/RTE.

## Por qué se registra como riesgo y no como gap de un proyecto puntual

No es un vacío de diseño de ningún PRD de Onboarding — RMTC/RTE son reportes sistemáticos masivos (de todas las transacciones que superan un umbral, no del onboarding de una cuenta puntual), de responsabilidad típica de Compliance/PLD y/o de un equipo de reportería regulatoria, no de Producto. Se captura como riesgo de contexto fijo porque:

1. **No hay evidencia en el Cerebro de que Bind PSP los genere** — puede ser que existan y simplemente no estén documentados acá (blind spot de documentación), o puede ser un incumplimiento real no detectado hasta ahora.
2. Es exactamente el tipo de hallazgo que la Regla Central de este Cerebro pide escalar sin asumir una resolución — no corresponde inventar que "seguramente ya se hace" ni tampoco alarmar como incumplimiento confirmado sin verificar.

## Qué falta para cerrar esto

Confirmar con Administración/Compliance/PLD si Bind PSP ya genera y presenta RMTC y RTE por algún proceso no documentado en este Cerebro (ej. a cargo de Worldsys, de un sistema de reportería regulatoria separado, o de un equipo de Compliance con su propio tooling). Si la respuesta es "no se genera", es una exposición regulatoria activa que amerita escalarse más allá de este Cerebro de Producto.

## Actualización (2026-09-08, 2ª ronda) — ya tiene IDEA de discovery propia

El PM pidió trackear esto como tema nuevo de discovery dentro del foco Onboarding. Se creó **PRD-244** en Jira (estado DISCOVERY) y su slice correspondiente en `1_proyectos/proyecto-onboarding-estrategico/prd-244_rmtc_rte_reportes_uif/proyecto.md` — ver item `tipo: iniciativa` hermano (`2026-09-08_onboarding_iniciativa_prd244_rmtc_rte_creado`). Este item de riesgo sigue siendo la fuente/justificación de por qué se abrió esa IDEA; el seguimiento operativo pasa a vivir en el slice, no acá.
