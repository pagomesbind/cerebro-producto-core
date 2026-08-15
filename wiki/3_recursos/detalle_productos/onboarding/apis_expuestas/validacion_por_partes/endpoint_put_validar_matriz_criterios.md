# PUT — Validar Matriz de Criterios

> Fuente: https://psp.bind.com.ar/developers/apis/validar-matriz-ob
> Producto: Onboarding — Validación por partes

## Descripción

Evalúa el estado de la solicitud respecto de los resultados de las consultas a servicios externos y otras reglas de matriz de riesgo de Bind PSP para la entidad.

- Si concluyó en que la solicitud es válida, el `estado` resultante será `1`. En este caso, puede continuarse con los demás pasos.
- Si concluyó que la solicitud no es válida, el `estado` resultante será `3`. La solicitud fue rechazada.

**Solo puede continuarse con los demás pasos si el estado resultado de este paso es `1`.**

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PUT` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}/matriz-riesgo` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding creada. |

## Bloque curl request

```bash
curl --location --request PUT 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/4fb30e39-9aeb-4d71-4f27-08dd72123456/matriz-riesgo' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
  "id": "5c2c9f02-29e2-447d-213a-08de2092de6e"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `estado` | int | Estado del onboarding: `1`=Pendiente, `2`=Aprobada, `3`=Rechazada, `4`=Validación Manual, `5`=Pendiente credenciales, `6`=Error alta, `7`=Aprobado a Revisar, `8`=Aprobado sin notificar, `9`=Vencida, `10`=Menor pendiente, `11`=Menor habilitado |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |
