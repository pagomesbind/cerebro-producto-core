# PSP as a Service (Norma 8432 BCRA) — modelos de aceptador/agrupador y retención de impuestos

> Estado: en producción.

> Fuente: Reunión "PeYa <> Bind PSP - Alternativas modelos" (minuta Gemini, 2026-07-14). Caso de uso concreto: integración de **PeYa (PedidosYa)**, pero el contenido de esta página es el modelo general que Bind PSP ofrece a cualquier cliente que quiera operar como "PSP as a Service" — no es exclusivo de PeYa.

## 0. Contexto normativo

La **Norma 8432 del BCRA** regula la actividad de los Proveedores de Servicios de Pago bajo la modalidad **"PSP as a Service"** (un PSP presta su licencia/infraestructura a otro actor para que este último ofrezca servicios de pago a sus propios comercios). Bind PSP tuvo que informar y documentar en detalle ante el Banco Central todos los procesos, riesgos y medidas de mitigación de cada cliente que opera bajo esta modalidad. A raíz de esta revisión, el Banco Central observó ajustes puntuales sobre el modelo que Bind ya venía operando con clientes de este tipo (no lo invalidó, pero exige adecuaciones).

Caso particular: los modelos con PeYa son **atípicos** porque hay **tres PSPs en la cadena** — Wibond (proveedor tecnológico de PeYa como PCP/proveedor de cuenta de pago), PeYa y Bind PSP — lo cual complejiza la definición de quién es agente de retención en cada tramo.

## 1. Modelo 1 — Bind PSP como aceptador y agrupador (con cuenta espejo)

Bind PSP toma ambos roles: **aceptador** (procesa el cobro QR/transferencia) y **agrupador** (agrupa la liquidación de todos los comercios del cliente). Cada comercio se da de alta con su CUIT/quid real.

- **Liquidación de impuestos en lote:** Bind PSP calcula impuestos por lote (no en tiempo real por transacción) — cuello de botella conocido, con demoras observadas de 1,5 a 5 horas en pruebas de estrés. Mitigación en curso: tomar lotes chicos (parametrizable, arrancando en ventanas de 30-60 min) priorizando transacciones con plazo de liquidación = 0.
- **Cuenta espejo (CVU):** como el comercio no vive en la Wallet de Bind PSP sino en la tecnología del cliente (PeYa), Bind PSP crea una **CVU espejo** propia donde Coelsa acredita en línea el cobro. Bind PSP, como agente de retención, debe debitar el impuesto de esa cuenta espejo **antes** de que el cliente se lleve los fondos a la cuenta de libre disponibilidad real del comercio — el Banco Central exigió esta adecuación explícitamente (antes no estaba tan formalizada).
- **Riesgo de doble imposición SIRTAC/CIRCUBA:** dos hechos imponibles distintos pueden aplicar sobre la misma transacción si no se distinguen bien — **SIRTAC** grava el cobro (PCT) y lo retiene el agente de retención del cobro (Bind PSP en este modelo); **CIRCUBA** (impuesto de "wallet"/CIRCUPA) grava la acreditación en la cuenta de pago (el "call-in") y lo retiene el proveedor de la cuenta de pago (PeYa/Wibond). Si Wibond aplica CIRCUBA automáticamente a toda acreditación sin distinguir si esa transacción ya tuvo SIRTAC retenido por Bind, se genera doble retención sobre el mismo hecho. Sin resolución cerrada a la fecha — Luciana Rudaz (Bind PSP) se llevó el punto para validar con el área de impuestos; alternativas evaluadas: (a) aplicar CIRCUBA a todo y devolver vía comprobante de crédito cuando llegue el webhook de débito de SIRTAC, o (b) esperar el segundo webhook para decidir si corresponde CIRCUBA — ambas consideradas riesgosas para la experiencia (hasta 4 movimientos simultáneos en la wallet del comercio por una sola transacción).
- **Latencia del cálculo de impuestos:** hoy el cálculo no es en tiempo real por límites de infraestructura (no de diseño) — Bind PSP ya está trabajando para bajarlo a <2 minutos por transacción (mismo problema que Bind PSP tiene internamente con sus propios comercios de cuenta espejo, ver nota comparativa de Pablo Gomes en la reunión).
- **Facturación:** en este modelo, como Bind PSP es agente de retención, es Bind PSP quien debe emitir factura al comercio (no solo una liquidación informativa) — punto que en el pasado no convencía a PeYa (no quería que un tercero facture directamente a sus comercios).

