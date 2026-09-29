# Ardid — Despliegues y Operación (lado Bind PSP)

> Estado: en producción — protocolo confirmado por el equipo técnico en un caso real, no documentación teórica.
>
> Fuente: reunión "Análisis de Riesgo - Fix de cambios de estados de las tarjetas" (2026-08-28, docId `1QLWJd6WyUAVTdul2c8tkZbue7eL84ddDZlZs-pJDEOo`), sobre el ticket AD-1374 (fix "actualización estado de pagos, corrección BIN" sobre la versión 1182 de Ardid, afecta los microservicios `transaction API` y `Transaction Service`).

## 1. Protocolo de rollback estándar de un despliegue

Confirmado por el equipo (Matías Alzogaray, Osmel Mata/Fintexa, Mateo Capitanich/Fintexa) ante el ticket AD-1374: **no alcanza con restaurar la imagen Docker anterior** (`docker-compose up -d --force-recreate --no-deps <servicio>` a partir del backup `.tar`) si el despliegue también modificó la base de datos. En ese caso, el rollback requiere **dos pasos**:

1. Restaurar la imagen Docker anterior del/de los microservicio(s) afectado(s).
2. Restaurar el backup de base de datos (SQL Server + Mongo) tomado inmediatamente antes del despliegue — se reserva una ventana de ~30 min previa al despliegue para tomar ese backup.

Es la primera vez que este protocolo de dos pasos (imagen + DB) queda documentado explícitamente para Ardid — antes solo se hablaba de restaurar la imagen. Aplica a cualquier despliegue de Ardid que incluya un script de corrección de datos (no solo cambios de código puro).

## 2. Riesgo de rechazos al activar reglas antifraude que no se estaban aplicando — caso Coto

El fix de AD-1374 activa reglas antifraude que, por un bug previo, no se estaban aplicando. Afecta especialmente a **Coto**, que consume las APIs de Ardid sin bypass — a diferencia de Botón Simple/Wallet, que sí pueden operar en modo bypass durante la ventana de mantenimiento. El equipo clasificó el riesgo como **🟡 amarillo** (cambio funcional, no solo técnico): activar las reglas correctamente puede generar un salto de rechazos de transacciones y reclamos de clientes que antes pasaban sin control.

**Mitigación acordada:** habilitar las reglas de forma gradual en vez de todas de una vez, y monitorear post-implementación la relación entre respuestas 200 y rechazos contra el volumen histórico.

**Deploy:** staging lunes 31/08 9hs, producción martes 01/09 en ventana 6:30-8:00 (media hora previa reservada para el backup de bases). Sin action item de Producto — el seguimiento queda en el equipo técnico (Hernán Clarich monitorea rechazos, Rocío Revelli hace la revisión post-implementación en Ardid).

## 3. Seguimiento post-despliegue (01/09) — solución temporal en Mongo, SQL Server sin resolver

> Estado: en producción, con parche manual sostenido — no es la solución de fondo.

> Fuente: mail "RE: Análisis de Riesgo - Fix de cambios de estados de las tarjetas" — Osmel Mata (Fintexa, SRE Sr, osmel.mata@fintexa.tech), 2026-09-10, a pedido de Matías Alzogaray.

El despliegue del 01/09 (§2) se aplicó **sin inconvenientes**: la vista de Pagos en la consola web quedó corregida y se regularizaron los **250.000 registros** que estaban trabados en estado `PENDING`.

- Esa regularización fue una **solución temporal**: implica seguir corriendo **manualmente un script sobre la base de datos MongoDB de Ardid** para ir moviendo esos registros de `PENDING` a `Realized`, hasta que el equipo de desarrollo de Pentass encuentre una solución permanente de fondo.
- Del lado de **SQL Server**, el fix implementado **no parece haber funcionado** como se esperaba; Fintexa sigue trabajando en conjunto con el equipo de soporte de Pentass para normalizarlo.
- Hay indicios (sin confirmación oficial ni documentación todavía) de que se está evaluando pasar Ardid/Akurtech de la versión actual **v1.18.2** a la **v1.19.x**, con la expectativa de que sea más estable.

## 4. Ventana de retención de MongoDB (45 días) — dueño técnico y motivo histórico (2026-09-22)

> Fuente: mail directo de Nicolás Colón a Osmel Mata (SRE, Fintexa/Pentass), 2026-09-22, en el marco del discovery de `ardid_desconocimientos`.

