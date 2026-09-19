---
id: 2026-09-17_conocimiento-boton-simple-2-0-pago-unico-obligatorio-y-saneamiento-favacard
pm: nicolas
fecha_captura: 2026-09-17
fuente: "Reuniones 'Análisis COBRO' y 'Análisis de riesgo: AD V 73' (2026-09-17), minutas Gemini"
producto: adquirencia
tema: Botón Simple 2.0 pasa a operar exclusivamente con cuentas pago_unico=1 (AD V73); saneamiento de base previo al despliegue, con el caso puntual de FAVACARD (2.562 accounts)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Continuación del saneamiento de la base de datos para el parámetro `pago_unico` ya documentado en `boton_simple_2_0.md §11` (definición formal acordada 2026-08-20: 1 = Botón de Pago, 0 = RXT).

**"Análisis COBRO" (12:00) — criterio de saneamiento cerrado:** Julieta Gimenez (Fintexa) explicó que el criterio inicial para incluir el saneamiento en la versión falló porque el campo `ID caja` se hereda de las `collectors` y no permitía un empalme seguro. Se acordó en cambio identificar de manera certera a los clientes que usan **Botón 0** y actualizar su campo `pago único` a `1`, para integrarlos en el grupo de selección de CBU para pagos de deudas (según los registros de la tabla de deudas). En paralelo, se detectaron `accounts` antiguas que operan con RXT (Ticket QR, Postberry, Astropay, Cucuru, Octopus) con el campo en `1` sin operar con Botón 0 — se actualizarán a `0` vía script para evitar su uso incorrecto en el pool de Botón 0.

**Caso puntual FAVACARD** (transcripto como "Fabacar" en la minuta, mismo cliente ya identificado en `boton_simple_2_0.md §8.2`): Nicolás Colón y Julieta Gimenez detectaron que la entidad tiene **2.562 accounts** (511 con pago único en `0`, 2.051 en `1`), y que accounts creadas por cobro con `ID caja` y `ID orden` propios terminaban siendo seleccionadas incorrectamente por el pool de Botón 0 pese a pertenecer a RXT. Se acordó que el script de saneamiento **omitirá esas 511 accounts** (con `ID caja` propio y valor `0`) para que se mantengan sin cambios. Melisa Belpassi indicó que se subirá además el desarrollo sobre el mínimo de CBU cortas reutilizables, junto con una guía de ABM (solicitada a Maxi) para configurar altas de clientes nuevos y existentes.

**"Análisis de riesgo: AD V 73" (16:29) — decisión de configuración y riesgo de despliegue:** se estableció que los flujos de **Botón Simple 2.0 operen exclusivamente con cuentas configuradas con `pago_unico = 1`** (ticket AD 151, caso de uso: entidades como FAVACARD que necesitan CBUs cortas reutilizables para cobros constantes sin reasignación). Daniel Zalazar manifestó preocupación por el saneamiento de datos previo que debe completar el equipo de base de datos **antes del despliegue a las 21:00hs** del 17/09, para evitar fallas en clientes ya integrados — Andrea Orsini y Maria Eugenia Vila señalaron riesgo de problemas de transaccionalidad si el saneamiento falla. **Clasificado en rojo**, con necesidad de monitoreo riguroso post-implementación.

> Fuente: Reuniones "Análisis COBRO" (2026-09-17, sección Detalles) y "Análisis de riesgo: AD V 73" (2026-09-17, sección Detalles, "Consideración de cuentas con pago único para botón simple 2.0").
