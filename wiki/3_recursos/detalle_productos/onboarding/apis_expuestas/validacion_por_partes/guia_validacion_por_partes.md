# Guía — Onboarding Validación por Partes

> Fuente: https://psp.bind.com.ar/developers/apis/guia-onboarding-en-partes
> Producto: Onboarding — Validación por partes

## Descripción

Esta solución permite validar en Bind PSP a un usuario analizándolo según los criterios indicados para el caso de uso y así aprobar el mismo para resultar en el alta de una cuenta, CVU, cuenta comitente, etc.

En este caso, se realiza la validación paso por paso en donde la entidad debe ejecutar cada validación en particular por separado hasta completar el flujo.

Esta funcionalidad está pensada para dar servicios a una Entidad que quiere construir su propio onboarding en su aplicación y necesita sólo algunos servicios de validación o quiere ir obteniendo información parcialmente durante el flujo.

La cantidad y orden de los pasos variará en función del caso de uso y de lo contratado por la Entidad.

## Configuración

Esta configuración será según el caso de uso. Los pasos totales y el orden de los mismos en el flujo asignado a la Entidad será configurado y documentado específicamente. Si no se completan todos los pasos no se aprobará la solicitud de onboarding.

La forma con que la Entidad debe integrarse (flujo, cantidad y orden de los pasos) al onboarding con esta modalidad será documentada según la necesidad del cliente debido a que, por su versatilidad, puede cambiar con cada caso de uso.

## Flujo

Flujo de onboarding en partes aprobado (ejemplo de un posible flujo):

1. Crear solicitud OB
2. Validar en Renaper (Datos y/o Rostro)
3. Validar en Nosis
4. Validar en Padrón A5 ARCA
5. Validar en listas Worldsys
6. Validar en UIF
7. Validar matriz
8. Alta de wallet
9. (Opcional) Actualizar datos adicionales / teléfono / email
10. Cerrar solicitud

## Flujo — Onboarding en partes aprobado (ejemplo de un posible flujo)

```
1. POST /solicitudes (crear solicitud)
   → Body: frente + dorso DNI + [documento/tramite/genero si PDF417 falla]
           + externalrefid (opcional)
   → Devuelve: id de solicitud

2. PATCH /solicitudes/{id}/renaper          → valida datos DNI en Renaper
3. PATCH /solicitudes/{id}/renaperRostro    → compara selfie vs Renaper
4. PATCH /solicitudes/{id}/nosis            → registra info Nosis para el CUIT
5. PATCH /solicitudes/{id}/afip/a5          → registra padrón A5 ARCA
6. PATCH /solicitudes/{id}/worldsys/search  → verifica listas PEP/terrorismo
7. PATCH /solicitudes/{id}/uif/sujeto-obligado → verifica condición UIF

[En cualquier momento, opcional:]
   PUT  /solicitudes/{id}                    → actualizar esPEP/esFatca/esOcde/estadoCivil/etc
   PATCH /solicitudes/{id}/contacto/telefono → actualizar teléfono
   PATCH /solicitudes/{id}/contacto/email    → actualizar email

8. PUT /solicitudes/{id}/matriz-riesgo
   → Evalúa todos los resultados de validaciones
   → estado=1 (válido, continuar) | estado=3 (rechazado, fin del flujo)

9. PATCH /solicitudes/{id}/alta-wallet       → crea cuentas Wallet/CVU/comitente
10. PUT  /solicitudes/{id}/alta-wallet       → cierra solicitud (confirma proceso)

11. [Si alta exitosa] EVENT webhook → aviso onboarding aprobado

12. GET /solicitudes/{id}                    → consultar estado completo + legajo
```

**Importante:**
- El orden y cantidad de pasos es configurable por entidad — Bind PSP documenta el flujo específico de cada caso de uso.
- Si la matriz de riesgo devuelve `estado=3`, la solicitud queda rechazada y no puede avanzar.
- Si el alta de wallet falla (HTTP 422), la solicitud debe completarse desde el backoffice.

## API Reference

| Método | Endpoint | Archivo |
|--------|----------|---------|
| `POST` | Crear solicitud OB | [endpoint_post_crear_solicitud.md](endpoint_post_crear_solicitud.md) |
| `PATCH` | Validar en Renaper Datos | [endpoint_patch_validar_renaper_datos.md](endpoint_patch_validar_renaper_datos.md) |
| `PATCH` | Validar en Renaper Rostro | [endpoint_patch_validar_renaper_rostro.md](endpoint_patch_validar_renaper_rostro.md) |
| `PATCH` | Validar en Nosis | [endpoint_patch_validar_nosis.md](endpoint_patch_validar_nosis.md) |
| `PATCH` | Validar en Padrón A5 ARCA | [endpoint_patch_validar_padron_a5.md](endpoint_patch_validar_padron_a5.md) |
| `PATCH` | Validar en listas Worldsys | [endpoint_patch_validar_worldsys.md](endpoint_patch_validar_worldsys.md) |
| `PATCH` | Validar en UIF | [endpoint_patch_validar_uif.md](endpoint_patch_validar_uif.md) |
| `PUT` | Actualizar datos adicionales | [endpoint_put_actualizar_datos_adicionales.md](endpoint_put_actualizar_datos_adicionales.md) |
| `PATCH` | Actualizar teléfono | [endpoint_patch_actualizar_telefono.md](endpoint_patch_actualizar_telefono.md) |
| `PATCH` | Actualizar email | [endpoint_patch_actualizar_email.md](endpoint_patch_actualizar_email.md) |
| `PUT` | Validar matriz | [endpoint_put_validar_matriz_criterios.md](endpoint_put_validar_matriz_criterios.md) |
| `PATCH` | Alta de wallet | [endpoint_patch_alta_wallet.md](endpoint_patch_alta_wallet.md) |
| `PUT` | Cerrar solicitud | [endpoint_put_cerrar_solicitud.md](endpoint_put_cerrar_solicitud.md) |
| `GET` | Consultar solicitud por ID | [endpoint_get_consultar_solicitud_id.md](endpoint_get_consultar_solicitud_id.md) |
| `GET` | Consultar solicitud por ID externo | [endpoint_get_consultar_solicitud_id_externo.md](endpoint_get_consultar_solicitud_id_externo.md) |
