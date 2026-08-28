# Plan de Mantenimiento AKS (Agosto 2026) — Reversión Post-Incidente + Optimización

> Reubicado desde `arquitectura_sistema/index.md §12` en la reestructuración PARA en cascada (2026-08-12). Fuente: Mail "Ajuste AKS Bind PSP" — daniel.zalazar@fintexa.tech (Infrastructure Leader, Fintexa), 2026-08-06.

Fintexa (SRE) propuso un plan de mantenimiento sobre la infraestructura de procesamiento del tenant Bind PSP, en 2 bloques, todavía pendiente de conformidad/aprobación de Bind PSP a la fecha del barrido original.

- **Contexto:** a raíz del incidente de julio vinculado a los balanceadores de carga (ver `detalle_productos/wallet/otros_manuales.md §7.2` para el diagnóstico de esas caídas), se habían escalado preventivamente varios recursos de procesamiento por encima de lo habitual. Con la situación normalizada, el plan busca devolverlos a su configuración previa y aplicar mejoras.
- **Bloque 1 — reducción de costos (riesgo bajo, sin corte de servicio):** pods del webhook sender de 32→16; nodos de procesamiento de 46→28; VM scale set de 18→9.
- **Bloque 2 — optimización de plataforma:** actualización de AKS (sin corte, con logs de Ingress como contingencia); reconfiguración del balanceador de carga externo (timeout de conexión inactiva de 30 min→4 min) — **única tarea con corte de servicio previsto, ~30 min, en ventana de bajo tráfico a coordinar**; distribución más uniforme de pods egress/webhooksender entre nodos.
- **Cronograma tentativo:** Bloque 1 la semana del 2026-08-10; Bloque 2 sin fecha confirmada, sujeto a aprobación de la ventana de mantenimiento.
- **Ticket de seguimiento (2026-08-07):** Fintexa cargó `INF-1516` (fintexa.atlassian.net) para la desescalada de AKS de la semana del 2026-08-10. Hernán Clarich (Bind) pidió puntualizar qué monitorear durante el cambio y si hace falta soporte del equipo de Pablo Serra (Fintexa) o de QA PSP.
- **Ejecución del Bloque 1 (2026-08-10/11):** plan de acción confirmado por Fintexa — martes 11/08 7:30-8:00hs, desescalado de pods sin reinicio de servicio (WebHookSender Wallet 32→16, Walletbind 20→15, Walletoperaciones 24→12); miércoles 12/08 7:30-9:00hs, desescalado de nodos (2 nodepools de 18→10 nodos cada uno, drenado gradual sin afectar todos los nodos a la vez; el nodepool de Rabbit —9 nodos— no se toca). Complementariamente se aplicará anti-affinity a los pods de comprobante/egress/webhooksender aceptador en cada despliegue futuro. **Confirmado 2026-08-11:** el desescalado de pods del martes se ejecutó según lo planeado, sin afectación de servicios; continúa el desescalado de nodos el miércoles.
- **Bloque 1 completado (2026-08-12/13):** el desescalado de nodos se ejecutó en 2 días (uno por nodepool) en vez de uno solo, por conflicto de agenda con otros despliegues — 12/08 un nodepool bajó de 18 a 10 nodos, monitoreado sin degradación; 13/08 se completó el segundo nodepool en las mismas proporciones, también sin afectación (Hernán Clarich confirmó: sin cambios en tasa de error ni en tiempo de respuesta). **Bloque 1 cerrado.** Bloque 2 (actualización de AKS + reconfiguración del balanceador, única tarea con corte de servicio) sigue sin fecha confirmada.
- **Nota operativa (2026-08-12):** la prueba de parametrización del Egress en STG (ver [`incidentes_de_plataforma.md` §7](incidentes_de_plataforma.md)) se suspendió el mismo día por falta de capacidad del equipo de SRE, que tenía en paralelo un despliegue de Aceptador y el desescalado de nodos — reagendada sin fecha nueva.