La ventana de retención de transacciones de Ardid en MongoDB (hoy **45 días**) la controla el **proveedor (Pentass/Akurtech)**, no infraestructura propia de Bind PSP — no es un parámetro que Bind pueda cambiar unilateralmente vía su propia infraestructura Azure. Osmel Mata lo confirmó por escrito ante la consulta directa de Nicolás Colón:

> "La gente de Pentass/Akurtech, debido a que en el pasado presentó muchos problemas de rendimiento (al principio se guardaba todo el histórico, luego pasamos a 90, 60 y finalmente 45 días), y luego de varias sugerencias de parte de ellos y pruebas en conjunto, se dejó en 45 días que era donde Ardid funcionaba bien con el histórico en MongoDB (teniendo en cuenta el gran volumen de datos que se almacenan por mes). Es un tema de rendimiento. Si ellos logran resolver ese problema, no veo inconveniente en que se incremente el histórico nuevamente."

Dos hechos duros confirmados para cualquier iniciativa futura que dependa de esta ventana:
1. **La reducción fue progresiva y deliberada**, en tres pasos: histórico completo → 90 días → 60 días → 45 días (valor actual) — ajustada activamente varias veces por el proveedor, con pruebas conjuntas con Bind, específicamente para resolver problemas de rendimiento de Ardid con el volumen de datos mensual.
2. **El proveedor no objeta ampliarla de nuevo, pero lo condiciona explícitamente a resolver antes ese problema de rendimiento.** Cualquier pedido de ampliación (ej. a 120 días, para cubrir contracargos que llegan más tarde que la ventana actual — ver proyecto `ardid_desconocimientos`) debería ir acompañado de una confirmación del proveedor de que el problema que motivó las 3 reducciones anteriores ya está resuelto, o se arriesga a reintroducirlo.

Resuelve (parcialmente) un gap abierto desde 2026-09-11 sobre quién era el dueño técnico del cambio de retención — el PM decidió en su momento no bloquear la estimación de `ardid_desconocimientos` por no tener este dato, así que la resolución llega después de haber avanzado con el diseño y la estimación.

## 5. Pase a staging de Ardid 1.19.x (29/09) — alcance técnico, riesgo amarillo y nuevas reglas de fraude

> Fuente: minuta Gemini de la reunión "Análisis de riesgo - Ardid V 1.19.0" (2026-09-25, 16:01), compartida por malzogaray@bind.com.ar. Participan por Fintexa/Pentass Matías Alzogaray (moderador), Daniel Zalazar, Osmel Mata, Luis y Santiago Fernandez; por Bind PSP Andrea Orsini, Pablo Serra, Gonzalo Rivera, Mariana Nadalin, Nicolás Colón, Pablo Gomes.

**⚠️ Qué versión se despliega — ver gap abierto:** el título de la reunión dice "Ardid V 1.19.0", pero el roadmap ya documentado en [`historico/historial_versiones.md`](historico/historial_versiones.md) decía que se saltaba directo a la 1.19.1 (con el fix UTC 0). No se aclaró en esta reunión si el nombre es solo el del evento o si efectivamente se despliega la 1.19.0 puntual — ver gap consolidado en [`../../../2_areas/gaps_y_preguntas.md`](../../../2_areas/gaps_y_preguntas.md).

**Cronograma de staging (no producción):**
- **Wallet:** lunes 28/09, 9:00–11:00 hs.
- **Ardid 1.19.x:** martes 29/09, 8:00–10:00 hs (separado del de Wallet a pedido de Andrea Orsini, para no pisar las regresiones y no bloquear en paralelo la ventana de pruebas de Nico Pomponio sobre Wallet). Ventana estimada de ~2 horas, incluyendo pruebas de regresión.
- Ambos se comunican a clientes como posible intermitencia en el ambiente de staging (no hay impacto de cliente real, es ambiente de pruebas).
- **Aparte:** un hotfix de producción (sin identificar cuál) se reprograma de hoy (25/09) al **lunes 28/09 a la mañana**, para reducir el impacto en horario de alta transaccionalidad.

