# Guía — Transferencias (Wallet)

> Fuente: https://psp.bind.com.ar/developers/apis/guia-transferencia-entrante
> Producto: Wallet — Transferencias

## ¿Cómo integrar transferencia entrante?

Esta solución permite recibir transferencias entrantes desde cualquier otra cuenta en pesos argentinos.

El sistema resuelve la gestión del saldo del CVU y al confirmar la operación registra el crédito.

Luego de ocurrir la transferencia, se evalúa la misma en un sistema de monitoreo transaccional que puede disparar una alerta por prevención de fraude.

La transferencia entrante puede ser:
- Interna: si es entre dos CVU de la misma entidad. En este caso, se resuelve internamente y no se procesa en la red.
- Externa: si es hacia la cuenta de otra entidad externa. En este caso, se debe procesar en la red.

## ¿Cómo integrar transferencia saliente?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-transferencia-saliente

Esta solución permite realizar transferencias salientes a cualquier otra cuenta en pesos argentinos.

El sistema resuelve la gestión del saldo del CVU. No se iniciará la operación si la cuenta no tiene saldo suficiente. Antes de procesar la transferencia se debita el saldo necesario para cursarla y, en caso de que la transferencia haya resultado errónea, se devuelve el saldo en concepto de reversa.

También, antes de iniciar la transferencia, se evalúa la misma en un sistema de monitoreo transaccional que puede desaprobarla según restricciones por prevención de fraude. En este paso la transferencia puede ser rechazada antes de procesarse.

La transferencia saliente puede ser:

Interna: si es entre dos CVU de la misma entidad. En este caso, se resuelve internamente y no se procesa en la red.

Externa: si es hacia la cuenta de otra entidad externa. En este caso, se debe procesar en la red.

La entidad debe monitorear una transferencia saliente hasta que obtenga un estado definitivo. Una transferencia puede resolver su estado definitvo en el momento, pero también puede quedar en proceso. En este caso la entidad puede consultar su estado hasta que se resuelva o aguardar al webhook con el aviso.

No siempre se obtiene un estado definitivo del procesador al crear la transferencia en línea y puede tardar unos segundos en resolverse.

## Flujo — Transferencia entrante aprobada

```
1. Pagador inicia transferencia desde su cuenta (CBU/CVU origen) al CVU del usuario

2. [Si externa] Se procesa en la red (COELSA/DEBIN)
   [Si interna] Se resuelve internamente entre CVUs de la misma entidad

3. Bind PSP recibe confirmación de la red
   → Registra crédito en la cuenta corriente del CVU destino
   → Saldo del CVU aumenta

4. Sistema de monitoreo transaccional evalúa la operación
   → Si pasa: EVENT "transfer.received" → webhook a URL configurada
   → Si alerta: se puede frenar o marcar para revisión (anti-fraude)
```

## Flujo — Conciliar transferencia entrante

```
Si no llegó el webhook (ej. timeout o error transitorio):
  1. GET /operación por ID externo → buscar por ID conocido
  2. POST /conciliar → forzar conciliación si ya está en la red pero sin registrar
```

## Flujo — Transferencia saliente aprobada

```
1. Entidad verifica saldo disponible (opcional pero recomendado)

2. POST /transferencia
   → Body: CVU/CBU destino + monto + moneda + concepto + externalRefId
   → Bind PSP: evalúa monitoreo transaccional ANTES de procesar
     → Si la evaluación rechaza: devuelve error (sin débito)
     → Si pasa: DÉBITA el saldo del CVU origen inmediatamente

3. Respuesta inmediata: estado PENDING o IN_PROGRESS
   → La entidad DEBE monitorear hasta estado definitivo:
     GET /operación/{id} → polling hasta COMPLETED o FAILED

4. EVENT "transfer.sent" → webhook cuando alcanza estado definitivo
   → Si COMPLETED: fondos acreditados en destino
   → Si FAILED:    REVERSA automática → saldo devuelto al CVU origen
```

## Flujo — Transferencia saliente rechazada

```
1. POST /transferencia
   → Monitoreo transaccional rechaza por prevención de fraude
   → Respuesta: error (NO se debita el saldo)

ó

1. POST /transferencia → débito del saldo → procesada en red
   → Red rechaza la transferencia
   → REVERSA automática → crédito devuelto al CVU origen
   → EVENT con estado FAILED
```

## Endpoints

| Método | Operación | Archivo |
|--------|-----------|---------|
| `POST` | Realizar una transferencia saliente | endpoint_post_transferir.md |
| `POST` | Conciliar transferencia entrante | endpoint_post_conciliar_entrante.md |
| `GET` | Consultar operación por ID | endpoint_get_consultar_operacion_id.md |
| `GET` | Consultar operación por ID externo | endpoint_get_consultar_operacion_id_externo.md |
| `EVENT` | Aviso de transferencia saliente | endpoint_event_transferencia_saliente.md |
| `EVENT` | Aviso de transferencia entrante | endpoint_event_transferencia_entrante.md |