## Depuración periódica de bases históricas — ventanas de mantenimiento de Apibank

> Fuente: `/sync_mails` — mail "Mantenimiento de bases de datos - Ventana 21/8 2am a 6am" (threadId `1a0209918df01a78`), Fintexa (Enrique Arnut / Juan Vázquez), 2026-08-20/21.

Fintexa (equipo de infraestructura) ejecuta periódicamente, aprovechando las ventanas de mantenimiento que abre el proveedor **Apibank**, un proceso de depuración de registros historificados (no vivos, no cambia estructura) en tres bases: **Comprobantes**, **Operaciones** y **Notificaciones**. El objetivo declarado es reducir el tamaño de las bases para mejorar performance y reducir costos operativos. Ticket de seguimiento del proveedor: `INF-1578` (Fintexa/Jira interno).

**Ejecución de la ventana del 21/08 (02:00-06:00am):** el proceso se detuvo a las 4am (2hs antes de lo previsto) con resultado parcial:
- `WalletOperacionesDB`: depuró del 2025-08-26 al 2025-10-14. Objetivo real: llegar hasta febrero 2026 — quedó lejos de la meta.
- `WalletComprobanteDB`: depuró del 2025-06-13 al 2025-08-14. Mismo objetivo (febrero 2026) — también quedó lejos.
- `Notificaciones`: se detuvo a las 4am **sin depurar nada**. Objetivo: llegar hasta mayo 2026.

No se explicó en el hilo por qué el proceso se detuvo antes de la hora límite de la ventana (6am) ni por qué `Notificaciones` no depuró nada.

**Pregunta sin responder al cierre de este hilo (gap operativo, no de la wiki):** Emma Vignoles (BIND) preguntó si se puede rediseñar este proceso para que no requiera una ventana de mantenimiento completa — por ejemplo, con microcortes — y si en esta ejecución se presentaron bloqueos temporales sobre las tablas afectadas. Ninguna de las dos preguntas fue respondida dentro de la ventana temporal de este barrido; en ejecuciones anteriores Fintexa había confirmado que el proceso "únicamente genera bloqueos temporales sobre las tablas afectadas" (no cambios de estructura ni de datos activos), lo cual habilitó el criterio de aprovechar esta ventana en particular.

**Corroboración por otra fuente (2026-08-25):** la minuta de "Repaso Semanal líderes" del 25/08 menciona, como decisión operativa menor, una ventana de mantenimiento nocturna (2:00-6:00) a coordinar con el DBA para eliminar comprobantes/operaciones pesadas — ver [`incidentes_de_plataforma.md §8`](incidentes_de_plataforma.md), mismo proceso de depuración descripto acá desde otra fuente.

## Ver también
- [relacion_con_fintexa.md](relacion_con_fintexa.md) — dotación de recursos y gobierno de arquitectura del mismo proveedor.
- [infraestructura_cloud_azure.md](infraestructura_cloud_azure.md) — cluster AKS afectado por este plan.
- [incidentes_de_plataforma.md §8](incidentes_de_plataforma.md) — corroboración por otra fuente (2026-08-25) de la ventana de mantenimiento de purga de bases.

---
*Última actualización: 2026-08-27 — `/context_merge`: nueva sección sobre la depuración periódica de bases históricas (Comprobantes/Operaciones/Notificaciones) en ventanas de mantenimiento de Apibank, con el resultado parcial de la ejecución del 21/08 y la pregunta operativa abierta sobre rediseño sin corte completo.*
*Última actualización anterior: 2026-08-14 — `/sync_mails`: Bloque 1 (desescalado de nodos) completado 12-13/08 sin degradación de servicio; nota sobre suspensión de la prueba de Egress en STG por conflicto de capacidad.*
*Última actualización anterior: 2026-08-12 — Reubicado desde `arquitectura_sistema/index.md §12` (reestructuración PARA en cascada). Contenido sin cambios.*
