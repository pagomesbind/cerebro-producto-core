# POST — Crear Sucursal (Comercios y Transacciones)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/comercio-crearsucursal
> Producto: Adquirencia > Comercios y Transacciones

> ⚠️ **NOTA DE MAPEO**: Este archivo estaba nombrado como "crear_comercio" pero el endpoint real del portal es "Crear Sucursal". Los comercios se configuran manualmente, no vía API. El archivo fue actualizado con el endpoint real equivalente.

## Descripción

"Da de alta una nueva sucursal en el comercio indicado." La sucursal representa "una subdivisión física de un comercio" donde pueden alojarse múltiples cajas registradoras.

## Request

**Método HTTP:** `POST`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/{id}/sucursales`

### curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/C07663/sucursales" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer {{access_token}}" \
--data-raw '{...}'
```

### Headers

| Header | Valor |
|--------|-------|
| `Content-Type` | `application/json` |
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string | SÍ | Código del comercio padre |

### Body

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `calle` | string | SÍ | Domicilio completo |
| `piso` | string | NO | Número de piso |
| `departamento` | string | NO | Número de departamento |
| `nombre` | string | SÍ | Denominación de sucursal |
| `codigoProvincia` | int | SÍ | ID de provincia |
| `codigoLocalidad` | int | NO | ID de localidad |
| `email` | string | SÍ | Correo electrónico |
| `telefono` | string | SÍ | Teléfono principal |
| `telefonoSecundario` | string | NO | Teléfono alterno |
| `codigoPostal` | string | SÍ | Código postal argentino |
| `caja[]` | object | SÍ | Datos de caja predeterminada |
| `caja[].nombre` | string | NO | Nombre de caja |
| `caja[].soloOrden` | boolean | SÍ | true/false según acepte órdenes |
| `caja[].tipoCajaId` | int | SÍ | 1 (presencial) o 2 (no presencial) |

### Request JSON

```json
{
  "calle": "Siempreviva 742",
  "nombre": "Sucursal de prueba",
  "codigoProvincia": 1,
  "codigoLocalidad": 247,
  "email": "sucursal@deprueba.com",
  "telefono": "116666666",
  "codigoPostal": "1414",
  "caja": [{
    "nombre": "Caja por defecto en sucursal de prueba",
    "soloOrden": true,
    "tipoCajaId": 2
  }]
}
```

## Response

### Respuesta exitosa (200)

```json
{
  "id": "[código_sucursal_generado]"
}
```

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación exitosa |
| `400` | Falta campo requerido |
| `422` | Provincia incorrecta o comercio inválido |
| `401` | Token autenticación inválido |
