# Cliente COTO — Historial Operativo de Devoluciones/Rendiciones (Botón LCK, BOTONLIQ)

> Estado: mezcla de en producción y seguimiento operativo (varios frentes sin cierre confirmado a la fecha del último barrido).
>
> Extraído desde [devoluciones_y_contracargos.md](devoluciones_y_contracargos.md) por umbral de tamaño de archivo (2026-08-27) — es la historia operativa completa de un único cliente (COTO) sobre el mecanismo general de devoluciones/contracargos ya documentado ahí (§1), separada para no diluir el contenido de producto transversal. Origen: IDEA Jira PRD-81 "COTO: Acomodar devoluciones parciales" y su evolución posterior en el tiempo (Botón LCK, archivo BOTONLIQ, tickets DAD-2171/DAD-2209).

## 1.1 Historia de producto y cluster de bugs de webhooks — cliente COTO (IDEA Jira PRD-81, Finalizada)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA PRD-81 "COTO: Acomodar devoluciones parciales" (PRD completo en la Descripción) + Epic AD-61 (11 tickets Finalizados + 1 aún Asignado, excluido). Complementa la documentación técnica de [devoluciones_y_contracargos.md §1](devoluciones_y_contracargos.md) con el origen de negocio y la cola de bugs que salieron a la luz al estabilizar la funcionalidad.

**Origen de negocio**: el sistema de cobro no tenía funcionalidades naturales para operar devoluciones parciales por API. El cliente **COTO** (grande, por salir en producción) consideraba esta funcionalidad como excluyente/bloqueante, y Producto aprovechó ese impulso comercial para terminar de cerrar una funcionalidad esencial del producto de Cobro — decisión explícita de priorizar por velocidad ("debe resolverse con gran velocidad porque COTO ya está por salir").

**Alcance aprobado** (MUST): más info del contracargo en el webhook, endpoint para consultar un contracargo por id. (Should): filtrar consulta de transacciones por hora/minuto/segundo. **Fuera de alcance** explícito: nuevo webhook de contracargo, contracargo con id externo, endpoints separados de transacción/lista de contracargos por id/id externo — 5 Story Points totales.

