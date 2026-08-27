---
id: 2026-08-26_wallet_fci_paso6_pcnt_resiliencia_w72
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), ticket WS-1374"
producto: wallet
tema: FCI — resiliencia del paso 6 (informe de lotes a PCNT) ante errores 502
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

[WS-1374](https://bindpsp.atlassian.net/browse/WS-1374), W 72, 3 SP, Epic WS-54. Se detectaron en producción errores `502 BadGateway` de PCNT al generar los paquetes (Suscripciones y Rescates) en el **paso 6** del proceso diario de FCI. Dos problemas de fondo, distintos del cluster de bugs de fórmula/robustez ya documentado en §4.1/§4.2:

1. **Sin reintentos:** un error en el paso 6, tanto en Suscripción como en Rescate, no tenía lógica de reintento.
2. **Pérdida de traza cruzada:** el registro de `FCIPasosDetalles` se generaba para el **par** Suscripción/Rescate junto — si la Suscripción se informaba OK pero el Rescate fallaba, el registro completo quedaba marcado como ERROR, perdiéndose la traza de que la Suscripción sí se había procesado correctamente en Poincenot.

**Refactor implementado:**
- Se separó la clasificación de operaciones (suscripciones/rescates/no-aplican) desde `InformarLoteOperacionesCommand` hacia `CalcularOperacionesCommand`, que ahora arma lotes separados por tipo y publica eventos `InformarLoteOperacionesEvent` que corresponden solo a un tipo (con discriminador agregado al evento).
- `InformarLoteOperacionesCommand` pasa a informar un único tipo por evento — una falla al informar rescates ya no descarta la información de suscripciones ya persistida en `FCIProcesoCuenta`/`FCIPasoDetalle`.
- Se incorporó configuración de reintentos de RabbitMQ (`UseMessageRetry`) para el consumo de `InformarLoteOperacionesEvent`, sumada al reintento transitorio existente (do-while) para problemas de comunicación momentáneos, que se mantiene sin cambios.

Sin desvíos respecto a la definición técnica. QA no pudo reproducir el 502 directamente (dependiente del proveedor); se validó por regresión general del flujo el 2026-08-07.

**Al mergear:** agregar como nueva entrada en §4.2 ("Robustez del proceso diario"), cerca de los ítems relacionados con el paso 6/paquetes (WS-387, WS-82) — mismo dominio de resiliencia del proceso diario de FCI.
