# Riesgos del Contexto Fijo — Bind PSP

> Riesgos que afectan a la plataforma o al negocio en general, no a un proyecto puntual — esos viven en la sección de riesgos de su propio `proyecto.md`. Compartido entre los tres PM/PO: **solo lo escribe `/context_merge`**. Cada PM aporta un riesgo de este alcance como item `tipo: riesgo` en `contexto_vivo/`.

## Capacidad del proveedor de infraestructura (Fintexa)

Dos reducciones de dotación consecutivas en el equipo de Fintexa asignado a Bind PSP (julio y agosto 2026 — Soporte, QA, SRE, Dev Wallet/Adquirencia/Mobile POS). Ver detalle en [3_recursos/arquitectura_sistema/relacion_con_fintexa.md](../3_recursos/arquitectura_sistema/relacion_con_fintexa.md).

## Seguridad — Ardid no aísla datos entre clientes (multi-tenencia)

Fintexa confirmó que Ardid no aísla datos entre organizaciones — clientes como Coto y BIN podrían ver operaciones ajenas entre sí. Sin fecha de resolución confirmada, del lado de Pentass. Ver [3_recursos/arquitectura_sistema/incidentes_de_plataforma.md §4](../3_recursos/arquitectura_sistema/incidentes_de_plataforma.md).

## Compliance — integridad de `LAVADOOPERACIONES` sin resolver

Conflicto de diseño abierto hace ~2 meses (a la fecha del hallazgo) sobre si la fuente de verdad del reporte antilavado a Worldsys/BCRA debe ser la tabla de comprobantes o de movimientos, y cómo tratar reversas. Bloquea desarrollo de Nicolás Colón. Ver [3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md §2](../3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md).

## PCI DSS del proveedor Fintexa — certificación sin confirmar en el texto narrativo del documento de arquitectura

La única mención de PCI DSS v4.0 Level 1 en el documento de arquitectura del proveedor es un diagrama; el texto narrativo y el resumen ejecutivo no lo listan entre los estándares de compliance. Ver [3_recursos/arquitectura_sistema/modelo_de_seguridad.md](../3_recursos/arquitectura_sistema/modelo_de_seguridad.md) y [gaps_y_preguntas.md](gaps_y_preguntas.md).

## Desalineación entre comisión facturada a la entidad y comisión real cobrada por el procesador

Si una configuración de comisión queda mal cargada en el sistema interno de Bind PSP y Soporte no lo detecta a tiempo, Bind PSP puede seguir facturando a una entidad/comercio con un arancel más bajo del real mientras el procesador (Coelsa u otro) le cobra a Bind PSP el arancel completo por cada transacción — la diferencia es pérdida neta directa, no solo un problema de UX/proceso. Precedente cuantificado (causa distinta, mismo patrón): pérdida de **$15.000.000 ARS en un solo mes**, sin fecha exacta ni detalle técnico registrado — solo como referencia de magnitud. Cualquier mecanismo de configuración de comisiones (convenios, arancel reducido/Coelsa, futuros orquestadores) debería incluir una forma de detectar automáticamente esta divergencia, no depender de que Soporte la note manualmente. Capturado 2026-08-20, sin ticket ni dueño de mitigación general asignado todavía.

## Saturación de la base de datos de impuestos por CUIT compartido entre entidades comerciales

La vista `RET_IIBB_REC_ACUM_LOTE` hace un `INNER JOIN` de `LIQ_IMP` contra `COMERCIO` por CUIT; como un mismo CUIT puede pertenecer a hasta ~200 sucursales/comercios distintos, cada transacción real se multiplica en el join (fan-out). Medido: 10 transacciones → 53 scans sobre `COMERCIO` y ~9,8M logical reads sobre `LIQ_IMP` (28,4 min reales); estimado a 500 transacciones → ~2.650 scans y ~490M logical reads (probablemente varias horas) — no ocurre en ambientes bajos por no tener ese volumen ni esa repetición de CUITs. Fintexa evalúa qué filtro agregar (acordado: filtro por código de comercio) sin romper la lógica de negocio. Ver detalle técnico en [3_recursos/detalle_productos/siscri/calculo_impuesto_online_qr.md §8](../3_recursos/detalle_productos/siscri/calculo_impuesto_online_qr.md) y [3_recursos/detalle_productos/agente_cobros_y_pagos/integracion_procesadores_pago.md](../3_recursos/detalle_productos/agente_cobros_y_pagos/integracion_procesadores_pago.md). Detectado 2026-08-20/21 (Julieta Gimenez/Ariel Profitti, Fintexa).

## Proyecto Servicios — continuidad de equipo y bloqueo de pruebas con tarjetas prepagas

Dos riesgos sobre el "Proyecto Servicios" (BPG/Pago Fácil, incorporado al pipeline de Wallet — ver [3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md §4](../3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md)): (1) **continuidad de conocimiento** — Pablo Serra (Fintexa) informó (2026-08-21) la baja del integrante identificado como quien más conocía el proyecto, sin plan de traspaso de conocimiento documentado; (2) **bloqueo de pruebas con tarjetas prepagas** (severidad media-alta, impacto directo en clientes) — el ambiente de staging no tiene tarjetas prepagas ni datos de prueba válidos provistos por Pago Fácil o el procesador Decidir, pese a rechazos recurrentes ya reportados por clientes; Andrea Orsini y Adriana Endzeliz gestionan con Decidir/Payway conseguir una tarjeta de prueba válida, sin fecha de resolución confirmada al 2026-08-25.

## Ver también
- [gaps_y_preguntas.md](gaps_y_preguntas.md) — vacíos de información del contexto fijo, distinto de riesgos ya identificados.
- [tareas.md](tareas.md) — backlog operativo, no riesgos.

---
*Última actualización: 2026-08-27 — nuevos riesgos "Saturación de la base de datos de impuestos por CUIT compartido" y "Proyecto Servicios — continuidad de equipo y bloqueo de pruebas con tarjetas prepagas".*
*Última actualización anterior: 2026-08-20 — nuevo riesgo "Desalineación entre comisión facturada a la entidad y comisión real cobrada por el procesador".*
*Última actualización anterior: 2026-08-12 — Creación del archivo en la reestructuración PARA en cascada, consolidando 4 riesgos ya documentados en la wiki pero sin un lugar propio.*
