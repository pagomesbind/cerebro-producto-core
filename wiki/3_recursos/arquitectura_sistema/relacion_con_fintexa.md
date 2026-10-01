# Relación con el Proveedor Fintexa — Dotación de Recursos y Gobierno de Arquitectura (COE)

> Reubicado y consolidado desde `arquitectura_sistema/index.md §11` (dotación de recursos) y `§13` (Comité de Arquitectura COE) en la reestructuración PARA en cascada (2026-08-12) — ambos temas son la relación operativa/de gobierno con el proveedor de infraestructura, no arquitectura técnica en sí.

## 1. Dotación de recursos — bajas consecutivas (julio-agosto 2026)

> Fuente: Mail "Cambios recursos FINTEXA - BIND PSP Julio 2026" — agustin.grau@fintexa.tech (2026-07-14).

A partir de julio 2026 quedaron efectivas bajas en el equipo de Fintexa asignado a Bind PSP: Franco Gimenez (Soporte), Rodrigo Lucero (QA), Pablo Martínez (SRE — pasa a quedar solo 1 semana al mes en guardia pasiva de Infra) y Daniel Perez Ojeda (Dev Wallet). Reducción de capacidad de soporte/SRE/QA del proveedor de infraestructura — ver riesgo registrado en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

> Fuente: Mail "Cambios recursos FINTEXA - BIND PSP AGOSTO 2026" — agustin.grau@fintexa.tech (2026-08-04).

A partir de agosto 2026, nuevas bajas: Federico Favia (QA Wallet), Marcelo Natrielo (Dev Adquirencia) y Leonel Zalegas (Dev Mobile POS). Además, modificaciones de rol: Mariela Marin deja de liderar el equipo de QA y pasa a ser QA bajo el scope del PM correspondiente (pierde el rol de lead); Pablo Vydra (Dev Mobile POS) baja su asignación al 50%. Segunda reducción consecutiva de dotación del proveedor en dos meses — reafirma el riesgo de capacidad ya registrado en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

## 2. Comité de Arquitectura COE — informe mensual (corte agosto 2026, vs. julio 2026)

> Fuente julio: Mail "INFORME Mensual Comité de Arquitectura COE" — alejandro.sfrede@fintexa.tech, 2026-08-07. Fuente agosto: mismo hilo, "RE: INFORME Mensual Comité de Arquitectura COE" — Alejandro Sfrede (Fintexa), 2026-09-02. Detalle completo en los adjuntos PDF (`COE-TAREAS-AGO2026.pdf` / `COE-TAREAS-30DIAS-SEP2026.pdf`), no leídos en ninguna de las dos corridas.

Estado consolidado de las iniciativas de arquitectura transversal seguidas por el Comité (referencia interna: tickets `PA-XXX`). El corte de agosto solo llegó completo para las categorías ✅ y 🟢 (el cuerpo plano del mail se cortó antes de 🔵/⚪/🔴) — esas tres categorías quedan con el corte de julio hasta la próxima corrida, **no asumir que no cambiaron**:

- ✅ **Listo / en producción** — corte agosto: **autenticación externa (Wallet y Aceptador) — migración productiva COMPLETA** (en julio: "resta 1 fase"). **Procedimiento de HOTFIX de corrección rápida** — pasa de "listo" a "operativo, con prueba real de punta a punta programada para cerrar la validación". Feature flags siguen disponibles. Notificaciones estabilizadas en Wallet y API buffer ya no se mencionan como ítems propios en el resumen de agosto (posible consolidación del texto, no necesariamente reversión).
- 🟢 **En progreso** — corte agosto: **Zero-Downtime** — roadmap ampliado a **40+ servicios de Wallet** (en julio sin alcance cuantificado). **Red de seguridad de mensajería** — pasa a "ya en ambiente de prueba productivo, validación final" (antes solo "en progreso" sin detalle). Nuevo ítem: **"Cierre del componente anterior de autenticación"**. **Onboarding unificado** — sube de categoría: estaba en julio en 🔵 (ver abajo) y en agosto ya tiene "base en ambiente de prueba" — dato relevante para el foco de Onboarding, aunque no hay todavía un PRD propio de Pablo Gomes que dependa de esto. Resto de ítems en progreso repetidos sin cambio aparente: depuración/retención de datos, protección de datos en registros, control de salidas de red, monitoreo de salud, modernización .NET 10, colas Quorum, programa de eficiencia/gobierno IA, políticas de workers.
- 🔵 **En diseño o definición (corte julio, sin confirmar en agosto):** Onboarding unificado (subió a 🟢 en agosto, ver arriba), rate limit por plan, auditoría de tokens, estrategia de mensajería, optimización de bases de datos, visibilidad de estado, acceso unificado de conciliación, catálogo de APIs, reporte mensual.
- ⚪ **Backlog (corte julio, sin confirmar en agosto):** programa de pruebas de seguridad + desarrollo seguro, mTLS, particionamiento, Hangfire, capacidad AKS, caché Redis, cierre de malla de servicios, prevención de fraude/compliance.
- 🔴 **Bloqueado (corte julio, sin confirmar en agosto):** evaluación de motor de base de datos (PostgreSQL).

