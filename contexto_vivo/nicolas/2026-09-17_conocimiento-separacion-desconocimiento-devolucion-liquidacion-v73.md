---
id: 2026-09-17_conocimiento-separacion-desconocimiento-devolucion-liquidacion-v73
pm: nicolas
fecha_captura: 2026-09-17
fuente: "Reunión 'Análisis de riesgo: AD V 73' (2026-09-17), minuta Gemini"
producto: adquirencia
tema: Separación de "desconocimientos" y "devoluciones" en archivos de liquidación y PDF de comercio, confirmada para AD V73 — resuelve el debate abierto desde 2026-09-03 sobre el ticket 361/2209 (cliente Coto)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 70dcf2a
---

> **Nota de merge (2026-09-21):** integrado en [desconocimientos_de_tarjeta.md](../../wiki/3_recursos/detalle_productos/adquirencia/desconocimientos_de_tarjeta.md) en vez de `devoluciones_y_contracargos.md` directo — el tema (desconocimientos de tarjeta) se extrajo a archivo propio por umbral de tamaño en este mismo merge (ver nota de reclasificación en el manifiesto).

En "Análisis de riesgo: AD V 73", Matias Alzogaray, Maria Eugenia Vila y Maximiliano Ambrosini abordaron la mejora para separar **desconocimientos (contracargos) y devoluciones**, tanto en los archivos de liquidación como en los reportes en formato PDF. Maximiliano Ambrosini detalló que el PDF mostrará ambos conceptos de forma separada, con distintos códigos. Como decisión, Gonzalo Damian Rivera indicó que se debe avisar previamente a los clientes y modificar el portal de desarrolladores con el nuevo formato de archivos; post-implementación se validará la correcta emisión.

**Resuelve un pendiente ya documentado:** esto es la confirmación, para la versión AD V73, del ticket 361 (vinculado al 2209) que en la reunión "Análisis COBRO" del 2026-09-03 había quedado "pendiente de más debate" sobre si entraba en la v73 o la v74 (corrección del PDF de liquidaciones para el cliente **Coto**, diferenciando "desconocimiento" de "devolución" — ver `webhooks_y_notificaciones.md`, última sección, y `devoluciones_y_contracargos.md §0`, que ya documenta el código `004` usado para diferenciar el desconocimiento de tarjeta de Botón Simple en el archivo de liquidación desde PRD-146/AD-1360). La novedad de esta reunión extiende/ratifica esa separación con códigos distintos también en el **PDF** de cara al comercio, con aviso previo a clientes y actualización del portal de desarrolladores antes del despliegue.

> Fuente: Reunión "Análisis de riesgo: AD V 73" (2026-09-17), minuta Gemini — sección Detalles ("Separación de desconocimientos y devoluciones en PDF y liquidaciones").
