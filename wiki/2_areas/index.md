# Áreas — Contexto Fijo de Bind PSP

> Segundo salto del PARA en cascada: el **contexto fijo, general y genérico** de la empresa, el equipo, los productos, las métricas y la dirección — todo lo que un PM necesita antes de bucear en el detalle técnico de `3_recursos/`. A diferencia de `1_proyectos/` (dinámica, cambia todos los días) esta carpeta es **canon compartido entre los tres PM/PO, vivida en el repo `CEREBRO_CORE`**: acá **nadie escribe directo**, ni siquiera una sesión de sync — todo aporte nace como item en `wiki/1_proyectos/contexto_vivo/` y solo `/context_merge` lo ingiere. Los ledgers propios del merge (`tareas.md`, `riesgos.md`, `gaps_y_preguntas.md`, `direccion/{decisiones,oportunidades,iniciativas}.md`, `changelog.md`) tienen escritura libre para esa skill; el resto (overviews, `procesos/`, `clientes/`, `direccion/{north_star,estado_actual,estacionalidad,estrategia}`) requiere permiso explícito antes de crear o modificar, incluso para el merge.

## Subcarpetas

| Carpeta | Contenido |
|---|---|
| [overview_empresa/](overview_empresa/index.md) | Qué es Bind PSP, el Grupo BIND, y la estructura organizacional/equipo. |
| [overview_productos/](overview_productos/index.md) | Qué es y qué vale cada producto (Wallet, Adquirencia, Agente de Cobros y Pagos, Onboarding, Ardid, y los que se sumen) — overviews de negocio, mantenidos por el usuario. |
| [procesos/](procesos/index.md) | Cómo trabaja el equipo: Jira, ceremonias de publicación, análisis de riesgo de despliegue, criterios de priorización/estimación. |
| [clientes/](clientes/index.md) | Cartera de clientes: qué producto integra cada uno, cómo lo opera, pricing. |
| [direccion/](direccion/index.md) | Hacia dónde va Bind PSP: North Star Metrics, estado actual, estrategia de los 3 focos, decisiones, oportunidades, cartera de iniciativas cross-PM. |

## Archivos sueltos

| Archivo | Contenido |
|---|---|
| [glosario.md](glosario.md) | Términos, siglas y errores de transcripción recurrentes. |
| [tareas.md](tareas.md) | Backlog **compartido** de lo general e importante del equipo — el backlog personal de cada PM vive en `1_proyectos/tareas.md`. |
| [riesgos.md](riesgos.md) | Riesgos del contexto fijo (capacidad del proveedor, compliance, plataforma) — distinto de los riesgos de un proyecto puntual, que viven en su propio `proyecto.md`. |
| [gaps_y_preguntas.md](gaps_y_preguntas.md) | Vacíos de información del contexto fijo — distinto de los gaps de un proyecto puntual, que viven en su propio `gaps.md`. |
| [changelog.md](changelog.md) | Resumen corto de cada merge que tocó esta capa, solo lo escribe `/context_merge`. |

## Ver también
- [1_proyectos/index.md](../1_proyectos/index.md) — lo dinámico y personal, en lo que trabaja cada PM día a día. Incluye `contexto_vivo/`, el buzón de todo aporte a esta capa.
- [3_recursos/index.md](../3_recursos/index.md) — el detalle técnico al que se baja cuando hace falta, incluido `datos/` (los stores acumulados que antes vivían en `control/`).

---
*Última actualización: 2026-08-15 — Pipeline de sincronización multi-PM: `control/` se desmanteló (ver `3_recursos/datos/` y `1_proyectos/logs_sync/`), `datasets/` se mudó a `3_recursos/datos/`, `gaps_y_preguntas.md` se mudó acá desde la raíz de `wiki/`, nuevo `direccion/iniciativas.md` y `changelog.md`. Escritura exclusiva de `/context_merge` sobre el repo `CEREBRO_CORE`.*
*Última actualización anterior: 2026-08-12 — Creación del índice raíz de `2_areas/` en la reestructuración PARA en cascada (no existía).*
