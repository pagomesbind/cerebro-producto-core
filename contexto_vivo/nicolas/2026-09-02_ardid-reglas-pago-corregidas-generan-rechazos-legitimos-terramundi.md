---
id: 2026-09-02_ardid-reglas-pago-corregidas-generan-rechazos-legitimos-terramundi
pm: nicolas
fecha_captura: 2026-09-02
fuente: "Reunión \"Join Soporte Clientes\" (2026-09-02)"
producto: ardid
tema: El fix del bug de grupo BIN mal configurado (2026-08-26) ya está impactando en producción — las reglas de Ardid ahora rechazan correctamente, generando picos de rechazo que antes no ocurrían por el bug
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

En la reunión "Join Soporte Clientes" (2026-09-02) se reportó un caso concreto de los efectos del fix documentado en `4_archivos/contexto_ingestado/2026-08-31_ardid-bug-grupo-bin-mal-configurado-bloquea-reglas-pago-coto.md` (ya mergeado al canon en `integracion_con_productos_bind.md`): Diego Gaston Weledniger reportó un **aumento significativo de rechazos de tarjetas de débito y crédito para el cliente Terramundi** (ficha `Peak Travel (Terramundi S.A.)` en `clientes/casos_de_uso_clientes.md` — ver item de cliente relacionado). Adriana Endzeliz explicó la causa: la corrección aplicada al filtro de grupo BIN (que antes estaba mal configurado y hacía que las reglas de pago **nunca** impactaran) ahora sí está impactando correctamente en los medios de pago — por lo que transacciones que antes pasaban sin ser evaluadas ahora se rechazan si no cumplen las reglas vigentes.

Rocio Revelli quedó a cargo de: (1) corregir un error técnico adicional en las reglas de Ardid que está agravando el índice de rechazos, (2) repasar todas las reglas de entidad establecidas actualmente, y (3) evaluar las configuraciones de reglas por cada entidad. En el análisis conjunto con Gonzalo Rivera se discutieron dos límites concretos de las reglas de validación vigentes: **$300.000 por transacción** y **$2.000.000 mensuales**. Se señaló como limitación operativa la dificultad para identificar, dado un rechazo puntual, cuál regla específica lo causó — Gonzalo Rivera compartió una consulta de base de datos ad hoc para facilitar el monitoreo de rechazos por entidad y marca, y se acordó ajustar los parámetros de las reglas para reducir la fricción de UX sin resignar seguridad.

> Fuente: Reunión "Join Soporte Clientes" (2026-09-02), minuta Gemini.
