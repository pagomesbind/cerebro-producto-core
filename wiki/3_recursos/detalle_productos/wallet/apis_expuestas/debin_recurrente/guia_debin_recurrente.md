# Guía — DEBIN Recurrente (Wallet)

> Fuente: https://psp.bind.com.ar/developers/apis/guia-debin
> Producto: Wallet — Debin recurrente

## ¿Cómo ingreso dinero con DEBIN recurrente?

Esta forma de hacer cash in en una cuenta de wallet se realiza mediante el tipo de operación DEBIN recurrente. En esta operación la Organización y Bind PSP están del lado vendedor y un banco o PSP externo están del lado comprador. Permite desde la cuenta de la Organización acreditar dinero, habiéndosela debitado a una cuenta de la misma titularidad de una entidad externa.

Ambas cuentas (tanto la cuenta a acreditar como la cuenta a debitar) deben ser de la misma titularidad (CUIT).

Para poder crear estas operaciones, primero las cuentas deben tener una suscripción de DEBIN recurrente activa con la cuenta externa de la cual quiere ingresar dinero. Al crear una suscripción esta queda implícitamente aceptada por la contraparte siempre y cuando sea entre cuentas de la misma titularidad.

La eliminación de una suscripción es definitiva. Se puede eliminar una suscripción pero luego no se podrá volver a crear. Sólo se puede volver a crear desde la entidad bancaria de la cuenta compradora.

Un usuario puede desconocer un DEBIN recurrente desde su banco e iniciar un contracargo para que se reverse arbitrariamente la operación por más que el usuario no tenga saldo en su cuenta.

## Flujo — DEBIN aprobado en línea

```
SETUP (una vez por cuenta):
  POST /suscripcion (CVU propio + CBU/CVU externo de misma titularidad)
  → Suscripción queda aceptada automáticamente (misma titularidad)
  → La eliminación es DEFINITIVA: solo puede recrearse desde el banco de la cuenta compradora

OPERATORIA NORMAL — DEBIN aprobado en línea:
  1. POST /debin (monto + externalRefId + suscripcion_id)
  2. Bind PSP solicita débito a la cuenta compradora (banco/PSP externo)
  3. Respuesta inmediata: aprobado → crédito en cuenta wallet del CVU destino
  4. EVENT "debin.recurrente" → webhook con estado COMPLETED

DEBIN rechazado en línea:
  1. POST /debin
  2. Respuesta inmediata: rechazado por el banco comprador
  → NO se acredita saldo
  → EVENT "debin.recurrente" con estado FAILED

DEBIN en proceso y luego aprobado:
  1. POST /debin → respuesta: IN_PROGRESS (no resuelto en línea)
  2. Entidad monitorea con GET /debin/{id}
  3. Más tarde: banco comprador aprueba → EVENT "debin.recurrente" con estado COMPLETED
     → Crédito acreditado en cuenta wallet

CONTRACARGO (posterior al cobro):
  → Usuario desconoce el DEBIN desde su banco
  → Bind PSP hace REVERSA: debita saldo de cuenta wallet (aunque no haya saldo)
  → EVENT "debin.contracargo" → webhook con aviso
  (Ver guía de contracargos)
```

## ¿Cómo tratar los contracargos?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-contracargodebin

Ver guía de contracargos DEBIN.

## Endpoints

| Método | Operación | Archivo |
|--------|-----------|---------|
| `POST` | Crear suscripción de recurrencia | endpoint_post_crear_suscripcion.md |
| `GET` | Consultar suscripciones | endpoint_get_consultar_suscripciones.md |
| `DELETE` | Eliminar suscripción | endpoint_delete_eliminar_suscripcion.md |
| `POST` | Crear DEBIN recurrente | endpoint_post_crear_debin.md |
| `GET` | Consultar operación por ID | endpoint_get_consultar_operacion_id.md |
| `GET` | Consultar operación por ID externo | endpoint_get_consultar_operacion_id_ext.md |
| `EVENT` | Aviso de DEBIN recurrente | endpoint_event_debin_recurrente.md |
| `EVENT` | Aviso de contracargo DEBIN | endpoint_event_contracargo_debin.md |
