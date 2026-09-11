# Incidente — Saturación de cola de generación de QR por carga masiva de Provincia Net

> Estado: causa raíz confirmada directamente por Ingeniería de Bind y Provincia Net (2026-09-10) — cola única compartida de generación de QR + retry storm de reintentos ante saturación. Plan de mitigación de corto y largo plazo acordado (ver abajo). Queda abierta, como pregunta secundaria de menor prioridad, por qué el reclamo se hizo notorio recién en septiembre y no en los picos iguales o mayores de junio-julio. Ver iniciativa asociada `PRD-66` en [`2_areas/direccion/iniciativas.md`](../../../2_areas/direccion/iniciativas.md), mecánica técnica del flujo que genera las ráfagas en [`automatizacion_creacion_masiva_qr.md`](automatizacion_creacion_masiva_qr.md), y detalle completo del análisis de datos en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §7/§8`.

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

## Causa raíz confirmada por Ingeniería y plan de mitigación (reunión "BIND / PNET: Performance, recurrencia, etc.", 2026-09-10)

Hernan Clarich (Bind, Arquitectura) confirmó en vivo el mecanismo que el análisis de datos de `dbo.Deuda` (2026-09-08/09) solo había podido inferir indirectamente: **existe una única cola compartida** de generación de QR entre todos los clientes del producto. Cuando la densidad de creación sube en una ventana de minutos (ej. una ráfaga de Provincia Net), todos los pedidos se demoran — y los clientes que piden QR "de a uno" (interactivos, como DEPAY) son los más perjudicados porque quedan detrás de los lotes masivos. El sistema sostiene de forma estable **~1000 QR/minuto**; por encima de ese umbral empieza a degradarse.

**Efecto amplificador — retry storm.** La política de reintentos de Provincia Net ante una respuesta 400 usa backoff exponencial (5s → 10s → 20s → 40s). Durante las ráfagas de saturación se observan picos donde **hasta el 100% de estos reintentos vuelven a fallar** — la cola se satura tanto que ningún reintento pasa en su primera ventana, lo que dispara una nueva ronda de reintentos y agrava aún más la congestión. Se discutió (sin decisión firme) que Provincia Net aumente su primer intervalo de espera (5s → 10s) para no seguir empujando carga durante el pico.

**Nota sobre el gap de "por qué apareció el reclamo justo en septiembre":** esta confirmación explica el mecanismo general de forma independiente de cualquier fecha puntual — no resuelve por sí sola por qué el reclamo se hizo notorio recién en septiembre (los picos de junio-julio fueron iguales o mayores sin reclamo conocido). Queda abierto como pregunta secundaria, de menor prioridad ahora que el mecanismo y el plan de arreglo ya están confirmados y en marcha. Ver `1_proyectos/prd-66_provincianet_creacion_masiva_qr/gaps.md`.

### Plan de mitigación acordado

- **Corto plazo (paliativo, ~1-1,5 mes, en curso del lado Bind):** escalar recursos — más vCores de base de datos y más pods de los microservicios que atienden la cola de generación de QR. Sin ticket ni fecha de fin formalizados en la reunión.
- **Largo plazo — ticket AD935 (cola diferenciada, ver arriba):** separar la cola única en 2 colas — una para tráfico interactivo/"de a uno", otra para ráfagas/batch. Arquitectura ya lo está discutiendo activamente, sin ETA concreta.
- **Pedido de Bind a Provincia Net, sin compromiso firme:** bajar la tasa de creación del canal individual/interactivo de PNET a ~800-900 QR/minuto (margen bajo el techo estable de ~1000/min) mientras Bind termina de escalar del lado propio, condicionado a las necesidades de negocio de cada ente de PNET.

### Líneas de exploración nuevas, sin decisión ni ETA

1. **Múltiples canales SFTP en paralelo, uno por caja pre-configurada.** Hoy el SFTP de Provincia Net no soporta paralelismo — un lote grande (ej. "La Matanza", horas de procesamiento) bloquea a cualquier archivo que llegue detrás, porque el pool de QR pre-generado está atado a una sola caja. Si Provincia Net tuviera varias cajas (administrativamente viable, confirmado por Facundo Collerone), Bind podría procesar varios canales SFTP en paralelo sin pisarse. Arquitectura lo evalúa, con el matiz de que los canales deberían ser elásticos, no reservar recursos ociosos la mayor parte del día para escalar solo durante el batch.
2. **Reducir el tiempo mínimo de despacho de un lote SFTP chico.** Hoy existe un intervalo mínimo de despacho del orden de ~30 minutos — aceptable para un lote de cientos de miles de registros, excesivo para un lote chico (ej. 100 QR). Pedido de Provincia Net, sin dueño ni ETA asignado.
3. **Ratio deuda-creada / QR-generado.** Estimación de memoria (~90% del tiempo de procesamiento es la generación del QR, no la creación de la deuda), sin métrica dura — Provincia Net pidió el dato real.
4. **Dato pendiente de envío de Bind a PNET:** histograma de duración de los picos/ráfagas de saturación (Bind ya tiene datos sueltos — un pico de 108 minutos, otro de 10 — falta consolidarlos y enviarlos formalmente). Sirve para que PNET calibre su política de reintentos.
5. **Cola de generación de QR exclusiva para Provincia Net (partición por cliente) — propuesta de Arquitectura, addendum posterior a la reunión del 09-10.** Alternativa o complemento a AD935 (que particiona por *tipo de tráfico*, interactivo vs. batch): en vez de eso, una cola de generación de QR separada **exclusiva para PNET**, distinta de la del resto de clientes — partición por *cliente*, no por tipo de tráfico. **Limitación reconocida explícitamente por el PM al traerla:** esta cola "no mejoraría a Provincia Net" — un ente mediano de PNET seguiría compitiendo por la misma capacidad dentro de su propia cola exclusiva; su único beneficio es **evitar que el volumen de PNET siga impactando al resto de los clientes** (DEPAY y cualquier otro cliente del canal interactivo compartido). Se propone evaluarla como **quick win**, más simple de implementar que la partición por tipo de tráfico. **Probable solapamiento con AD935:** el análisis de `dbo.Deuda` ya estableció que PNET concentra ~90-97% del volumen del sistema en los picos — si esa es también la composición del tráfico "batch/ráfaga" que AD935 aísla, ambas colas terminarían aislando casi el mismo tráfico en la práctica; vale que Arquitectura confirme si son redundantes, o si la partición por cliente (más simple y potencialmente más rápida de implementar) puede servir de puente mientras se diseña la partición por tipo de tráfico (más general, cubre a futuros clientes de alto volumen además de PNET). Sin decisión ni ETA.

### Contexto de negocio de Provincia Net y riesgo de crecimiento

Provincia Net segmenta a sus propios clientes (municipios/entes) en 3 tipos: (a) 4-5 entes "muy particulares" con proceso continuo de cierre de deuda/emisión de factura, exclusivos del canal SFTP, calendarizados entre sí; (b) entes medianos con mucho volumen pero sin urgencia de tiempo, manejados de forma asincrónica; (c) clientes de consumo individual/interactivo ("de a uno") — sin proceso batch, van directo contra la API, y son los que hoy reportan timeouts (ej. DEPAY). Provincia Net proyecta que este tercer segmento va a crecer fuerte en los próximos meses (nuevos sectores: telefonía, transporte, entre otros) — capturado como riesgo de contexto fijo en [`2_areas/riesgos.md`](../../../2_areas/riesgos.md) (si este crecimiento se concreta antes de la mitigación de largo plazo, el número de clientes afectados por el mismo problema puede multiplicarse, no solo los de PNET).

**Dirección estratégica de PNET (informativa, sin acción de Bind):** evalúan migrar el caso de uso de impresión en factura a un QR estático (un QR fijo por destino/factura, con el importe actualizándose por fuera) en vez de generar un QR dinámico nuevo por factura — eliminaría de raíz la contención para ese segmento. Sin fecha ni compromiso.

> Fuente: Reunión "BIND / PNET: Performance, recurrencia, etc." (2026-09-10, 45min) — transcripción completa provista por Facundo Collerone (Provincia Net). Participantes: Bind PSP (Pablo Gomes, Hernan Clarich — Arquitectura, Gonzalo Rivera, Mariana), Provincia NET (Facundo Nicolas Collerone, Ricardo Andres Lavia). Detalle completo en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §8`. Capturado por Pablo Gomes, 2026-09-10.

