# Configurar Onboarding con Wallet

> Estado: en producción. Reubicado desde `detalle_productos/onboarding/manuales_operativos.md §2` en la reestructuración PARA en cascada (2026-08-12). Objetivo: dejar configurado un flujo de onboarding que finalice con la creación de cuentas en Wallet.

**Precondiciones:** tener la organización creada (ver instructivo interno de Notion), y tener un flujo de onboarding creado que incluya el paso de alta wallet.

**Configuraciones:**
- Solicitar por Jira la creación del registro en el archivo de configuración del BFF a Wallet, indicando: AMBIENTE (STG/PROD), `x-aplicacion` = CódigoEntidad, `idOrganización` = idOrganización.
- Si la organización no quiere que se asigne el alias por defecto y lo quiere hacer ella, debe desmarcarse la opción desde la configuración de la Entidad en el backoffice de onboarding.

**Validaciones:** en staging, ejecutar regresión automática (ver instructivo interno).

## Ver también
- [consultar_solicitud_y_archivos.md](consultar_solicitud_y_archivos.md) — cómo consultar el resultado del paso `alta-Wallet` una vez configurado.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/onboarding/manuales_operativos.md §2` (reestructuración PARA en cascada). Contenido sin cambios.*
