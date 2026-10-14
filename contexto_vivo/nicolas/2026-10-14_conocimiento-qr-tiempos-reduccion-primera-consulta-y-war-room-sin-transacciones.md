---
id: 2026-10-14_conocimiento-qr-tiempos-reduccion-primera-consulta-y-war-room-sin-transacciones
pm: nicolas
fecha_captura: 2026-10-14
fuente: "Reunión \"Wallet - Tiempos de QR\" (2026-10-13), solo resumen del mail de Gemini (Drive invalidado, sin minuta completa)"
producto: adquirencia
tema: Pagos QR — nuevos reclamos de demora (>7,5 s), acuerdo de bajar 2,5 s la primera consulta a Coelsa y ajustar la segunda, y War Room por ausencia total de transacciones
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "Actualiza la config vigente de doble consulta documentada en mecanica_qr_coelsa.md (T1 = 4,5 s / T2 = +2 s desde la respuesta de T1, decidida el 2026-08-31). Los valores nuevos exactos no están en el resumen."
confianza: media
estado: en_cola
---

**Qué se habló (reunión "Wallet - Tiempos de QR", 2026-10-13):**

- **Reclamos de tiempos.** Vuelven los reclamos por demoras en pagos QR de Wallet: hay pagos que **superan los 7,5 segundos**. El resumen no dice qué clientes reclamaron.
- **Cambio de configuración acordado.** Se acuerda **bajar 2,5 segundos la primera consulta** a Coelsa (T1) y **ajustar la segunda** (T2). Si la base es la config vigente desde el 31/08 (T1 = 4,5 s), el T1 nuevo quedaría en unos **2 s**. Es una inferencia: el resumen no da los valores finales, ni dice si el cambio ya se aplicó en producción.
- **Falla crítica y War Room.** Durante la reunión se detectó una **ausencia total de transacciones** y se abrió un canal de War Room. El resumen no dice qué producto ni qué ventana afectó, ni cómo se resolvió.
- **Informe de seguimiento.** Juan Pablo Carubelli (Keep IT Simple) y Lautaro Duarte arman un informe comparativo de tiempos de pagos QR, **una semana antes contra una semana después** del cambio de configuración. La minuta dice "6 al 13 de marzo" y "13 al 20 de marzo", lo que no cierra con la fecha de la reunión (13/10). Es casi seguro un error de transcripción por **octubre** (6–13/10 antes, 13–20/10 después).

**Por qué importa:** el análisis del 2026-08 (PRD-199) desaconsejaba bajar T1 por debajo de ~4 s, porque el promedio de resolución de Coelsa está en esa zona y un T1 muy corto solo agrega consultas que vuelven sin resultado. El cambio va en la dirección contraria y hay que medirlo con el informe de Carubelli/Duarte.

> Fuente: Reunión "Wallet - Tiempos de QR" (2026-10-13), resumen del mail de Gemini.
