---
id: 2026-09-21_arquitectura_desacoplado_conciliacion_movimientoscomp
pm: pablo
fecha_captura: 2026-09-21
fuente: "mail 'RE: [sin asunto]' de Gonzalo Genna (Banco Industrial) a Maria Vila/Pablo Gomes/Ariel/Nicolas, originalmente 2026-09-08, reenviado con Pablo Gomes en copia el 2026-09-21 — pegado verbatim por el PM en /idea_start sobre resiliencia_api_bank/"
producto: transversal
tema: Cambios exactos en el archivo de conciliación MovimientosComp al pasar a modelo desacoplado de API Bank
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/modelo_acoplado_vs_desacoplado.md
tipo_destino: actualizar
contradice: "no — completa con precisión técnica lo que el archivo ya dice en términos generales sobre cambio de ID de conciliación y pérdida del reporte horario"
confianza: alta
estado: ingestado
merge_commit: f230716c54a5ca6600a2bce4e46bf0292d56a58c
---

## Conocimiento

Banco Industrial (Gonzalo Genna) detalló el impacto exacto en el archivo de conciliación que hoy usa Bind (`MovimientosComp`, armado según la contabilidad) al migrar una cuenta al modelo desacoplado:

- **No hay cambio de formato de interfaz ni de nombre de archivo** — sigue siendo `MovimientosComp`.
- **Campo `REFERENCIA_MONI`:** en débitos, pasa a enviarse el ID de Coelsa — igual que ya ocurre hoy en los créditos. Ejemplo textual del banco:
  - Hoy (Origin ID / ID interno): `1-30717449076-W93400014586895-1`
  - Con desacoplado (ID Coelsa): `WGRXJE27Q6W7W0P97MYQL3`
  - El banco deja abierta una pregunta técnica: *"hay que ver cuál persisten uds al momento de ejecutar la transacción"* — es decir, Bind tiene que decidir/confirmar qué identificador persiste en su propia base al ejecutar la transacción, dado el cambio de formato.
- **NSBT — nuevo formato de armado:** `NSBTD-1-1-749049-264-1-20260310-125-41-1-1`, con un máximo posible de **68 caracteres**.
- **Contracargos:** si Bind usa códigos de movimiento para conciliar, en esa operatoria va a recibir **mayor nivel de diferenciación (nuevos códigos)**.
- **Confirmación explícita y sin matices:** *"el reporte 'online' (Cada una hora) no va a poder utilizarse para conciliar ésta operatoria"* en el modelo desacoplado.

## Por qué actualiza el archivo existente

`arquitectura_sistema/modelo_acoplado_vs_desacoplado.md` ya documenta en términos generales que (a) cambia el ID de conciliación de Origin ID a ID Coelsa en débitos, y (b) se pierde el reporte horario. Este mail aporta la especificación técnica exacta que faltaba: el nombre del campo afectado (`REFERENCIA_MONI`), ejemplos literales de ambos formatos de ID, el formato completo del nuevo NSBT con su límite de caracteres, el detalle de contracargos, y confirma sin ambigüedad (ya no "en revisión") que el reporte horario no sirve para conciliar bajo este esquema. No contradice nada — completa.

## Pregunta técnica sin responder por el banco

El propio Gonzalo Genna deja abierta la definición de qué ID persiste Bind al ejecutar la transacción — esto es trabajo de definición técnica de Bind (equipo de Administración/Euge), no un gap del Cerebro. Ver `1_proyectos/resiliencia_api_bank/proyecto.md §7` y `tareas.md` T-073 (resuelta, pero esta sub-pregunta queda para cuando el proyecto avance a Fase 3/implementación).
