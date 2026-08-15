# Endpoint — Aviso de fin de proceso (EVENT)

> Fuente: https://psp.bind.com.ar/developers/apis/webhook-procesofci
> Producto: Wallet — Cuenta remunerada

## Descripción

Se envía una notificación a través de un HTTP POST cada vez que se finaliza un proceso diario de cuenta remunerada con FCI.

Cada webhook debe responderse simplemente con un HTTP code 200, así se considerará que la Entidad recibió la notificación satisfactoriamente. De otra manera, el envío del webhook ingresará en un esquema de reintentos.

El webhook se enviará a la URL del destino que se haya configurado previamente en la Entidad.

Para recibir este evento la organización debe tener parametrizada la URL destino para el tipo de evento `"RESUMEN_OPERACIONES_FCI"`.

No debe validarse la estructura exacta del mensaje. Bind PSP puede agregar arbitrariamente nuevos atributos opcionales al request por nuevas funcionalidades o mejoras.

## Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `mensajeId` | string | Identificador único del webhook. |
| `evento` | string | Tipo de evento. Valor fijo: `"RESUMEN_OPERACIONES_FCI"` |
| `procesoId` | int | Identificador del proceso. |
| `procesoFecha` | datetime | Fecha del proceso. |
| `procesoEstado` | string | Estado. Valor fijo: `"FINALIZADO_OK"` |
| `codigoFondo` | string | Código del fondo común de inversión. |
| `valorCuotaParte` | double | Valor de una cuotaparte del FCI en la fecha del proceso. |
| `procesoFechaHoraAlta` | datetime | Fecha y hora en que inició el proceso. |
| `procesoFechaHoraUltimaModificacion` | datetime | Fecha y hora de última actualización. |
| `totalSuscripciones` | int | Cantidad de suscripciones realizadas. |
| `sumatoriaSuscripciones` | double | Importe total por suscripciones. |
| `totalRescates` | int | Cantidad de rescates realizados. |
| `sumatoriaRescates` | double | Importe total por rescates. |
| `cantidadCPOperadasSuscripciones` | double | Cantidad de cuotapartes suscriptas. |
| `cantidadCPOperadasRescates` | double | Cantidad de cuotapartes rescatadas. |

## Ejemplo JSON

```json
{
  "mensajeId": "88e8b10f-e473-4e65-9bea-b715659dc153",
  "evento": "RESUMEN_OPERACIONES_FCI",
  "procesoId": 243,
  "procesoFecha": "2026-05-28",
  "procesoEstado": "FINALIZADO_OK",
  "codigoFondo": "IAMAHPE AR",
  "valorCuotaParte": 14089.671373000000000,
  "procesoFechaHoraAlta": "2026-05-28T18:52:31.9017029+00:00",
  "procesoFechaHoraUltimaModificacion": "2026-05-28T19:01:03.3234378+00:00",
  "totalSuscripciones": 562,
  "sumatoriaSuscripciones": 3272311353.02,
  "totalRescates": 43,
  "sumatoriaRescates": 4122123321123.48,
  "cantidadCPOperadasSuscripciones": 232249,
  "cantidadCPOperadasRescates": 293
}
```
