# PUT — Modificar Sucursal (Comercios y Transacciones)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/comercio-modificarsucursal
> Producto: Adquirencia > Comercios y Transacciones

> ⚠️ **NOTA DE MAPEO**: Este archivo estaba nombrado como "consultar_comercio" pero el endpoint real del portal en esta posición es "Modificar Sucursal". Actualizado con el endpoint real.

## Descripción

"Modifica los atributos de una sucursal existente."

Nota: el sistema advierte que esta integración podría omitirse si se utilizan "valores fijos a crear una única vez manualmente."

## Request

**Método HTTP:** `PUT`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/{id}/sucursales/{idSucursal}`

### curl request

```bash
curl -v -X PUT "https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/C07663/sucursales/S02932" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer {{access_token}}" \
--data-raw "{...}"
```

### Headers

| Header | Valor |
|--------|-------|
| `Content-Type` | `application/json` |
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string | SÍ | Código del comercio |
| `idSucursal` | string | SÍ | Código de la sucursal a modificar |

### Body

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `calle` | string | SÍ | Domicilio completo |
| `piso` | string | NO | Piso |
| `departamento` | string | NO | Departamento |
| `nombre` | string | SÍ | Denominación de sucursal |
| `codigoProvincia` | int | SÍ | Id de provincia |
| `codigoLocalidad` | int | SÍ | Id de localidad |
| `email` | string | SÍ | Correo electrónico |
| `telefono` | string | SÍ | Número telefónico |
| `telefonoSecundario` | string | NO | Teléfono alternativo |
| `codigoPostal` | string | SÍ | Código postal argentino |

### Request JSON

```json
{
  "calle": "Calle modificada 123",
  "piso": "",
  "departamento": "",
  "nombre": "Sucursal modificada",
  "codigoProvincia": 1,
  "codigoLocalidad": 247,
  "email": "email@modificado.com",
  "telefono": "1233333333",
  "telefonoSecundario": "",
  "codigoPostal": "1414"
}
```

## Response

Respuesta vacía (sin contenido en body).

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Modificación exitosa |
| `400` | Falta algún campo requerido |
| `422` | Provincia inválida / Comercio o sucursal inválidos |
| `401` | Token de autenticación inválido |
