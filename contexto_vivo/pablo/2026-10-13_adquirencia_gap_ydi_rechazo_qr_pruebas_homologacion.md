---
id: 2026-10-13_adquirencia_gap_ydi_rechazo_qr_pruebas_homologacion
pm: pablo
fecha_captura: 2026-10-13
fuente: "/sync_mails — hilos 'Homologación Billetera YDI - Aceptador Tecnología Financiera ID 531' (threadId 1a0d90d31e67036b) y 'Homologación Billetera YDI - Aceptador BindPagos ID 532' (threadId 1a0d90d19f1e5027), Coelsa / Globant (Gianna Pirotta, en representación de YDI) / Alan Martínez, 2026-10-09"
producto: adquirencia
tema: Pagos de prueba rechazados durante la homologación de interoperabilidad QR de la billetera YDI (YPF Digital) con los dos aceptadores de Bind — sin diagnóstico todavía
tipo: gap
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "complementa el item ya mergeado/en curso de homologación de YDI (2026-09-28_adquirencia_homologacion_billetera_ydi_coelsa, ya en_cola/fuera de disco local) — ese item documentaba el inicio del proceso de homologación (25/09) y el intercambio de datos de aceptador; este es un hallazgo posterior del mismo proceso, sin contradicción de hechos, solo delta cronológico."
confianza: alta
estado: en_cola
merge_commit:
---

**Contexto:** la homologación de interoperabilidad QR de la nueva billetera YDI (YPF Digital SAU) con los dos aceptadores de Bind (BIND PAGOS ID PSP HOMO 531 / PROD 164, y BIND PSP ID PSP HOMO 532 / PROD 184) arrancó el 25/09/2026 con el intercambio de datos de conexión (URI de API Resolve/IEP en HOMO, access_token, dominio inverso test) entre Alan Martínez (Bind) y Coelsa.

**Delta del 09/10/2026 — primeras pruebas de pago fallan en ambos aceptadores:** Gianna Pirotta (Globant, en representación técnica de YDI) reporta en ambos hilos que al leer los QR de Bind, los pagos de prueba fueron **rechazados**. Comparte el detalle de una transacción por cada aceptador:

- Aceptador 531 (BIND PAGOS): `creation_date: 2026-10-09T21:02:25.06`, `total_payment_amount: 1900.00`, `ID COELSA: 0V1JXON1704RL1VNZ64EL7`.
- Aceptador 532 (BIND PSP): `creation_date: 2026-10-09T20:46:04.61`, `total_payment_amount: 1530.00`, `ID COELSA: L18MKX9R106PX0O9O6WYV4`.

**Gap:** al cierre de esta corrida, ninguno de los dos hilos tiene respuesta de Bind (Alan Martínez) ni diagnóstico de la causa del rechazo — no se sabe si es un problema de configuración del lado de YDI/Globant, de Coelsa, o de los aceptadores de Bind. Dado que las pruebas en vivo recién comienzan el 19/10 según el cronograma original, esto podría ser una prueba preliminar o un primer intento fallido que conviene seguir antes de esa fecha.

> Fuente: hilos "Homologación Billetera YDI - Aceptador Tecnología Financiera ID 531" (`1a0d90d31e67036b`) y "Homologación Billetera YDI - Aceptador BindPagos ID 532" (`1a0d90d19f1e5027`), Gianna Pirotta (Globant), 2026-10-09.
