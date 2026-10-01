# Proceso de Publicaciones Mensuales — Ceremonias Clave

> Contenido completo transcrito desde `wiki/3_recursos/conocimiento_interno/proceso/proceso_publicaciones_mensuales.md` (ingesta original), reubicado desde `detalle_productos/transversal/procesos_internos.md §1` en la reestructuración PARA en cascada (2026-08-12) — es un proceso interno del equipo, no conocimiento de producto.
>
> ⚠️ **Contradicción sin resolver (2026-09-07):** el ciclo **mensual** de 4 ceremonias descrito abajo es el proceso documentado en la ingesta original. Una decisión más reciente (ver [`direccion/decisiones.md`](../direccion/decisiones.md) [2026-09-01]) reforma el ciclo hacia **quincenal con Release Candidates** (versiones congeladas 10-15 días, desacople de Adquirencia/Wallet, protocolo de hotfix formalizado), motivada por una sobrecarga operativa crítica (5 lanzamientos en 24hs) y una multa de $75M por errores de Ardid (ver [riesgos.md](../riesgos.md)). Al 2026-09-07 la reforma está "en aplicación desde la v73" (primer Release Candidate publicado en Staging el 2026-09-07, próxima revisión 2026-09-08) pero **no hay confirmación de que reemplace formalmente este documento** — este merge no elige versión ganadora, ver gap abierto en [`gaps_y_preguntas.md`](../gaps_y_preguntas.md) [2026-09-07].

A continuación se describen las ceremonias clave a llevar a cabo por cada versión mensual (proceso documentado originalmente — ver nota de contradicción arriba).

## Cierre de alcance

**Fecha:** Segundo lunes de cada mes.

**Objetivo:** Acordar el alcance propuesto de la versión a publicar a fin de mes.

**Tareas del PM:**
- [ ] Crear la publicación principal del mes.
- [ ] Asignar a la versión del mes a todas las US y BUG que se encuentren en estado `FINALIZADO`, `CON DEFECTO`, `EN QA`, `EN CURSO` y que no tengan una versión asignada sin publicar.
- [ ] Analizar con Fintexa y con el negocio los tickets en estado `EN CURSO` asignados a la versión, cuyo esfuerzo por terminar es mucho y no se llegarán a entregar en una semana, y desasignarlos de la versión.
- [ ] Analizar con el negocio si hay que asignar a la versión tickets muy importantes (Prioridad Highest) que estén `LISTO PARA DESARROLLO`, `ASIGNADO` o `BACKLOG` y que no tengan una versión asignada sin publicar.
- [ ] Organizar meet con stakeholders internos (QA, PRODUCTO y OPERACIONES) y con los PM de Fintexa y facilitar la discusión y cierre del alcance.

## Corte de desarrollos

**Fecha:** Tercer lunes de cada mes.

**Objetivo:** Ajustar al alcance final de la versión.

**Tareas del PM:**
- [ ] Validar que todos los tickets dentro del alcance acordado están en estado `EN QA` o `CON DEFECTO` o `FINALIZADO`.
- [ ] Organizar meet con los PM de Fintexa y facilitar la discusión y cierre del alcance.
- [ ] Negociar qué hacer con los tickets del alcance acordado que aún siguen en estado `BACKLOG`, `ASIGNADO`, `LISTO PARA DESARROLLO` o `EN CURSO`. Por defecto, los tickets en este estado deben ser desasignados de la versión.
- [ ] Empezar seguimiento de tareas de QA asignadas al equipo (regresiones y test unitarios).

## Go / No Go

**Fecha:** Cuarto lunes de cada mes.

**Objetivo:** Evaluar aprobación del pasaje a producción de la versión.

**Tareas del PM:**
- [ ] Confirmar pasaje a producción de todos los tickets que están asignados a la versión del mes y están en estado `FINALIZADO`
- [ ] Negociar qué hacer con los tickets del alcance acordado que aún no están en estado `FINALIZADO`. Por defecto, estos tickets deben ser desasignados de la versión.
- [ ] Confirmar forma y fecha de pasaje a producción.
- [ ] Comunicar a Bind PSP sobre el pasaje a producción planificado.

