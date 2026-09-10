---
id: 2026-09-10_adquirencia_reunion_pnet_causa_raiz_cola_unica_y_mitigacion
pm: pablo
fecha_captura: 2026-09-10
fuente: "Reunión 'BIND / PNET: Performance, recurrencia, etc.' (2026-09-10, 45min) — transcripción completa provista por Facundo Collerone (Provincia Net), dejada por el PM en `raw/`. Participantes: Bind PSP (Pablo Gomes, Hernan Clarich — Arquitectura, Gonzalo Rivera, Mariana), Provincia NET (Facundo Nicolas Collerone, Ricardo Andres Lavia). Detalle completo en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §8 'Reunión 2026-09-10'`."
producto: adquirencia
tema: causa raíz confirmada en vivo por Ingeniería de la demora de generación de QR (cola única compartida + retry storm) y plan de mitigación corto/largo plazo acordado con Provincia Net
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md
tipo_destino: actualizar
contradice: "no — confirma y extiende el mecanismo ya inferido estadísticamente en el archivo canon (sección 'Confirmación cuantitativa' y 'Junio-julio como control'), esta vez con explicación directa de Ingeniería de ambos lados en vez de inferencia sobre datos históricos"
confianza: alta
estado: en_cola
merge_commit:
---

**Por qué esto es canon y no solo del proyecto:** el archivo `incidente_qr_masivo_provincia_net.md` ya documenta la investigación de esta saturación de cola como conocimiento de producto transversal (no solo de PRD-66) — esta reunión aporta la explicación directa de Ingeniería del mecanismo, que hasta ahora solo se había inferido estadísticamente, más el plan de mitigación concreto. Corresponde agregarse a ese archivo, con referencia cruzada a `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §8` para el detalle completo de la reunión.

## Causa raíz — confirmada directamente por Ingeniería de Bind en la reunión

Hernan Clarich (Bind, Arquitectura) confirmó en vivo el mecanismo que el análisis de datos de `dbo.Deuda` (2026-09-08/09) solo había podido inferir indirectamente: **existe una única cola compartida** de generación de QR entre todos los clientes del producto. Cuando la densidad de creación sube en una ventana de minutos (ej. una ráfaga de Provincia Net), todos los pedidos se demoran — y los clientes que piden QR "de a uno" (interactivos, como DEPAY) son los más perjudicados porque quedan detrás de los lotes masivos. El sistema sostiene de forma estable **~1000 QR/minuto**; por encima de ese umbral empieza a degradarse.

**Efecto amplificador — retry storm.** La política de reintentos de Provincia Net ante una respuesta 400 usa backoff exponencial (5s → 10s → 20s → 40s). Hernan reportó que, durante las ráfagas de saturación, ve picos donde **hasta el 100% de estos reintentos vuelven a fallar** — es decir, la cola se satura tanto que ningún reintento pasa en su primera ventana, lo que dispara una nueva ronda de reintentos y agrava aún más la congestión. Se discutió (sin decisión firme) que Provincia Net aumente su primer intervalo de espera (5s → 10s) para no seguir empujando carga durante el pico.

**Nota sobre el gap de "por qué apareció el reclamo justo en septiembre" (`1_proyectos/prd-66_provincianet_creacion_masiva_qr/gaps.md`):** esta confirmación explica el mecanismo general de forma independiente de cualquier fecha puntual — no resuelve por sí sola por qué el reclamo se hizo notorio recién en septiembre (los picos de junio-julio fueron iguales o mayores sin reclamo conocido). Queda abierto como pregunta secundaria, de menor prioridad ahora que el mecanismo y el plan de arreglo ya están confirmados y en marcha.

## Plan de mitigación acordado

- **Corto plazo (paliativo, ~1-1,5 mes, en curso del lado Bind):** escalar recursos — más vCores de base de datos y más pods de los microservicios que atienden la cola de generación de QR. Sin ticket ni fecha de fin formalizados en la reunión.
- **Largo plazo — ya trackeado como ticket AD935 (ver sección de arriba de este mismo archivo canon, "cola diferenciada"):** separar la cola única en 2 colas — una para tráfico interactivo/"de a uno", otra para ráfagas/batch. Hernan confirmó que Arquitectura ya lo está discutiendo activamente (venía de una reunión de Arquitectura sobre este mismo tema el mismo día), sin ETA concreta.
- **Pedido de Bind a Provincia Net, sin compromiso firme:** bajar la tasa de creación del canal individual/interactivo de PNET a ~800-900 QR/minuto (margen bajo el techo estable de ~1000/min) mientras Bind termina de escalar del lado propio, condicionado a las necesidades de negocio de cada ente de PNET.

