---
id: 2026-10-15_transversal_decision_portafolio_en_app_roadmap
pm: pablo
fecha_captura: 2026-10-15
fuente: "Sesión de trabajo con Pablo Gomes (Claude Code), 2026-10-14/15 — plan aprobado ~/.claude/plans/dapper-giggling-fern.md"
producto: transversal
tema: El portafolio de producto vive en la app Roadmap de Producto; Jira queda para desarrollo
tipo: decision
destino_propuesto: wiki/2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "wiki/2_areas/procesos/gestion_jira.md — hoy describe a Jira Product Discovery (PRD) como lugar del roadmap y del ciclo de vida de las IDEAs"
confianza: alta
estado: en_cola
merge_commit:
---

**Fecha:** 2026-10-15 · **Estado:** Aprobado (decisión del PM líder; falta socializar con Nicolás Colón y Luciana Rudaz)

**Contexto / problema.** El roadmap estaba repartido entre Jira Product Discovery (PRD), con sincronización manual y frágil, y decks por cliente (ej. el roadmap de Compliance presentado a PLAFT en octubre 2026). No había forma de cruzar el roadmap de un cliente con el resto de las iniciativas para saber si entra en la capacidad del equipo por mes o por trimestre.

**Decisión.**
1. El portafolio de iniciativas de producto (mes de salida, producto, responsable, SP estimados, estado, clientes, etiquetas) pasa a vivir en la app **Roadmap de Producto Bind PSP** (artifact de claude.ai con base compartida): https://claude.ai/artifact/VgnW2yVbqEYCF2HeMpJ9yo. Es la fuente de verdad del roadmap para los tres PM.
2. **Jira queda para la gestión del desarrollo** (épicas e historias en WS/AD/OB/ARD/SER) y como fuente del avance de delivery de cada iniciativa. Jira PRD queda como origen histórico; su reemplazo formal en las skills (`/idea_start`, `/idea_jira`) es una fase 2 a decidir.
3. La planificación se hace **por mes de salida** (sin inicio–fin), y la capacidad se mira por mes y por trimestre. La capacidad de referencia es el SP neto publicado por producto en una ventana móvil de 3 meses, descontando el soporte (SOPORTE, REGRESIONES, COE, INICIATIVAS TÉCNICAS, REQUERIMIENTOS INTERNOS, deuda técnica), según el Pulso de Delivery. Primer cálculo (jul–sep 2026): Wallet 37,4 SP/mes neto (58,1 bruto, 35,6% soporte), Cobro 53,8 SP/mes neto (93,3 bruto, 42,3% soporte); Onboarding, Servicios y Ardid sin datos de delivery.
4. Entran al roadmap las IDEAs desde DISCOVERY en adelante; PARKING LOT queda fuera; STAND BY se muestra aparte («En pausa») sin consumir capacidad.
5. **La app no escribe en la wiki.** Toda modificación de `1_proyectos/` la hace el Cerebro de cada PM (Claude Code con CLAUDE.md, skills y checklist de cierre). La app registra pedidos en una cola (`pms/{pm}/queue`) que el Cerebro procesa con `/roadmap sync`. El canon (`2_areas/`, `3_recursos/`) sigue siendo exclusivo de `/context_merge`.

**Impacto en roadmap/producto.** Carga inicial: 103 iniciativas desde PRD (93 de DISCOVERY en adelante + 7 en PENDIENTE que estaban comprometidas en el roadmap de Compliance + 3 finalizadas recientes). Los meses de las iniciativas de Compliance se tomaron del deck acordado (prioridad sobre Jira). Nueva skill `/roadmap` (nivel usuario de Pablo; a promover al core cuando se valide). Al cargar se vio que octubre 2026 tiene 180 SP planificados contra ~91 SP de tope neto (Wallet + Cobro): hay que repriorizar.
