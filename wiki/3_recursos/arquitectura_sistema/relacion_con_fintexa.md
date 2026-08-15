# Relación con el Proveedor Fintexa — Dotación de Recursos y Gobierno de Arquitectura (COE)

> Reubicado y consolidado desde `arquitectura_sistema/index.md §11` (dotación de recursos) y `§13` (Comité de Arquitectura COE) en la reestructuración PARA en cascada (2026-08-12) — ambos temas son la relación operativa/de gobierno con el proveedor de infraestructura, no arquitectura técnica en sí.

## 1. Dotación de recursos — bajas consecutivas (julio-agosto 2026)

> Fuente: Mail "Cambios recursos FINTEXA - BIND PSP Julio 2026" — agustin.grau@fintexa.tech (2026-07-14).

A partir de julio 2026 quedaron efectivas bajas en el equipo de Fintexa asignado a Bind PSP: Franco Gimenez (Soporte), Rodrigo Lucero (QA), Pablo Martínez (SRE — pasa a quedar solo 1 semana al mes en guardia pasiva de Infra) y Daniel Perez Ojeda (Dev Wallet). Reducción de capacidad de soporte/SRE/QA del proveedor de infraestructura — ver riesgo registrado en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

> Fuente: Mail "Cambios recursos FINTEXA - BIND PSP AGOSTO 2026" — agustin.grau@fintexa.tech (2026-08-04).

A partir de agosto 2026, nuevas bajas: Federico Favia (QA Wallet), Marcelo Natrielo (Dev Adquirencia) y Leonel Zalegas (Dev Mobile POS). Además, modificaciones de rol: Mariela Marin deja de liderar el equipo de QA y pasa a ser QA bajo el scope del PM correspondiente (pierde el rol de lead); Pablo Vydra (Dev Mobile POS) baja su asignación al 50%. Segunda reducción consecutiva de dotación del proveedor en dos meses — reafirma el riesgo de capacidad ya registrado en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

## 2. Comité de Arquitectura COE — informe mensual (julio 2026)

> Fuente: Mail "INFORME Mensual Comité de Arquitectura COE" — alejandro.sfrede@fintexa.tech, 2026-08-07. Detalle completo en el adjunto `COE-TAREAS-AGO2026.pdf` (no leído en esa corrida).

Estado consolidado de julio 2026 de las iniciativas de arquitectura transversal seguidas por el Comité (referencia interna: tickets `PA-XXX`):

- ✅ **Listo / disponible a verticales:** autenticación externa (Wallet y Aceptador — resta 1 fase), procedimiento de HOTFIX de corrección rápida, notificaciones estabilizadas en Wallet, feature flags disponibles a verticales, API buffer.
- 🟢 **En progreso:** Zero-Downtime (Hernán Clarich lo escaló a verticales el mismo día), red de seguridad de mensajería, depuración/retención de datos, protección de datos en registros, control de salidas de red, monitoreo de salud, modernización .NET 10, colas Quorum, programa de eficiencia y gobierno (IA), políticas de workers.
- 🔵 **En diseño o definición:** **Onboarding unificado**, rate limit por plan, auditoría de tokens, estrategia de mensajería, optimización de bases de datos, visibilidad de estado, acceso unificado de conciliación, catálogo de APIs, reporte mensual.
- ⚪ **Backlog:** programa de pruebas de seguridad + desarrollo seguro, mTLS, particionamiento, Hangfire, capacidad AKS, caché Redis, cierre de malla de servicios, prevención de fraude/compliance.
- 🔴 **Bloqueado:** evaluación de motor de base de datos (PostgreSQL).

## Ver también
- [mantenimiento_y_capacidad_aks.md](mantenimiento_y_capacidad_aks.md) — plan de mantenimiento AKS de agosto 2026, ejecutado por el mismo proveedor.
- [calidad_y_cicd.md](calidad_y_cicd.md) — roadmap técnico declarado por el proveedor, contrastar contra el estado real reportado acá por el COE.

---
*Última actualización: 2026-08-12 — Reubicado y consolidado desde `arquitectura_sistema/index.md §11` y `§13` (reestructuración PARA en cascada). Contenido sin cambios.*
