# Endpoint — Conciliar transferencia entrante

> Fuente: https://psp.bind.com.ar/developers/apis/conciliar-transferencia-entrante
> Producto: Wallet — Transferencias

## Descripción

Intenta conciliar una transferencia entrante consultando por el id Coelsa. El caso de uso en el que aplica es cuando un usuario reclama que hizo una transferencia al CVU de la organización pero no ve el movimiento impactado.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/ConciliarTransferencia` |
| Content-Type | `application/json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `coelsaId` | string | REQUIRED | Identificador de Coelsa de la transferencia. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/ConciliarTransferencia' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
"CoelsaId": "80V1JXON1874QG39Z64EL7"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `idOperacion` | int | Identificador de la operación consultada. |
| `conciliada` | boolean | Indica si la operación consultada fue conciliada o no. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa. No fue necesario conciliar porque la operación ya existía en nuestro sistema |
| `200` | Consulta exitosa. La operación no existía en nuestro sistema y fue conciliada |
| `200` | Consulta exitosa. La operación consultada no existe. No se concilió |
| `422` | Hubo un error de time out en un servicio externo |
| `401` | Token de autenticación inválido |
