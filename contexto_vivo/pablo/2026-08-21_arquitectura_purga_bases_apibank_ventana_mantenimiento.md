---
id: 2026-08-21_arquitectura_purga_bases_apibank_ventana_mantenimiento
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_mails — mail 'Mantenimiento de bases de datos - Ventana 21/8 2am a 6am' (threadId `1a0209918df01a78`), Fintexa (Enrique Arnut / Juan Vázquez), 2026-08-20/21"
producto: arquitectura_sistema
tema: Depuración periódica de bases históricas (WalletOperacionesDB, WalletComprobanteDB, Notificaciones) durante ventanas de mantenimiento de Apibank — proceso parcial, pregunta abierta sobre bloqueos
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/mantenimiento_y_capacidad_aks.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

Fintexa (equipo de infraestructura) ejecuta periódicamente, aprovechando las ventanas de mantenimiento que abre el proveedor **Apibank**, un proceso de depuración de registros historificados (no vivos, no cambia estructura) en tres bases: **Comprobantes**, **Operaciones** y **Notificaciones**. El objetivo declarado es reducir el tamaño de las bases para mejorar performance y reducir costos operativos. Ticket de seguimiento del proveedor: `INF-1578` (Fintexa/Jira interno).

**Ejecución de la ventana del 21/08 (02:00-06:00am):** el proceso se detuvo a las 4am (2hs antes de lo previsto) con resultado parcial:
- `WalletOperacionesDB`: depuró del 2025-08-26 al 2025-10-14. Objetivo real: llegar hasta febrero 2026 — quedó lejos de la meta.
- `WalletComprobanteDB`: depuró del 2025-06-13 al 2025-08-14. Mismo objetivo (febrero 2026) — también quedó lejos.
- `Notificaciones`: se detuvo a las 4am **sin depurar nada**. Objetivo: llegar hasta mayo 2026.

No se explicó en el hilo por qué el proceso se detuvo antes de la hora límite de la ventana (6am) ni por qué `Notificaciones` no depuró nada.

**Pregunta sin responder al cierre de este hilo (gap operativo, no de la wiki):** Emma Vignoles (BIND) preguntó si se puede rediseñar este proceso para que no requiera una ventana de mantenimiento completa — por ejemplo, con microcortes — y si en esta ejecución se presentaron bloqueos temporales sobre las tablas afectadas. Ninguna de las dos preguntas fue respondida dentro de la ventana temporal de este barrido; en ejecuciones anteriores Fintexa había confirmado que el proceso "únicamente genera bloqueos temporales sobre las tablas afectadas" (no cambios de estructura ni de datos activos), lo cual habilitó el criterio de aprovechar esta ventana en particular.

> Fuente: Mail "Mantenimiento de bases de datos - Ventana 21/8 2am a 6am" — Enrique Arnut / Juan Vázquez (Fintexa), 2026-08-20/21; pregunta de Emma Vignoles sin respuesta en el hilo, 2026-08-21.
