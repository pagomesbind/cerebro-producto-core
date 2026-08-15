# Guía — ¿Cómo funciona cuenta remunerada?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-cuentaremunerada
> Producto: Wallet — Cuenta remunerada

## Descripción

Esta solución permite realizarle créditos diarios a cada cuenta por un rendimiento ganado al tener invertido su saldo en un fondo común de inversión, aún permaneciendo el saldo de la misma a la vista y totalmente utilizable en todo momento.

Para esto el sistema se encarga de realizar todos los cálculos necesarios para suscribir o rescatar saldo en el fondo común de inversión según corresponda para cada cuenta, y luego ejecutar estas operaciones de inversión en el broker. Sólo se considerarán las cuentas que tienen asociadas una cuenta comitente y que tengan habilitada la remuneración.

El proceso es automático sobre cuentas habilitadas para ello y no requiere de ninguna acción adicional de la Organización. Cada cuenta habilitada también debe tener una cuenta comitente creada, activa y asociada.

Finalmente, al final de cada proceso, se acredita automáticamente el monto correspondiente a la ganancia por rendimiento del saldo invertido el día anterior, y se notifica a la Organización de esta novedad por webhook.

La entidad debe tener en cuenta que los saldos invertidos son extraídos de la cuenta recaudadora. Entonces, debe prever un mecanismo financiero para reservar los fondos suficientes para no afectar la operatoria normal de los clientes.

El proceso funciona una vez por día y sólo los días hábiles.

## Flujo — Proceso diario de cuenta remunerada

```
PRE-REQUISITO por cuenta:
  POST /cuenta-comitente → crear cuenta comitente en el broker
  → Asociar a la cuenta de wallet + habilitar remuneración

PROCESO AUTOMÁTICO (1 vez por día hábil, sin intervención de la Organización):

  1. Bind PSP calcula el saldo a suscribir o rescatar del FCI (Fondo Común de Inversión)
     para cada cuenta habilitada
     → Los fondos invertidos se extraen de la cuenta recaudadora

  2. Bind PSP ejecuta operaciones de suscripción/rescate en el broker
     → Las cuentas sin comitente activa son ignoradas

  3. Al final del proceso:
     → Se acredita la ganancia por rendimiento del día anterior a cada cuenta
     → EVENT "rendimiento.fci" → webhook por cada cuenta (monto acreditado)
     → EVENT "conclusion.proceso.fci" → webhook cuando termina el proceso completo

CONSULTAS:
  GET /tna → tasa nominal anual vigente del FCI
  GET /proceso/{fecha} → estado del proceso de un día específico
```

## Endpoints del módulo

| Tipo | Descripción | Archivo |
|------|-------------|---------|
| `POST` | Crear cuenta comitente | [endpoint_post_crear_cuenta_comitente.md](endpoint_post_crear_cuenta_comitente.md) |
| `GET` | Consulta de TNA | [endpoint_get_consultar_tna.md](endpoint_get_consultar_tna.md) |
| `GET` | Consultar proceso | [endpoint_get_consultar_proceso_fci.md](endpoint_get_consultar_proceso_fci.md) |
| `EVENT` | Aviso de pago de rendimiento | [endpoint_event_rendimiento_fci.md](endpoint_event_rendimiento_fci.md) |
| `EVENT` | Aviso de fin de proceso | [endpoint_event_conclusion_proceso_fci.md](endpoint_event_conclusion_proceso_fci.md) |