## 2. Modelo 2 — PeYa como agrupador (sin cuenta espejo) — considerado el más limpio

PeYa pasa a ser el **agrupador** de sus comercios (habilitado porque PeYa también es PCP regularmente inscripto en el Banco Central) y el **agente de retención**. Bind PSP sigue siendo el aceptador y le presta el servicio a PeYa (no a los comercios directamente).

- **Sin cuenta espejo:** toda la acreditación va a una CVU normal (no espejo) creada por Bind PSP en Coelsa al momento del alta del comercio — es una "cuenta recaudadora" individualizada por comercio, sin saldo propio, subcuenta de la CVU recaudadora del aceptador.
- **Liquidación por archivo o evento:** Bind PSP calcula los impuestos por lote (igual mecánica que el Modelo 1) y pone a disposición de PeYa un **archivo de liquidación** con el detalle de impuestos retenidos por comercio; PeYa hace el débito real a sus comercios en un momento posterior (ej. T+1). Alternativa ya evaluada y bien recibida por el cliente: sumar un **evento/webhook de notificación del cálculo de impuestos** (similar al webhook de pago) además del archivo — el archivo seguiría usándose para conciliación. También es posible consultar el detalle de impuestos calculados directamente dentro de cada transacción vía API.
- **Facturación:** la emisión de factura al comercio pasa a estar en cabeza de PeYa (no de Bind PSP) — puntos abiertos: (a) por qué concepto factura PeYa a sus comercios sin ser aceptador (riesgo de estar cobrando "servicios de agregador/aceptador PSP de QR" sin tener esa licencia), y (b) ineficiencia impositiva de Ingresos Brutos al facturar una comisión que no es ingreso real de PeYa. Ambos puntos quedaron para validación conjunta con los equipos de contabilidad/impuestos de ambas partes.
- **Gap de integración:** según Bind PSP (Luciana Rudaz), este modelo ya está desarrollado y listo — el único desarrollo pendiente sería el evento de notificación de liquidación, si el cliente lo prefiere sobre el archivo.

## 3. Estado a la fecha de esta reunión (2026-07-14)

Ninguno de los dos modelos está cerrado — quedaron dos validaciones pendientes en simultáneo con los equipos de contabilidad/impuestos de Bind PSP y de PeYa: (1) el tratamiento SIRTAC/CIRCUBA para evitar doble imposición, y (2) el esquema de facturación (concepto, quién factura a quién, riesgo de encuadre como aceptador sin licencia en el Modelo 2). Se programó una reunión de seguimiento con ambos equipos contables para el día siguiente. El equipo de Bind PSP (Luciana Rudaz) se inclina por el Modelo 2 como "el más limpio y prolijo", con gap de integración muy bajo para el cliente.

## Ver también

- [detalle_productos/adquirencia/agrupador_mayorista.md](agrupador_mayorista.md) — modelo de entidad agrupadora liquidando a un único CBU/CVU propio (mecánica de agrupación en general, sin el componente normativo de PSP as a Service).
- [detalle_productos/siscri/configuracion_entidades.md](../siscri/configuracion_entidades.md) — motor de cálculo de impuestos (SISCRI) que ejecuta el cálculo por lote mencionado acá, incluye el parámetro `IIBB_SIRTAC_Liq` por entidad.
- [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md) — gap abierto sobre CVU emitidas por Banco Industrial a entidades no-PSPCP (2026-06-25), mismo tipo de tensión regulatoria en otro contexto.

---
*Última actualización: 2026-07-15 — Creación del archivo (`/sync_meetings`), a partir de la reunión "PeYa <> Bind PSP - Alternativas modelos" del 2026-07-14.*