## 3. Modelo de evolución del ecosistema — producto único, repositorio único, release periódico único

> Fuente: mail "Fw: Evolución del ecosistema" (Agustín Grau, CTO Fintexa, 2026-09-16, reenviado 2026-09-18).

Agustín Grau comunicó formalmente — acordado con Emma Vignoles — cómo Fintexa encara la incorporación de nuevos clientes al ecosistema que hoy usa Bind PSP (cada nuevo cliente trae productos/módulos nuevos, ajustes sobre lo existente e integraciones con terceros, ej. conexión con Payway por ISO para e-commerce):

- **Decisión de fondo:** sostener **un único producto, un único repositorio y un release periódico único**, instalado en distintos ambientes según el cliente — no forks ni ramas separadas por cliente.
- Fintexa comunica todo lo que vaya desarrollando, aun cuando no impacte directamente en la operación de Bind PSP.
- Todo lo nuevo se diseña **modular, separable por producto y por feature**, para poder habilitarse o no por cliente.
- **Retrocompatibilidad es prioridad explícita:** lo que hoy funciona en Bind PSP tiene que seguir funcionando igual.
- **Bind PSP no prueba, en una primera instancia, los productos/features nuevos que no usa** — sí corre una regresión sobre su propio alcance para validar que nada se vio afectado.
- Si más adelante Bind PSP (u otro cliente) necesita activar un producto/feature ya existente para otro cliente, se conversa en ese momento — no hay activación automática.

Esta decisión encuadra formalmente por qué el ecosistema (Ardid/Akurtech, Wallet, Adquirencia sobre la misma base) evoluciona con roadmaps de release que incluyen features no usadas por Bind — ver por ejemplo el roadmap de Akurtech 1.19/1.19.1/1.20 en [`detalle_productos/ardid/historico/historial_versiones.md`](../detalle_productos/ardid/historico/historial_versiones.md) — es la política general detrás de ese patrón, no un caso aislado.

## 3bis. Informe mensual COE — septiembre 2026 (vs. agosto) y detalle de la reunión "Repaso Semanal líderes" del mismo período

> Fuente informe: mail "RE: INFORME Mensual Comité de Arquitectura COE" — Alejandro Sfrede (Fintexa), 2026-10-01, mismo hilo histórico `19fdd426c2490389` de julio/agosto ya capturado en §2. Fuente reunión: "Repaso Semanal líderes" (2026-09-29), con Alejandro Sfrede, Melisa Belpassi, Daniel Zalazar, Hernán Clarich (Fintexa).

**Tres frentes de fondo señalados por el informe de septiembre:**

1. **Despliegues sin interrupción de servicio (zero-downtime) pasan a estándar obligatorio** — sus tickets de implementación están en revisión final antes del pasaje a producción. Confirma y formaliza el roadmap que en agosto figuraba como "en progreso, ampliado a 40+ servicios de Wallet" (§2).
2. **Desarrollo de interoperabilidad entre billeteras** (marco regulatorio del Banco Central) avanzó, con una estrategia de despliegue diseñada explícitamente para no arriesgar la operación actual. En el detalle por estado figura como "Interoperabilidad entre billeteras Auth2 (AUTH EXTERNAL para Open Finance)" dentro de 🟢 En desarrollo.
3. **Exposición de seguridad real identificada en un panel administrativo**, con la corrección ya definida y lista para implementarse — coincide con el hallazgo del Admin Centralizador (CVSS 8.7) ya tratado como hotfix (ver [`2_areas/riesgos.md`](../../2_areas/riesgos.md) y [`2_areas/direccion/decisiones.md`](../../2_areas/direccion/decisiones.md) [2026-09-25]); este informe no aporta detalle nuevo sobre ese punto, solo lo confirma a nivel de reporte ejecutivo de arquitectura.

**Detalle completo por estado (septiembre 2026):**
- ✅ Completado: corrección del cuello de botella de performance en Notificaciones por base de datos · sanitización de datos sensibles en registros técnicos · autenticación externa en Wallet.
- 🟢 En desarrollo: interoperabilidad entre billeteras Auth2 (Open Finance) · migración de colas de mensajería · simulación de proveedores externos para pruebas (primer proveedor: GP) · estándar único de registro de eventos (logs) · monitoreo de salud de servicios.
- 🟡 En revisión y aprobación: despliegues sin interrupción de servicio por vertical · notificaciones/webhooks (estabilidad de envío) · estándar de desarrollo seguro.
- 🔵 Listo para iniciar desarrollo: optimización de la base de datos de Deuda · regla de control de cambios de contrato de API · certificación ISO 9001 (ver nota de desalineación en [`cumplimiento_normativo/certificaciones_iso_y_seguridad.md`](../cumplimiento_normativo/certificaciones_iso_y_seguridad.md)) · fix de red (DNS) para dos servicios.

