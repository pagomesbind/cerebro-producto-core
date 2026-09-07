---
id: 2026-09-04_riesgo-getnet-deprecacion-arquitectura-lectura-qr
pm: nicolas
fecha_captura: 2026-09-04
fuente: "Reunión \"Producto - Prioridades\" (2026-09-04)"
producto: adquirencia
tema: Getnet deprecará a fin de este trimestre la arquitectura actual de sus dispositivos POS (provistos por Santander), lo que dejaría de permitir la lectura de códigos QR de Getnet — ~5% del volumen de QR leído por Bind
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: baja
estado: ingestado
merge_commit: ee14a4b68342c2020cd4dfbc817cd6bc347de70d
---

En la reunión "Producto - Prioridades" (2026-09-04), Matías Alzogaray compartió un mail recibido de **Luciana Rudaz** (del lado de **Getnet**, no confundir con la Luciana Rudaz PM de Bind PSP que participaba de la misma reunión — mismo nombre, personas distintas) donde se reitera que la migración de Getnet a una nueva arquitectura es una iniciativa en curso desde el año pasado, con **plazo estimado de adecuación al nuevo circuito para fines de este trimestre (Q)**. El mail advierte que, al llegar esa fecha, la arquitectura actual quedará deprecada y las operaciones que sigan dependiendo de ella "se verán afectadas".

**Impacto identificado:** los dispositivos de punto de venta de Getnet son los que provee **Santander**. Pablo Gomes estimó que esto podría afectar a un **~5%** de los QR que Bind lee actualmente (sin confirmar exactamente qué clientes dependen de esos dispositivos). Nicolás Colón señaló que sería necesario salir con una **versión intermedia de código QR** para no perder esa capacidad de lectura — sin certeza todavía sobre el alcance exacto de la complicación técnica.

**Mitigación acordada:** el tema se irá levantando en las reuniones periódicas con Wallet (dos por semana) apenas haya definición adicional, ya que requiere soporte de ese equipo. Se clasificó con **prioridad 1** interna para tenerlo en el radar, aunque **sin fecha de resolución confirmada todavía** — Pablo Gomes explícitamente pidió no ponerle una fecha "confirmada" en el tablero hasta tener más certeza, solo dejarlo visible como pendiente.

> Fuente: Reunión "Producto - Prioridades" (2026-09-04, tramo 14:01), minuta Gemini + transcripción.
