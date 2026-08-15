# Endpoint — Crear comprobante

> Fuente: https://psp.bind.com.ar/developers/apis/crear-nuevo-comprobante
> Producto: Wallet — Saldo en pesos

## Descripción

Crea un nuevo comprobante de ajuste de saldo en una cuenta.

La entidad debe crear sus propios tipos de comprobante. No tiene permitido utilizar los tipos de comprobante reservados para operaciones internas del sistema (IdTipoComprobante: 1, 2, 3, 4, 5 y 6) ya que puede resultar en dificultades para el proceso de conciliación.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/Comprobante` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idTipoComprobante` | string | REQUIRED | Tipo de comprobante. No usar IDs reservados: 1, 2, 3, 4, 5, 6. |
| `idCuenta` | string | REQUIRED | Cuenta sobre la cual se realiza el ajuste de saldo. |
| `importe` | double | REQUIRED | Importe del ajuste. |
| `referencia` | string | OPTIONAL | Referencia externa. Máx 50 caracteres. |
| `idComprobanteRelacionado` | string | OPTIONAL | Identificador de comprobante relacionado. |
| `idExterno` | string | OPTIONAL | Identificador externo de la entidad. Máx 50 caracteres. |
| `fechaExterna` | string | OPTIONAL | Fecha externa informativa. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/Comprobante' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "idTipoComprobante": 357,
  "idCuenta": 274931,
  "importe": 100,
  "referencia": "Recarga",
  "idComprobanteRelacionado": null,
  "idExterno": "123",
  "fechaExterna": "2024-09-03"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador del comprobante creado. |
| `saldo` | double | Saldo actual de la cuenta luego de crear el comprobante. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación exitosa |
| `422` | Tipo de comprobante inválido |
| `422` | Cuenta inválida |
| `422` | idExterno inválido |
| `401` | Token de autenticación inválido |
