# Seguridad APP Wallet — Remediación de Hallazgos de Pentest Mobile (Sep-2024)

> Estado: en producción. Fuente: Notion histórico, Epic **"Seguridad (foco APP Wallet)"**. Reubicado desde `detalle_productos/wallet/otros_manuales.md §-1` en la reestructuración PARA en cascada (2026-08-12) — es contenido específico de la APK Wallet, no un manual genérico de Wallet. A diferencia de otras Epics, sus tickets vinculados son casos de prueba QA (no historias de desarrollo), cada uno atado a una observación numerada de un **informe de pentest mobile** externo (`Informe-Pentest-Mobile-Bind-Sep_24`).

Focos de remediación identificados a partir del informe:

- **Gestión de sesiones simultáneas**: el pentest detectó que la app permitía múltiples sesiones concurrentes sin invalidación cruzada. La remediación centraliza la validación de token en un endpoint dedicado (`Validate token`) consumido también desde el **Portal Admin** — al cerrar sesión en una pestaña/dispositivo, una sesión abierta en otro lado debe quedar invalidada al primer intento de uso.
- **Política de contraseñas de Access Management no reflejada en la APK**: la app no comunicaba al usuario los requisitos reales de contraseña definidos en Access Management, ni validaba contra esa política antes de enviar — remediación: la app debe validar client-side contra la política real y mostrar los requisitos explícitos en la pantalla de cambio de contraseña.

**Lectura para estimaciones futuras**: un pentest externo con hallazgos de sesión/autenticación en mobile típicamente deriva en trabajo cross-cutting (backend de validación de token + reflejo en cada front — app y admin) más que en un fix aislado.

> **Fase 2** ([WS-29](https://bindpsp.atlassian.net/browse/WS-29)/[WS-66](https://bindpsp.atlassian.net/browse/WS-66), 15 SP c/u, publicado W 65 2025-11-17): continuación del pentest — sin detalle técnico adicional accesible por API más allá del título (mismo patrón: casos de prueba QA atados a observaciones numeradas del informe).

## Ver también
- [3_recursos/arquitectura_sistema/hardening_y_remediacion_de_pentests.md](../../arquitectura_sistema/hardening_y_remediacion_de_pentests.md) — pentests de plataforma más amplios (no solo APP), remediaciones de Access Management/API.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/wallet/otros_manuales.md §-1` (reestructuración PARA en cascada). Contenido sin cambios.*
