---
id: 2026-09-07_wallet_iniciativa_getnet_jira_creado
pm: pablo
fecha_captura: 2026-09-07
fuente: "/idea_jira — creación completa en Jira de getnet_oauth2_resolve"
producto: wallet
tema: creación en Jira — Getnet migra su API Resolve a OAuth2.0
tipo: iniciativa
proyecto: getnet_oauth2_resolve
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Novedad puntual:** el proyecto BAU `getnet_oauth2_resolve/` (Pablo Gomes) completó su creación en Jira. IDEA **PRD-237** ("Autenticación configurable por aceptador para la lectura de códigos QR") transicionada a **EN APROBACION** — categoría BAU, producto Wallet, cliente SOPORTE (pedido interno de Integraciones, no de un cliente puntual), SP estimado 10 (rango de riesgo 10–18), prioridad **Highest** a pedido explícito del PM por el deadline duro impuesto por Getnet (corte del circuito de autenticación anterior, 30/09/2026).

Epic **WS-1599** creada en el espacio de desarrollo de Wallet, con 2 Historias en Backlog: **WS-1600** (Highest — capacidad de autenticarse contra un aceptador con el mecanismo que tenga configurado, token fijo u OAuth2, aplicada concretamente a Getnet) y **WS-1601** (Medium — extender el mecanismo de API ya existente para que Soporte gestione aceptadores, hoy sin usarse en la práctica, para que también soporte el nuevo mecanismo). La Epic no tiene un análisis técnico-funcional formal previo — esa definición queda a cargo de Fintexa, que ya tiene su propio análisis y diseño en curso por la urgencia del plazo; la descripción de la Epic es un resumen armado desde el PRD, con esa limitación declarada explícitamente.

Próximo paso: T-068 (`tareas.md`) — pedir a Fintexa el documento de análisis/diseño ya elaborado, y confirmar si el ticket que Alan Martínez (Fintexa) ya cargó por su cuenta es el mismo que resuelve esta migración.
