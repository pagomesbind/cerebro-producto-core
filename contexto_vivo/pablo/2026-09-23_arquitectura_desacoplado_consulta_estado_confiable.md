---
id: 2026-09-23_arquitectura_desacoplado_consulta_estado_confiable
pm: pablo
fecha_captura: 2026-09-23
fuente: "Validación directa con Banco Industrial (Ignacio Ghillini y Álvaro Aguirreburualde) — chat pegado por el PM durante la preparación del material de /idea_solution sobre resiliencia_api_bank"
producto: transversal
tema: La consulta de estado de una transferencia se resuelve contra una base intermedia del banco, no contra su core — acota el riesgo de la ventana de sincronización del modelo desacoplado a la consulta de saldo, no a la de estado
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/modelo_acoplado_vs_desacoplado.md
tipo_destino: actualizar
contradice: "no — precisa el riesgo operativo ya documentado (ventana de sincronización), distinguiendo la consulta de saldo (sí puede quedar desactualizada) de la consulta de estado de una operación puntual (confiable de inmediato)"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

## Conocimiento

Dos confirmaciones puntuales del proveedor bancario, obtenidas directamente por el PM, que precisan el riesgo ya documentado de la ventana de sincronización del modelo desacoplado:

1. **El identificador propio (`origin_id`) sigue sirviendo para reconsultar el estado de una transferencia, sin importar el modelo.** Ignacio Ghillini (Banco Industrial): *"con el origin ID siempre van a poder buscarlo"*. Esto es un dato distinto del cambio de identificador en el archivo de conciliación (`REFERENCIA_MONI`, ya documentado) — ese cambio es sobre el archivo batch de conciliación, no sobre cómo la compañía reconsulta el estado de una operación vía API.

2. **La consulta de estado de una operación puntual se resuelve contra una base intermedia del banco, no contra su core contable.** Álvaro Aguirreburualde (Banco Industrial), respondiendo si una consulta posterior a un aviso "completado" en línea podría devolver un estado desactualizado por la demora del core en sincronizar: *"te va a devolver el completed, no vamos al core a buscar ese estado, lo respondemos desde la base intermedia"*.

## Por qué esto precisa (no contradice) el riesgo ya documentado

El archivo ya advierte que, durante la ventana de 2 a 5 minutos, "el saldo se actualiza contra un caché" y puede no reflejar el core real. Esta nueva confirmación aclara que ese riesgo aplica específicamente a la **consulta de saldo agregado de la cuenta** (endpoint de saldo de cuenta recaudadora) — no a la **consulta de estado de una transferencia puntual ya confirmada**, que el banco resuelve siempre contra una base intermedia consistente, sin ir a buscar al core. Es una distinción importante para cualquier análisis de riesgo futuro sobre este modelo: no todas las consultas están expuestas a la misma inconsistencia transitoria.