## Líneas de exploración nuevas, sin decisión ni ETA

1. **Múltiples canales SFTP en paralelo, uno por caja pre-configurada.** Hoy el SFTP de Provincia Net no soporta paralelismo — un lote grande (ej. "La Matanza", horas de procesamiento) bloquea a cualquier archivo que llegue detrás, porque el pool de QR pre-generado está atado a una sola caja. Si Provincia Net tuviera varias cajas (administrativamente viable, confirmado por Facundo Collerone), Bind podría procesar varios canales SFTP en paralelo sin pisarse (ejemplo usado en la reunión: "5 canales"). Hernan se lo lleva a Arquitectura (con Alejandro) — con el matiz de que los canales deberían ser elásticos, no reservar recursos ociosos la mayor parte del día para escalar solo durante el batch.
2. **Reducir el tiempo mínimo de despacho de un lote SFTP chico.** Hoy existe un intervalo mínimo de despacho del orden de ~30 minutos (un daemon que revisa cada tanto) — aceptable para un lote de cientos de miles de registros, pero excesivo para un lote chico (ej. 100 QR). Pedido de Ricardo Lavia (PNET), sin dueño ni ETA asignado.
3. **Ratio deuda-creada / QR-generado.** Hernan estimó de memoria que ~90% del tiempo de procesamiento es la generación del QR (no la creación de la deuda en sí), sin métrica dura — Provincia Net pidió el dato real para entender mejor el cuello de botella.
4. **Dato pendiente de envío de Bind a PNET:** histograma de duración de los picos/ráfagas de saturación (Bind ya tiene datos sueltos de reuniones anteriores — un pico de 108 minutos, otro de 10 — falta consolidarlos y enviarlos formalmente). Sirve para que PNET calibre su política de reintentos.

## Contexto de negocio de Provincia Net (útil para entender la demanda futura)

Provincia Net segmenta a sus propios clientes (municipios/entes) en 3 tipos: (a) 4-5 entes "muy particulares" con proceso continuo de cierre de deuda/emisión de factura, que necesitan mucho volumen en poco tiempo — exclusivos del canal SFTP, calendarizados entre sí para no cruzarse; (b) entes medianos que piden mucho volumen pero sin urgencia de tiempo — manejados de forma asincrónica; (c) clientes de consumo individual/interactivo ("de a uno") — sin ningún proceso batch, van directo contra la API, y son los que hoy reportan timeouts (ej. DEPAY). Provincia Net proyecta que este tercer segmento va a crecer fuerte en los próximos meses (nuevos sectores: telefonía, transporte, entre otros) — capturado por separado como riesgo (`2026-09-10_direccion_riesgo_crecimiento_clientes_individuales_qr`).

**Dirección estratégica de PNET (informativa, sin acción de Bind):** evalúan migrar el caso de uso de impresión en factura a un QR estático (un QR fijo por destino/factura, con el importe actualizándose por fuera) en vez de generar un QR dinámico nuevo por factura — eliminaría de raíz la contención para ese segmento. Sin fecha ni compromiso, mencionado para contexto.

## Ver también

- `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §8` — transcripción resumida completa de la reunión, con todos los participantes y el detalle punto por punto.
- `1_proyectos/prd-66_provincianet_creacion_masiva_qr/gaps.md` — gap de causa raíz por fecha específica, todavía sin resolver pero con prioridad reducida tras esta reunión.
- `1_proyectos/tareas.md` T-085/T-086/T-087 — seguimiento de los compromisos de Pablo Gomes.
- `2026-09-10_direccion_riesgo_crecimiento_clientes_individuales_qr` (contexto vivo) — riesgo de escalamiento de la contención a medida que crece la base de clientes individuales.
