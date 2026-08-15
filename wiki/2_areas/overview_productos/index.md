# Índice — Líneas de Producto de Bind PSP

> Índice local del módulo. El Bibliotecario lo consulta antes de abrir un overview de producto específico. Ver también [empresa.md](../overview_empresa/overview_empresa_general.md) y [equipo.md](../overview_empresa/overview_equipo.md).

| Producto | Descripción breve | Proveedor / Software Factory | Archivo |
|---|---|---|---|
| **Wallet** | Billetera digital vía API (PSP as a Service / multiPSP) | Keepit (subcontratada de FINTEXA) | [wallet_overview.md](overview_wallet.md) |
| **Adquirencia** | Cobro a comercios (QR, tarjeta, transferencia); liquidaciones e impuestos (SISCRI) | FINTEXA | [adquirencia_overview.md](overview_adquirencia.md) |
| **Agente de Cobros y Pagos** | Capa multi-collector sobre API BANK (ex-CVUCollect) | FINTEXA | [cobros_overview.md](overview_agente_cobros_y_pagos.md) |
| **Onboarding** | Alta automática de comercios/cuentas con validación KYC/AML en 3 fases | FINTEXA | [onboarding_overview.md](overview_onboarding.md) |
| **Ardid** (rebrandeado "Akurtech" desde v1.18, mayo 2026) | Monitoreo transaccional / antifraude | Pentass | [ardid_overview.md](overview_ardid.md) — manual técnico completo en [`3_recursos/detalle_productos/ardid/`](../../3_recursos/detalle_productos/ardid/index.md) |

## Documentación técnica relacionada

- **Endpoints por producto**: `wiki/3_recursos/detalle_productos/<producto>/apis_expuestas/` (texto literal del portal público, mantenido por `/sync_web`) y el resto de `wiki/3_recursos/detalle_productos/<producto>/` (mecánica interna, manuales de configuración/integración, mantenido por `/ingest` y `/sync_notion_docs`). Estos overviews son de negocio/funcionales — los detalles técnicos viven en ese módulo.
- **Conciliador**: producto mencionado en [equipo.md](../overview_empresa/overview_equipo.md) (área Administración y recaudaciones) sin overview propio todavía — ver gap registrado en [../gaps_y_preguntas.md](../gaps_y_preguntas.md).

---
*Última actualización: 2026-07-20 — Corregido el puntero muerto de Ardid (`ardid_manual_tecnico/` → `detalle_productos/ardid/`, la carpeta se había movido sin actualizar este índice) y refrescada la sección de documentación técnica relacionada, ya poblada desde la Fase 1. Movido de `2_areas/productos/` a `0_direccion/producto/` en la reforma estructural (ver `../decisiones.md`).*
*Última actualización anterior: 2026-07-02 — Creación del módulo, ingesta Fase 1 (5 productos).*
