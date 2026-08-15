# EVENT — Webhook: Devolución Botón Simple 1.0

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/webhook-addevbs10
> Producto: Adquirencia > Botón Simple

## Descripción

"Se envía una notificación a través de un HTTP POST cada vez que se registra un contracargo asociado a una transacción."

"Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente."

"Puede ser que el importe de la transacción no haya sido completamente devuelto, entonces el estado su estado seguirá siendo ACREDITADO."

## ⚠️ Notas y Advertencias del Portal

> Confirmación obligatoria: Responder con HTTP 200 es imprescindible; caso contrario activa reintentos automáticos.

> Devoluciones parciales: Transacciones devueltas parcialmente mantienen estado "ACREDITADO" (no "DEVUELTA").

> Desconocimientos: Se informan como contracargos tipo "desconocimiento".

## Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `When` | datetime | Fecha/hora de envío en UTC+0 |
| `Payload.TipoEvento` | string | Valor fijo: "CONTRACARGO" |
| `Payload.TipoOrigen` | string | Valor fijo: "ENTIDAD" |
| `Payload.IdentificadorOrigen` | string | Código unívoco de la Entidad |
| `Payload.DestinoPrincipal` | string | URL destino principal |
| `Payload.IdMensaje` | string | Id guid de la notificación |
| `MensajePago.IdentificadorTransaccion` | string | Id transacción original |
| `MensajePago.IdentificadorOrdenVenta` | string | PaymentId (link de pago) para Botón Simple |
| `MensajePago.TipoTransaccion` | string | Canal: BotonSimple |
| `MensajePago.FechaNegocio` | datetime | Fecha/hora pago cliente (UTC-3) |
| `MensajePago.FormaPago` | string | Medio utilizado (TTDD, TTCC, Transfer, Transf30) |
| `MensajePago.ImporteBruto` | decimal | Importe total pagado |
| `MensajePago.EstadoTransaccion` | string | Estado: "DEVUELTA" |
| `MensajePago.CuentaVendedor` | string | CVU del comercio |
| `MensajePago.IdentificadorPagador` | string | CUIT del cliente |
| `MensajePago.CuentaPagador` | string | CBU/CVU del pagador |
| `InformacionAdicionalMensaje[]` | array | Tuplas clave-valor adicionales |
| `Type` | string | Tipo evento: "CONTRACARGO" |

## Payload de Ejemplo

```json
{
  "When": "2026-06-16T14:23:40.1630666Z",
  "Payload": {
    "TipoEvento": "CONTRACARGO",
    "TipoOrigen": "ENTIDAD",
    "IdentificadorOrigen": "BS20",
    "TipoDestino": "ENTIDAD",
    "IdentificadorDestino": "BS20",
    "DestinoPrincipal": "https://123456.com/webhook",
    "DestinoSecundario": "https://123456e.com/webhook",
    "FechaEmision": "2026-06-16T14:23:39.7751462+00:00",
    "IdMensaje": "1457ab39-170b-409d-9a6b-c19d1b332d0c",
    "MensajePago": {
      "IdentificadorProcesador": "67REZ8NP1MKY3M124KVGOP",
      "IdentificadorTransaccion": "1398916",
      "IdentificadorOrdenVenta": "0000532600009999034401",
      "IdentificadorReferencia": "NCQA-BS2.0-5932",
      "IdOrdenVentaQr": "999903440",
      "TipoTransaccion": "Boton20",
      "RubroMovimiento": "TransferenciaEntranteCvu",
      "FechaNegocio": "2026-06-16T11:23:37.5581857-03:00",
      "FechaProceso": "2026-06-16T11:18:58.6846225+00:00",
      "FormaPago": "TransferCvu",
      "Moneda": "ARS",
      "ImporteBruto": 5912,
      "EstadoTransaccion": "DEVUELTA",
      "Retenciones": [],
      "Cpa": "C1006ACT",
      "CuentaVendedor": "322-20-1-735135-8-5",
      "IdentificadorVendedor": "CVU:00005319083200672123456WAL:|CBU:3220001805007352123458",
      "IdentificadorPagador": "20415865091",
      "CuentaPagador": "0000532609240002744097",
      "CodigoComercio": "C22903",
      "CodigoSucursal": "S18803",
      "CodigoCaja": "B00000623451",
      "Entidad": "BS20",
      "Psp": "531",
      "Procesador": "67REZ8NP1MKY3M124KVGOP",
      "InformacionAdicionalMensaje": [
        {"Descripcion": "motivoContracargo", "Valor": "NCQA-BS2.0"},
        {"Descripcion": "importe", "Valor": "5912.00"},
        {"Descripcion": "contracargoParcial", "Valor": "False"},
        {"Descripcion": "idContracargo", "Valor": "7835"},
        {"Descripcion": "fechaContracargo", "Valor": "06/16/2026 11:23:37"},
        {"Descripcion": "estadoContracargo", "Valor": "ACEPTADO"},
        {"Descripcion": "importeContracargo", "Valor": "5912.00"},
        {"Descripcion": "tipoContracargo", "Valor": "contracargo"},
        {"Descripcion": "idDebin", "Valor": "7L8GYKNXR4EYKZXNMPRZ50"},
        {"Descripcion": "debinIdApiBank", "Valor": ""}
      ]
    }
  },
  "Type": "CONTRACARGO"
}
```

### Respuesta esperada al Webhook

| Código | Descripción |
|--------|-------------|
| `200` | Evento recibido correctamente |
