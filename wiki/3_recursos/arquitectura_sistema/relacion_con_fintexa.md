# Relación con el Proveedor Fintexa — Dotación de Recursos y Gobierno de Arquitectura (COE)

> Reubicado y consolidado desde `arquitectura_sistema/index.md §11` (dotación de recursos) y `§13` (Comité de Arquitectura COE) en la reestructuración PARA en cascada (2026-08-12) — ambos temas son la relación operativa/de gobierno con el proveedor de infraestructura, no arquitectura técnica en sí.

## 1. Dotación de recursos — bajas consecutivas (julio-agosto 2026)

> Fuente: Mail "Cambios recursos FINTEXA - BIND PSP Julio 2026" — agustin.grau@fintexa.tech (2026-07-14).

A partir de julio 2026 quedaron efectivas bajas en el equipo de Fintexa asignado a Bind PSP: Franco Gimenez (Soporte), Rodrigo Lucero (QA), Pablo Martínez (SRE — pasa a quedar solo 1 semana al mes en guardia pasiva de Infra) y Daniel Perez Ojeda (Dev Wallet). Reducción de capacidad de soporte/SRE/QA del proveedor de infraestructura — ver riesgo registrado en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

> Fuente: Mail "Cambios recursos FINTEXA - BIND PSP AGOSTO 2026" — agustin.grau@fintexa.tech (2026-08-04).

A partir de agosto 2026, nuevas bajas: Federico Favia (QA Wallet), Marcelo Natrielo (Dev Adquirencia) y Leonel Zalegas (Dev Mobile POS). Además, modificaciones de rol: Mariela Marin deja de liderar el equipo de QA y pasa a ser QA bajo el scope del PM correspondiente (pierde el rol de lead); Pablo Vydra (Dev Mobile POS) baja su asignación al 50%. Segunda reducción consecutiva de dotación del proveedor en dos meses — reafirma el riesgo de capacidad ya registrado en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

## 2. Comité de Arquitectura COE — informe mensual (corte agosto 2026, vs. julio 2026)

> Fuente julio: Mail "INFORME Mensual Comité de Arquitectura COE" — alejandro.sfrede@fintexa.tech, 2026-08-07. Fuente agosto: mismo hilo, "RE: INFORME Mensual Comité de Arquitectura COE" — Alejandro Sfrede (Fintexa), 2026-09-02. Detalle completo en los adjuntos PDF (`COE-TAREAS-AGO2026.pdf` / `COE-TAREAS-30DIAS-SEP2026.pdf`), no leídos en ninguna de las dos corridas.

Estado consolidado de las iniciativas de arquitectura transversal seguidas por el Comité (referencia interna: tickets `PA-XXX`). El corte de agosto solo llegó completo para las categorías ✅ y 🟢 (el cuerpo plano del mail se cortó antes de 🔵/⚪/🔴) — esas tres categorías quedan con el corte de julio hasta la próxima corrida, **no asumir que no cambiaron**:

- ✅ **Listo / en producción** — corte agosto: **autenticación externa (Wallet y Aceptador) — migración productiva COMPLETA** (en julio: "resta 1 fase"). **Procedimiento de HOTFIX de corrección rápida** — pasa de "listo" a "operativo, con prueba real de punta a punta programada para cerrar la validación". Feature flags siguen disponibles. Notificaciones estabilizadas en Wallet y API buffer ya no se mencionan como ítems propios en el resumen de agosto (posible consolidación del texto, no necesariamente reversión).
- 🟢 **En progreso** — corte agosto: **Zero-Downtime** — roadmap ampliado a **40+ servicios de Wallet** (en julio sin alcance cuantificado). **Red de seguridad de mensajería** — pasa a "ya en ambiente de prueba productivo, validación final" (antes solo "en progreso" sin detalle). Nuevo ítem: **"Cierre del componente anterior de autenticación"**. **Onboarding unificado** — sube de categoría: estaba en julio en 🔵 (ver abajo) y en agosto ya tiene "base en ambiente de prueba" — dato relevante para el foco de Onboarding, aunque no hay todavía un PRD propio de Pablo Gomes que dependa de esto. Resto de ítems en progreso repetidos sin cambio aparente: depuración/retención de datos, protección de datos en registros, control de salidas de red, monitoreo de salud, modernización .NET 10, colas Quorum, programa de eficiencia/gobierno IA, políticas de workers.
- 🔵 **En diseño o definición (corte julio, sin confirmar en agosto):** Onboarding unificado (subió a 🟢 en agosto, ver arriba), rate limit por plan, auditoría de tokens, estrategia de mensajería, optimización de bases de datos, visibilidad de estado, acceso unificado de conciliación, catálogo de APIs, reporte mensual.
- ⚪ **Backlog (corte julio, sin confirmar en agosto):** programa de pruebas de seguridad + desarrollo seguro, mTLS, particionamiento, Hangfire, capacidad AKS, caché Redis, cierre de malla de servicios, prevención de fraude/compliance.
- 🔴 **Bloqueado (corte julio, sin confirmar en agosto):** evaluación de motor de base de datos (PostgreSQL).

## Ver también
- [mantenimiento_y_capacidad_aks.md](mantenimiento_y_capacidad_aks.md) — plan de mantenimiento AKS de agosto 2026, ejecutado por el mismo proveedor.
- [calidad_y_cicd.md](calidad_y_cicd.md) — roadmap técnico declarado por el proveedor, contrastar contra el estado real reportado acá por el COE.

---
*Última actualización: 2026-09-03 — `/context_merge`: §2 actualizado con el corte de agosto 2026 del informe COE (delta vs. julio, categorías ✅/🟢 completas, 🔵/⚪/🔴 pendientes de confirmar).*
*Última actualización anterior: 2026-08-12 — Reubicado y consolidado desde `arquitectura_sistema/index.md §11` y `§13` (reestructuración PARA en cascada). Contenido sin cambios.*
