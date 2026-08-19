---
id: 2026-08-18_transversal_riesgos_md_por_proyecto
pm: pablo
fecha_captura: 2026-08-18
fuente: "conversación libre con el usuario — revisión de la estructura de 1_proyectos/ antes de desplegar el Cerebro al resto de los PO"
producto: transversal
tema: agregar riesgos.md por proyecto/subproyecto, mismo patrón lazy que gaps.md
tipo: decision
destino_propuesto: CLAUDE.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9306bc6b7cffeb57db264f132b0e0e6a1ec53d8e
---

**Contexto/Problema:** El usuario planteó si convenía llevar simetría total entre proyecto y nivel global para los cuatro ledgers de proyecto (`gaps.md`, `tareas.md`, `decisiones.md`, `riesgos.md`) — es decir, que cada proyecto/subproyecto tuviera los cuatro, y que además hubiera un cuarto nivel "global" de los cuatro dentro de `1_proyectos/` (además del canon en `2_areas/`).

**Análisis:** Se evaluó cada ledger por cardinalidad y ciclo de vida, no por simetría formal:
- **Gaps y decisiones a nivel proyecto:** ya están bien como están (creación lazy, la primera vez que hace falta). Son memoria de trabajo del discovery — se generan y resuelven en volumen mientras el proyecto está activo, se referencian todo el tiempo, y se archivan como unidad junto con el proyecto al cerrar. No corresponde aplanarlos a un archivo global.
- **Riesgos a nivel proyecto:** es el hueco real. Un riesgo específico de una IDEA (ej. atraso de una dependencia, riesgo de scope) hoy no tiene dónde vivir sin ensuciar `wiki/2_areas/riesgos.md` (que es solo lo general e importante del equipo). Se decide sumar `riesgos.md` por proyecto/subproyecto, con el mismo patrón lazy que `gaps.md` (nace la primera vez que surge un riesgo específico de ese proyecto, no se provisiona de entrada).
- **Tareas a nivel proyecto:** se descarta. `1_proyectos/tareas.md` funciona bien plano porque es una lista de ejecución personal (tipo GTD) de baja duración de vida — partirla por proyecto obligaría a mirar N archivos para saber "qué tengo que hacer hoy". Sin cambios.
- **Cuarto nivel "global" dentro de `1_proyectos/` (además del canon en `2_areas/`):** se descarta. Ya lo cubre el patrón existente `contexto_vivo/` → canon (`2_areas/gaps_y_preguntas.md`, `direccion/decisiones.md`, `riesgos.md`, `tareas.md`) para lo que es general de la empresa. Agregar otra capa intermedia triplicaría dónde buscar cada tipo de dato sin ganancia real.

**Decisión tomada:** Sumar `riesgos.md` como archivo opcional (lazy, igual que `gaps.md` y `decisiones.md`) dentro de la carpeta de cada proyecto/subproyecto en `1_proyectos/`, para riesgos específicos de ese proyecto/discovery. No se agrega `tareas.md` a nivel proyecto. No se agrega una capa global adicional dentro de `1_proyectos/`. El resto de la estructura documentada en `CLAUDE.md` (§1_proyectos, §Protocolo de Clasificación PARA) queda sin cambios.

**Impacto en el roadmap/producto:** Cambio de convención de estructura de la wiki, aplicable a los tres Cerebros (Pablo, Nicolás, Luciana) antes del despliegue al resto del equipo de Producto. No afecta ningún proyecto/PRD puntual — es tooling/convención del propio sistema.

**Estado:** Aprobado (por el usuario, dueño de este Cerebro — confirmar con Nicolás/Luciana o con quien lidere el despliegue si corresponde alinear antes del rollout).

**Cambio concreto propuesto para `CLAUDE.md`:**
1. En la sección `## El modelo: PARA en cascada de 3 saltos`, punto 1 (`1_proyectos/`): donde dice *"con su propio contexto local (`proyecto.md`, `gaps.md`, `decisiones.md`, `artefactos/`)"* → agregar `riesgos.md` a la lista: *"con su propio contexto local (`proyecto.md`, `gaps.md`, `decisiones.md`, `riesgos.md`, `artefactos/`)"*.
2. En `## Protocolo de Clasificación PARA (Fintech Core)`, bullet `1_proyectos/`: donde describe la carpeta de cada proyecto/slice (`proyecto.md` + `gaps.md` + `decisiones.md` + `artefactos/`) → agregar `riesgos.md` al patrón, con la misma nota de creación lazy que ya aplica a `gaps.md`/`decisiones.md` ("según haga falta").
3. En `## Reglas Generales de Control y Mantenimiento de Memoria`, agregar un punto nuevo (o extender el punto 1 de gaps) aclarando que un riesgo específico de un proyecto/IDEA va directo a `riesgos.md` de esa carpeta (mismo criterio que gaps/decisiones: si cruza varios slices de un proyecto general, va al `riesgos.md` del padre); un riesgo de contexto fijo/general de la empresa sigue naciendo como item `tipo: riesgo` en `contexto_vivo/` rumbo a `wiki/2_areas/riesgos.md`.
4. En el `Checklist de cierre de sesión/skill`, agregar `riesgos.md` junto a "gaps y decisiones del proyecto (directo, si aplica)".
