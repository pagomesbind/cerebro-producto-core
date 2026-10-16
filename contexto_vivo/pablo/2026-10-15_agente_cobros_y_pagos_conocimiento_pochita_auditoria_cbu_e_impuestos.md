---
id: 2026-10-15_agente_cobros_y_pagos_conocimiento_pochita_auditoria_cbu_e_impuestos
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Pochita' (2026-10-15, 17:15)"
producto: agente_cobros_y_pagos
tema: Pochita — división de liquidaciones >1000M ya en producción; hallazgos de CBU inconsistentes, contracargos no descontados automáticamente, y plan de registro de auditoría
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## En producción desde la noche anterior (14/10)

**División automática de liquidaciones superiores a $1.000 millones en múltiples transferencias**, con grilla de estado filtrable por código de entidad y exportable. Interfaz permite filtrar por producto, ID de liquidación, CBU, comercio y entidad.

## Hallazgos operativos abiertos

1. **CBU inconsistentes entre base de comercios y contratos**: 3 entidades (incluyendo **Ripsa** y **Credicuotas**) tienen un CBU distinto en la base de comercios respecto al contrato firmado. Hay que validar con cada entidad/contrato cuál es el correcto antes de generar excepciones innecesarias en las transferencias.
2. **Contracargos y desconocimientos no se descuentan automáticamente de las liquidaciones** — hoy requiere modificación manual, con el riesgo operativo que eso implica (varias personas con permisos para modificar montos, sin registro de quién hizo qué). Nico (producto Cobro) estima que la **versión 75 (producción 5/11)** resuelve la mayoría de los tickets asociados, pero Emma Vignoles remarcó que **depender solo de los ciclos de versión para un problema crítico en producción es inadecuado** — pidió que toda modificación manual de montos quede en un **registro de auditoría** mientras tanto.
3. **Retenciones de impuestos duplicadas**: entidades del "protocolo 164" que usan botón de pagos ya reciben una retención descontada por Banco Industrial (informada en el archivo de impuestos) — el sistema interno de Pochita **no debe volver a descontarla**. Se pidió configurar una regla de exclusión específica.
4. **Perfiles de usuario y auditoría de ejecución**: se definió crear un perfil de usuario restringido para quién puede ejecutar el proceso de liquidaciones, con registro de auditoría de quién ejecutó o modificó montos (varias personas tienen hoy permisos operativos).

## Automatizaciones en curso/pedidas

- **Carga automática de feriados** desde páginas oficiales del gobierno/BCRA — hoy solo hay consultas internas al ecosistema; se requiere solicitar un endpoint de inserción con los permisos de seguridad informática correspondientes.
- **Consulta automática de saldo de cuentas recaudadoras** vía API (para prevenir desvíos/rechazos de pagos) — pendiente de implementar el endpoint que ya aportó Pablo Gomes.
- **Preliquidación**: agrupar importes por cuenta de débito y mostrar el saldo de la cuenta recaudadora con validaciones de riesgo antes de ejecutar.
- **Generalización de "movimiento de fondos"**: Pablo Gomes propuso que la funcionalidad de recuperación de impuestos (en desarrollo para la sumatoria de billeteras) se generalice como un **movimiento de fondos entre cuentas PCP con distintos conceptos** (impuestos, PMC, etc.), en vez de limitarse solo a recuperación de impuestos.
- **Control de conciliación CBU Collect vs. liquidaciones**: configurado, pase a producción previsto martes o miércoles siguiente.
- **Automatización de inversiones/planillas de Drive**: evaluado usar una cuenta de servicio de Gmail para que la herramienta interactúe con documentos del banco sin intervención manual de Gabriela Rojas — pendiente que Hernán cree la cuenta de servicio.

## Reconocimiento

Emma Vignoles destacó el éxito de la herramienta Pochita y sugirió presentarla internamente como caso de éxito al cierre de año.

> Fuente: reunión "Pochita", 2026-10-15 17:15hs (Pablo Gomes, Emma Vignoles, Gabriela Rojas, Ana María Moreno, María Eugenia Vila).
