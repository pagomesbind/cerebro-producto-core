# Incidentes de Plataforma y Capacidad (Julio-Agosto 2026)

> Consolidado desde `detalle_productos/wallet/otros_manuales.md §10, §11, §11.1, §11.2, §12, §13` en la reestructuración PARA en cascada (2026-08-12) — es infraestructura/capacidad transversal (seguimiento 100% de Engineering/Infraestructura/Fintexa, ningún próximo paso recae en Producto en ninguno de estos casos), no conocimiento de producto Wallet. Es un hilo continuo de reuniones semanales "Repaso Semanal líderes" sobre el mismo tema de fondo: sobrecarga de infraestructura por clientes de alto volumen.

## 1. Incidente Wallet Bean Service — pérdida de mensajes por reinicio de pods (2026-07-14)

> Fuente: Reunión "Reunión del 14 jul 2026 a las 19:31 GMT-03:00" (minuta Gemini).

- **Síntoma:** el "Wallet Bean Service" (microservicio que publica eventos internos de Wallet, incluye el consumer de "Bin") venía reiniciando pods de forma inesperada, con pérdida de mensajes en tránsito. Causa: un pod entra en estado de caché/crash, se reinicia, y **no puede recuperar los mensajes que tenía en memoria**. El esquema de reintento actual (2 intentos cada 10 segundos) resulta insuficiente.
- **Decisión — migración a MassTransit:** en vez de que el mismo pod reintente y retenga el mensaje en memoria, MassTransit devuelve el mensaje a la cola ante un fallo, permitiendo que **otro pod lo tome**. La mayoría de los consumers "críticos" de Wallet ya habían migrado hace meses; este incidente destapó que el Bin del Wallet Bean Service había quedado pendiente.
- **Plan de despliegue:** despliegue separado el jueves por la mañana (no mezclado con el despliegue general de productos), aprovechado para mejorar la lógica de reintento.
- **Pospuesto:** actualización de Control Plane a la última versión estable — descartado hacerlo en la misma semana por riesgo de reinicio general.
- **Hallazgos sin resolver (seguimiento técnico):** discrepancia del tag de State Monitor entre `main` y `dev`; errores recurrentes en `Delete CBU` (sospecha de llamador incorrecto desde el microservicio de Cobros); errores `TX019` en `Get Transfer` atribuidos tentativamente a API Bank.

## 2. Sobrecarga de infraestructura por tráfico de clientes de alto volumen (2026-07-14)

> Fuente: Reunión "Repaso Semanal líderes" (minuta Gemini).

- **Global 66 y Credicuotas identificados como los mayores generadores de carga** sobre la base de datos compartida: Global 66 produce ráfagas de más de **9.000 comprobantes/minuto**; Credicuotas realiza consultas inusuales de madrugada. Próximos pasos: pedirle a Global 66 distribuir el envío en el tiempo, calcular rate limits razonables, investigar qué tipo de comprobante genera cada cliente.
- **700 transferencias BCF sin insertar** (madrugada 2026-07-14): sin caída confirmada del lado del proxy de Ingres — a investigar con la entidad origen (Happy Bank).
- **Mantenimiento de bases de datos pendiente de agendar:** requiere ventana formal de ~3hs de downtime.
- **Deshabilitado el agente de un namespace específico de Ingres** (recomendación de Microsoft) para mitigar timeouts de conexiones entrantes.
- **Propuesta de cambio de política de staging:** ventana operativa diaria de despliegue hasta las 11:00 AM en vez del congelamiento actual de lunes/martes completos.
- **Re-crear CVU dado de baja** (WS-772): `POST /CVU` sobre una cuenta con CVU dado de baja ahora lo **rehabilita** en vez de fallar.

## 3. INF-1392 — causa raíz del timeout de inserción de transferencias (2026-07-21/22)

> Fuente: Reunión "INF-1392 / Análisis de riesgos" (minuta Gemini). Continuación técnica de §2.

- **Causa raíz:** el microservicio que inserta transacciones en la base transaccional (CBU Colet y reporte) tenía el **timeout mal configurado en milisegundos en vez de segundos** — un aumento previo del valor no tuvo efecto real.
- **Fix en dos partes:** (1) mitigación inmediata sin nueva imagen, solo reinicio del microservicio; (2) segunda parte requiere despliegue de código.
- **Sin plan de rollback formal** porque no se despliega imagen nueva — ante falla, se revierte la variable de entorno.
- **Riesgo amarillo:** existe mecanismo de recuperación manual ya usado en el incidente de Ingres previo (§2) para recomponer transferencias no insertadas.
- **Postergado a la mañana del 2026-07-22** por conflicto de agenda con un despliegue de Ardid. Afecta directamente a clientes de **CBU Colet** y al sistema **Botón Simple 2.0**.

## 4. Decisiones de capacidad — rate limiting, migración de Ardid y API Buffer (2026-07-28)

