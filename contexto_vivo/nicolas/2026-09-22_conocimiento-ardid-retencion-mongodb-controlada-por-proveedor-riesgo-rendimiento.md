---
id: 2026-09-22_conocimiento-ardid-retencion-mongodb-controlada-por-proveedor-riesgo-rendimiento
pm: nicolas
fecha_captura: 2026-09-22
fuente: "Mail directo de Nicolás Colón a Osmel Mata (SRE, Fintexa/Pentass), 2026-09-22, en el marco del discovery de ardid_desconocimientos"
producto: ardid
tema: Dueño técnico y motivo histórico de la ventana de retención de transacciones de Ardid en MongoDB
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/despliegues_y_operacion.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

La ventana de retención de transacciones de Ardid en MongoDB (hoy 45 días) la controla el proveedor (Pentass/Akurtech), no infraestructura propia de Bind PSP — no es un parámetro que Bind pueda cambiar unilateralmente vía su propia infraestructura Azure.

Osmel Mata (SRE, Fintexa/Pentass) lo confirmó por escrito ante la consulta directa de Nicolás Colón ("Quién decide cuánto tiempo para atrás se guarda en Mongo sobre Ardid? Hoy está seteado en 45 días por ejemplo, pero necesitamos que sea más"):

> "La gente de Pentass/Akurtech, debido a que en el pasado presentó muchos problemas de rendimiento (al principio se guardaba todo el histórico, luego pasamos a 90, 60 y finalmente 45 días), y luego de varias sugerencias de parte de ellos y pruebas en conjunto, se dejó en 45 días que era donde Ardid funcionaba bien con el histórico en MongoDB (teniendo en cuenta el gran volumen de datos que se almacenan por mes). Es un tema de rendimiento. Si ellos logran resolver ese problema, no veo inconveniente en que se incremente el histórico nuevamente"

Dos hechos duros quedan confirmados para cualquier iniciativa futura que dependa de esta ventana:

1. **La reducción fue progresiva y deliberada**, en tres pasos: histórico completo → 90 días → 60 días → 45 días (valor actual). No es un límite arbitrario ni una config por defecto sin revisar — fue ajustado activamente varias veces por el proveedor, con pruebas conjuntas con Bind, específicamente para resolver problemas de rendimiento de Ardid con el volumen de datos mensual.
2. **El proveedor no objeta ampliarla de nuevo, pero lo condiciona explícitamente a resolver antes ese problema de rendimiento.** Cualquier pedido de ampliación (ej. a 120 días, para cubrir contracargos que llegan más tarde que la ventana actual) debería ir acompañado de una confirmación del proveedor de que el problema que motivó las 3 reducciones anteriores ya está resuelto — de lo contrario, el riesgo es reintroducir el mismo problema de rendimiento.

Esto resuelve (parcialmente) un gap abierto desde 2026-09-11 sobre quién era el dueño técnico del cambio de retención — en su momento el PM decidió no bloquear la estimación del proyecto `ardid_desconocimientos` por no tener este dato, así que la resolución llega después de haber avanzado con el diseño y la estimación. El detalle completo del historial de decisión del proyecto está en el gap propio de esa IDEA.
