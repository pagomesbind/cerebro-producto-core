---
id: 2026-09-09_transversal_riesgo_control_tecnologico_ledger_techfin
pm: pablo
fecha_captura: 2026-09-09
fuente: "Assessment de auditoría del banco tras el fraude de Transferencias Pull (raw/BIND PSP- Assessment 14052026.xlsx, hoja 'Aspectos Identificados', área 'Productos', PRIORIDAD Alta, PLAZO-COSTO 90 días). Remediación liderada por Hernán Clarich y Mariana Nadalin."
producto: transversal
tema: Dependencia de un proveedor externo (Techfin) para la creación del saldo virtual (ledger), sin un control estricto de un sistema interno robusto del banco/Bind PSP
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no — sin archivo de canon existente que documente el control interno del ledger frente a Techfin específicamente. Relacionado pero distinto de la obligación de segregación de fondos ya capturada el 2026-09-08 (`4_archivos/contexto_ingestado/2026-09-08_cumplimiento_pspcp_segregacion_fondos_cuenta_operativa.md`) — aquella es sobre dónde están los fondos reales; esta es sobre quién controla la creación del saldo virtual que los representa."
confianza: media
estado: ingestado
merge_commit:
---

## Qué encontró el banco

"Existe una vulnerabilidad potencial en la creación del saldo virtual, especialmente al depender de un proveedor de desarrollo externo (Techfin) para tocar saldos sin un control estricto de un sistema interno robusto del banco." Justificación explícita: "El core de la PSP (el ledger) debe estar bajo control estricto de la entidad. Delegar la creación de dinero virtual sin control es un riesgo sistémico." La mitigante que propone el propio assessment es genérica ("realizar una auditoría técnica, evaluar si hay posibles vulnerabilidades sobre los sistemas actuales"), con nota de que está "relacionado con el Pentest previo a pasaje a Prod" — el mismo pentest whitebox mencionado en el punto de Quality Gate de Infraestructura/Desarrollo.

## Por qué se captura como riesgo, no como gap de un proyecto puntual

El Cerebro no tiene ningún documento de arquitectura que describa el modelo de control interno sobre la creación de saldo virtual frente a Techfin (a diferencia de la arquitectura acoplado/desacoplado frente a API Bank, que sí está documentada en `arquitectura_sistema/modelo_acoplado_vs_desacoplado.md`). Es plausible que exista un control real hoy (código de confianza media, no alta, por falta de fuente directa de Ingeniería/Arquitectura) pero no hay evidencia documentada en el Cerebro que lo confirme o lo descarte — mismo patrón que el hallazgo de segregación de fondos del 2026-09-08.

## Qué haría falta para cerrar esto

Confirmar con Arquitectura/Ingeniería (no solo con Producto): (1) qué controles existen hoy sobre las operaciones de Techfin que impactan el ledger/saldo virtual (aprobación, límites, logging, reconciliación); (2) si el pentest whitebox ya presupuestado (ver punto de Quality Gate de Infraestructura) incluye este vector específico o haría falta un alcance separado; (3) si Producto (dueño de Wallet) tiene visibilidad de las operaciones que Techfin ejecuta sobre saldo, o si es una caja negra completa.

Ver tarea relacionada `T-077` en `tareas.md`.