> Fuente: Reunión "Repaso Semanal líderes" (minuta Gemini). Continuación de §2 — un nuevo cliente de alto volumen (Tienda Nube) y decisiones más concretas.

- **Nuevo generador de carga — Tienda Nube:** inserta transacciones en COEC todos los días a las 6:00 AM; espera escalar a 5.000 tx diarias. Tercer cliente de alto volumen sobre la infraestructura compartida (junto a Global 66/Credicuotas).
- **Rate limiting — decisión concreta:** tope de **500 transacciones por minuto por entidad**.
- **API Buffer para Wallet — pendiente de producción:** 2 versiones completadas en staging sin pasar a producción; requiere reconfigurar Ingress.
- **Migración de infraestructura de Ardid:** caídas recurrentes por agotamiento de recursos en VMs obsoletas — migración a SKU más nuevo de la **serie D**.
- **Gap de observabilidad (sin resolver):** health checks internos de Kubernetes existen, pero no hay tablero centralizado ni alertas proactivas de negocio para Operaciones.
- **🔴 Riesgo de seguridad — Ardid no es multi-empresa:** Fintexa advirtió que Ardid no aísla datos entre clientes — organizaciones como **Coto y BIN podrían ver operaciones ajenas** entre sí. Pendiente del lado de Pentass, sin fecha confirmada. Ver gap registrado en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

## 5. Migración a Auto External v2 (W 71.4, 2026-07-29)

> Fuente: Reunión "FIX - Emisión W 71.4" (minuta Gemini). Análisis de riesgo del despliegue del 2026-07-30 7:00am. **Nota de alcance:** Auto External v2 es una iniciativa de infraestructura del CoE, no un desarrollo de Producto — se documenta acá solo por el riesgo operativo que implica para Wallet (dólar CCL, cuentas remuneradas).

- **Contexto:** Auto External v2 ya corre en producción para servicios nuevos (totalizadores, Mastercard). Migración en tres etapas; la primera mueve tres servicios no críticos: **Pix, Lirium y Poisot**.
- **Riesgo catalogado en rojo:** un fallo podría afectar el **dólar (CCL) y las cuentas remuneradas**, ninguno de estos tres flujos se prueba hoy en producción directamente.
- **Ticket 1693 (riesgo rojo, sin poder probar en staging):** fix de monto en dólares de compras CCL cerradas en el día.
- **Rollback:** redesplegar la versión anterior del microservicio afectado, ~10 minutos.

## 6. Repaso Semanal líderes (2026-08-04) — rate limit Ripsa, ventana CBU Collect, purga de BD

> Fuente: Reunión "Repaso Semanal líderes" (minuta Gemini). Continuación de §2 y §5.

- **Dos incidentes de "Rate Limit" separados en dos tickets:** (1) **Ripsa** — errores `429` en API de notificaciones, distinto de Tienda Nube (§4); (2) **CBU Collect** — problema de API distinto, requiere ventana de mantenimiento propia. Venían mezclados bajo `INF-14-1072`.
- **Purga diaria de bases de datos — Webhook Sender y Botón Simple:** proceso nocturno (4:00-5:00am) que elimina registros de 2023/2024 para mantener retención de **3 meses**.
- **Escalabilidad de Ardid:** estable tras migración de zona/reajuste de núcleos (§4). El equipo prioriza correr pruebas de estrés con métricas reales antes de escalar más recursos.
- **Migración Auto External v2 — avance de fases (continúa §5):** fase 2 resuelve problemas detectados en la fase 1.
- **Esquema desacoplado de Personal Pay por finalizar; se prioriza el mismo esquema para "BM PCP"** — ver [modelo_acoplado_vs_desacoplado.md](modelo_acoplado_vs_desacoplado.md) para el detalle completo de esta migración.

## 7. Incidentes de seguridad con Poicenot — parametrización de Egress pendiente (2026-08-11/13)

> Fuente: Mail "Prueba de Egress en STG" — daniel.zalazar@fintexa.tech (2026-08-11/12); minuta "Repaso Semanal líderes" (2026-08-11).

- **Síntoma:** se detectaron incidentes de seguridad vinculados a la conexión del servicio de **Egress** con **Poicenot** (integración externa, ver `integraciones_externas.md`) — la minuta de líderes del 11/08 lo cataloga como "Gestión de Vulnerabilidades", prioridad Alta.
- **Fix propuesto:** una parametrización en el servicio de Egress. El cambio es un despliegue que **afecta a todas las conexiones que salen por Egress, no solo a Poicenot** — requiere ventana de prueba dedicada en STG.
- **Ventana de prueba agendada y suspendida:** programada para el jueves 13/08 de 8:00 a 9:00hs; el mismo 12/08 Fintexa avisó que la suspendía — el equipo de SRE tenía en paralelo un despliegue de Aceptador y el desescalado de nodos de AKS (ver [`mantenimiento_y_capacidad_aks.md`](mantenimiento_y_capacidad_aks.md)) y no tenía capacidad para atender las tres cosas. Sin fecha nueva confirmada.
- **Contingencia mientras tanto:** control manual — todas las mañanas se verifica a mano si hay errores de conexión con Poicenot y, de haberlos, se reinicia el servicio de Egress.
- **Nota de alcance:** Poicenot es uno de los 3 servicios no críticos (junto a Pix y Lirium) ya migrados a Auto External v2 (ver §5) — este incidente es de seguridad/conectividad, no de la migración en sí.

