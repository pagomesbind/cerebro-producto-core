# Índice Maestro — Detalle de Productos

> Este módulo aloja todo el conocimiento detallado de producto, incluyendo su API pública oficial (en `<producto>/apis_expuestas/`, intocable salvo por `/sync_web`) y todo lo que no es API: mecánica interna, manuales de configuración/integración, aprendizajes de reuniones, documentación de procesadores externos, hacks operativos, y cualquier conocimiento — técnico o no — relevante a cualquier área de Bind PSP (Producto, Soporte, Comercial, Integraciones, Administración). Lo que es arquitectura de infraestructura no ligada a un producto vive aparte, en [arquitectura_sistema/](../arquitectura_sistema/index.md).

> Los overviews de negocio vivos de cada producto (contexto actual, noticias, novedades) están en [2_areas/overview_productos/](../../2_areas/overview_productos/index.md) y los mantiene el usuario directamente — este módulo los complementa con el detalle técnico/operativo, no los reemplaza.

## Cómo está organizado

Primero por **producto**, luego por **archivo temático de funcionalidad** dentro de cada producto (sin esquema fijo de nombres — cada carpeta agrupa por tema, no 1 archivo fuente = 1 archivo destino). Alimentado por `/ingest` y `/sync_notion_docs`.

## Productos

| Producto | Módulo | Overview de negocio |
|---|---|---|
| **Adquirencia** (Solución de Cobros) | [adquirencia/index.md](adquirencia/index.md) | [overview_adquirencia.md](../../2_areas/overview_productos/overview_adquirencia.md) |
| **Wallet** | [wallet/index.md](wallet/index.md) | [overview_wallet.md](../../2_areas/overview_productos/overview_wallet.md) |
| **Onboarding** | [onboarding/index.md](onboarding/index.md) | [overview_onboarding.md](../../2_areas/overview_productos/overview_onboarding.md) |
| **Agente de Cobros y Pagos** | [agente_cobros_y_pagos/index.md](agente_cobros_y_pagos/index.md) | [overview_agente_cobros_y_pagos.md](../../2_areas/overview_productos/overview_agente_cobros_y_pagos.md) |
| **Ardid/Akurtech** | [ardid/index.md](ardid/index.md) | [overview_ardid.md](../../2_areas/overview_productos/overview_ardid.md) |
| **Siscri** (accesorio — motor de impuestos compartido por Adquirencia y Wallet) | [siscri/index.md](siscri/index.md) | — (sin overview propio, mencionado en adquirencia/wallet) |
| **Servicios** (Pago Fácil) | [servicios/index.md](servicios/index.md) | — (sin overview propio — gap abierto) |
| **Portal Admin** | [portal_admin/index.md](portal_admin/index.md) | — (sin overview propio) |
| **Portal Comercio** | [portal_comercio/index.md](portal_comercio/index.md) | — (sin overview propio) |
| **APK Wallet** | [apk_wallet/index.md](apk_wallet/index.md) | — (sin overview propio) |
| **Ecosistema Wallet con Adquirencia** (plataformas multi-comercio white-label) | [ecosistema_wallet_adquirencia/index.md](ecosistema_wallet_adquirencia/index.md) | — |
| **Conciliador** (accesorio) | Sin contenido todavía — ver gap en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md) | — |

---
*Última actualización: 2026-08-12 — Reestructuración PARA en cascada: `transversal/` eliminado (desarmado por producto/tema, sin cajones multi-producto); `cobros/` renombrado a `agente_cobros_y_pagos/`; nuevos módulos `portal_admin/`, `portal_comercio/` y `ecosistema_wallet_adquirencia/`; overviews de negocio movidos de `0_direccion/producto/` a `2_areas/overview_productos/`.*
*Última actualización anterior: 2026-07-03 — Creación del módulo. Reemplaza `ardid_manual_tecnico/`, `mecanica_interna_productos/` y `conocimiento_interno/` (retiradas), consolidando su contenido reorganizado por producto y funcionalidad.*
