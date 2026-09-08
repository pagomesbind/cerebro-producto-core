# API BANK — Banco Industrial

> Referencia técnica de la API pública de **Banco Industrial** (documentada en `https://sandbox.bind.com.ar/apidoc/`, formato apidoc.js) que Bind PSP consume internamente para operar cuentas y CVU — es la base técnica que sustenta tanto **Wallet** como **Agente de Cobros y Pagos** (ambos usan Banco Industrial como banco sponsor/custodio de las cuentas CBU/CVU). Relevada por Pablo Gomes el 2026-09-01 desde el JSON fuente del portal (`api_data.json`), 87 endpoints tabulados en 10 grupos funcionales. No confundir con la API pública **propia de Bind** documentada en `detalle_productos/<producto>/apis_expuestas/` (dominio de `/sync_web`) — este módulo es la API del proveedor bancario que Bind consume, no la que Bind expone.
>
> **Grupos fuera de esta ronda de relevamiento:** `Referencias` (31 endpoints tipo catálogo — códigos de concepto, moneda, estado de transacción, etc., referenciados desde varios de los archivos de abajo como "pendiente de relevar"), `Cheques` y `Persona`. Los prefijos de error `CH` (Cheques) e `IN` (Inversiones/fondos) en [errores.md](errores.md) sugieren funcionalidad adicional no tabulada en los 87 endpoints del índice del portal.

## Documentos de este módulo

| Archivo | Contenido |
|---|---|
| [autenticacion.md](autenticacion.md) | Login JWT — punto de entrada obligatorio a toda la API. |
| [cuenta.md](cuenta.md) | Consulta de cuentas por CBU/CVU/alias, alias CBU, listado de cuentas y movimientos. |
| [billetera.md](billetera.md) | Alta/baja/modificación de CVU, alias de CVU, transferencias desde CVU — el grupo más relevante para Wallet y Agente de Cobros y Pagos. |
| [transferencia.md](transferencia.md) | Transferencias salientes desde cuenta "normal" (no CVU) — por beneficiario, CBU, CVU o alias. |
| [transferencia_mep.md](transferencia_mep.md) | Transferencias MEP (Mercado Electrónico de Pagos) — suscripción/rescate de FCI, cancelación de saldos deudores, transferencias entre cuentas. |
| [debin.md](debin.md) | Débito Inmediato (DEBIN) — alta/baja de cuenta vendedora, crear/consultar/eliminar pedidos, recurrencia (suscripciones). |
| [vista.md](vista.md) | El parámetro `:view_id` transversal (`owner` vs. `delegate`) usado en casi todos los demás grupos. |
| [webhooks.md](webhooks.md) | Administración de suscripciones de webhook del cliente (alta/modificación, listado, baja, envío de prueba). |
| [eventos.md](eventos.md) | Payloads de los eventos que el banco envía por webhook (DEBIN acreditado/rechazado/devuelto, transferencias CBU/CVU recibidas/reversadas, MEP, alta de cuenta PSI). |
| [alta_de_cuenta.md](alta_de_cuenta.md) | Onboarding de cuentas CBU/CVU vía API BANK (PSI/STI, PF/PJ) — no usado hoy por Bind, documentado como referencia. Incluye gap del catálogo de códigos PSI no accesible desde el portal público. |
| [errores.md](errores.md) | Catálogo completo de códigos de error de todas las APIs del banco — referencia cruzada transversal. |

## Ver también

- [3_recursos/detalle_productos/wallet/index.md](../../detalle_productos/wallet/index.md) — mecánica de producto de Wallet que consume esta API (alta de CVU, alias, transferencias).
- [3_recursos/detalle_productos/agente_cobros_y_pagos/index.md](../../detalle_productos/agente_cobros_y_pagos/index.md) — el otro producto que opera CVU contra Banco Industrial.
- [../modelo_acoplado_vs_desacoplado.md](../modelo_acoplado_vs_desacoplado.md) — relación arquitectónica con Banco Industrial a nivel de plataforma.

---
*Última actualización: 2026-09-07 — `/context_merge`: creación del módulo completo (11 archivos) desde relevamiento del portal público de developers de API BANK, contexto_vivo de Pablo Gomes (2026-09-01).*
