---
id: 2026-09-07_cumplimiento_separacion_comercios_extraccion_pago_pago_facil
pm: pablo
fecha_captura: 2026-09-07
fuente: "sesión de trabajo con el PM — armado del documento de integración de Pago Fácil (cobro QR extracciones + pago de servicios)"
producto: adquirencia
tema: Definiciones de Cumplimiento confirmadas para el caso de uso de Pago Fácil (QR extracciones + pago de servicios)
tipo: decision
destino_propuesto: 3_recursos/cumplimiento_normativo/limites_operativos_uif_ros.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: d7e1ccf
---

## Definiciones de Cumplimiento confirmadas para la integración de Pago Fácil (QR extracciones + pago de servicios)

Durante el armado del documento de integración técnica para Pago Fácil (cobro presencial con QR interoperable, para pago de servicios y extracción de efectivo en sucursales), el PM confirmó tres definiciones de negocio/Cumplimiento que hasta ahora no estaban canonizadas:

1. **Los comercios y CVU vendedores tendrán titularidad (CUIT) de Pago Fácil**, para poder acceder al arancel reducido en Coelsa (en vez de titularidad de Bind PSP).
2. **Las operatorias de pago de servicios y extracciones deben separarse en distintos comercios.** El PM la marca explícitamente como una **definición estricta del área de Cumplimiento** — no es una preferencia técnica, es un requisito no negociable.
3. Si más adelante se evalúa un tercer caso de uso para este cliente (ejemplo dado: Retail), **podría tratarse de un nuevo comercio adicional** — mismo patrón de separación por operatoria, no un cuarto caso mezclado en uno de los comercios existentes.

**Por qué importa:** esto resuelve parcialmente el gap abierto el 2026-09-03 (`2026-09-03_adquirencia_gap_limites_pld_extracciones.md`, todavía sin mergear) — confirma que la separación de operatorias por comercio **sí es un requisito confirmado**, no solo una preocupación mencionada de pasada en una reunión. Lo que ese gap todavía deja abierto son los **límites transaccionales exactos** (por operación y acumulados mensuales) para la operatoria de extracción — sobre eso no hubo definición numérica en esta sesión, sigue pendiente de Compliance/Legales.

> Fuente: sesión de trabajo del PM armando el documento "Integración de Pago Fácil a Bind PSP — Cobro presencial con QR", 2026-09-07. Documento entregable en `outputs/pago_facil_integracion_qr.pdf`.