**Cluster de bugs encontrados en QA al estabilizar el webhook de contracargo/devolución** (evidencia de que el webhook de [§1](devoluciones_y_contracargos.md#1-documentación-devoluciones-parciales) pasó por varias rondas de corrección antes de quedar como está documentado hoy):
- Formato de fecha incorrecto en `fechaContracargo` (MM/DD/AAAA en vez de DD/MM/AAAA).
- `EstadoTransaccion` informado como `ACREDITADO` cuando en realidad ya estaba `DEVUELTA`.
- Webhooks disparados con el contracargo todavía en estado `PENDIENTE`, en vez de esperar a un estado definitivo (`RECHAZADO` o `ACEPTADO`).
- Contracargo QR **parcial** con estado `RECHAZADO` no generaba webhook (sí lo hacía el total).
- Webhook de devolución de pago con tarjeta informaba el `IdTransaccion` en el campo donde se esperaba `IdContracargo`.
- Consulta de contracargo no devolvía el `TransaccionId` (pedido agregado sobre la marcha).
- Tanda de correcciones menores agrupadas en un solo ticket ("Correcciones varias de Webhooks de contracargos"): `idComprobante` informado sin sentido en el webhook de contracargo rechazado, entre otras.

**Lectura para estimaciones futuras**: mismo patrón que el cluster de "Deuda" en [boton_simple_2_0.md §3](boton_simple_2_0.md) — un webhook de evento de negocio (acá: contracargo/devolución) tiende a generar una cola de bugs de "campo incorrecto/estado prematuro/caso no contemplado" proporcional a la cantidad de estados y medios de pago que atraviesa (QR, tarjeta, transferencia), no al tamaño original de la Epic (acá: 5 SP la IDEA, pero 8 de los 12 tickets de la Epic fueron bugs encontrados después).

**Versiones de publicación** (vía `/sync_releases`, backfill XML 2026-07-13): el alcance MUST original — [AD-63](https://bindpsp.atlassian.net/browse/AD-63) (endpoint consultar contracargo) y [AD-62](https://bindpsp.atlassian.net/browse/AD-62) (más info en el webhook), más [AD-64](https://bindpsp.atlassian.net/browse/AD-64) (filtro por hora/minuto/segundo) — se publicaron en **AD 66** (2025-12-16), junto con el resto del cluster de bugs de esa misma tanda: [AD-388](https://bindpsp.atlassian.net/browse/AD-388) (webhook con contracargo PENDIENTE) y [AD-357](https://bindpsp.atlassian.net/browse/AD-357)/[AD-288](https://bindpsp.atlassian.net/browse/AD-288) (correcciones de webhook, `IdTransaccion` en vez de `IdContracargo`). El resto del cluster salió en **AD 67.2** (2026-02-10): [AD-444](https://bindpsp.atlassian.net/browse/AD-444) (formato de fecha), [AD-389](https://bindpsp.atlassian.net/browse/AD-389) (`EstadoTransaccion` ACREDITADO vs DEVUELTA), [AD-316](https://bindpsp.atlassian.net/browse/AD-316) (contracargo QR parcial rechazado sin webhook), [AD-298](https://bindpsp.atlassian.net/browse/AD-298) (falta `TransaccionId`). Capítulo posterior no incluido en la IDEA original: **AD 70.2** (2026-07-02) [AD-1348](https://bindpsp.atlassian.net/browse/AD-1348) — contracargo QR de una cuenta Wallet sin saldo quedaba PENDIENTE para siempre en vez de RECHAZADO; corregido para que Wallet informe el `motivoRechazo` real, aunque el Admin **todavía no lo muestra al comercio** (mejora sugerida, sin ticket propio a la fecha).

**Bug adicional (julio 2026) — `BOTONLIQ` no incluye devoluciones de días anteriores:**
- **Síntoma:** devoluciones hechas por Admin el 25/06 sobre transacciones del 18-19/06 no aparecieron en el archivo `A102BOTONLIQ260626.626` del día siguiente, pese a que Bind ya había desarrollado (a pedido de COTO) que las devoluciones de días anteriores figuren en el `BOTONLIQ` correspondiente al día en que se hace la devolución.
- **Confirmado como bug** por Bind (2026-07-02): en ambiente de prueba funciona correctamente, no así en producción. Ticket Jira Soporte de COTO: `BP-48516`.
- **Resolución:** ad hoc para esta ocurrencia — se subió manualmente al ticket un archivo con las devoluciones faltantes incluidas (2026-07-15, dos semanas después del reporte original). **No hay confirmación de que el fix de raíz haya salido a producción** — registrado como gap en `../../../2_areas/gaps_y_preguntas.md`.

> Fuente: Mail "Archivo de Liquidaciones -> A102BOTONLIQ260626.626 -> No incluyeron Devoluciones" — federico@coto.com.ar / pagomes@bind.com.ar / mvila@bind.com.ar (2026-07-01 a 2026-07-15).

**Cambio de formato (AD V70.3, julio 2026) — Botón LCK, headers y encoding:**
- El archivo de rendiciones (Botón LCK, ticket 2171 para Coto) pasa a diferenciar explícitamente las **devoluciones parciales**, que antes no salían discriminadas del resto — impacta a todos los clientes que consumen el archivo de rendiciones, no solo a Coto.
- Cambio técnico transversal al mismo archivo: headers de **Pascal Case → Snake Case** y encoding a **UTF-8 con BOM**.
- Despliegue planeado para el martes (no lunes, para evitar arrastrar un fin de semana sin observar el comportamiento) — comunicado a clientes pendiente, ver `tareas_producto.md` T-024.

**Ejecución del despliegue (2026-07-30) — pruebas finales y hallazgos:**

> Fuente: reunión "Análisis de riesgos - AD 70.3" (2026-07-30), minuta Gemini.

Tras el cambio de formato descripto arriba (y la baja parcial de alcance de julio, ver informe semanal abajo — solo DAD-1791/timeout pasó a v71, el resto del alcance de Botón LCK/rendiciones de Coto siguió como AD 70.3), el pase a producción finalmente se ejecutó el **2026-07-30 a las 16:00hs**, tras dos semanas de reprogramaciones. Cinco tickets en el alcance final:

- 🟢 Verde, sin cambio funcional: formato del archivo Excel de liquidaciones (headers con guiones/mayúsculas, encoding UTF-8).
- 🟢 Verde, con cambio funcional: Botón Link no debe mostrar registro de devolución cuando una transacción se devuelve en su totalidad el mismo día en que nació.
- 🟢 Verde, sin cambio funcional: redondeo del CFT (Costo Financiero Total) al final del cálculo en vez de sumar decimales individuales, para evitar arrastre de error de redondeo en liquidaciones con muchas transacciones.
- 🟡 Amarillo (ticket interno 855, réplica de un ticket de PMC): comercios sin certificado propio interrumpían la generación de certificados de IVA/ingresos brutos para el resto del lote — se agregó una validación para omitir ese comercio puntual y seguir con el resto sin cortar el proceso. Riesgo identificado como el de mayor probabilidad de falla (depende del cierre del proceso diario de PMC, ~16hs).
- 🟡 Amarillo, con cambio funcional (Coto): las devoluciones parciales no se informaban en el archivo Botón LCK — se agrega el detalle con ID de transacción `003` para que Coto pueda conciliar.
- **Excepción conocida, aceptada explícitamente por Pablo Gomes para no bloquear el pase:** cuando una transacción con tarjeta tiene **dos devoluciones parciales**, la segunda se informa con el detalle `002` en vez de `003` (y se informa como si fuera el total) — caso de baja frecuencia, queda para un fix posterior sin fecha comprometida.
- **Riesgo operativo señalado por el propio equipo de Fintexa (Andrea Orsini):** casi todas las pruebas de esta versión las hizo una sola persona de su lado, sin segunda revisión — riesgo de cobertura de testing en un cambio complejo.

**Informe semanal Adquirencia (13-17 julio 2026) — versión 70.3 cancelada, ticket crítico DAD-1791 y hotfix de timeout:**

> Fuente: Mail "Informe Semanal Adquirencia" — Melisa Belpassi (Fintexa, PM), 2026-07-17.

- **DAD-1791 (crítico de soporte)** — "[SOPORTE] RXT PROD - VARIAS ENT. - Operaciones no figuran en BD Transacciones (AD-588)": se trabajó en la versión 70.3 para incluirlo, pero **el deploy de 70.3 fue cancelado por Bind** — sus tickets, incluido DAD-1791, pasaron a la versión 71 (sin fecha de salida definida a la fecha).
- **Mitigación propuesta mientras tanto:** subir el timeout de Financial hacia el sistema de pagos externo de **500ms a 15s**, para bajar la cantidad de transacciones que no llegan a insertarse. Cambio de config en producción + reinicio secuencial de pods (servicio con 9 réplicas, sin caída de servicio), sin redeploy ni cambio de código — calificado de bajo riesgo por Fintexa, con mecanismo de contingencia para transferencias en curso durante el reinicio. Propuesta llevada también al grupo de Coordinación de versiones. **Ejecución confirmada (reunión "Análisis COBRO", 2026-07-20):** Melisa Belpassi coordina el reinicio del pipeline con Infraestructura (~30 min, fuera de horario laboral, sin pérdida de transaccionalidad esperada).
- **Hotfix DAD-2171 (Botón LCK/BOTONLIQ — ver más abajo) reprogramado:** iba a pasar el jueves 16/07 a las 15hs; se envió toda la documentación el miércoles, pero ese mismo día se decidió suspenderlo y reprogramarlo para el martes siguiente. **Seguimiento (reunión "Análisis COBRO", 2026-07-20):** desarrollo y pruebas de conciliación/visualización (QR vs. débito y transferencias) seguían con confusiones sobre la definición original del ticket — se sumó a Fintexa a los canales de QA para validar si las pruebas corren correctamente, con prioridad para el lanzamiento planeado para el día siguiente (2026-07-21).
- **DAD-1884 validado en producción:** el fix de "Procesos a cambiar en CVU Collect" (desplegado en 70.1 el 24/06) fue validado esta semana — Franco Giménez creó un nuevo lote de CVU para la entidad A161 y se confirmó comportamiento esperado en producción.

**Bug detectado (no resuelto, 2026-07-16) — transacciones con split después de las 17:00hs se acreditan recién al día siguiente:** el débito se ejecuta correctamente en el horario esperado, pero el crédito de la pata split queda pendiente y el banco/Coelsa lo acredita recién al día siguiente. No es una falla del split en sí (que sí se ejecuta), sino de la acreditación posterior de esa pata. Ver `tareas_producto.md` T-023.

> Fuente: reunión "Análisis de Riesgos - AD V 70.3" (2026-07-16), minuta Gemini.

**Informe semanal Adquirencia (20-24 julio 2026) — timeout confirmado, versión 71 acotada, caso GST:**

> Fuente: Mail "RE: Informe Semanal Adquirencia" — Melisa Belpassi (Fintexa, PM), 2026-07-24.

- **Mitigación de timeout Financial (DAD-1791) confirmada en producción:** desde que se aplicó el cambio de config el miércoles 22/07, Fintexa monitoreó y **no volvió a ver transacciones que no se inserten** — cierra el loop del hotfix descripto arriba.
- **Nueva versión 71 acotada, sale jueves 30/07:** al no poder desplegarse en los primeros 10 días del mes y ser la versión 71 completa demasiado extensa para adelantarla, por pedido de Matías Alzogaray se armó una versión acotada con los tickets ya listos para entrega (el resto sigue en pruebas).
- **Caso productivo cliente GST (ecosistema cerrado) — plazo de liquidación QR mal configurado:** el plazo de liquidación de las operaciones QR estaba en 1 en vez de 0. Caso ya cerrado; a partir de este hallazgo Fintexa empezó a revisar convenios y plazos de liquidación de otros clientes para armar una propuesta de mejora general.
- **DAD-2171 (Botón LCK/BOTONLIQ):** Fintexa adjuntó documento de análisis sobre la demora en la salida a producción del hotfix (no leído en esta corrida).

**Reactivación urgente del ticket 2171 (Coto) — 2026-08-03:**

> Fuente: reunión "Análisis COBRO" (2026-08-03), minuta Gemini.

El ticket 2171 (Botón LCK/rendiciones para Coto, ver arriba) — que Pablo Gomes había postergado previamente — vuelve a agenda con urgencia por pedido explícito del cliente. Persisten inconsistencias en las fechas de liquidación/proceso/negocio (especialmente en contracargos, donde las fechas se sobrescriben incorrectamente), que chocan con un ticket más amplio de mejoras en PDF/Excel ya en curso. Nicolás Colón se reúne con Euge (Coto) y Matías Alzogaray para decidir si se avanza con la solución acotada actual o se amplía el alcance — el equipo reconoce que una ampliación significativa no sería viable para el despliegue del día. Ver `tareas_producto.md` T-074.

**Informe semanal Adquirencia (27-31 julio 2026) — caso Tienda Nube, DAD-2171 pausado por inconsistencia, deploy V71 postergado:**

> Fuente: Mail "RE: Informe Semanal Adquirencia" — Melisa Belpassi (Fintexa, PM), 2026-07-31.

- **Caso Tienda Nube — operaciones no figuraban en BD:** la consulta `GetComercioConvenio()` se degradaba con la concurrencia que Tienda Nube genera todos los días a las 6am contra un único comercio. Paliativo aplicado: índice sugerido sobre la tabla `COMERCIO_CONV` (resolvió parcialmente) + escalado del recurso de la base compartida de **20 a 50 DTU** — el pico del 31/07 06hs se procesó sin excepciones ni degradación. Recomendación de fondo (pendiente, a la espera del OK de Nicolás Colón): incorporar **cache a nivel de API** para esta consulta en vez de depender de escalar recursos — feedback interno de Emma Vignoles: "hay que dejar de hacer todo por fuerza bruta, la cuenta la paga Bind y no tenemos billetera".
- **DAD-2171 (Botón LCK/BOTONLIQ, ver más arriba) completado pero pausado por inconsistencia recién detectada:** el desarrollo ya cerrado solo cubría `BOTONLIQ` (alcance acotado a pedido de la urgencia de Coto). Al validar fechas/formas de liquidación con Eugenia Vila se detectó que **los archivos generados por el sistema no coinciden entre sí** — hay un ticket más amplio, **DAD-2209**, que pedía corregir todos los archivos de rendición (no solo BOTONLIQ), y quedó fuera del alcance urgente. El pasaje de rendiciones a producción quedó frenado hasta que se decida el alcance real. Emma Vignoles: "mal organizado el requerimiento, mal el análisis, y peor las demoras — Coto lleva 3 semanas de atraso, al menos". Gap registrado en `../../../2_areas/gaps_y_preguntas.md`.
- **Deploy de la versión 71 postergado a lunes:** estaba previsto para el jueves 30/07, pero se corrió al lunes 03/08 para no arriesgar la demo de Coca-Cola Andina en producción del 31/07 (ver `1_proyectos/proyecto-coca-cola-andina/proyecto.md`). Errores ya reportados en los últimos tickets entregados fueron solucionados y puestos a disposición de QA externo.
- **AD-839 — Impuestos QRI no debitados (Wallet), ticket de desarrollo DAD-2235 en progreso**, a la espera de definir en qué versión se incluye. Emma Vignoles plantea, sin resolver, una pregunta funcional de fondo: si el lote de débito de impuestos hoy solo soporta una única entidad (falta de soporte multientidad) — gap registrado en `../../../2_areas/gaps_y_preguntas.md`.

**Decisión — botones de descarga separados (CSV/Excel) en vez de reemplazar el formato, y rollback de AD-1381 — 2026-08-03:**

> Fuente: reuniones "Análisis COBRO" y "AD 71 - Reunión de Pre-despliegue" (2026-08-03), minutas Gemini.

En el Go/No-Go de la versión AD 71 del mismo día (release general de Adquirencia, no específico de este PRD), el equipo decidió revertir en `main` el ticket **AD-1381** — que cambiaba el formato de exportación de transacciones de CSV a Excel — porque afecta a los clientes que automatizan su conciliación sobre el formato CSV previo; no se les puede migrar el formato sin aviso. En paralelo, en "Análisis COBRO", el equipo llegó a una salida equivalente por otro camino: en vez de reemplazar el formato, ofrecer **botones separados de descarga estándar (CSV) y descarga Excel**, dejando que cada cliente elija — el equipo acordó definir rápido esta estrategia para evaluar si entra en la próxima versión. Criterio acordado para futuros cambios de formato de exportación: ofrecer ambas opciones y avisar a clientes con al menos 2 semanas de anticipación.

**Informe semanal Adquirencia (03-07 agosto 2026) — DAD-2171 en producción (v71.1), incidente AD-863, homologación GP urgente:**

> Fuente: Mail "RE: Informe Semanal Adquirencia" — Melisa Belpassi (Fintexa, PM), 2026-08-07.

- **DAD-2171 (Botón LCK/BOTONLIQ) sale a producción — versión 71.1, jueves 06/08.** Cierra el "pausado" de la entrada anterior: se agregó la funcionalidad de devoluciones parciales al archivo BOTONLIQ (ausente hasta ahora) y se resolvieron las incongruencias detectadas la semana previa — idempotencia del archivo según hora de corrida, transacciones diferidas creadas de noche que no se informaban, devoluciones totales de QR no registradas, devoluciones parciales duplicadas/mal tipificadas, y el cálculo del plazo de liquidación en fines de semana. **Sigue en trabajo** lo detectado durante el desarrollo del ticket — no está 100% cerrado pese al deploy. El ticket más amplio DAD-2209 (corregir todos los archivos de rendición, no solo BOTONLIQ) sigue sin alcance confirmado. Ver `tareas_producto.md` T-018/T-074 y ficha de cliente COTO.
- **Versión 71 a producción sin incidentes (lunes 03/08).**
- 🚨 **Incidente AD-863 (06/08, ~1 hora, impacto alto) — pérdida de habilitación de POS con Global Processing en 5 entidades productivas.** Causa raíz: un intento de eliminar una regla de pago sobre la entidad de pruebas `DemoBindPsp` (ticket AD-862) afectó también a 5 entidades productivas, por un defecto en el endpoint de eliminación de reglas que no filtraba correctamente por entidad — se perdió la Regla N.º 3 (habilitación del procesador GP) y varios comercios no podían operar con terminales POS. Se restauró manualmente la regla en cada entidad afectada; servicio normalizado a las 10:15hs. Acción correctiva: corregir el filtro del endpoint para que la eliminación afecte solo a la entidad seleccionada + agregar casos de prueba sobre modificaciones de reglas críticas.
- ⚙️ **Versión 71.2 — QR masivo para Provincia NET, en armado.** Provincia NET pidió pruebas en producción con generación masiva de QRs asociados a deudas para la semana del 10/08 (ver `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md`). Requiere pasar a producción la **API de Deuda**, que trae cambios de contrato en campos de respuesta (`montoPagado`, `montoPendiente`, `MontoProximoVencimiento`, `MontoTotal`) y en `DevolucionDeuda` — Fintexa pidió reunión de impacto para alinear la comunicación a clientes antes del pase.
- 🔧 **Homologación urgente con Global Processing — deadline 13/08, en riesgo.** GP notificó 3 cambios de producción obligatorios antes del 13/08: v2.7 (URLs de alta/actualización de subcomercios), v2.8 (URL de autenticación) y v2.9 (validaciones sobre URL de comercios) — más un bug nuevo detectado (creación de comercio falla si la fecha de nacimiento del titular se envía en null). Fintexa reporta **varias incidencias abiertas del lado de GP que ponen en riesgo el plazo**: en la 2.8 GP no especificó cuál URL cambiar, avisaron que tras implementar hasta 2.9 va a hacer falta volver a dar de alta algunos comercios, y aparecieron errores 05 de pago al dar de alta comercios nuevos en STG. Se está tratando directamente con Alan Martínez y Gonzalo Rivera (Bind). Ver `tareas_producto.md` (nueva tarea 🔴, deadline 13/08) — no confundir con el frente ya trackeado en T-082 (URL de comercios electrónicos e-commerce/Edits 26-42, alcance distinto: ese ya tiene ticket `AD-1510` cargado y análisis cerrado del lado de Bind).
- 🗒️ **Versión 72 en armado**, fecha prevista 17/08 (a confirmar).

---
*Ver también: [devoluciones_y_contracargos.md](devoluciones_y_contracargos.md) para la documentación técnica general del webhook de contracargo/devolución que este historial estabiliza sobre el caso COTO.*
*Última actualización: 2026-08-27 — Archivo nuevo, extraído desde `devoluciones_y_contracargos.md` (antes §1.1) por umbral de tamaño de archivo. Contenido sin cambios de fondo.*
