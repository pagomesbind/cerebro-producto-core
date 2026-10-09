---
id: 2026-10-09_conocimiento-ardid-wallet-v73-integraciones-alta-cuentas-auditoria-rechazos
pm: nicolas
fecha_captura: 2026-10-09
fuente: "Reunión 'INTEGRACIONES Y SOPORTE' (2026-10-08, ~10:00), solo el resumen del mail de Gemini (mail Gmail 1a11bc9179e197d5). Drive desconectado, sin minuta completa"
producto: ardid
tema: "Wallet V73 vista desde Integraciones/Soporte: las operaciones pasan por Ardid, hay una tabla de auditoría de rechazos, una caída de Ardid frena las transacciones, se controla a diario el alta de cuentas, se avisa a Getnet y los archivos de devolución llegan separados"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no. Complementa el item 2026-10-08_conocimiento-wallet-deshabilitacion-automatica-bloqueo-ardid-comportamiento-real-w73 (todavía capturado), que es la mirada de la historia; este agrega la mirada operativa para Integraciones/Soporte"
confianza: media
estado: en_cola
---

**Contexto.** El 08/10, Producto (Nicolás Colón) le presentó al equipo de Integraciones y Soporte cómo cambia la operación con la **versión 73 de Wallet**. Solo hay disponible el resumen del mail de Gemini; para completar el detalle hace falta la minuta de Drive.

**Qué cambia operativamente con W73:**
- **Las operaciones de Wallet pasan por Ardid.** Ardid analiza cada operación antes de que se ejecute.
- **Nueva tabla de auditoría** que guarda los rechazos de Ardid. Es la fuente para que Soporte investigue por qué se rechazó una operación.
- **Si Ardid se cae, se frenan las transacciones.** Ardid queda en el camino crítico, sin bypass según el resumen. Es un punto de riesgo operativo para Soporte y conviene confirmar contra el diseño si existe algún modo degradado.
- **Control del alta de cuentas en Ardid.** Una consulta SQL diaria identifica las cuentas de Wallet que no quedaron dadas de alta en Ardid. Para el proceso de alta hay además una colección de JMeter. Se recomienda **automatizar** la consulta (responsables: Franco Giménez y Pablo Salto) para que corra todos los días y mande el resultado por mail. Producto comparte la consulta y la colección en el grupo de Integraciones. Es la misma práctica de "monitoreo diario del alta de cuentas pendientes en Ardid" que ya salió en "W 73 - Análisis de riesgos" (01/10).
- **Getnet:** hay que avisarle por mail del cambio en el manejo de las operaciones de pago. Responsable: "Gómez", nombre dudoso en la minuta.
- **Reglas de rechazo:** el grupo va a extraer y mandar a Integraciones la tabla completa de reglas de rechazo de Ardid con sus identificadores, para que Soporte pueda mapear cada rechazo a su regla. Se vincula con el identificador de regla en los rechazos (item `2026-10-06_conocimiento-ardid-rechazos-hash-alertas-configurables-identificador-regla`).
- **Nuevo circuito para personas jurídicas** en la incorporación. El resumen no dice si se refiere al onboarding de PJ (item `2026-10-08_conocimiento-onboarding-pj-ingreso-via-jira-documentacion-sa-srl-y-res-224`) o a la segmentación PJ de Ardid (PRD-263).
- **Los archivos de devolución llegan separados.** El resumen no da más detalle.

**Otros temas de la reunión:**
- Comisión aplicada al caso **Uber**: Franco Giménez la consulta con Comercial para dar una respuesta formal.
- Hay que ponerle **nombre a la guía externa** para clientes. El resumen no aclara de qué producto es la guía; probablemente sea la de W73/Ardid.

> Fuente: Reunión "INTEGRACIONES Y SOPORTE" (2026-10-08), resumen del mail de Gemini.