## 8. Repaso Semanal líderes (2026-08-25) — despliegues Wallet 7.2/AuthExternal v2.0 cerrados, decisión pendiente Zero Downtime vs. Sentinela

> Fuente: mail "Repaso Semanal líderes: Mar, 25 de ago de 2026" (minuta directa de Matías Alzogaray por mail, no Gemini), 2026-08-25 (threadId `1a03a1edad15f8f1`). Continuación de §2, §4 y §6.

**Despliegues técnicos recientes confirmados como exitosos y sin reportes de problemas:**
- Versión **7.2 de Wallet** completada y desplegada.
- Migración de **AuthExternal a la versión 2.0** finalizada de forma limpia, sin reportes de incidentes — corrobora, desde una fuente distinta, el cierre de la migración a Auto External v2 ya en curso desde §5-§6.
- Pruebas en desarrollo de **Zero Downtime** (escalar/desescalar microservicios sin pérdida de mensajes) superadas con éxito.

**Decisión de arquitectura pendiente (Parking Lot, sin resolver todavía):** queda como decisión técnica central priorizar entre **Zero Downtime** (aplicarlo a microservicios críticos) vs. **Sentinela** (para resolver problemas recientes con comprobantes) — postergada a la reunión de Arquitectura del jueves siguiente (2026-08-27), donde también se iba a ejecutar el análisis post-mortem de un incidente ocurrido el viernes anterior (2026-08-21). El Cerebro no tiene hoy detalle de ese incidente ni de a qué "problemas recientes con comprobantes" se refiere Sentinela — queda como punto a confirmar en el próximo barrido si hay minuta de esa reunión de Arquitectura.

**Prueba de carga de Wallet 7.2 (contexto ampliado, dueño de la ejecución: Juan Pablo Carubelli):** motivada por el aumento esperado de generación de comprobantes por la salida a producción de clientes de alto volumen — **Arcos Dorados** (septiembre 2026) y la futura integración de QR en los slots del **Hipódromo de Palermo**. Postergada dos veces (cierre de la versión 72, luego prioridad del propio despliegue), queda activa para ejecutarse la semana del 25/08 con métricas reales de producción (no cargas genéricas), con foco en el comportamiento del sistema ante creación simultánea y masiva de comprobantes/vouchers.

**Otra decisión operativa de la misma minuta:** ventana de mantenimiento nocturna (2:00-6:00) a coordinar con el DBA para eliminar comprobantes/operaciones pesadas — corrobora, desde otra fuente, la depuración periódica de bases ya documentada en [`mantenimiento_y_capacidad_aks.md`](mantenimiento_y_capacidad_aks.md).

## Ver también
- [mantenimiento_y_capacidad_aks.md](mantenimiento_y_capacidad_aks.md) — plan de mantenimiento AKS de agosto 2026, relacionado con la capacidad de infraestructura discutida acá; §8 corrobora la ventana de purga de bases documentada ahí.
- [modelo_acoplado_vs_desacoplado.md](modelo_acoplado_vs_desacoplado.md) — migración de Personal Pay y riesgos del modelo desacoplado.
- [detalle_productos/wallet/historial_confiabilidad_transferencias_y_comprobantes.md](../detalle_productos/wallet/historial_confiabilidad_transferencias_y_comprobantes.md) — historial de bugs de confiabilidad relacionado.

---
*Última actualización: 2026-08-27 — `/context_merge`: nuevo §8, Repaso Semanal líderes (25/08) — cierre de despliegues Wallet 7.2/AuthExternal v2.0, pruebas de Zero Downtime superadas, decisión de arquitectura pendiente (Zero Downtime vs. Sentinela) y contexto de la prueba de carga de Wallet 7.2 (Arcos Dorados, Hipódromo de Palermo).*
*Última actualización anterior: 2026-08-14 — `/sync_mails`: nuevo §7, incidente de seguridad Egress/Poicenot (parametrización pendiente, ventana de prueba suspendida por conflicto de capacidad con el desescalado de AKS).*
*Última actualización anterior: 2026-08-12 — Consolidado desde `detalle_productos/wallet/otros_manuales.md §10-§13` (reestructuración PARA en cascada). Contenido sin cambios de fondo.*
