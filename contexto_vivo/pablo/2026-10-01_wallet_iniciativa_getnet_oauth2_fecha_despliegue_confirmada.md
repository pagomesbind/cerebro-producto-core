---
id: 2026-10-01_wallet_iniciativa_getnet_oauth2_fecha_despliegue_confirmada
pm: pablo
fecha_captura: 2026-10-01
fuente: "/sync_meetings — reunión 'W 73 - Análisis de riesgos', 2026-10-01"
producto: wallet
tema: Despliegue de V73 (Getnet OAuth2 incluido) confirmado para el 08/10, activación por etapas
tipo: iniciativa
proyecto: getnet_oauth2_resolve
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Novedad puntual:** el proyecto `getnet_oauth2_resolve/` (PRD-237, Pablo Gomes) tiene fecha y plan de despliegue confirmados tras la reunión formal de análisis de riesgos de la versión 73 de Wallet. Despliegue a producción el **jueves 08/10 a las 6:30hs** (dentro del hito del 12/10 acordado con Getnet), con activación en dos etapas: microservicio desplegado el jueves con el flag de autenticación configurable por aceptador apagado, y recién el viernes 09/10 se cargan los aceptadores con su nueva configuración y se levanta el flag — fuera del horario de apertura transaccional por coincidir con semana de pagos. Contingencia de rollback vía el propio flag ya confirmada en sesiones anteriores.

Comentario consolidado posteado en Jira PRD-237 el 2026-10-01.
