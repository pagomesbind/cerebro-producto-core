---
id: 2026-09-16_conocimiento-worldsys-reversas-comprobantes-resuelto-octubre
pm: nicolas
fecha_captura: 2026-09-16
fuente: "Mail 'Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas.' — hilo 2026-06-04 a 2026-09-15, mensajes nuevos del 2026-09-10 y 2026-09-15"
producto: transversal
tema: Se resuelve el criterio de integridad de LAVADOOPERACIONES (comprobantes vs. reversas) que estaba "sin resolver" desde 2026-07-16 — entra en vigor 01/10/2026
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md §2
tipo_destino: actualizar
contradice: "no contradice — resuelve el punto marcado 'sin resolver, 2026-07-16' en reporteria_worldsys_bcra.md §2, y desbloquea la tarea T-019 de 2_areas/tareas.md ('Nicolás Colón está bloqueado sin poder avanzar')"
confianza: alta
estado: en_cola
---

**Resolución del criterio, y cronología completa desde la reunión de discovery (03/06/2026):**

El punto §2 de `reporteria_worldsys_bcra.md` ("Integridad de LAVADOOPERACIONES: comprobantes vs. movimientos, y tratamiento de reversas") quedó marcado como "sin resolver" el 2026-07-16, bloqueando a Nicolás Colón (T-019 en `2_areas/tareas.md`) desde hacía ~2 meses. El hilo de mail completo muestra que sí se resolvió:

1. **Reunión inicial (03/06/2026, minuta de Leandro Competiello — Worldsys/PMO):** se acuerda evaluar cómo incorporar ~500 nuevos tipos de comprobante y cómo distinguir reversiones/devoluciones/contracargos/rechazos de operaciones originales, sin duplicar impacto en los acumuladores de alertas PLD.
2. **Intercambio técnico (09/06 y 06/07/2026, Pablo Stach — Worldsys):** se descarta la opción de "matchear la reversión contra el registro original ya persistido y restarle el monto" — Compliance One (el motor de ingesta de Worldsys) **no soporta operaciones aritméticas contra registros ya cargados**, solo importa lo que viene en el archivo de entrada. Se confirma como única vía viable: **enviar la reversión como un registro nuevo e independiente, con monto negativo**, siempre que viaje el CUIT/CUIL. Sobre trazabilidad: no hace falta que el sistema catalogue el registro como "reversión" — alcanza con que el monto negativo figure en el listado para que el acumulador dé el neto correcto. Riesgo de timing reconocido y aceptado: si la reversión se informa después del cierre del procesamiento mensual de alertas, ese período no la descuenta (queda para el siguiente).
3. **Archivo de ejemplo (01/09/2026, Nicolás Colón):** Nicolás envía a Worldsys el archivo con los 3 cambios esenciales acordados — (a) cambio de `IdOperacion` por `IdComprobante` en el campo `NUMEROOPERACION` (imperceptible para Worldsys), (b) reemplazo de la lista fija de `TIPOOPERACION` por la nueva interfaz `TiposComprobantes` (alimentada periódicamente), (c) inserción de registros de devolución con monto negativo.
4. **Confirmación de recepción (10/09/2026, Pablo Stach):** Worldsys confirma que recibió el archivo de ejemplo y arranca pruebas de ingesta.
5. **Escalamiento de urgencia (10/09/2026, Diego Scaldaferri, Gerente de Cumplimiento y Prevención de LA/FT/FP de BIND):** "Importante avanzar con este cambio ya que tenemos un potencial riesgo no visualizado" — confirma que mientras el cambio no esté en producción, las reversas/devoluciones siguen sin netearse en los acumuladores de alertas PLD (riesgo de falsos positivos o, peor, de que el criterio de "movimientos de dinero" que pedía el área de PLD según Emma Vignoles nunca haya distinguido una reversa de una operación real).
6. **Plan de implementación (15/09/2026, Leandro Competiello):** Worldsys confirma que el tema lo toma él junto con el Account Manager Gonzalo Quintana; enviarán un documento de alcance/tareas/horas a consumir (es una evolución, no un cambio menor); coordinarán una prueba de captura en ambiente QA la semana del 21/09; **la intención es que el nuevo esquema entre en vigencia a partir del procesamiento del 01 de octubre de 2026** (primera corrida del mes).
7. **Pedido de confirmación de Nicolás (15/09/2026, 18:59):** Nicolás pregunta explícitamente si Bind PSP puede avanzar con el desarrollo de su lado y si el archivo enviado es correcto — Worldsys responde el mismo día confirmando el plan del punto 6, sin objetar el archivo.

**Nota:** el campo agregado finalmente fue "un campo nuevo con el ID de comprobante relacionado" (`IdComprobanteRelacionado`) — coincide exactamente con la alternativa que `reporteria_worldsys_bcra.md §2` ya tenía documentada como "se está evaluando en cambio". Combinado con el monto negativo del punto 2 de arriba (ambos mecanismos conviven: el monto negativo neteando el acumulador, el ID relacionado dando trazabilidad para el analista).

> Fuente: hilo de mail "Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas." (lcompetiello@worldsys.com.ar, pstach@worldsys.io, msimonetti@bind.com.ar, dscaldaferri@bind.com.ar, ncolon@bind.com.ar — 2026-06-04 a 2026-09-15).
