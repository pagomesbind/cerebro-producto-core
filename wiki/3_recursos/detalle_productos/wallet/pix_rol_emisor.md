# PIX Rol Emisor — pagos en ARS leyendo QR PIX (BRL) — Wallet

> Estado: en producción.

> Fuente: Notion histórico, Epic **"PIX Rol Emisor"** (~100 SP estimados, Negocio). Complementa el rol de **cobro** PIX ya documentado en otras partes de la wiki: acá Wallet actúa como **emisor** — el usuario paga en pesos leyendo un QR brasileño.

## 1. Qué resuelve

Permitir que organizaciones/wallets de Bind PSP paguen en **ARS** a partir de leer e interpretar un **QR PIX en BRL** — vía integración con **PagBrasil** (proveedor de servicios PIX). El comercio brasileño recibe BRL; el usuario final argentino paga con su saldo en ARS. Resuelve dos dolores a la vez: el cálculo de tipo de cambio y la operación de envío de fondos al exterior para pagarle al proveedor brasileño — ambos quedan opacos para el usuario final.

**Cliente principal**: Astropay (+ leads de BINDX).

## 2. Mecánica del flujo

1. **Consultar cotización** ARS/BRL.
2. **Leer e interpretar el QR PIX**: puede ser (a) **QR estático** (importe embebido = 0) → el usuario ingresa el importe en BRL manualmente; (b) **QR dinámico** (importe embebido ≠ 0) → el sistema toma el valor directamente del código; (c) sin escanear QR, usando una **clave Pix** (`pix_key` + `pix_key_type` + `amount_brl`). Pix usa el estándar EMV-QRCPS, solo en modalidad "presentado por el comerciante".
3. **Iniciar y confirmar el pago** contra la API de PagBrasil.
4. **Compensación cambiaria interna — pieza clave**: por cada pago PIX concretado, Bind PSP debe **ejecutar una compra de dólar CCL** (ver [dolar_ccl.md](dolar_ccl.md)) para convertir los dólares que se transferirán al proveedor brasileño en los reales que hay que liquidarle al comercio. Es decir, el circuito de cambio de moneda ya construido para CCL se reutiliza como pieza de back-office de este producto, igual que en el caso DIRECTA de [crypto.md](crypto.md) — patrón recurrente: nuevos canales de pago internacional se apoyan en el motor CCL existente en vez de construir un circuito cambiario propio.

## 3. Devoluciones (SHOULD HAVE, bajo volumen esperado)

El comercio devuelve BRL pero el usuario recibe ARS — análogamente, cada devolución dispara una **venta de dólar CCL** para convertir los dólares recibidos de vuelta a pesos. Se evaluó explícitamente lanzar el MVP **sin esta funcionalidad** por el bajo volumen esperado de devoluciones en este canal.

> **Actualización (`/sync_releases`):** contrario a quedar solo como SHOULD HAVE, la recepción de devoluciones se construyó y publicó — Epic "PIX rol emisor: Recibir devolución" ([WS-46](https://bindpsp.atlassian.net/browse/WS-46), 15 SP, W 66 2025-12-15).

## 4. Alcance MVP vs. fuera de alcance

- **MVP**: solicitud/lectura de datos del QR PIX, inicio de pago, confirmación de pago.
- **Fuera de alcance inicial**: devolución de pagos PIX, e iniciar pagos con **Chave Pix** (clave Pix sin QR) — quedó como COULD HAVE.
- Time to market presionado por el propio banco (BIND), que quería tener este producto disponible para ofrecer a sus clientes.

## 5. Mantenimiento en producción (vía `/sync_releases`)

- **Cotización CCL para PIX por tabla, no por settings** ([WS-376](https://bindpsp.atlassian.net/browse/WS-376), publicado W 67 2026-01-27): la cotización CCL usada para el pago PIX tomaba Owner/Entidad de un appsetting fijo — pasó a leerse de `ParametrosOrganizaciones` (por `OrganizacionId` = x-entidad, `CanalOperacion = 'PagoPix'`, `Procesador = 'POICENOT'`), habilitando configuración por organización sin deploy.
- **Webhook publicado vía egress** ([WS-129](https://bindpsp.atlassian.net/browse/WS-129), W 67): el API Webhook de PIX Roaming se ruteó por egress en todos los ambientes (infra).

## Ver también

- [dolar_ccl.md](dolar_ccl.md) — circuito de compra/venta de dólar CCL reutilizado como compensación cambiaria de este producto.
- [crypto.md](crypto.md#2-caso-directa--expatriación-de-fondos-vía-cripto-compliance-driven) — mismo patrón de apalancarse en CCL para un canal de pago internacional nuevo.
