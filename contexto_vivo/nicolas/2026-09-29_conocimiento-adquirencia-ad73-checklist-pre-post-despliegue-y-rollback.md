---
id: 2026-09-29_conocimiento-adquirencia-ad73-checklist-pre-post-despliegue-y-rollback
pm: nicolas
fecha_captura: 2026-09-29
fuente: "Mail 'MINUTA - Reunión de Pre-despliegue AD 73: Jue, 24 de sept de 2026' — Matías Alzogaray, enviado 2026-09-28"
producto: adquirencia
tema: AD V73 — nueva fecha del pase (martes 29/09, 20:30 acordado vs. 21hs en la ficha de riesgo), MS afectados, excepciones del rollback y checklist pre/post despliegue por ticket
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md
tipo_destino: actualizar
contradice: "sí — el párrafo 'Despliegue AD V73' de incidente_qr_masivo_provincia_net.md dice 'fecha confirmada 24/09/2026, 21hs'. Ese pase se canceló y se reprogramó al martes 29/09 a las 20:30 (ver también el item en_cola 2026-09-25_conocimiento-v73-adquirencia-y-wallet-reprogramadas y el capturado 2026-09-29_conocimiento-ad-v73-pase-confirmado-29-09-y-v74-en-planificacion). Inconsistencia menor dentro de la misma minuta: la ficha de riesgo pegada al final todavía dice 'Hora: 21 hs'"
confianza: alta
estado: ingestado
merge_commit: 3492d04
---

**Fecha y hora.** El pase se reprogramó "de manera definitiva" al **martes 29/09 a las 20:30hs** (se había sugerido el lunes y se descartó para dar tiempo a corregir liquidaciones y re-testear). La ficha de riesgo que acompaña la minuta mantiene **Hora: 21 hs** y **duración de 2 horas y media**: probablemente quedó sin actualizar desde la versión del 24/09.

**Errores bloqueantes que motivaron la cancelación.** La minuta cita los tickets **1361, 1791 y 1360**: los totales del PDF de liquidación restaban **devoluciones y desconocimientos por duplicado**. (El mail de Fintexa del 25/09 fijó después AD-1822 como el bloqueante del nuevo pase; ver item `2026-09-26_conocimiento-liquidaciones-ad73-definiciones-registro-y-regeneracion`.)

**Microservicios/APIs afectados:** PaymentAcceptor.Rendicion, PaymentAcceptor.Deuda, PaymentAcceptor.Promotions, PaymentAcceptor.WorkflowPagos, PaymentAcceptor.CardOrchestrator, Middleware.Financial, Middleware.Aggregator, Shared.Comercio, Shared.Comisiones, Shared.Pdf, Bind.Configuracion.Admin, Bind.Configuracion.BFF, Bff.BackofficeComercio, Web.BackofficeComercio, Web.Portal20, BotonSimple.PaymentForm.Web.

**Rollback.** Para la mayoría de los MS: revertir las imágenes en AKS (`kubectl set image deployment/{ms-name}`). Excepciones críticas:
- DAD-2437 (pago único en Botón Simple 2.0) tiene su propio script inverso, `SaneamientoPagoUnico-ROLLBACK.sql`.
- DAD-2209/2257, DAD-2294/2493 y el flujo de Beneficiarios (DAD-2290/2293/2492) se revierten obligatoriamente en conjunto.
- DAD-2265 (corrección de unicidad de emails) no borra los duplicados que se hayan creado durante el pase.

**Checklist por ticket (pre / durante / post pase):**

| Ticket AD | DAD | Qué es | Acción |
|---|---|---|---|
| AD-87 | DAD-489 | [Promociones][API] "Todas las condiciones enviadas son inválidas" aun siendo válidas | Post: dar de alta un CF de prueba y ver si funciona |
| AD-1463 | DAD-2378 | [Admin][Convenio] el alta de convenio no valida máximo contra mínimo | Post: crear un convenio y validar que se cobren bien las comisiones |
| AD-1398 | DAD-2257 | [Cobro] Separar desconocimientos de devoluciones en el PDF de liquidación | Pre: avisar a clientes y actualizar la web de developers con el formato de los archivos |
| AD-1361 | DAD-2209 | [Cobro] Corregir archivos y registros de liquidaciones | Pre: avisar a clientes y actualizar la web de developers (Gonzalo Rivera y equipo) |
| AD-1234 | DAD-1986 | [Portal] el Excel de transacciones no trae la fecha de las devoluciones | Verificar durante el pase |
| AD-1237 | DAD-1984 | [Portal] error o cierre de página al crear usuario operador | Verificar durante el pase |
| AD-1676 | DAD-2943 | [Soporte] demora de más de 35s en la disponibilidad de datos de QR Dinámico | Pre: avisar a Provincia Net. Post: Infra revisa la performance de las colas nuevas |
| AD-1512 | DAD-2437 | [BS2.0] Considerar solo Accounts con PagoUnico=1 | Post: revisar y quedar atentos |
| AD-1392 | DAD-2231 | [Mejora interna] baja y deshabilitación de formas de pago que no liquidan impuestos | Post: revisar los parámetros en prod al liquidar (día siguiente al pase) |

> Fuente: Mail "MINUTA - Reunión de Pre-despliegue AD 73: Jue, 24 de sept de 2026 a las 4:30pm – 5:00pm (GMT-03)" — Matías Alzogaray (2026-09-28).
