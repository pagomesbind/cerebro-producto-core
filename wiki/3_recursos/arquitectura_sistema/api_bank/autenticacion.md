# API BANK — Autenticación

> Grupo de un solo endpoint, pero es el punto de entrada obligatorio a toda la API BANK: todos los demás endpoints (Cuenta, Billetera, Transferencia, Debin, etc.) requieren el token JWT que devuelve este login en el header `Authorization`.

## Login — `Login`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Autenticacion-Login

Luego de establecer el enlace vía HTTPS utilizando el certificado provisto, existe un segundo nivel de seguridad: es necesario enviar en cada request un header con el token obtenido de este servicio, con el formato `Authorization: JWT XXXXXX`.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/login/jwt` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `body.username` | String | Sí | Nombre de usuario. |
| `body.password` | String | Sí | Contraseña. |

### Ejemplo de body

```json
{
  "username": "user",
  "password": "XXXXX"
}
```

### Response — atributos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `process` (header) | String | Identificador del proceso. |
| `token` | String | JWT token de autenticación, a usar en el header `Authorization: JWT :token` del resto de los endpoints. |
| `expires_in` | Number | Tiempo de validez del token, en segundos. |

### Ejemplo de response — "Login exitoso"

```json
{
  "token": "EWRWERWERWERWERERWREWRWERWRWE",
  "expires_in": 3600
}
```

### Códigos de error

| Código | Descripción |
|--------|-------------|
| `GE401` | Token inválido o el usuario no existe. |

## Nota adicional — flujo de "vista delegada"

El grupo [Vista](vista.md) (`ConsultaVistasDisponibles`) documenta un segundo mecanismo de autenticación para operatoria delegada (clientes PSI/STI operando en nombre de un tercero), vía el header adicional `Delegate-authentication` con el token recibido al finalizar el onboarding — complementario a este login estándar, no un reemplazo.

## Nota de relevamiento

Grupo completo (1/1 endpoint relevado) desde `https://sandbox.bind.com.ar/apidoc/api_data.json`.

> Capturado por Pablo Gomes, 2026-09-01.
