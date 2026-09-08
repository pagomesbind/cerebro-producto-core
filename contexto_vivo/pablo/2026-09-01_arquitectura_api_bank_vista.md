---
id: 2026-09-01_arquitectura_api_bank_vista
pm: pablo
fecha_captura: 2026-09-01
fuente: "Portal público de developers API BANK — https://sandbox.bind.com.ar/apidoc/#api-Vista"
producto: transversal
tema: API BANK (Banco Industrial) — Vista — referencia de endpoints
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/api_bank/vista.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: d783db8
---

## Contexto

Grupo de un solo endpoint, pero introduce un concepto transversal a toda la API BANK: el parámetro `:view_id` que aparece en casi todos los endpoints de Cuenta, Billetera, Transferencia y Debin (ej. `ConsultaCuentas`, `ConsultaDeMovimientos`).

## Consulta de vistas disponibles — `ConsultaVistasDisponibles`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Vista-ConsultaVistasDisponibles

Retorna el listado de vistas disponibles. Los propósitos funcionales de cada vista, según el portal:

- **`owner`**: el cliente opera sobre sus propias cuentas.
- **`delegate`**: el cliente PSI/STI opera en nombre de un tercero utilizando un token delegado.

### Consideraciones para operaciones delegadas (vista `delegate`)

Cuando se consumen servicios utilizando la vista `delegate`, es **obligatorio** enviar el header `Delegate-authentication` con el token recibido al finalizar el flujo de onboarding o de la renovación del token (ver grupo `Alta_De_Cuenta`, endpoint `PSIRenovarToken`).

Posibles errores propios de esta modalidad:
- `PA002` (Vista inválida) — se retorna si el header `Delegate-authentication` no es enviado.
- `401 Unauthorized` — se retorna si el token delegado enviado es incorrecto o expiró.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/views` |

### Headers

| Header | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| `Authorization` | String | Sí | Formato `"JWT :token"`. |

### Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| (raíz) | String[] | Listado de identificadores de vista. |

### Ejemplo de response

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
