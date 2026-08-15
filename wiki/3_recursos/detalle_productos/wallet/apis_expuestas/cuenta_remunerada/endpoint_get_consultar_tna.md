# Endpoint — Consulta de TNA

> Fuente: https://psp.bind.com.ar/developers/apis/consulta-de-tna
> Producto: Wallet — Cuenta remunerada

## Descripción

Devuelve el valor en porcentaje de Tasa Nominal Anual (TNA) actual por invertir el saldo con la funcionalidad de cuenta remunerada.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-remunera/v1/api/v1.201/Tna` |

## Parámetros del Request

Sin contenido.

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-remunera/v1/api/v1.201/Tna' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `promedio` | double | Valor de TNA actual en porcentaje. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `200` | Falta alguna configuración en la entidad |
| `401` | Token de autenticación inválido |
