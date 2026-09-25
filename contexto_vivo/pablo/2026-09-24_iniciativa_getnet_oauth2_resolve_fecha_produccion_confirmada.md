---
id: 2026-09-24_iniciativa_getnet_oauth2_resolve_fecha_produccion_confirmada
pm: pablo
fecha_captura: 2026-09-24
fuente: "/sync_meetings — reunión 'W 73 - Impacto de temas' (2026-09-24, 15:01, minuta Gemini, docId 1E_7KvojN4bdtUBL474fbEIx8mGxANb0A7vS8zbJhwSU)"
producto: wallet
tema: PRD-237 — fecha de pase a producción de Wallet v73 (incluye Getnet OAuth2) fijada en jueves 08/10, dentro del nuevo hito con Getnet
tipo: iniciativa
proyecto: PRD-237
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 2bc1252
---

Tras revisar dependencias de infraestructura y onboarding sin resolver, el equipo fijó el **jueves 08/10/2026** como fecha de pase a producción de la versión de Wallet que empaqueta la migración de Getnet a OAuth2.0 — dentro del nuevo hito del 12/10 ya acordado con Getnet ese mismo día (ver `getnet_oauth2_resolve/proyecto.md` §8), sin conflicto de plazos. Contingencia confirmada: feature flag para desactivar el modelo nuevo si falla, sin afectar al resto de los aceptadores. Riesgo nuevo abierto: el pase cae en plena semana de vencimientos (alta transaccionalidad de pagos QR) — reunión de análisis de riesgo agendada para el 25/09 (ver `riesgos.md`).
