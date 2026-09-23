---
id: 2026-09-21_riesgo-eliminacion-comercios-coelsa-mismo-cuit-inhabilita-entidades
pm: nicolas
fecha_captura: 2026-09-21
fuente: "Reunión 'Weekly - Producto / Operaciones' (2026-09-21)"
producto: adquirencia
tema: Eliminar un comercio en Coelsa deshabilita a todas las entidades que comparten el CUIT de BIN PCP
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

En la reunión "Weekly - Producto / Operaciones" (2026-09-21), Gonzalo Rivera reportó un problema operativo grave: cuando una entidad pide **eliminar** (no bloquear) un comercio en Coelsa, la eliminación deshabilita en Coelsa a **todas las demás entidades que comparten el mismo CUIT y actividad comercial** — es decir, todos los comercios dados de alta bajo el CUIT de BIN PCP. Esto ya había pasado antes (caso "Tinflanor") y **volvió a pasar el mismo día de la reunión**, con Tinflanor de nuevo.

Detalle técnico: bloquear un comercio (para que no opere momentáneamente) y eliminarlo (baja definitiva, requerida por normativa PLD para dejar una fecha de baja formal) son operaciones distintas; hoy no existe una forma de dar de baja un comercio individual sin afectar a los demás que comparten CUIT. La mitigación actual es puramente manual y arriesgada: darle de baja temporalmente **todos** los comercios de la entidad (interrumpiendo su operatoria ~15 minutos) y luego rehabilitar solo el que corresponde, para que el CUIT+actividad comercial+ID PCP vuelva a estar activo en Coelsa.

Fintexa (a través de "Grau") respondió que Bind ya tiene las herramientas para resolverlo (endpoint de eliminar CBU corta) y que debe hacerlo Bind mismo — no ofreció una solución de fondo (ej. permitir baja selectiva por comercio sin afectar al resto del CUIT). Pablo Gomes propuso, como paliativo inmediato, que **nadie elimine un comercio** sin coordinar antes, y evaluar alternativas por base de datos (marcar fecha de baja directamente, sin pasar por el endpoint de eliminación que dispara el efecto colateral).

**Por qué es más grave de lo que parece hoy:** Gonzalo Rivera advirtió que el riesgo crece con la migración pendiente a la versión "184" de Coelsa — si alguien elimina un comercio por error o desconocimiento durante o después de esa migración, se puede dejar sin operar a todas las entidades que comparten el CUIT de BIN PCP. Se decidió escalar el caso a Fintexa formalmente (ya cargado por Lula), pero sin plan de resolución estructural todavía — el riesgo de que "el conocimiento se pierda" y vuelva a pasar sigue latente.

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-09-21), minuta Gemini.
