---
id: 2026-10-06_ardid_oportunidad_conciliacion_facturacion_coto
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_mails — mail \"Dolor en facturación de ARDID - COTO\" de Gonzalo Rivera (Team Leader Integraciones y Soporte), 2026-10-05, threadId 1a10de1bcf4fbe5d, a Pablo Gomes/Nicolás Colón/Luciana Rudaz, cc Rocío Revelli/Mariana Nadalin/Emma Vignoles"
producto: ardid
tema: Falta de ID único para reconciliar la facturación de Ardid con las bases transaccionales de Wallet — dolor concreto detectado con el cliente COTO
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Gonzalo Rivera (Team Leader de Integraciones y Soporte) levantó el 2026-10-05 un punto pendiente sobre la **facturación de Ardid a COTO**, dirigido a los tres PM (Pablo Gomes, Nicolás Colón, Luciana Rudaz) — es un dolor que "seguramente" se va a repetir con otras entidades futuras, no exclusivo de COTO.

**El problema:** hoy es dificultoso hacer un cruce certero entre las transacciones que se le cobran a una entidad por Ardid y lo que efectivamente se ve en las bases de datos transaccionales de Wallet. Gonzalo adjuntó un Excel con dos pestañas de agosto 2026 ("Agosto 4845" — transacciones que pasaron por Ardid y que se facturan a COTO; "Wallet Agosto Coto" — detalle de transacciones de Wallet del mismo mes) para ilustrar el problema.

**El punto de dolor puntual:** no existe un ID o valor único que persista entre todas las bases involucradas. Hoy la única forma de cruzar es usar distintas columnas según el tipo de operación:

- Saliente externa → se cruza con el id de operación en Wallet.
- Entrante externa → se cruza con el `ArdidTransactionId` en Wallet.
- QR entrante → **no hay forma de cruzar.**
- Transacciones rechazadas por Ardid → **no hay operación generada, no hay forma de cruzar.**

Es decir, para 2 de los 4 escenarios (QR entrante, rechazos de Ardid) el cruce es directamente imposible con el esquema de datos actual.

**Por qué es una oportunidad, no solo un bug puntual:** Gonzalo explícitamente marca que esto "seguramente" se repite con "otras futuras entidades" — no es un caso aislado de COTO, es una limitación estructural del esquema de trazabilidad entre Ardid y Wallet que afecta a cualquier entidad facturada por uso de Ardid. Esto conecta con la iniciativa ya abierta `2026-09-28_transversal_iniciativa_conciliacion_agente_cobros_pagos_nico_colon` (conciliación automática de transferencias entrantes con Coelsa, `pm_destino: Nicolás Colón`) — ese item es sobre conciliación con Coelsa específicamente; este dolor es sobre conciliación interna Ardid↔Wallet para fines de facturación, un alcance distinto aunque de la misma familia de problema (falta de ID transversal persistente). Vale la pena que el merge los deje referenciados entre sí en `oportunidades.md`.

**Estado:** sin discovery iniciado, sin IDEA en Jira. Candidata a evaluación — definir un ID único/correlación transversal entre Ardid y las bases transaccionales de cada producto que lo consume (Wallet, y potencialmente otros) sería la resolución de fondo.
