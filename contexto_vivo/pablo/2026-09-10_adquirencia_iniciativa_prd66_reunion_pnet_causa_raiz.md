---
id: 2026-09-10_adquirencia_iniciativa_prd66_reunion_pnet_causa_raiz
pm: pablo
fecha_captura: 2026-09-10
fuente: "Actualización de `1_proyectos/index.md §2` a partir de la reunión 'BIND / PNET: Performance, recurrencia, etc.', 2026-09-10."
producto: adquirencia
tema: PRD-66 — causa raíz de la demora de generación de QR confirmada en vivo con Provincia Net, plan de mitigación acordado
tipo: iniciativa
proyecto: PRD-66
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 0de2694
---

**Novedad puntual (no estado completo del proyecto, eso está en Jira/`proyecto.md`):** en una reunión directa entre Bind PSP y Provincia Net (2026-09-10), Ingeniería de ambos lados confirmó en vivo la causa raíz de la demora de generación de QR que venía siendo investigada desde principios de septiembre (reclamo de DEPAY/AD-1676): una única cola compartida de generación de QR, agravada por una política de reintentos de Provincia Net que en los picos de saturación genera un "retry storm" (hasta 100% de reintentos fallidos). Se acordó un plan de mitigación de corto plazo (escalado de recursos, paliativo ~1-1,5 mes) y se confirmó que el de largo plazo (separar la cola en interactiva/batch, ticket AD935) ya está en discusión activa de Arquitectura. Se abrieron además 4 líneas de exploración sobre el canal SFTP de Provincia Net (multi-canal en paralelo, reducir tiempo de despacho de lotes chicos, ajuste de backoff de reintentos, medición del ratio deuda/QR).

Detalle completo en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §8` y en el item de conocimiento `2026-09-10_adquirencia_reunion_pnet_causa_raiz_cola_unica_y_mitigacion` (pendiente de merge a `3_recursos/detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md`).
