# Endpoint — Consultar cuenta por ID

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-cuenta-por-id
> Producto: Wallet — Cuentas

## Descripción

Obtiene los datos de una cuenta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Cuenta/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador de la cuenta (path param). |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Cuenta/274931' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador de la cuenta. |
| `codigo` | string | Identificador externo de la entidad. |
| `cuitCuil` | string | CUIT/CUIL del titular. |
| `nombre` | string | Nombres del titular. |
| `apellido` | string | Apellidos del titular. |
| `razonSocial` | string | Razón Social del titular. |
| `email` | string | Correo electrónico del titular. |
| `celular` | string | Teléfono celular del titular. |
| `actividadAfip` | string | Código de actividad ARCA. |
| `idOrganizacion` | int | Id de la entidad a la que pertenece la cuenta. |
| `habilitado` | boolean | Si la cuenta está habilitada o no. |
| `cvu` | string | CVU asociado a la cuenta. |
| `alias` | string | Alias asignado al CVU. |
| `nombreCvu` | string | Nombre con que se creó el CVU. |
| `domicilio.calle` | string | Calle del domicilio. |
| `domicilio.numero` | string | Número del domicilio. |
| `domicilio.piso` | string | Piso del domicilio. |
| `domicilio.departamento` | string | Departamento del domicilio. |
| `domicilio.localidadCodigo` | string | Código de localidad. |
| `domicilio.provinciaCodigo` | string | Código de provincia. |
| `domicilio.cp` | string | Código postal. |
| `domicilio.cpa` | string | Código postal argentino. |
| `domicilio.localidadNombre` | string | Nombre de la localidad. |
| `domicilio.provinciaNombre` | string | Nombre de la provincia. |
| `cuentaCVUId` | int | Identificador del CVU. |
| `esPep` | boolean | Persona políticamente expuesta. |
| `esFatca` | boolean | FATCA. |
| `esUif` | boolean | Sujeto obligado UIF. |
| `organizacionCuentaBancoId` | string | Cuenta bancaria recaudadora asociada a la entidad. |
| `fechaNacimiento` | datetime | Fecha de nacimiento del titular. |
| `ocupacion` | string | Ocupación del titular. |
| `estadoCivil` | string | Estado civil del titular. |
| `dni` | string | DNI del titular. |
| `fechaAltaSiscri` | datetime | Fecha de alta en el sistema de cálculo de impuestos. |
| `fechaMonitoreada` | datetime | Fecha de alta en el sistema de monitoreo transaccional de fraude. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | No existe una cuenta con ese ID |
| `401` | Token de autenticación inválido |