**Alcance técnico de la v1.19.x:**
- APIs/microservicios afectados: Transfer API Gateway, SQL Server, MongoDB.
- Se crean 4 índices nuevos en las colecciones `transaction` y `transfer` de MongoDB — posible intermitencia/lentitud temporal en pantallas principales, dashboard, pagos y transferencias mientras se actualizan imágenes Docker y corre el actualizador de base de datos.
- El componente Transfer Service se reinicia por la inyección de una nueva variable de entorno.
- **Nuevas reglas de fraude incorporadas:** ráfagas de pago, IP, geolocalización y dominios reputacionales — con posibles comportamientos anómalos o rechazos temporales mientras entran en vigencia (sin más detalle de mecánica; posible input para ampliar [`blacklist_whitelist_rafagas.md`](blacklist_whitelist_rafagas.md) cuando haya documentación del proveedor). Rocío Revelli arma un set de pruebas específico para validar el impacto de estas reglas nuevas de pagos y comercios — no confirmado si son las mismas "reglas interentidades" que el canon atribuye a la 1.20.
- **Plan de rollback:** scripts de reversión en carpeta `rollbacks`, restauración de copias de respaldo previas de archivos y Docker Compose, y comandos `Drops Index` para deshacer los índices nuevos si hay falla de rendimiento.
- **Lección aprendida citada por Osmel Mata:** en el despliegue anterior de la 1.18.2 en producción, la recreación de índices de MongoDB tardó "varias horas", a diferencia de staging — a tener en cuenta para el futuro pase a producción de la 1.19.x.
- Se realizan backups de SQL y MongoDB al momento del despliegue; monitoreo a cargo del equipo de Fintech + DBA (Juan).
- **API externa:** Luis (Pentass) hace un repaso exhaustivo para confirmar que no hay cambios en los endpoints de la API externa de Ardid usados por Botón Simple/Wallet, y reporta cualquier hallazgo.

**Compatibilidad de integraciones confirmada:** Pablo Serra preguntó explícitamente si había cambios de firma o de endpoints usados por las integraciones de Botón Simple y Wallet. Luis (Pentass) confirmó, tras consultar con la líder de desarrollo (Lorena), que **no hubo cambios en los endpoints consumidos por Ardid** en este ciclo — dato que sostiene la clasificación de riesgo.

**Riesgo asignado:** **amarillo** — por el impacto potencial en el transaccionamiento (no por cambios de integración, que se descartaron).

**Precedente citado (no nuevo, pero relevante acá):** para producción, el impacto se mitiga solicitando la desconexión de Coto durante su ventana de mantenimiento (22:00–08:00) — mismo patrón ya documentado en el caso AD-1374 (ver §2).

**Hotfix de producción pendiente (mención separada, mismo día):** Osmel Mata (Fintexa, SRE) envía por mail la consulta pendiente sobre fecha y horario de un hotfix de producción — posible relación con el parche manual de `PENDING` de §3, no confirmado.

Seguimiento: Andrea Orsini ejecuta las regresiones de Wallet y Ardid tras cada pase (flujos de servicios y botones); Matías Alzogaray distribuye la minuta con el plan de acción post pase a staging.

## Ver también
- [modulo_pagos.md](modulo_pagos.md) — reglas antifraude de pagos con tarjeta que este fix corrige.
- [../../../2_areas/procesos/analisis_de_riesgo_de_despliegue.md](../../../2_areas/procesos/analisis_de_riesgo_de_despliegue.md) — proceso general de análisis de riesgo de despliegue (semáforo, informe), del que este caso es una instancia concreta.

---
*Última actualización: 2026-09-29 — `/context_merge`: nueva §5, pase a staging de Ardid 1.19.x (29/09) — alcance técnico, riesgo amarillo y nuevas reglas de fraude (Pablo Gomes).*
*Última actualización anterior: 2026-09-23 — `/context_merge`: nueva §4, dueño técnico y motivo histórico de la ventana de retención de MongoDB (45 días) — controlada por el proveedor, condicionada a resolver rendimiento (Nicolás Colón).*
*Última actualización anterior: 2026-09-11 — `/context_merge`: nueva sección "Seguimiento post-despliegue (01/09) — solución temporal en Mongo, SQL Server sin resolver" (mail de Osmel Mata, Fintexa, 2026-09-10).*
*Última actualización anterior: 2026-08-31 — `/context_merge`: archivo nuevo, item de `contexto_vivo/` (reunión "Análisis de Riesgo - Fix de cambios de estados de las tarjetas", 2026-08-28).*
