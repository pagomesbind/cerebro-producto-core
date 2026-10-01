---
id: 2026-10-01_iniciativa_salud_api_clientes_requerimiento_uat_keepit
pm: pablo
fecha_captura: 2026-10-01
fuente: "/sync_mails — hilo \"Especificaciones API monitoreo y Background Service Cache\" (threadId 1a0d3d66f6f8215b), Keepit Simple / Hernán Clarich, 2026-10-01"
producto: wallet
tema: "PRD-262 (salud del ecosistema vía API) — Keepit arranca el requerimiento técnico de Etapa 1 en UAT, Pablo confirma que Elastic Proxy entra en la primera entrega"
tipo: iniciativa
proyecto: PRD-262
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Keepit Simple (Juan Pablo Carubelli) confirmó el 2026-10-01 que el requerimiento técnico de Etapa 1 de la API de salud del ecosistema (PRD-262, Background Service Cache + API de consumidor) ya está cargado en el tablero de Jira, y abrió 4 bloques de preguntas técnicas para avanzar en UAT/staging (workspace y datos de Log Analytics, identidad de consulta vía Managed Identity/App Registration, alcance de producto APIM visible en UAT, runtime del microservicio). Pablo Gomes aclaró que el **Elastic Proxy Ingress/Egress debe incluirse en la primera entrega**, no diferirse a Etapa 2+ como lo tenía entendido Keepit, porque ahí viven los datos de terceros externos (Coelsa, API Bank) y sin eso la funcionalidad base con clientes queda incompleta. Hernán Clarich (Fintexa) confirmó el mismo día que ya hay datos de `ApiManagementGatewayLogs` disponibles en el ambiente de UAT; el resto de los puntos técnicos queda pendiente de su revisión. Juan Pablo Carubelli (Keepit) avisó que está de licencia el viernes 02/10 y el lunes 05/10.

> Fuente: hilo "Re: Especificaciones API monitoreo y Background Service Cache" — Juan Pablo Carubelli (Keepit), Hernán Clarich (Fintexa), Pablo Gomes, 2026-10-01, threadId `1a0d3d66f6f8215b`.
