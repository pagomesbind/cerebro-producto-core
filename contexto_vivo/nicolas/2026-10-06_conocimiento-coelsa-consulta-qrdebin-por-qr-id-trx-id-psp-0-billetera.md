---
id: 2026-10-06_conocimiento-coelsa-consulta-qrdebin-por-qr-id-trx-id-psp-0-billetera
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Mail 'Fwd: Nueva respuesta en tu ticket #495865 - Consulta de operación por qr_id_trx PRODUCCION' — respuesta de Soporte Coelsa (Franco Ferrufino) del 2026-09-15, reenviada por Gonzalo Rivera el 2026-10-05"
producto: adquirencia
tema: Coelsa — cómo consultar una operación QRDebin por qr_id_trx en producción (id_psp = 0 cuando Bind es la billetera y no hay PSP vendedor)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/coelsa_qr_catalogo_apis_tecnico.md
tipo_destino: actualizar
contradice: "no (en el canon). Sí corrige una restricción registrada en 1_proyectos/bajar-tiempos-pagos-qr/proyecto.md (reunión 2026-08-31): 'un banco no puede consultar operaciones donde no fue el iniciador'"
confianza: alta
estado: en_cola
---

Respuesta de Soporte Coelsa al ticket **#495865** ("Consulta de operación por qr_id_trx PRODUCCION"), abierto por Agustín Grau (Fintexa) con Gonzalo Rivera en copia.

- **Cada tipo de operación tiene su identificador único:**
  - `GET Debin3` se consulta con `ori_trx_id`, el ID único de operaciones TRANSFERENCIA, DEBIN, TRXPL, CASHOUT, entre otras.
  - En **QRDebin** el ID único es `QR_ID_TRX`, que es **alfanumérico**.
- **Endpoint para QRDebin:** `GET /apiDebinV1/QR/QRDebin/{qr_id_trx}/{id_psp}`. Ya está en el catálogo. Lo nuevo es la regla del segundo parámetro.
- **Regla de `id_psp`:** si **no hay PSP del lado vendedor** y **Bind es la billetera**, se manda **`0`**.

**Por qué importa.** Gonzalo Rivera lo reenvió el 05/10 a los 3 PM, Mariana Nadalin incluida, como lo relacionado con la **demora de los pagos QR que quedan en estado 4 o 5**. En la reunión del 31/08 de `bajar-tiempos-pagos-qr` (PRD-199) se había dicho que no había forma estándar de reconsultar en Coelsa esas operaciones trabadas: no había un Coelsa ID persistido, la consulta por QRTRXID no respondía de forma consistente y regía la restricción de que "un banco no puede consultar operaciones donde no fue el iniciador". La respuesta de Coelsa abre la vía para consultar por `qr_id_trx` con `id_psp = 0` en el rol de billetera. Falta confirmar que funcione en producción para los casos trabados.

> Fuente: Mail "Fwd: Nueva respuesta en tu ticket #495865 - Consulta de operación por qr_id_trx PRODUCCION" — Franco Ferrufino, Soporte Coelsa (2026-09-15), reenviado por Gonzalo Rivera (2026-10-05).
