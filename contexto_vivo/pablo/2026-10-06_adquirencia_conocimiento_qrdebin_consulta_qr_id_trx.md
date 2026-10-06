---
id: 2026-10-06_adquirencia_conocimiento_qrdebin_consulta_qr_id_trx
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_mails — mail \"Fwd: Nueva respuesta en tu ticket #495865 - Consulta de operación por qr_id_trx PRODUCCION\", forward de Gonzalo Rivera, 2026-10-05, threadId 1a10d49a05bafc03, contenido original del ticket Coelsa de soporte 2026-09-15"
producto: adquirencia
tema: Endpoint Coelsa para consultar operaciones QRDebin por QR_ID_TRX — insumo para diagnosticar demoras de pagos QR en estado 4/5
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Gonzalo Rivera reenvió el 2026-10-05 la respuesta de Soporte Coelsa al ticket #495865 ("Consulta de operación por qr_id_trx PRODUCCION", respondido originalmente el 2026-09-15 por Franco Ferrufino de Soporte Coelsa), marcando explícitamente que es **"lo relacionado a la demora de los pagos QR cuando quedan con estado 4 o 5"** — es decir, lo trae como insumo técnico para ese problema recurrente, no como novedad aislada.

**Contenido técnico del ticket (Coelsa):**

- El servicio `GET Debin3` se consulta usando como parámetro el `ori_trx_id` — identificador único para operaciones de tipo TRANSFERENCIA, DEBIN, TRXPL, CASHOUT, entre otras.
- Para el caso específico de **QRDebin**, el identificador único a usar es el **`QR_ID_TRX`** (alfanumérico) — distinto del `ori_trx_id` general.
- Endpoint para consultar una operación QRDebin por su `QR_ID_TRX`: **`GET /apiDebinV1/QR/QRDebin/{qr_id_trx}/{id_psp}`**.
- Si no hay una PSP del lado vendedor (porque Bind es la billetera actuando del lado comprador/vendedor sin un PSP externo intermediario), el valor de `{id_psp}` a colocar es **`0`**.

**Por qué importa:** esto es la pieza de API que permite, dado un `QR_ID_TRX`, consultar el estado real de una operación QR directamente en Coelsa — insumo directo para diagnosticar casos de pagos QR que quedan "colgados" en estado 4 o 5 (demora), un problema que Gonzalo Rivera viene señalando como recurrente en Integraciones y Soporte. No se identificó en este mail un caso puntual nuevo de estado 4/5 — es la documentación de la herramienta de diagnóstico, no un incidente nuevo.
