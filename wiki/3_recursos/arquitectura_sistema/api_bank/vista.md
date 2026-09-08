# API BANK — Vista

> Grupo de un solo endpoint, pero introduce un concepto transversal a toda la API BANK: el parámetro `:view_id` que aparece en casi todos los endpoints de [Cuenta](cuenta.md), [Billetera](billetera.md), [Transferencia](transferencia.md) y [Debin](debin.md) (ej. `ConsultaCuentas`, `ConsultaDeMovimientos`).

## Consulta de vistas disponibles — `ConsultaVistasDisponibles`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Vista-ConsultaVistasDisponibles

Retorna el listado de vistas disponibles. Los propósitos funcionales de cada vista, según el portal:

- **`owner`**: el cliente opera sobre sus propias cuentas.
- **`delegate`**: el cliente PSI/STI opera en nombre de un tercero utilizando un token delegado.

### Consideraciones para operaciones delegadas (vista `delegate`)

Cuando se consumen servicios utilizando la vista `delegate`, es **obligatorio** enviar el header `Delegate-authentication` con el token recibido al finalizar el flujo de onboarding o de la renovación del token (ver grupo [Alta_De_Cuenta](alta_de_cuenta.md), endpoint `PSIRenovarToken`).

Posibles errores propios de esta modalidad:
- `PA002` (Vista inválida) — se retorna si el header `Delegate-authentication` no es enviado.
- `401 Unauthorized` — se retorna si el token delegado enviado es incorrecto o expiró.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/views` |

### Response

```json
["owner", "delegate"]
```

### Códigos de error

| Código | Descripción |
|--------|-------------|
| `GE500` | Error general. |
| `GE403` | Error de permisos. |

## Nota de relevamiento

Grupo completo (1/1 endpoint relevado) desde `https://sandbox.bind.com.ar/apidoc/api_data.json`.

> Capturado por Pablo Gomes, 2026-09-01.
