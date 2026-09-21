---
id: 2026-09-21_adquirencia_conocimiento_v73_rafagas_qr_y_despliegue
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_mails — mail 'Minuta: Análisis de riesgo: AD V 73' (threadId 1a0b604212500a77), Matías Alzogaray, 2026-09-18 (minuta de la reunión del 17/09)"
producto: adquirencia
tema: Política de despriorización de ráfagas QR (>200 req/min) y plan de despliegue de riesgo Alto/Crítico de AD V73 (24/09)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: f230716c54a5ca6600a2bce4e46bf0292d56a58c
---

## Política nueva de gestión de colas QR (V73)

En la reunión de análisis de riesgo de AD V73 (17/09) se aprobó una política de **despriorización temporal (no rechazo) de ráfagas de QR dinámico**: cuando una fuente supera las **200 peticiones por minuto**, esas peticiones se envían a una **cola secundaria** en vez de competir por latencia con el resto del tráfico. La motivación explícita es la incidencia de Provincia Net (ya documentada en `incidente_qr_masivo_provincia_net.md`/`automatizacion_creacion_masiva_qr.md`) — esta política es la pieza de mitigación de infraestructura que faltaba formalizar del lado de gestión de colas, complementaria a las mejoras de infra (cola de Deuda+QR, duplicación de pods Workers, escalado de BD) ya comunicadas al cliente el 16/09 (ver `2026-09-16_adquirencia_pnet_mejoras_performance_distribucion_pedidos`, todavía en cola).

Ticket de soporte asociado: AD-1676 — "[SOPORTE] [Intermitencia] Demora mayor a 35s en la disponibilidad de datos de QR Dinámico" (DAD-2943, plan: que Infra revise las colas nuevas y su performance post-despliegue).

## Despliegue AD V73 — fecha y alcance de riesgo

- **Fecha confirmada:** 24/09/2026, 21hs, duración estimada 2 a 2.5 horas.
- **Prioridad/Impacto:** Alta/Crítica — cambios estructurales en archivos de liquidación que pueden romper integraciones de clientes, actualización de millones de registros en BD, incidentes previos sobre webhooks y QRs.
- **Orden de despliegue innegociable en 3 bloques:** Código → Verificación/Saneamiento de BD → Filtro. Alterar el orden rompe la conciliación externa y la asignación de CVUs en Botón Simple 2.0/RxT (dejaría a 32 Collectors sin stock).
- **Riesgo más crítico identificado:** las conciliaciones de bancos y comercios externos van a **fallar completamente** si esos terceros no adaptaron sus parsers al nuevo código de liquidación **004** (archivos BOTONLIQ/DEVBOTON) — acción previa pendiente: avisar a clientes y actualizar la documentación pública de developers con el nuevo formato (AD-1398/DAD-2257).
- **Zonas vulnerables adicionales durante el pase:** integraciones POS↔Global Processing (reembolsos/anulaciones), webhook FechaNegocio de Botón 2.0, todo el flujo de Pagos FX 2.0 del portal (carga de documentos, cotizaciones, validaciones).
- **Plan de rollback:** reversión estándar de imágenes por MS vía `kubectl set image` en AKS, salvo excepciones críticas que requieren revertirse en conjunto: DAD-2437 tiene script inverso propio (`SaneamientoPagoUnico-ROLLBACK.sql`); DAD-2209/2257, DAD-2294/2493 y el flujo de Beneficiarios (DAD-2290/2293/2492) deben revertirse juntos obligatoriamente; DAD-2265 (unicidad de emails) no elimina los duplicados ya creados durante la subida si se hace rollback.

> Fuente: mail "Minuta: Análisis de riesgo: AD V 73: Jue, 17 de sept de 2026" (Matías Alzogaray, threadId `1a0b604212500a77`), 2026-09-18.
