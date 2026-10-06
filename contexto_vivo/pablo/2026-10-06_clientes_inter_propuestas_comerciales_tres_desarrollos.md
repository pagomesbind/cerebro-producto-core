---
id: 2026-10-06_clientes_inter_propuestas_comerciales_tres_desarrollos
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_mails — mail \"Propuestas Técnicas y Comerciales - Nuevos desarrollos solicitados\" de Alan Martínez (Área Técnica, Bind PSP), 2026-10-05, threadId 1a10d0052972ecd2, a josefina.cereijo/joao.luiz/julia.pereira@inter.co, cc Emma Vignoles/Gonzalo Rivera/Pablo Gomes"
producto: wallet
tema: Bind envía a INTER propuestas técnico-comerciales para 3 nuevos desarrollos solicitados por el cliente (Wallet y Onboarding)
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

> Fuente: mail, no brochure de Notion. El cliente **INTER** ya tiene ficha en `log_clientes.md` (producto Wallet/Dólar CCL) — este item complementa su cronología, no reemplaza la ficha.

Alan Martínez (Área Técnica de Bind PSP) envió el 2026-10-05 a INTER las propuestas técnicas y comerciales de **tres nuevos desarrollos que el cliente había solicitado previamente** (no hay discovery de Producto documentado en el Cerebro para ninguno de los tres — esta es la primera noticia que llega al PM por este canal, vía copia del mail):

1. **Nuevos datos en los avisos Webhook de Dólar CCL** (producto: Wallet) — ampliación de información enviada en las notificaciones webhook existentes de la operatoria Dólar CCL ya usada por INTER.
2. **Reprocesamiento masivo de solicitudes en Verificación Manual** (producto: Onboarding) — capacidad de reprocesar en lote solicitudes que quedaron en revisión manual.
3. **Motivo de error de alta en el panel de solicitudes** (producto: Onboarding) — exponer en el panel el motivo específico por el que una alta falló.

Cada propuesta fue enviada como PDF separado (`INTER - Presupuesto - Datos en webhooks de Dólar CCL.pdf`, `INTER - Presupuesto - Reprocesamiento masivo Verificación Manual.pdf`, `INTER - Presupuesto - Motivo de Error de Alta en el Panel de Solicitudes.pdf`) con alcance, cronograma estimado de implementación y condiciones comerciales — ninguno leído automáticamente por esta skill (contenido no abierto, son adjuntos de presupuesto comercial).

**Por qué es relevante para Producto pese a ser una gestión comercial/técnica directa:** el envío lo hizo Alan Martínez (Área Técnica) directo al cliente, sin que conste que pasó por el proceso de discovery/PRD habitual de Producto — los tres desarrollos no tienen IDEA en Jira ni carpeta en `1_proyectos/`. Vale la pena que el PM confirme si esto fue una gestión ad hoc fuera del proceso estándar (posible gap de proceso) o si hay contexto previo no capturado en el Cerebro. Si alguno de los tres avanza a desarrollo real, debería generar su propia IDEA — hoy quedan solo como antecedente comercial en la ficha del cliente.
