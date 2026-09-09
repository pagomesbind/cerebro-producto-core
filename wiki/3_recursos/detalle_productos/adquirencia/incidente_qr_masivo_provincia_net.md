# Incidente — Saturación de cola de generación de QR por carga masiva de Provincia Net

> Estado: en investigación — causa raíz sin confirmar. Decisión de convivencia de sistemas ya tomada (ver abajo). Ver iniciativa asociada `PRD-66` en [`2_areas/direccion/iniciativas.md`](../../../2_areas/direccion/iniciativas.md) y detalle completo del análisis de datos en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §7`.

## Problema detectado (2026-09-04, reunión "Producto - Prioridades")

Provincia Net **genera códigos QR de forma masiva** (batch, a través de API o endpoint), saturando la cola general de generación de QR de Bind PSP. Impacto: latencia en generación de QR para **todos los clientes** afectados, de hasta **+35 segundos**. Clientes con reclamos identificados en la reunión: **Provincia Net** y **DEPAY** (confirmado por un reclamo separado del mismo cliente el 08/09 — ver abajo). Recurrencia: **principios de mes** (cuando hay más deudas/facturación de municipios).

**Solución propuesta (en evaluación):** crear una **cola diferenciada** para generación masiva de QR — ruta para batch/masivo (Provincia Net) separada de la ruta de generación normal (resto de clientes), para evitar contaminación cruzada. Ticket AD935 (sin cotización inicial), prioridad 1. Posible como fix según Matías Alzogaray, riesgo bajo (cambio de cola, no de lógica central).

## Decisión de arquitectura — convivencia de sistemas (reunión "Análisis COBRO", 2026-09-07)

Existe un error reportado en ticket 1676/DAD-2943 (generación masiva de QR para Provincia Net sin respuesta desde hace semanas) — se justificaba seguir usando el "proceso antiguo" porque el nuevo desarrollo no soporta los volúmenes masivos de velocidad requeridos por Provincia Net.

**Decisión tomada:** mantener **ambos sistemas conviviendo operativamente** — el antiguo (funcionando, pero pensado para volumen masivo) y el nuevo (desarrollado, pero con limitaciones de throughput) coexisten en producción. Vincular ambos a PRD-66. La funcionalidad "Convivencia reporter" (ya finalizada previamente) quedó asignada como Prioridad 2 en el cierre oficial de la versión 73 de Adquirencia.

> Fuente: Mail de Matías Alzogaray, minuta "Análisis COBRO" (reunión 2026-09-07 12:00-13:00). Capturado por Pablo Gomes, 2026-09-08.

## Confirmación cuantitativa vía análisis de datos (2026-09-08)

A raíz de un reclamo repetido de **DEPAY** (WhatsApp, 2026-09-08 — "siempre recibimos PRECARGADO" al consultar el QR, timeout de 30s del lado del cliente) y del ticket de Soporte [AD-1676](https://bindpsp.atlassian.net/browse/AD-1676) (2026-09-04, mismo síntoma con 35s, atribuido a Provincia Net), un análisis de `dbo.Deuda` (export por entidad/día/estado) **confirma con datos lo que la reunión del 09-04 ya había diagnosticado cualitativamente**:

- **PNET (código A066) es el driver casi exclusivo de los picos de volumen** — 899.914 deudas en 37 días (agosto + primera semana de septiembre), 2,5× la entidad #2 (RIPSA) y más que todas las demás ~40 entidades sumadas.
- **Pico extremo el 2026-09-01: 210.431 deudas de PNET en un solo día — 78,9% de todo el volumen del sistema esa jornada** (266.736 en total) — confirma la recurrencia "principios de mes" (ciclo de facturación mensual de municipios).
- **DEPAY (código A042) no incrementó su propio volumen**: 1.174 → 1.204 deudas/día, sin cambio en 5+ semanas — confirma que DEPAY es un tercero afectado por la cola compartida, no un contribuyente del problema.
- **No hay evidencia de deudas trabadas para siempre**: de todo lo creado antes del 1/9, solo 13 filas en total siguen en PRECARGADO — la demora es de cola bajo pico de carga, no una falla de procesamiento.
- **No se identificó ninguna otra entidad nueva** generando volumen relevante — el único contribuyente secundario con crecimiento notable es CobroExpress (código `C`, 2,29×), muy por debajo de PNET.

## Junio-julio como control — la causa raíz sigue sin confirmar (misma sesión, 2026-09-08)

Al sumar el export de junio-julio (98 días de historia en total) para poner a prueba con más rigor la hipótesis de que "PNET cambió su forma de operar", el resultado **corrige la lectura inicial** (que solo comparaba 4 semanas de agosto-septiembre): el volumen de los picos de PNET **no es nuevo** — 4 picos ≥100.000/día ya en junio-julio, uno de ellos (17/06: 237.958) más grande que el del 01/09. Agosto fue, de hecho, un mes más tranquilo que junio/julio en promedio diario.

Una primera lectura de "estallido aislado antes del pase a producción de la carga masiva SFTP (13/08) vs. rampa sostenida después" **quedó en duda tras objeción del PM, verificada con los propios datos**: la concentración de PNET en el volumen total del sistema durante los picos de junio-julio (94,8%-96,7%) fue igual o mayor que la del pico del 01/09 (78,9%) — si la sola dominancia de PNET saturara la cola, junio/julio deberían haber tenido el mismo problema, y no hay evidencia de reclamos esos meses.

**Lead alternativo sin confirmar:** un cambio de parametrización de tiempos de **resolución de pagos** QR contra Coelsa (proyecto `bajar-tiempos-pagos-qr`/PRD-199, Nicolás Colón — ver [`mecanica_qr_coelsa.md` Parte 5](mecanica_qr_coelsa.md)) entró en producción el 2026-08-31, un día antes de la ventana de reclamos — mecanismo distinto al que reporta DEPAY (que pregunta por el estado de una Deuda recién creada, no por el resultado de un pago), pero la coincidencia temporal es fuerte y no está descartada.

**Sin conclusión cerrada.** DEPAY se confirma estable en los 4 meses completos (1.035-1.346/día, sin tendencia) y no hay backlog permanente. Pero la causa raíz de "por qué ahora y no en junio/julio" sigue abierta. Pendiente antes de cualquier conclusión o comunicación a Fintexa/PNET: confirmar con Ingeniería (Nicolás Colón, Gonzalo Rivera) si ambos mecanismos (generación de QR y resolución de pagos QR) comparten cola/infraestructura, y si hubo reclamos de latencia en junio-julio que no llegaron a escalarse a Jira.

> Fuente: sesión de análisis de datos con el PM — `raw/analisis cantidad de deudas.xlsx` (ago-sep) + `raw/analisis deudas junio y julio.xlsx` (jun-jul), export `dbo.Deuda` por entidad/día/estado + `dim_entidades.csv`. Capturado por Pablo Gomes, 2026-09-08. Análisis completo (gráfico diario por entidad + ranking) armado como artifact para discusión con Fintexa. Tarea de seguimiento: T-072 en `1_proyectos/tareas.md`.

## Ver también

- [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) — mecánica normativa/técnica de QR Coelsa (normativa, flujo de pago, alta de comercio, interchange, State Monitor de resolución de pagos).
- [`2_areas/direccion/iniciativas.md`](../../../2_areas/direccion/iniciativas.md) — novedad de PRD-66 (investigación en curso).
- `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md` — detalle técnico completo del análisis de datos, gaps y tareas.

---
*Creado: 2026-09-09 — `/context_merge` desde `contexto_vivo/` (Pablo Gomes): saturación de cola de generación de QR por carga masiva de Provincia Net, decisión de convivencia de sistemas, y análisis de datos que confirma el volumen de PNET pero deja la causa raíz de la ventana de reclamos (por qué ahora, no en junio/julio) sin confirmar.*
