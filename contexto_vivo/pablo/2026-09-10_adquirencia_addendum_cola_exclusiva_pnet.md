---
id: 2026-09-10_adquirencia_addendum_cola_exclusiva_pnet
pm: pablo
fecha_captura: 2026-09-10
fuente: "Sesión de trabajo directa con el PM (Pablo Gomes) sobre el discovery `1_proyectos/qr_masivo_sftp_paralelo/`, posterior a la reunión BIND/PNET del mismo día — el PM trajo una idea planteada por Arquitectura."
producto: adquirencia
tema: addendum al incidente de saturación de cola de QR — propuesta de Arquitectura de una cola exclusiva para Provincia Net (partición por cliente, distinta de AD935)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md
tipo_destino: actualizar
contradice: "no — complementa el item ya en cola 2026-09-10_adquirencia_reunion_pnet_causa_raiz_cola_unica_y_mitigacion con una 5ª línea de exploración que surgió después de esa reunión; no se editó ese item porque ya está en_cola"
confianza: media
estado: ingestado
merge_commit: 201b3e0
---

**Idea adicional de Arquitectura (post-reunión 09-10):** en vez de (o además de) AD935 — que separa la cola de generación de QR por **tipo de tráfico** (interactivo vs. batch/ráfaga) — se planteó una cola de generación de QR **exclusiva para Provincia Net**, separada de la del resto de los clientes. Es una partición por **cliente**, no por tipo de tráfico.

**Limitación reconocida explícitamente por el PM al traerla:** esta cola "no mejoraría a Provincia Net" — un ente mediano de PNET seguiría compitiendo por la misma capacidad dentro de su propia cola exclusiva, sin resolver ningún problema de PNET en sí. Su único beneficio es **evitar que el volumen de PNET siga impactando al resto de los clientes** (DEPAY y cualquier otro cliente del canal interactivo compartido) — se propone evaluarla al menos como **quick win**, más simple de implementar que separar por tipo de tráfico.

**Probable solapamiento con AD935:** el análisis de datos de `dbo.Deuda` (`prd-66_provincianet_creacion_masiva_qr/gaps.md`) ya estableció que PNET concentra ~90-97% del volumen del sistema en los minutos de pico — si esa es también la composición del tráfico "batch/ráfaga" que AD935 busca aislar, una cola "PNET vs. resto" y una cola "batch vs. interactivo" terminarían aislando casi el mismo tráfico en la práctica. Vale que Arquitectura confirme si son redundantes, o si la partición por cliente (más simple de razonar y potencialmente más rápida de implementar) puede servir de puente mientras se diseña la partición por tipo de tráfico (más general, cubre a futuros clientes de alto volumen además de PNET).

## Ver también

- `3_recursos/detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md` — el incidente base, con AD935 ya documentado como línea de mitigación de largo plazo.
- `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §7` — registro de esta idea en el timeline del proyecto.
- `1_proyectos/qr_masivo_sftp_paralelo/proyecto.md` (estacionamiento S4) — donde se documentó primero, aunque pertenece conceptualmente al incidente de PRD-66, no a ese discovery de paralelismo del SFTP.
