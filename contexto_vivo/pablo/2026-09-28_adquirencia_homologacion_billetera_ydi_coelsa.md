---
id: 2026-09-28_adquirencia_homologacion_billetera_ydi_coelsa
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_mails — mails Coelsa 'Resolución del ticket 502085' y 'Resolución del ticket 502086' (threadIds 1a0e02ab46f88262 y 1a0e02ab2d900e88), 2026-09-25/27"
producto: adquirencia
tema: Nueva billetera YDI (YPF Digital) inicia homologación de interoperabilidad QR con los dos aceptadores de Bind
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Coelsa (Integration Center Management, `icm@coelsa.com.ar`) notificó el 2026-09-25 el inicio del proceso de homologación de interoperabilidad de una nueva billetera bajo el "Procedimiento Interno de Homologación para Billeteras y Aceptadores" (vigente desde octubre 2023, mismo trámite ya documentado para otros pagadores en `mecanica_qr_coelsa.md`):

**Datos de la billetera nueva:**
- Denominación: **YDI**
- Razón social: YPF Digital SAU
- CUIT: 33718163809
- ID BILLETERA COELSA en HOMO: 112

Coelsa pidió a Bind los datos de **ambos** aceptadores propios para arrancar las pruebas cruzadas de acreditación en homologación — se abrió un ticket por cada uno:

**Ticket #502085 — Aceptador "BIND PSP":**
- Razón social: BIND PAGO SA, CUIT 30717449076
- ID PSP HOMO: 532 / ID PSP PROD: 184
- URI API Resolve/IEP HOMO: `https://gw-staging-qrbind.epays.services/resolve/instore/external/resolve`
- Dominio inverso test: `com.TESTbind`

**Ticket #502086 — Aceptador "BIND PAGOS" (Tecnología Financiera):**
- Razón social: BIND PAGOS, CUIT 30717618870
- ID PSP HOMO: 531 / ID PSP PROD: 164
- Misma URI de API Resolve/IEP HOMO y mismo dominio inverso test que el aceptador 532.

Alan Martínez (BIND, Área Técnica) respondió el 2026-09-25 con los datos de ambos aceptadores más un QR de prueba de monto abierto para cada uno. Los dos tickets llegaron a estado resuelto (encuesta de satisfacción de Coelsa) sin que quede registrado ida y vuelta de incidencias — homologación arrancó sin objeciones visibles en este hilo.

**Cronograma del proceso de pruebas (según el mail de Coelsa):**
- Comienzo de la homologación: 2026-09-25
- Reuniones vía Teams para pruebas en vivo: a partir del **2026-10-19**

**Referencia normativa citada por Coelsa** (aplica en general al régimen de homologación de billeteras/aceptadores, no solo a este caso — relevante para `cumplimiento_normativo/`): Comunicación "A" 7769 del BCRA — si el administrador (Coelsa) certifica billeteras que no completaron satisfactoriamente la integración, tiene 2 días hábiles para notificar por mail a la Gerencia de Sistemas de Pago (`sdep_vigilancia_estadisticas@bcra.gob.ar`) y a la Gerencia de Coordinación de Supervisión (`supervision@bcra.gob.ar`), pudiendo derivar en actuaciones sumariales (Ley 21.526, arts. 41 y 42).