**Certificaciones:** las tres certificaciones en curso (ISO 9001, ISO 27001 y el programa de seguridad exigido por el socio de procesamiento) están en preparación — detalle completo en [`cumplimiento_normativo/certificaciones_iso_y_seguridad.md`](../cumplimiento_normativo/certificaciones_iso_y_seguridad.md) (archivo nuevo, va a esa capa por ser contenido de cumplimiento normativo, no de arquitectura).

**Detalle operativo del zero-downtime y temas adyacentes (reunión "Repaso Semanal líderes", 2026-09-29):**

- **Migración a cero tiempo de inactividad, en 3 etapas:** priorizando primero los microservicios más críticos — **Webhook Sender** es el primero — para evitar pérdida de mensajes durante despliegues continuos. Esquema ya comunicado a los líderes técnicos.
- **Escalado automático de bases de datos:** Daniel Zalazar asume revisar y configurar el escalado/desescalado automático de BD, en conjunto con el equipo de infraestructura y desarrollo — pruebas iniciales sobre microservicios específicos antes de extenderlo al resto del ecosistema, para medir impacto en costos. Queda pendiente ("requiere más debate") la prueba de escalamiento en sí, a cargo de Daniel Zalazar, en conjunto con el despliegue de cero downtime.
- **Ventanas de mantenimiento para depuración de tablas grandes:** las tablas de comprobantes y operaciones están depuradas solo hasta **febrero de 2026** — se necesitan ventanas adicionales. Emma Vignoles objetó que los tiempos actuales (4 horas por cada 2 meses de datos) generan bloqueos con pérdida de transacciones; Gonzalo Rivera sugirió programar las ventanas según los horarios de menor operatoria de **BSF** (decisión acordada: buscar ventana basada en esos horarios). Daniel Zalazar se compromete a revisar optimizaciones con el DBA.
- **Hallazgos operativos menores relacionados (Ardid):** un proceso automático que cambia el estado de transacciones pendientes de validación quedó con registros trabados desde el 28/09 — se ejecuta manualmente hasta resolverse en la próxima versión; también hay una incidencia de tiempo de espera excesivo que afecta la visualización de la pestaña de transferencias, en resolución.

## 4. Desvío de responsabilidad Fintexa↔Penta — performance de Ardid afecta su comercialización a clientes

En la reunión "Weekly - Producto / Operaciones" (2026-09-21), Mariana Nadalin y Pablo Gomes reportaron demoras y fallas en la generación de reportes de Ardid ("tirás un reporte y no trae datos"), y describieron un **desvío de responsabilidad circular entre Fintexa y Penta** (proveedor de infraestructura/hosting de Ardid): "del lado de Fintexa nos dicen que es Penta, Penta nos dice que es Fintexa, y así damos vueltas". Se acordó escalar el reclamo conjuntamente a Fintexa, Hernán Clarich (Arquitectura) y Penta, y evaluar si el problema está relacionado con cómo están paginadas las consultas en las versiones que gestiona Matías Alzogaray.

El riesgo de negocio (Ardid comercializado a Coto y ofrecido a Grupo DESA con esta performance sin resolver) y su actualización del 22/09 — donde Hernán Clarich atribuyó la causa a optimización de consultas de backend, no ya al desvío Fintexa↔Penta — están documentados en [`2_areas/riesgos.md`](../../2_areas/riesgos.md). Esta entrada queda como referencia del lado proveedor/infraestructura; el detalle de impacto comercial y seguimiento vive en el ledger de riesgos.

## Ver también
- [mantenimiento_y_capacidad_aks.md](mantenimiento_y_capacidad_aks.md) — plan de mantenimiento AKS de agosto 2026, ejecutado por el mismo proveedor.
- [calidad_y_cicd.md](calidad_y_cicd.md) — roadmap técnico declarado por el proveedor, contrastar contra el estado real reportado acá por el COE.
- [2_areas/riesgos.md](../../2_areas/riesgos.md) — riesgo de negocio "Performance de Ardid afecta su comercialización a Coto y Grupo DESA".

---
*Última actualización: 2026-10-01 — `/context_merge`: nueva sección "3bis. Informe mensual COE — septiembre 2026" (zero-downtime a estándar obligatorio, interoperabilidad entre billeteras, detalle operativo de 3 etapas de zero-downtime/escalado de BD/ventanas de mantenimiento) (Pablo Gomes).*
*Última actualización anterior: 2026-09-21 — `/context_merge`: nueva sección "Modelo de evolución del ecosistema" (producto único/repo único/release periódico único, retrocompatibilidad como prioridad, comunicado por el CTO de Fintexa).*
*Última actualización anterior: 2026-09-03 — `/context_merge`: §2 actualizado con el corte de agosto 2026 del informe COE (delta vs. julio, categorías ✅/🟢 completas, 🔵/⚪/🔴 pendientes de confirmar).*
*Última actualización anterior: 2026-08-12 — Reubicado y consolidado desde `arquitectura_sistema/index.md §11` y `§13` (reestructuración PARA en cascada). Contenido sin cambios.*
