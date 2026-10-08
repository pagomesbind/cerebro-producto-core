---
id: 2026-10-08_conocimiento-pago-facil-minuta-07-10-piloto-prd-comprobante-mail-uat-26-10
pm: nicolas
fecha_captura: 2026-10-08
fuente: "Mail 'Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 7-10' — Guillermo Paolucci (Western Union) 2026-10-07; respuesta de Adriana Endzeliz (Comercial Bind PSP) 2026-10-07"
producto: servicios
tema: Pago Fácil (Bind–SEPSA) — seguimiento semanal del 07/10: estado del piloto productivo, fechas del comprobante por mail, alias fuera de octubre, pedidos de datos del pagador y de Mercedes Benz
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

Para sumar al §5 de `pago_facil_mantenimiento.md` (seguimiento semanal del Piloto Productivo Bind-SEPSA). Es la minuta que escribió Western Union, no un documento de Bind: los puntos son su lectura de la reunión.

- **Piloto en producción:** al terminar una operación, quedó en estado **INICIADA** y hubo que refrescar varias veces hasta que pasó a **confirmada**. Piden definir un tiempo mínimo. Bind ya hizo ajustes para optimizarlo.
- **Bug del contador de pago:** el countdown muestra el vencimiento del link y no los **15 minutos** que corresponden. A revisar.
- **Envío del comprobante por mail:** lo pedido el 9/9 se recibió y está OK para avanzar. **UAT la semana del 26/10, producción el 27/10.**
- **Confirmación online a las entidades:** SEPSA está analizando el documento funcional. Pendiente de SEPSA.
- **Mapeo de errores:** Brian Yuzefoff (WU) pidió más detalle de los errores. Adriana Endzeliz respondió ese mismo día: en general, si una API de Bind falla, el error es **429 (too many requests)**, y si hay caída o interrupción, **500**. Esa descripción es dudosa: ver el gap `2026-10-08_gap-pago-facil-errores-api-429-generico`.
- **Datos del pagador:** para pagos con QR y transferencia, SEPSA necesita saber desde qué billetera se pagó, y para pagos con tarjeta, con qué tarjeta. SEPSA lo está analizando. **Ese dato no va a estar en el SFTP hasta diciembre**; mientras tanto, como contingencia, se baja del Admin.
- **Alias para pagos con transferencia:** en curso. Pasa a producción en la próxima versión, **no entra en la de octubre 2026**. Piden priorizarlo y definir fecha.
- **Quitar la flecha del checkout:** Bind pasó una propuesta con pantallas y WU devolvió comentarios de Marketing. Es un cambio de front, en curso. Adriana Endzeliz tiene que confirmar la fecha de pasaje e intentar juntarlo con el alias.
- **Mercedes Benz:** necesita identificar en el reporte transaccional el **CUIT del pagador** (titular de la billetera o cuenta que transfiere) y la descripción del CVU de destino que ve el usuario. Hay que validar si el dato está en el archivo batch; en el archivo diario el campo está. Se va a coordinar una reunión con IT de BPG para definir el TID.
- **Conciliaciones:** habrá una reunión en la que Bind les explique qué contienen los archivos de conciliación por SFTP.

> Fuente: Mail "Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 7-10" — Guillermo Paolucci (Western Union), 2026-10-07; respuesta de Adriana Endzeliz, 2026-10-07.
