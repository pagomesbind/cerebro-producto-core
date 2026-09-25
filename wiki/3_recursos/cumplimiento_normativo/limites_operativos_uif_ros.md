# Límites Operativos Mensuales por Segmento de Cliente — Gestión de Riesgo UIF/ROS

> Estado: en producción. Fuente: Reunión "Join Soporte Clientes" (2026-07-29), minuta Gemini. Reubicado desde `detalle_productos/transversal/cumplimiento_normativo.md §4` en la reestructuración PARA en cascada (2026-08-12). Ver decisión registrada en [`decisiones.md`](../../2_areas/direccion/index.md).

Compliance estableció topes operativos mensuales para decidir de forma objetiva cuándo pedir documentación de respaldo adicional a un cliente, evitando que el equipo genere Reportes de Operaciones Sospechosas (ROS) innecesarios ante la Unidad de Información Financiera (UIF) — cada ROS tiene costo asociado y puede afectar la reputación del cliente si no está bien fundamentado.

- **Límites:** $25.000.000/mes para **personas humanas**, $300.000.000/mes para **personas jurídicas**.
- **Consecuencia de superar el límite:** obligatorio presentar documentación de respaldo adicional; el proceso de qué documentación exactamente está siendo definido por el equipo de cumplimiento.
- **Objetivo declarado:** monitorear el comportamiento del cliente sin perder la relación comercial, manteniendo igualmente el control de los límites establecidos (caso citado: Global 66, ver [2_areas/tareas.md](../../2_areas/tareas.md) T-071).
- **Revisión de cartera de clientes complejos (mismo foro):** Arcos Dorados, Coto, Pella, Tienda Nube, Nera, Prometeo, Terra Blockchain, Andina, Grupo Slot y GCTs identificados como cartera de seguimiento prioritario. Terra Blockchain (gestionado vía Gallo) presenta hallazgos concretos de riesgo — ver ficha del cliente en [`2_areas/clientes/casos_de_uso_clientes.md`](../../2_areas/clientes/casos_de_uso_clientes.md).

## Definiciones de Cumplimiento confirmadas para casos de uso multi-operatoria bajo un mismo cliente (caso Pago Fácil, 2026-09-07)

> Fuente: sesión de trabajo del PM armando el documento "Integración de Pago Fácil a Bind PSP — Cobro presencial con QR" (2026-09-07). Entregable en `outputs/pago_facil_integracion_qr.pdf`.

Durante el armado del documento de integración técnica para **Pago Fácil** (cobro presencial con QR interoperable, para pago de servicios y extracción de efectivo en sucursales), Cumplimiento confirmó tres definiciones que aplican como criterio general a este tipo de integración multi-operatoria:

1. **Los comercios y CVU vendedores tendrán titularidad (CUIT) de Pago Fácil**, para poder acceder al arancel reducido en Coelsa (en vez de titularidad de Bind PSP).
2. **Las operatorias de pago de servicios y extracciones deben separarse en distintos comercios.** Es una **definición estricta del área de Cumplimiento** — no una preferencia técnica, es un requisito no negociable, relevante para el monitoreo por operatoria de límites UIF/ROS de esta sección.
3. Si más adelante se evalúa un tercer caso de uso para este cliente (ej. Retail), podría tratarse de un **nuevo comercio adicional** — mismo patrón de separación por operatoria, no un cuarto caso mezclado en uno de los comercios existentes.

Esto confirma que la separación de operatorias por comercio **es un requisito confirmado**, no solo una preocupación mencionada de pasada. Quedan sin definición numérica los **límites transaccionales exactos** (por operación y acumulados mensuales) para la operatoria de extracción — pendiente de Compliance/Legales.

## Nueva regla — revisión PLD obligatoria para legajos PJ con umbral >$10.000/mes (2026-09-24)

> Fuente: reunión "Revisión OB PJ | Interna" (2026-09-24), capacitación interna del flujo de onboarding PJ de La Virginia (PRD-223) a los equipos de PLD y Soporte.

**Decisión acordada:** a partir del **1 de octubre de 2026**, todo legajo de persona jurídica que vaya a operar con un umbral superior a **$10.000 mensuales** debe pasar obligatoriamente por la revisión de cumplimiento (PLD) antes de habilitarse — expuesto por Mauro Suppan (PLD) durante la capacitación.

> ⚠️ **Posible reapertura de una disputa ya dada por resuelta:** este mismo monto ($10.000) y el mismo deadline (1/10/2026) coinciden con la cifra que la decisión de `direccion/decisiones.md` [2026-09-21] descartó como error de transcripción, al confirmar $1.000 como el límite operativo vigente de cuentas de PJ sin documentación (implementado como el `ClientBankType` restrictivo de Ardid, ver `detalle_productos/wallet/organizaciones_y_configuracion.md §8`). Se documentan acá como **mecanismos conceptualmente distintos** (este es un gate de revisión PLD sobre el legajo; aquel es un tope operativo de cuenta), pero sin confirmar todavía si son realmente independientes — ver gap abierto en [`2_areas/gaps_y_preguntas.md`](../../2_areas/gaps_y_preguntas.md) [2026-09-25].

## Ver también
- [reporteria_worldsys_bcra.md](reporteria_worldsys_bcra.md) — mismo dominio PLD/UIF, mecanismo de reporte diario relacionado.

---
*Última actualización: 2026-09-25 — `/context_merge`: nueva sección — regla de revisión PLD obligatoria para legajos PJ >$10.000/mes desde el 1/10/2026, con nota de posible reapertura de la disputa $1.000/$10.000 ya dada por resuelta el 2026-09-21.*
*Última actualización anterior: 2026-09-08 — `/context_merge`: nueva sección de definiciones de Cumplimiento confirmadas para casos multi-operatoria (caso Pago Fácil, separación de comercios por operatoria y titularidad CUIT).*
*Última actualización anterior: 2026-08-12 — Reubicado desde `detalle_productos/transversal/cumplimiento_normativo.md §4` (reestructuración PARA en cascada). Contenido sin cambios.*
