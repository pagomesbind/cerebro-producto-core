---
id: 2026-08-24_adquirencia_ad8_no_funciona_como_espera_soporte
pm: pablo
fecha_captura: 2026-08-24
fuente: "/idea_problem — sesión de problem statement del proyecto convenios_configuracion, corrección aportada en vivo por el PM"
producto: adquirencia
tema: Epic AD-8 (canal_entidad/canal_comercio) no funciona como espera el equipo operativo, pese a estar documentado como validado en producción
tipo: gap
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mejoras_admin_backoffice_prd88.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/adquirencia/mejoras_admin_backoffice_prd88.md §2 — el documento caracteriza el patrón canal_entidad/canal_comercio del Epic AD-8 como ya construido y validado en producción (76 tickets, desde AD 67.5)"
confianza: media
estado: en_cola
merge_commit:
---

Durante el discovery de `/idea_problem` sobre el proyecto `convenios_configuracion` (rediseño de la herencia de convenios entre entidad y comercio), el PM (Pablo Gomes) aportó una corrección directa sobre el estado real del Epic AD-8 (canales de cobro, patrón `canal_entidad`/`canal_comercio`), que el discovery original de ese proyecto (`/idea_start`, 2026-08-21) había tomado como referencia arquitectónica probada para espejar en el nuevo diseño de convenios.

**Lo que dice hoy el canon:** `3_recursos/detalle_productos/adquirencia/mejoras_admin_backoffice_prd88.md §2` describe el Epic AD-8 como ya construido y en producción desde AD 67.5 (76 tickets), resolviendo el problema de "defaults a nivel entidad que se propagan, con habilitaciones/excepciones efectivas por comercio" para el dominio de canales de cobro.

**Lo que aportó el PM en esta sesión:** ese mecanismo (AD-8) se intentó usar para resolver un problema análogo, pero quedó **mal definido y mal ejecutado** — no funciona como lo espera el equipo operativo de Soporte de Cobro (mismo equipo, referente Gonzalo Rivera, que reporta el dolor de convenios). No se precisó en la sesión si el problema es de diseño (el modelo de datos no captura bien el caso de uso), de ejecución (bugs), o de ambos — es una afirmación de resultado ("no funciona como se espera"), no un diagnóstico técnico detallado.

**Por qué importa:** si AD-8 no funciona como documenta el canon, cualquier otra iniciativa de Adquirencia que lo tome como referencia de "patrón ya validado y reusable" (no solo `convenios_configuracion`) puede estar partiendo de una premisa falsa. Vale la pena que quien mantiene `mejoras_admin_backoffice_prd88.md` confirme con el propio Gonzalo Rivera (o releve tickets de soporte sobre canales de cobro) si el "no funciona como se espera" es puntual, generalizado, o ya conocido y en backlog de arreglo — y ajuste la caracterización del documento en consecuencia (marcándolo como "construido pero con problemas conocidos" en vez de "validado en producción", si corresponde).

**Impacto directo en `convenios_configuracion`:** el Gate 3 de ese proyecto (que adoptó la analogía con AD-8) quedó parcialmente reabierto — ver `1_proyectos/convenios_configuracion/decisiones.md` (2026-08-24). El nuevo diseño de convenios debe partir del mecanismo real de herencia (copia puntual al crear el comercio, no vínculo vivo) y no asumir que basta con replicar `canal_entidad`/`canal_comercio`.