## Pasaje a prod

**Fecha:** Martes y miércoles de la última semana de cada mes.

**Objetivo:** Pasar a producción la versión.

**Tareas del PM:**
- [ ] Monitorear pasaje y documentar el resultado.
- [ ] Si hubo algún problema o exepción durante el pasaje a producción, desasignar de la versión a los tickets que finalmente no fueron publicados.

## Snapshot — calendario de despliegues de septiembre 2026

> Instantánea puntual de un mes concreto, útil como ejemplo real de cómo se aplicó el ciclo de arriba — no reemplaza el proceso general. Fuente inicial: mail "Cronograma Septiembre" de Matías Alzogaray (2026-09-07); actualizado y consolidado con el tablero de seguimiento presentado en la reunión "Weekly - Producto / Operaciones" del 2026-09-14.

**Confirmadas (según el tablero del 14/09, con fecha):**
- **Onboarding Persona Jurídica (La Virginia):** 16/09 (terminó saliendo el 17/09 por un día de corrimiento — ver `direccion/iniciativas.md`, proyecto PRD-223).
- **Pagos Efex (Pagos FX) — versión 72.3 TR:** 17/09 (confirmado también en `direccion/decisiones.md` [2026-09-11]).
- **PMC (Adquirencia) — 22/09:** archivo PMC vacío (arreglo) + PMC Impuestos Misiones (ambos pedidos de Soporte).
- **Adquirencia V 73 (Botón/Cobro + Agente de Cobros y Pagos):** ⚠️ corrida dos veces. Pase original 24/09 — **cancelado el mismo día** en la "Reunión de Pre-despliegue AD 73" (2026-09-24), por retrasos en QA, requerimientos tardíos, cambios de alcance y errores críticos detectados en liquidaciones. Reprogramado formalmente al **martes 29/09, 20:30hs** (acuerdo de esa misma reunión). Alcance: masividad de Provincia Net + resto de QR (Botón 2.0), Pagos Efex del portal, tratamiento de contracargos, convivencia de R por T con Botón 2.0 (pedido de Favacard), corrección de archivos/registros de liquidaciones y separación de desconocimientos/devoluciones (ver [`detalle_productos/agente_cobros_y_pagos/liquidaciones_reversas_y_comprobantes.md`](../../3_recursos/detalle_productos/agente_cobros_y_pagos/liquidaciones_reversas_y_comprobantes.md) y [`detalle_productos/adquirencia/desconocimientos_de_tarjeta.md`](../../3_recursos/detalle_productos/adquirencia/desconocimientos_de_tarjeta.md)). **✅ Fecha de pase confirmada (martes 29/09):** en la "Weekly - Producto / Operaciones" del 28/09, Matías Alzogaray quedó a cargo de mandar un recordatorio a todos los involucrados sobre los puntos de la V73 "para el despliegue de mañana" — confirma martes 29/09, descarta el borrador de aviso con fecha lunes 28/09 de Gonzalo Rivera (cierra la ambigüedad señalada abajo; la minuta no da la hora exacta, se mantiene 20:30hs de la fuente anterior). Aviso a clientes: actualizaciones de liquidaciones/PDF (separación de desconocimientos y devoluciones), aviso sobre BINes a Ripsa "y el grupo", aclaración de que no se esperan interrupciones de servicio. **Incidencia abierta post-pase:** error reportado en el módulo de reportería de transferencias (Matías Alzogaray a cargo de la corrección) y un reporte de cuentas deshabilitadas por fraude con saldo pendiente de "1900" (sin moneda ni cliente identificado en el resumen de la minuta). **V74 ya en planificación** (misma reunión del 28/09): Luciana Rudaz tiene que crear y sumar un ticket faltante sobre optimización de liquidaciones y mandarle la información a Matías Alzogaray; del lado de Adquirencia, la reunión "Análisis COBRO" del 28/09 empezó a armar el listado de tickets de la V74. **⚠️ Ambigüedad histórica ya resuelta arriba (dejada para trazabilidad):** la acción de la minuta del 24/09 asignada a Gonzalo Rivera decía notificar "para el lunes por la noche", el resumen de la misma minuta decía "martes a las 8:30 de la noche", y un mail posterior de Gonzalo Rivera (24/09 17:03) proponía un borrador de aviso con fecha **lunes 28/09 21:00** — sin confirmación de envío. Un mail de Fintexa sobre liquidaciones (25/09) hablaba del "pasaje previsto para el martes" — ver gap ya cerrado en [`4_archivos/gaps_resueltos.md`](../../4_archivos/gaps_resueltos.md).
- **Wallet — versión 73:** corrida de 28/09 a **"el 8"** (probablemente 08/10, la minuta "W 73 - Impacto de temas" del 2026-09-24 no aclara el mes) — motivo: retrasos de infraestructura que impiden cumplir la fecha prevista. Reunión de análisis de riesgo el 25/09 para evaluar viabilidad del pase el 8; contexto técnico mencionado: "nuevos modelos de aceptadores requieren activaciones controladas". Alcance original: soporte de Getnet (prioridad 1, ver `tareas.md` T-031) y alta de comitente recuperando de onboarding — un cliente (sin identificar en el resumen) recibirá aviso de nueva fecha de lanzamiento "programada para el 12" (probable 12/10).

