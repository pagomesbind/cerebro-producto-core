# GET — Generar Código QR Estático

> Sincronizado el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/qr-generarcodigoqr
> Producto: Adquirencia > QR Estático

## Descripción

Devuelve el string del código QR de la caja indicada.

Devuelve un string conformado de forma standard según el EMVCo y aceptado por el ecosistema de Transferencia 3.0.

El string deberá ser convertido en imagen por el aplicativo de la Entidad de manera de poder ser publicado o impreso.

## Request

**Método HTTP:** `GET`
**Path:** `/bindentidad-qr-v2/v2/api/v1.201/generacion-qr-estatico`
**Base URL Staging:** `https://gw-staging-qrbind.epays.services`
**URL Completa Staging:** `https://gw-staging-qrbind.epays.services/bindentidad-qr-v2/v2/api/v1.201/generacion-qr-estatico`

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |
| `Cache-Control` | `no-cache` |

### Parámetros de Query

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `CodigoCaja` | string | OPCIONAL | Es el código de la caja de la que se quiere generar el código QR. |
| `CodigoCajaExterno` | string | OPCIONAL | Es el código externo de la caja de la que se quiere generar el código QR. |

## curl request

```bash
curl -v -X GET "https://gw-staging-qrbind.epays.services/bindentidad-qr-v2/v2/api/v1.201/generacion-qr-estatico?CodigoCaja=B00000455196" -H "Cache-Control: no-cache" -H "Authorization: Bearer {{access_token}}"
```

## Response

### Campos de respuesta exitosa (200)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `codigoComercio` | string | Código del comercio. |
| `nombreComercio` | string | Nombre del comercio. |
| `cuit` | string | CUIT del comercio. |
| `qrCode` | string | Código para generar la imagen del QR. |
| `entidad` | string | Código de la entidad. |
| `codigoSucursal` | string | Código de la sucursal. |

### Errores

| Descripción |
|-------------|
| Token de autenticación inválido |

## ⚠️ Notas y Advertencias del Portal

> Si se modifica algún atributo del comercio, de la sucursal o de la caja, deberá volverse a regenerar el QR estático de la caja con este mismo método debido a que la composición del mismo pudo haber cambiado.
