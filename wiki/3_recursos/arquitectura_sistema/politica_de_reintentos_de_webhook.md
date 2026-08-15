# Política de Reintentos de Webhook

> Estado: en producción, con una excepción de canal sin confirmar (ver §3). Reubicado desde `detalle_productos/transversal/seguridad_y_webhooks.md §2` en la reestructuración PARA en cascada (2026-08-12), consolidando en un solo archivo lo que antes estaba repetido con contenido parcialmente divergente en `documentacion_api/general_info.md` y `detalle_productos/adquirencia/webhooks_y_notificaciones.md`.

## 🎯 Objetivo
Documentar la estrategia de reintentos que aplica el sistema cuando la URL del cliente para recibir un *webhook* **NO responde HTTP 200 (OK)**.

## ⏱️ Estrategia de Reintentos general (10 Intentos Máx.)
El sistema realiza un total de 10 intentos. Los tiempos de espera entre reintentos se han calculado a partir de los registros de log y son los siguientes (valores redondeados para la documentación):

| Intento Nro. | Intervalo Aprox. desde el Intento Anterior | Tiempo Acumulado Aprox. desde el Envío Inicial |
| --- | --- | --- |
| **1** | Envío Inicial | 0 segundos |
| **2** | **18 segundos** | 18 segundos |
| **3** | **18 segundos** | 36 segundos |
| **4** | **19 segundos** | 55 segundos |
| **5** | **18 segundos** | 1 minuto 13 segundos |
| **6** | **18 segundos** | 1 minuto 31 segundos |
| **7** | **2 minutos 10 segundos** | 3 minutos 41 segundos |
| **8** | **2 minutos 10 segundos** | 5 minutos 51 segundos |
| **9** | **1 hora** | 1 hora 5 minutos 51 segundos |
| **10** | **1 hora** | 2 horas 5 minutos 51 segundos |

## 🔑 Reglas de Finalización
- **Finalización por Éxito (`HTTP 200`):** Si en cualquier intento (del 2 al 10) el *endpoint* responde con un código **HTTP 200**, la política de reintentos se detiene inmediatamente.
- **Fallo Definitivo:** Si el décimo intento también falla, la notificación se marca como **fallida permanentemente**, y no se realizarán más envíos.

Esta es también la versión publicada en el portal público de developers (`psp.bind.com.ar/developers`) como contrato con los clientes — mantenida por `/sync_web`, que la referencia a este documento como fuente.

## 📲 Mensaje a compartir con el cliente

Comparto la información sobre nuestra política de reintentos cuando la URL de su webhook no responde con un HTTP 200.
Nuestro sistema intentará enviar el webhook 10 veces con una estrategia de espera creciente, buscando darle tiempo a su servidor para recuperarse sin saturarlo.

**⏱️ Secuencia de Reintentos (Tiempo desde el intento anterior)**

- Intentos 1 al 6: Se realizan rápidamente, espaciados en 18-19 segundos (todo en menos de 2 minutos).
- Intentos 7 al 8: El intervalo aumenta a 2 minutos y 10 segundos para esperar una recuperación de fallos temporales.
- Intentos 9 al 10: El tiempo se extiende a 1 hora entre cada envío, dando margen para solucionar problemas mayores de infraestructura.

✅ Puntos Clave:
Finalización por Éxito: Si en cualquier intento recibimos un HTTP 200, el proceso se detiene de inmediato.
Fallo Definitivo: Si el décimo intento falla, la notificación se marca como fallo definitivo y no se realizarán más envíos.

## ⚠️ 3. Excepción de canal sin confirmar — Agente de Cobros y Pagos (CVUCollect)

`detalle_productos/agente_cobros_y_pagos/cuenta_recaudadora_usd.md` documenta que, para el circuito CVUCollect del Agente de Cobros y Pagos, el envío de webhook está **acoplado al propio request de creación de transferencia** con un comportamiento distinto al de arriba: reintentos de **~7 segundos con 3 intentos**, no 10 intentos en 2 horas — y que la latencia de esos reintentos demora la respuesta del endpoint de creación de transferencia (quedó pendiente separar ambos procesos, ticket en estado "Refinar" al cierre del relevamiento que lo documentó).

**No está confirmado si esto es:**
(a) una implementación real y distinta para ese canal específico, o
(b) documentación desactualizada de una época anterior a que se unificara la política general de 10 intentos.

Registrado como gap abierto en [`../../2_areas/gaps_y_preguntas.md`](../../2_areas/gaps_y_preguntas.md) — no asumir ninguna de las dos lecturas sin confirmar con el equipo técnico.

## Ver también

- [mtls_apis_y_webhooks.md](mtls_apis_y_webhooks.md) — autenticación del webhook saliente cuando el cliente exige mTLS.
- `detalle_productos/adquirencia/` — estado del componente Webhook Sender (obsolescencia, falta de contingencia automática ante pérdida en reinicios, mecanismo de recuperación manual) — pendiente de incorporar acá en el desarme de archivos-cajón de Adquirencia.

---
*Última actualización: 2026-08-12 — Reubicado y consolidado desde `detalle_productos/transversal/seguridad_y_webhooks.md §2`, `documentacion_api/general_info.md §Webhooks` y la referencia cruzada en `cobros/cuenta_recaudadora_usd.md §2` (reestructuración PARA en cascada). Contradicción de canal (§3) registrada como gap, no resuelta unilateralmente.*
