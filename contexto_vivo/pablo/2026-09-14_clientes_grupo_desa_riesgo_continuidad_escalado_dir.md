---
id: 2026-09-14_clientes_grupo_desa_riesgo_continuidad_escalado_dir
pm: pablo
fecha_captura: 2026-09-14
fuente: "/idea_problem — discovery del proyecto rechazos_bines_payway (PRD-251); declaración directa del PM + captura de WhatsApp reenviada por Alberto Murad (director de Bind PSP) a la CEO actual"
producto: adquirencia
tema: Grupo DESA (cliente de mayor volumen de Botón Simple 1.0 de la compañía) en riesgo de continuidad — reclamo reiterado por fallas de pago con tarjeta, escalado a nivel de dirección de Bind PSP
tipo: riesgo
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no — la ficha de GRUPO DESA no tiene hoy ningún riesgo de continuidad registrado (columna 'Riesgo' en log_clientes.md está en '—', sin valor); este item completa un vacío, no corrige un dato existente"
confianza: alta
estado: ingestado
merge_commit: pendiente
---

Durante el discovery de `/idea_problem` sobre el proyecto de BINs de Payway, el PM confirmó que **Grupo DESA (EDEA/EDEN/EDELAP/EDESA/EDES, recaudador RIPSA) amenaza con dar de baja el servicio** a raíz del volumen de rechazo de sus pagos con tarjeta vía Botón Simple 1.0. Es el cliente de mayor volumen de ese canal en toda la compañía: 79,7% de todo el volumen de tarjeta no presente de Bind PSP en agosto de 2026, y 90,3% de todo el rechazo de tarjeta no presente de la compañía en ese mismo mes.

El PM aportó como respaldo una captura de WhatsApp del 2026-09-14: una referente operativa del cliente (María Elena) escribe a un contacto comercial de Bind PSP ("Marce") reportando que "seguimos con los mismos inconvenientes, y lo peor es que impacta directamente en todos los CEUs... que ya de por sí estamos más complicados que de costumbre" y "la gente no puede pagar por el boton" — pidiendo una actualización sobre el estado de la solución. Alberto Murad (director de Bind PSP, ex-CEO) reenvía esos mensajes internamente a la CEO actual (Emma) marcando "preocupe esto...." y anticipando que "va a ser tema de la reunión de mañana".

**Lo que esto agrega al canon:** ni la ficha de cliente de GRUPO DESA en `casos_de_uso_clientes.md` ni la columna "Riesgo" de `log_clientes.md` (hoy en "—", sin valor) registran hoy ningún riesgo de continuidad sobre esta cuenta. Corresponde: (1) sumar una entrada de cronología a la ficha de GRUPO DESA en `casos_de_uso_clientes.md` documentando el reclamo y la escalada a dirección (2026-09-14), y (2) actualizar la columna "Riesgo" de esa fila en `log_clientes.md` de "—" a un valor real (Alto, dado que amenaza con irse y es el cliente de mayor volumen del canal).

**Importante — solo una fracción del rechazo de este cliente tiene causa en el sistema de identificación de BINs** (5,3%, ver [`1_proyectos/rechazos_bines_payway/proyecto.md`](../rechazos_bines_payway/proyecto.md)); el 94,7% restante tiene otra causa raíz, probablemente decisión del propio banco emisor. Este item documenta el riesgo comercial en sí (relevante más allá de ese proyecto puntual), no una conclusión de que el proyecto de BINs vaya a resolverlo por completo.

## Ver también

- [`1_proyectos/rechazos_bines_payway/proyecto.md`](../rechazos_bines_payway/proyecto.md) (PRD-251) — problem statement con el detalle cuantitativo completo del cruce contra tráfico real de agosto 2026.
