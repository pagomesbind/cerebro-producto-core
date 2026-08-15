# POST — Crear Tipo de Comprobante

> Fuente: https://psp.bind.com.ar/developers/apis/crear-nuevo-tipo-de-comprobante
> Producto: Wallet — Saldo en pesos

## Descripción

Crea un nuevo tipo de comprobante para la entidad.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/TipoComprobante` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `nombre` | string | REQUIRED | Nombre del tipo de comprobante. |
| `codigo` | string | REQUIRED | Código externo de la entidad. |
| `descripcion` | string | OPTIONAL | Descripción adicional. |
| `signo` | int | REQUIRED | `1` = Crédito, `-1` = Débito |
| `tipoMovimiento` | string | REQUIRED | Tipo de movimiento: `"001"` = Cobros y pagos, `"002"` = Retiros en efectivo, `"003"` = Depósitos en efectivo, `"004"` = Transferencias entre cuentas |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/TipoComprobante' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "nombre": "Carga de saldo en efectivo",
  "codigo": "XXX001",
  "descripcion": "Carga de saldo en efectivo",
  "signo": 1,
  "tipoMovimiento": "001"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador del tipo de comprobante creado. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación exitosa |
| `422` | El nombre ya existe |
| `422` | El código ya existe |
| `400` | Signo inválido |
| `400` | Faltan campos requeridos |
| `401` | Token de autenticación inválido |
