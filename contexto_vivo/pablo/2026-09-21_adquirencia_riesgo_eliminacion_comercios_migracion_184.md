---
id: 2026-09-21_adquirencia_riesgo_eliminacion_comercios_migracion_184
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_meetings — reunión \"Weekly - Producto / Operaciones\" (14:58, con Mariana Nadalin, Gonzalo Rivera, Matías Alzogaray, Nicolás Colón), 2026-09-21"
producto: adquirencia
tema: Eliminar un comercio con el mismo CUIT+actividad comercial que otros deshabilita en Coelsa a TODOS los comercios que comparten ese CUIT (riesgo agravado por la migración PSP 164→184)
tipo: riesgo
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Mecanismo confirmado por Gonzalo Rivera (Adquirencia):** en Coelsa, un comercio se identifica por la combinación CUIT + actividad comercial + ID PCP. Bind PSP tiene dadas de alta, bajo el mismo CUIT de BIN PCP, muchos comercios de entidades distintas. Cuando alguien pide **eliminar** (no bloquear) uno de esos comercios, la baja se aplica a nivel de esa combinación CUIT+actividad+PCP en Coelsa — lo que **deja de operar a todos los demás comercios que comparten ese mismo CUIT PCP**, no solo al que se quería dar de baja. Ya ocurrió al menos dos veces: con Tinflanor (caso histórico) y de nuevo la mañana del 2026-09-21.

**Por qué es distinto de "bloquear":** Pablo Gomes propuso bloquear en vez de eliminar, pero Gonzalo Rivera aclaró que a nivel PLD no es equivalente — un comercio bloqueado sigue "activo" a efectos de reportería normativa, mientras que uno dado de baja necesita fecha de baja imputada en la base para dejar de considerarse operativo ante regímenes informativos.

**Workaround manual actual (confirmado con Fintexa/Grau):** en vez de usar el endpoint que elimina el comercio completo (que dispara la baja compartida en Coelsa), hacer manualmente: (1) eliminar el CBU corto asociado vía Swagger — deja de poder cobrar con QR; (2) opcionalmente, poner la fecha de baja por base de datos. Fintexa (Grau) confirmó que Bind PSP ya tiene la herramienta para hacerlo así ("tienen la herramienta, háganlo") y no ofrece una solución del lado de ellos que separe ambos efectos. Gonzalo Rivera valida el workaround pero no lo tiene automatizado ni documentado como procedimiento estándar todavía.

**Por qué se agrava con la migración PSP 164→184 (riesgo central, no solo el caso puntual):** cuantas más entidades convivan bajo el mismo CUIT de BIN PCP tras la migración, mayor la probabilidad de que alguien —por error, desconocimiento o sin saber del riesgo— pida eliminar un comercio y tire abajo la operatoria de comercios de otras entidades no relacionadas. Gonzalo Rivera lo marcó explícitamente como su mayor preocupación, por encima del caso puntual de Tinflanor.

**Mitigación acordada en la reunión (sin desarrollo, solo proceso):** "que nadie elimine un comercio" — si alguien pide eliminar un comercio, avisar antes de tocar nada. Sin excepción documentada ni alerta automática todavía. Adicional: en el panel de administración hoy tampoco se puede eliminar un cliente (solo comercio) — Pablo Gomes indicó que "eso habría que habilitar", sin acción concreta tomada en la reunión.

**Estado:** riesgo mapeado, sin prioridad de desarrollo (Gonzalo Rivera lo calificó "prioridad me parece que es cero, pero sí tenerlo mapeado"). Sin ticket, sin owner de una solución de fondo (ej. separar la baja de comercio de la baja de CUIT+actividad+PCP en Coelsa, o alertar antes de ejecutar la eliminación).
