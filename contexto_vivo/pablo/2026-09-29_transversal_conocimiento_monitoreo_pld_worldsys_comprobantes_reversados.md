---
id: 2026-09-29_transversal_conocimiento_monitoreo_pld_worldsys_comprobantes_reversados
pm: pablo
fecha_captura: 2026-09-29
fuente: "/sync_mails — hilo \"Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas.\" (threadId 19e93c4ee24328fc, Worldsys/Compliance — Pablo Stach, Leandro Competiello, Victoria Simonetti, Diego Scaldaferri, Nicolás Colón; 2026-06-04 a 2026-09-28)"
producto: transversal
tema: Monitoreo PLD/AML (Compliance One) — nuevo mecanismo para discriminar reversas/devoluciones de los acumuladores de alertas
tipo: conocimiento
destino_propuesto: wiki/3_recursos/cumplimiento_normativo/monitoreo_pld_worldsys_complianceone.md
tipo_destino: crear
contradice: "no — módulo distinto del mismo proveedor (Worldsys) que el ya documentado en wiki/3_recursos/detalle_productos/onboarding/integracion_worldsys_complianceone.md (ese cubre el repositorio de legajo/documentos de PRD-147; este cubre el motor de alertas PLD/AML sobre transacciones). Aclarar la relación entre ambos módulos al mergear."
confianza: alta
estado: ingestado
merge_commit:
---

Worldsys (proveedor del sistema **Compliance One**, ya conocido en el Cerebro por su módulo de legajo/KYC de Onboarding — PRD-147) opera también el motor de monitoreo transaccional PLD/AML de Bind PSP: importa un archivo de operaciones y comprobantes, y sobre ese universo corre acumuladores mensuales que disparan alertas de prevención de lavado. El requerimiento nació en una reunión del 2026-06-03 (Diego Scaldaferri — Gerente de Cumplimiento y Prevención de LA/FT/FP — señalando "un potencial riesgo no visualizado") y se resolvió técnicamente entre junio y septiembre 2026.

## Problema de negocio
Las reversas/devoluciones de operaciones (contracargos, rechazos, reembolsos) se venían informando a Compliance One como movimientos independientes, sin relación con la operación original — quedaban sumadas de más en los acumuladores que alimentan las alertas mensuales de PLD, generando falsos positivos.

## Limitación dura del motor de Compliance One
El proceso de importación de Compliance One **solo importa datos del archivo de entrada** — no vincula ni resta contra registros ya persistidos en corridas anteriores. Es decir: **no es posible** que el sistema tome una reversa, busque la operación original ya cargada y le reste el monto directamente.

## Mecanismo acordado (el único viable dentro de esa limitación)
Enviar la reversa como un **registro nuevo e independiente con monto negativo**. El acumulador suma el conjunto de operaciones del período; el monto negativo compensa al positivo de la original y el acumulador queda neto correcto — sin que el sistema "resте" nada, solo suma valores. Condición necesaria: la reversa debe traer también el CUIT/CUIL para asignarse a la persona correcta.
- **No hace falta** vincular explícitamente la reversa con la operación original para el análisis PLD — alcanza con que el monto negativo figure en el listado de operaciones (se evaluó y descartó el requisito de trazabilidad explícita).
- **Timing, limitación conocida y aceptada:** si la reversa se informa después del cierre del procesamiento mensual de alertas, no se descuenta en ese período — es una cuestión de oportunidad del dato, no resoluble por el sistema.

## Modelo de datos (interfaz de comprobantes)
- Operaciones y comprobantes son entidades distintas; el registro de una reversa se genera únicamente en comprobantes.
- Cada comprobante tiene su propio ID (`IdComprobante`), distinto del `IdOperacion`. La reversa lleva su propio `IdComprobante` (no comparte el de la original) más un campo adicional `IdComprobanteRelacionado` que apunta al `IdComprobante` de la operación que reversa. Ejemplo:
  | IdComprobante | Monto | IdComprobanteRelacionado |
  |---|---|---|
  | 778899 | $1.000 | NULL |
  | 778900 | -$1.000 | 778899 |
- Cambios de interfaz acordados con Worldsys: `NUMEROOPERACION` pasa de `IdOperacion` a `IdComprobante` (imperceptible para el análisis); la lista fija de `TIPOOPERACION` se reemplaza por una nueva interfaz de `TiposComprobantes` alimentada periódicamente (~500 tipos nuevos a incorporar); se evalúa además si el envío será por evento o incremental diario, y si el tipo de operación se amplía de 2 a 3 dígitos.
- Puntos que quedaron abiertos en el diseño (sin resolver a la fecha del hilo): si se envían todos los tipos de comprobante existentes o solo los autorizados por Bind PSP, y si la implementación inicial cubre solo Wallet o también Comercios.

## Estado de implementación (al 2026-09-28)
Worldsys confirmó una **prueba exitosa en ambiente bajo (QA)** del nuevo mecanismo, y está a la espera de que Bind envíe el **listado actualizado de tipos de operación** para cargarlo en el ambiente productivo. El objetivo de fecha, acordado desde julio, es tener el mecanismo activo **a partir del procesamiento de la primera semana de octubre de 2026** (el próximo ciclo mensual de alertas).

> Fuente: hilo de mail "Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas." — minuta original de la reunión del 03/06/2026 (Leandro Competiello), definición técnica del mecanismo por Pablo Stach (Worldsys, 06/07/2026), confirmación de prueba en QA y pedido del listado productivo por Pablo Stach (28/09/2026), seguimiento de estado por Victoria Simonetti (PLA/FT/FP, 28/09/2026).