**Sin fecha confirmada al 14/09:**
- **Emisión — GetNet** (DEM-1964, DEM-1965 — circuito nuevo, depende de T-068/T-069).
- **Adquirencia:** ProvinciaNet (DAD-2943), Favacard (DAD-2437), incorporar arancel Coelsa en webhook de Cobro (DAD-2801), fix de devoluciones por Pago Fácil, error de reporte de transacciones en el Admin, mejora de tiempos de liquidación (estas 3 últimas, prioridad 2/3).
- **Wallet:** reporte normativo FSI, desactivación automática de cuentas bloqueadas.
- **Ardid — versión 19:** pendiente de que RAW (Fintexa) entregue documentación.
- **Servicios:** fix tarjeta prepaga, error de validación de recaptcha.
- **Tienda Nube — error en consulta de transferencias salientes:** no se pudo resolver en el mes por complejidad de desarrollo (Melisa Belpassi, Fintexa) — se traslada a la versión 74.

## Ver también

- [gestion_jira.md](gestion_jira.md) — estados de ticket de desarrollo sobre los que operan estas ceremonias (`FINALIZADO` es el nombre real y único del estado terminal).
- [analisis_de_riesgo_de_despliegue.md](analisis_de_riesgo_de_despliegue.md) — informe de riesgo que se arma antes de cada despliegue, complementario a estas ceremonias.
- [requerimientos_al_equipo_tecnico.md](requerimientos_al_equipo_tecnico.md) — cómo entra un pedido al backlog que luego pasa por este ciclo mensual.

---
*Última actualización: 2026-10-01 — `/context_merge`: confirmada la fecha real del pase de AD V73 (martes 29/09, resuelve la ambigüedad lunes/martes — gap rotado a `gaps_resueltos.md`), aviso a clientes efectivamente comunicado, incidencia abierta en reportería de transferencias, y V74 ya en planificación (ticket de optimización de liquidaciones pendiente de Luciana Rudaz) — con permiso explícito del usuario (Nicolás Colón).*
*Última actualización anterior: 2026-09-29 — `/context_merge`: snapshot de septiembre — Adquirencia V73 cancelada y reprogramada al martes 29/09 20:30 (con ambigüedad sin resolver sobre el aviso a clientes), Wallet V73 corrida de 28/09 a "el 8" — con permiso explícito del usuario (Nicolás Colón).*
*Última actualización anterior: 2026-09-23 — `/context_merge`: nueva sección "Snapshot — calendario de despliegues de septiembre 2026" (cronograma inicial del 07/09 consolidado con el tablero del 14/09), con permiso explícito del usuario para procesar el backlog de régimen D acumulado (pablo + nicolas).*
*Última actualización anterior: 2026-08-12 — Reubicado desde `detalle_productos/transversal/procesos_internos.md §1` (reestructuración PARA en cascada). Contenido sin cambios; corrección `HECHO`→`FINALIZADO` ya aplicada en la fuente (2026-07-04).*
