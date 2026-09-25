---
id: 2026-09-24_clientes_bcf_sin_ficha_fraude_60pc_volumen_wallet
pm: pablo
fecha_captura: 2026-09-24
fuente: "/sync_meetings — reunión 'Join Soporte Clientes' (2026-09-23, 10:02), minuta Gemini, docId 19KB7bu5GvFkNi9GwAu4KbdjwA-EQswrNwT3im5yAX74"
producto: transversal
tema: cliente BCF sin ficha en log_clientes.md pese a concentrar más del 60% de la transaccionalidad de Wallet y presentar alto nivel de fraude/cuentas mula
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 2bc1252
---

## Descripción

En la reunión "Join Soporte Clientes" (2026-09-23, 10:02, minuta Gemini), Gonzalo Rivera advirtió que la entidad **BCF concentra más del 60% de la transaccionalidad de Wallet**, pero presenta un **alto nivel de fraude y cuentas mula** — riesgo operativo significativo. No existe hoy un equipo de auditoría formal sobre este cliente: BCF realiza su propio proceso de onboarding sin validación previa de Bind PSP.

**Decisión acordada en la misma reunión (ya capturada aparte como conocimiento operativo, no repetida acá):** Adriana Endzeliz solicitará formalmente a BCF la versión actualizada de su instructivo/manual de onboarding, para que el equipo pueda auditarlo y mitigar los incidentes de fraude.

**El gap:** pese a que BCF ya aparece mencionado en al menos otra reunión previa sincronizada por esta skill (2026-09-16, "Join Soporte Clientes" — contracargos de Octagon "además de un problema de fraude señalado por separado con BCF", ver `4_archivos/contexto_ingestado/2026-09_contexto_ingestado/2026-09-18_clientes_octagon_contracargos_fallas_cajeros.md`), **BCF no tiene ficha en `wiki/2_areas/clientes/log_clientes.md`** — verificado con búsqueda exacta (`BCF`) en el log maestro, 0 resultados. Dado que es, según esta reunión, el cliente con mayor volumen de Wallet y con riesgo de fraude activo, la ausencia de ficha es una laguna relevante, no solo un detalle administrativo — impide documentar en `casos_de_uso_clientes.md` el seguimiento del riesgo de fraude y la auditoría del onboarding que se está por pedir.

## Pregunta para el usuario / siguiente paso

¿"BCF" es el nombre completo del cliente, o una sigla/abreviación que tiene un nombre distinto cargado (o pendiente de cargar) en Notion? Mientras no se confirme, no corresponde crear una ficha en `casos_de_uso_clientes.md` sin pasar primero por `log_clientes.md` (dominio exclusivo de `/sync_customers`) — este item queda para que `/sync_customers` lo levante en su próximo barrido de Notion, o para que el usuario confirme el nombre canónico.

## Fuente

Reunión "Join Soporte Clientes" (2026-09-23, 10:02 GMT-03:00), minuta de Gemini. Cita relevante: Gonzalo Damian Rivera sobre concentración de transaccionalidad y fraude de BCF; Adriana Endzeliz sobre la decisión de solicitar el manual de onboarding actualizado.