## Ver también

- [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) — mecánica normativa/técnica de QR Coelsa (normativa, flujo de pago, alta de comercio, interchange, State Monitor de resolución de pagos).
- [automatizacion_creacion_masiva_qr.md](automatizacion_creacion_masiva_qr.md) — mecánica técnica completa del flujo SFTP→ETL→SP Orquestador→reportes→webhook que produce las ráfagas masivas de PNET.
- [`2_areas/direccion/iniciativas.md`](../../../2_areas/direccion/iniciativas.md) — novedad de PRD-66.
- [`2_areas/riesgos.md`](../../../2_areas/riesgos.md) — riesgo de escalamiento por crecimiento del segmento de clientes individuales de Provincia Net.
- `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md` — detalle técnico completo del análisis de datos, gaps y tareas.

---
*Última actualización: 2026-09-11 — `/context_merge` desde `contexto_vivo/` (Pablo Gomes): addendum a las líneas de exploración — 5ª línea, propuesta de Arquitectura de una cola de generación de QR exclusiva para Provincia Net (partición por cliente, distinta de AD935), con su limitación reconocida y el probable solapamiento con AD935 sin confirmar.*
*Última actualización anterior: 2026-09-10 — `/context_merge` desde `contexto_vivo/` (Pablo Gomes): causa raíz confirmada directamente por Ingeniería de Bind y Provincia Net (cola única + retry storm), plan de mitigación corto/largo plazo, líneas de exploración nuevas (multi-canal SFTP, despacho de lotes chicos, ratio deuda/QR), y contexto de negocio/crecimiento de Provincia Net.*
*Creado: 2026-09-09 — `/context_merge` desde `contexto_vivo/` (Pablo Gomes): saturación de cola de generación de QR por carga masiva de Provincia Net, decisión de convivencia de sistemas, y análisis de datos que confirma el volumen de PNET pero deja la causa raíz de la ventana de reclamos (por qué ahora, no en junio/julio) sin confirmar.*
