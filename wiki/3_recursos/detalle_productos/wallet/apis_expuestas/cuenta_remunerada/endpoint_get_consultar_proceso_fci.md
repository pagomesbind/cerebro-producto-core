# Endpoint — Consultar proceso

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-proceso-fci
> Producto: Wallet — Cuenta remunerada

## Descripción

Devuelve la información de un proceso de inversión en FCI por fecha.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/sharedentidad-remunera/v1/api/v1.201/Proceso/{fechaProceso}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `fechaProceso` | string | REQUIRED | Día del proceso (path param). Formato: `YYYY-MM-DD` |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/sharedentidad-remunera/v1/api/v1.201/Proceso/2026-05-28' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `procesoId` | int | Identificador del proceso. |
| `procesoFecha` | datetime | Fecha del proceso. |
| `procesoEstado` | string | Estado del proceso. Valor fijo: `"FINALIZADO_OK"` |
| `codigoFondo` | string | Código del fondo común de inversión. |
| `valorCuotaParte` | double | Valor de una cuotaparte del FCI en la fecha del proceso. |
| `procesoFechaHoraAlta` | datetime | Fecha y hora en que inició el proceso. |
| `procesoFechaHoraUltimaModificacion` | datetime | Fecha y hora de última actualización. |
| `totalSuscripciones` | int | Cantidad de suscripciones realizadas en el proceso. |
| `sumatoriaSuscripciones` | double | Importe total por suscripciones. |
| `totalRescates` | int | Cantidad de rescates realizados en el proceso. |
| `sumatoriaRescates` | double | Importe total por rescates. |
| `cantidadCPOperadasSuscripciones` | double | Cantidad de cuotapartes suscriptas. |
| `cantidadCPOperadasRescates` | double | Cantidad de cuotapartes rescatadas. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |
