---
artifact: golive-checklist
version: "1.1"
created: 2026-07-20
status: en curso
context: Ejemplo ilustrativo — cifras y nombres ficticios. Continúa el caso del preview de documentación KYB.
---

# Checklist de go-live: Preview de documentación KYB

> Responsable de toda tarea: PM de Onboarding [Ejemplo]. El "Socio/interesado" es la persona o área con la que hay que resolverla — no reemplaza al PM como dueño de la fila.

## Necesarias para producción (bloqueadores)

| ID | Tarea | Socio/interesado | Estado |
|---|---|---|---|
| T-201 | Conseguir que Ing./Arquitectura resuelva la metadata de Fintexa (o cierre un plan B del lado de Bind) — sin esto no se puede armar la pantalla de preview | Ing./Arquitectura | 🔴 Bloqueador — Pendiente |
| T-202 | Conseguir que Ingeniería/Data instrumente el evento "vio preview"/"abandonó en preview" — sin esto no se puede medir la hipótesis del A/B test | Ingeniería/Data | 🔴 Bloqueador — Pendiente |
| T-203 | Conseguir de Diseño las imágenes de ejemplo por tipo de documento (unipersonal + sociedad) | Diseño | 🟡 Pendiente (unipersonal alcanza para lanzar si hace falta priorizar) |

## Otras tareas importantes del proyecto

| ID | Tarea | Socio/interesado | Estado |
|---|---|---|---|
| T-204 | Avisar a Soporte de la nueva pantalla antes del lanzamiento, para que sepan explicarla si un comercio pregunta | Soporte (Gonzalo Rivera) [Ejemplo] | ✅ Hecho (2026-08-10) |
| T-205 | Pedirle a un segundo PM que revise el copy de la pantalla | — (interno de Producto) | 🟢 Pendiente, no urgente |
| T-206 | Confirmar con Legal/Cumplimiento que la pantalla no modifica los requisitos de KYB en sí (solo los muestra antes) | Cumplimiento [Ejemplo] | ✅ Hecho (2026-08-05) |

---
*Historial de revisiones: v1.0 (2026-07-20) — primera versión, generada a partir de la revisión cruzada por área, del relevamiento de riesgos y de `riesgos.md` del proyecto. v1.1 (2026-08-12) — T-204 y T-206 marcadas hechas por `/sync_meetings` tras confirmarse en la reunión "Repaso pre-lanzamiento KYB"; comentario de Jira reposteado automáticamente en ese momento.*
