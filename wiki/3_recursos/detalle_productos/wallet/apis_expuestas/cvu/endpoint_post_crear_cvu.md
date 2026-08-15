# Endpoint — Crear CVU

> Fuente: https://psp.bind.com.ar/developers/apis/crear-cvu
> Producto: Wallet — CVU

## Descripción

Crea un CVU asignado a una cuenta existente.

Sólo se puede asignar un alias cada 24hs.

En caso de elegir no generar alias automático, se tienen solo 5 segundos para poder asignar un alias a un CVU recién creado, sino Coelsa por normativa asigna uno aleatorio al mismo. En caso de elegir crear el alias automáticamente, por defecto, al crear un CVU se le asigna un alias conformado concatenando un código interno y el CUIT del titular de la cuenta. En ambos casos, el alias no podrá modificarse por 24 hs.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CVU` |
| Content-Type | `application/json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta para la cual se le quiere crear el CVU. |
| `nombreCVU` | string | OPTIONAL | Nombre con el que se creará el CVU en Coelsa. Es recomendable volver a enviar los nombres y apellidos concatenados en este atributo para evitar errores en la creación del CVU. Guardar cuidado de enviar un dato normalizado sin caracteres especiales y de una longitud máxima de 40 caracteres. |
| `aliasAutomatico` | boolean | OPTIONAL | Indica si luego de crear el CVU se le asignará automáticamente un alias o no. Valor por defecto: `true` |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CVU' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
"idCuenta": 274926,
"nombreCVU": "Juan Alberto Perez"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador del CVU creado. Es diferente al CVU de la cuenta. Se utiliza luego para realizar acciones sobre el CVU, como por ejemplo: Eliminar CVU. |
| `cvu` | string | CVU creado. |
| `alias` | string | Alias creado por defecto para este CVU. Puede modificarse. |
| `idCuenta` | int | Identificador de la cuenta. |
| `nombreCvu` | string | Nombre con que se creó el CVU. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación exitosa |
| `422` | Hubo un time out con el banco al solicitarle la creación del CVU |
| `422` | Error intermitente del banco al crear el CVU |
| `400` | Algún dato de la solicitud tiene un formato inválido |
| `401` | Token de autenticación inválido |
