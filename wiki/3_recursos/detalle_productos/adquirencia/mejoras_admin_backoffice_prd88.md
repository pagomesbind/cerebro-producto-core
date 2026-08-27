# Mejoras y Bugs de Admin/Backoffice de Integraciones (IDEA Jira PRD-88)

> Estado: mezcla de en producción y en curso. Reubicado desde `detalle_productos/adquirencia/configuracion_entidades_y_comercios.md` en la reestructuración PARA en cascada (2026-08-12). Fuente: Jira `bindpsp.atlassian.net`, IDEA [PRD-88](https://bindpsp.atlassian.net/browse/PRD-88) "Mejoras para integraciones y soporte" → Epics [AD-223](https://bindpsp.atlassian.net/browse/AD-223) "Sanear Crear Entidad" (22 tickets), [AD-8](https://bindpsp.atlassian.net/browse/AD-8) "ABM de canales de cobro" (76 tickets — el Epic más grande del barrido de Jira de este proyecto), [AD-232](https://bindpsp.atlassian.net/browse/AD-232) "Errores y mejoras admin en general" (14 tickets), [AD-7](https://bindpsp.atlassian.net/browse/AD-7) "ABM de roles y usuarios" (10 tickets) y [AD-230](https://bindpsp.atlassian.net/browse/AD-230) "Configurar webhooks entidad" (1 ticket).
>
> **Motivación de negocio**: alto volumen de reclamos de clientes por errores/demoras en atención a integraciones, con ~50% del capacity de desarrollo consumido en tareas de soporte manual — objetivo bajar a 30% para abril 2026, dándole al equipo de integraciones herramientas de autoservicio desde el Admin en vez de requerir scripts/tickets a nivel 2.
>
> **Cobertura de esta ingesta**: dado el volumen (~147 tickets combinados), se aplicó triage agresivo sobre una muestra representativa. Al momento de esta ingesta, **la mayoría de las Epics seguían "En curso"/"EN QA"** pese a que la IDEA madre figura "Finalizada" — mismo patrón de discrepancia documentado en otras IDEAs de este proyecto (ver [feedback_jira_status_vs_produccion]).

## 1. Alta de Entidad — mejoras y bugs (Epic AD-223)

- **Campo Id de cuenta** (ver [configuracion_de_entidades.md §1](configuracion_de_entidades.md)) ahora acepta **cualquier valor numérico entero positivo** en el formulario de Admin — antes limitado a 1 o 2, pero en la práctica depende del Id de cuenta Coelsa del PSP. Bug relacionado corregido: el campo permitía letras, debía validarse como solo numérico.
- **Nueva opción "username" al crear entidad**: elegir si los usuarios por defecto en Access Management del portal comercio usan como username el CUIT del comercio o el modo estándar `Admin@{codigoComercio}` — antes hardcodeado. Por defecto queda el modo estándar.
- **Adherir cuenta vendedora Coelsa desde el propio alta de entidad**: ahora puede indicarse en el formulario que se adhiera automáticamente (antes solo vía proceso manual). Semáforo a nivel entidad con 3 estados: ✅ (adherida, muestra `account_id`), ❌ (error, muestra `account_id` y detalle), ⚪ (no se eligió adherir).
- **Bugs de datos de Impuestos**: autocompletado incorrecto de Provincia y Localidad; la entidad no se creaba en Siscri por un error en `tipoIIBB` cuando el agente de retención era Bind PSP.
- **Versiones de publicación**: campo input de Id de cuenta (AD-291/AD-229, AD 67.2); Siscri `tipoIIBB` + IIBB no numérico (AD-584/AD-538, AD 68) + adherir cuenta vendedora (AD-393, AD 68); autocompletado Provincia/Localidad (AD-585, AD 69); no se visualiza error en Cuenta ID (AD-913, AD 70.1); opción "username" (AD-429/AD-226, AD 70.1).

## 2. Rediseño de arquitectura de Canales de Cobro (Epic AD-8, 76 tickets)

El Epic más grande del barrido de Jira de este proyecto (más grande incluso que FCI Cuenta Remunerada). Cubre un **rediseño de fondo** de cómo se habilitan los canales de cobro (QR, POS, Botón Simple) en un comercio:

- **Problema de origen**: el flag `habilitado` del comercio disparaba automáticamente la creación de infraestructura de canal QR (alta en Coelsa, CVU, suscripción DEBIN recurrente, split) aunque el comercio no debiera operar con QR.
- **Modelo nuevo**: la creación automática de canales pasa a depender exclusivamente de `canal_entidad` (canales por defecto a nivel entidad); las habilitaciones efectivas de cada comercio quedan en `canal_comercio`, con campo de error dedicado para reintento sin perder el resto de la configuración.
- **Endpoint de migración**: migra masivamente (por entidad o para todos los comercios) los canales existentes al nuevo modelo `canal_comercio`, tolerando errores comercio por comercio.
- **Endpoint `UpdateQr`**: cambia `split` de `true`↔`false` en un comercio ya habilitado.
- **Reintento de habilitación desde el Admin**: botón "Reintentar" por canal, distinguiendo errores técnicos internos (reintento inmediato) de errores externos de procesador (hasta 3 intentos), con mensaje traducido y persistido (`MensajeErrorDescripcion`).
- **Cluster de bugs post-rediseño** (varios abiertos al momento de esta ingesta): POS con arancel reducido pedía teléfono/fecha de nacimiento indebidamente, o el canal quedaba "habilitado" en `CanalComercio` sin reflejarse en GP (falta Especificación tipo 32/17); cambiar `split=true`→`false` rompía devoluciones (rechazadas por Api Bank) hasta volver a `true`; un canal de Botón Simple reintentado y marcado "habilitado" no habilitaba realmente "Cobrar con link" en Portal Comercio; transacciones del día no se veían en el módulo Transacciones del Admin (sí en Portal Comercio); desasociar reglas de pago de un canal Botón Simple rompía la re-asociación posterior sin arrojar error.
- **Nota de volumen**: ~30 de los 76 tickets son Tests/Test Plans de regresión de QA sin contenido de aprendizaje adicional.
- **Versiones de publicación**: el grueso (21 tickets) salió en **AD 67.5** (2026-03-03). Fixes puntuales: AD 66 (2025-12-16), AD 67.2 (2026-02-10, split en entidad mayorista), AD 67.3 (2026-02-19, no permite editar BS con error), AD 68 (2026-03-30, alta POS con datos null), **AD 69.2 HF** (2026-05-11, hotfix dedicado — arancel reducido pide teléfono/fecha indebidamente, alta POS reducido no figura en GP, reproceso con error no habilita el canal).

> ⚠️ **Contradicción registrada (2026-08-24) — dos hallazgos independientes cuestionan la caracterización de arriba como "patrón ya validado y reusable en producción". Ver antes de usar esta sección como referencia para otra iniciativa.**
>
> **1. El propio equipo operativo dice que no funciona como se espera.** Durante el discovery de `/idea_problem` sobre el proyecto `convenios_configuracion` (rediseño de la herencia de convenios entre entidad y comercio), el PM (Pablo Gomes) aportó una corrección directa: el discovery original de ese proyecto (`/idea_start`, 2026-08-21) había tomado el Epic AD-8 de arriba como referencia arquitectónica probada para espejar en el nuevo diseño de convenios, pero ese mismo mecanismo (`canal_entidad`/`canal_comercio`) se intentó usar para resolver un problema análogo y quedó **mal definido y mal ejecutado** — no funciona como lo espera el equipo operativo de Soporte de Cobro (referente Gonzalo Rivera, el mismo que reporta el dolor de convenios). No se precisó si el problema es de diseño, de ejecución (bugs), o de ambos. **Por qué importa:** si AD-8 no funciona como documenta esta sección, cualquier otra iniciativa de Adquirencia que lo tome como "patrón ya validado" puede estar partiendo de una premisa falsa. Quien mantiene este archivo debería confirmar con el propio Gonzalo Rivera (o relevar tickets de soporte sobre canales de cobro) si el "no funciona como se espera" es puntual, generalizado, o ya conocido y en backlog — y ajustar la caracterización de §2 en consecuencia (de "validado en producción" a "construido pero con problemas conocidos", si corresponde). Impacto directo: el Gate 3 de `convenios_configuracion` (que adoptó la analogía con AD-8) quedó parcialmente reabierto — ver `1_proyectos/convenios_configuracion/decisiones.md` (2026-08-24); el nuevo diseño de convenios debe partir del mecanismo real de herencia (copia puntual al crear el comercio, no vínculo vivo), no asumir que basta con replicar `canal_entidad`/`canal_comercio`.
> Fuente: `/idea_problem` — sesión de problem statement del proyecto `convenios_configuracion`, corrección aportada en vivo por el PM (2026-08-24).
>
> **2. El contrato real de la API de Convenios no coincide con esta descripción informal.** El mismo discovery relevó el spec OpenAPI real de la "Api Comercios" — ver [gestion_convenios_comisiones.md](gestion_convenios_comisiones.md), que documenta el modelo real (Convenio maestro + ComercioConvenio con override/`FromCommerce`) y reemplaza cualquier descripción informal de convenios que se apoyara en esta sección.
> Fuente: `/idea_solution` — spec OpenAPI 3.0.1 "Api Comercios", aportado por el PM (2026-08-24).
>
> Se mantiene el texto original de §2 arriba por trazabilidad (fue el resultado documentado del barrido de Jira de PRD-88). Gaps escalados — pendiente de decisión del usuario, ver `gaps_y_preguntas.md`.

## 3. ABM de Roles y Usuarios (Epic AD-7)

La mayor parte ya está documentada en [agrupador_mayorista.md §3](agrupador_mayorista.md) (migración a **AccessManagement 2.0**, `RolTemplate`/`PermisoTemplate`) — esta IDEA confirma que la migración se completó preservando compatibilidad con Portal Comercio, TIN/WICO y MPOS. Delta nuevo: bug de login que no validaba si un miembro estaba dado de baja — solo validaba bloqueo por intentos fallidos (`bloqueadoHasta`), permitiendo el ingreso de usuarios ya dados de baja.

## 4. Webhooks de entidad (Epic AD-230) y otras mejoras de Admin (Epic AD-232)

- **AD-230** ("Configurar webhooks entidad"): el único ticket vinculado quedó en **Backlog, sin arrancar** — pese a que la IDEA madre PRD-88 figura "Finalizada".
- **AD-232** (muestra de 5 de 14 tickets): ancho de columnas configurable en grillas (Convenios/Reglas de pago; ordenar registros quedó en Backlog), optimización del calendario del filtro de Transacciones, y la misma opción de "username" ya cubierta en AD-223 (ticket duplicado en dos Epics).

## Ver también
- [configuracion_de_entidades.md](configuracion_de_entidades.md) — flujo de alta de entidad que este PRD mejora.
- [agrupador_mayorista.md](agrupador_mayorista.md) — AccessManagement 2.0 en detalle.
- [gestion_convenios_comisiones.md](gestion_convenios_comisiones.md) — contrato real de la API de Convenios (2026-08-24), en disputa con §2 — ver nota de contradicción arriba.

---
*Última actualización: 2026-08-27 — `/context_merge`: §2 suma nota de contradicción (doble hallazgo: AD-8 no funciona como espera el equipo operativo de Soporte de Cobro, y el contrato real de la API de Convenios difiere de esta descripción informal — ver `gestion_convenios_comisiones.md`).*
*Última actualización anterior: 2026-08-12 — Reubicado desde `detalle_productos/adquirencia/configuracion_entidades_y_comercios.md` (reestructuración PARA en cascada). Contenido sin cambios de fondo.*
