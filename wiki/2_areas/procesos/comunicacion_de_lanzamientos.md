# Comunicación de Lanzamientos de Producto

> Estado: acordado — no confirmado como implementado.

## Acuerdo (2026-08-18)

En la weekly de seguimiento de Productos (Luciana Rudaz, Pablo Gomes, Nicolás Colón, 2026-08-18) se acordó instaurar un canal estándar para comunicar internamente cada vez que se lanza una funcionalidad: un hilo de correo dirigido a todo Bind PSP (posible nombre: "avisos de producto"), donde cada lanzamiento se reporta como una comunicación corta tipo "one-pager" (qué se hizo, cuándo).

La primera comunicación prevista es sobre la funcionalidad de consulta de cotitulares/totalizadores.

**Objetivo explícito:** dejar evidencia y visibilidad de los desarrollos terminados, en vez de depender de avisos verbales sueltos — dolor mencionado explícitamente por el equipo ("vamos haciendo, vamos haciendo y no se nota que se hizo").

**Sin definir:** quién lo inaugura formalmente, fecha límite concreta. A confirmar en un próximo barrido si ya se implementó.

> Fuente: Reunión "Productos - Weekly Seguimiento" (2026-08-18), minuta Gemini.

## Propuesta relacionada (sin decisión formal, a probar) — calendario de ventanas de despliegue anticipado

> Fuente: reunión "Adquirencia V72: Pre-Despliegue" (2026-08-27), minuta Gemini.

Esta sección cubre comunicación **externa** (a clientes) y el **calendario** de fechas de pase a producción — distinto del acuerdo de arriba, que es sobre el aviso **interno** de que algo ya se lanzó.

**Contexto que la motivó:** el pase a producción de la versión 72 de Cobro/Adquirencia se reprogramó del jueves 27/08 21hs a la noche del lunes 31/08 por 12 tickets con errores críticos de QA sin cerrar. Gonzalo Rivera (Integraciones/Soporte) planteó una queja de fondo, no puntual de este release: las reprogramaciones recurrentes de fechas ya comunicadas a clientes generan una percepción de falta de profesionalismo — citó el precedente reciente de APIBank (modificación de fecha la misma semana) y señaló que los clientes ya ponen en marcha sus propios avisos internos (popups en billeteras, personal de control) en base a la fecha que Bind les confirma, y tienen que reavisar cuando esa fecha cambia. Pablo Gomes respondió que el riesgo de postergar es preferible al de pasar a producción algo que después falle, pero reconoció que la comunicación institucional después de la reunión de riesgo debe mejorar. El proceso ya documentado en [`analisis_de_riesgo_de_despliegue.md`](analisis_de_riesgo_de_despliegue.md) define cómo se arma el informe de riesgo y su semáforo, pero no contempla un calendario de ventanas *anticipado* — la fecha de pase hoy se fija recién en la reunión de riesgo puntual (con 4 días hábiles de antelación mínima), sin margen si aparecen tickets críticos de QA a último momento, como pasó acá.

**Propuesta discutida:** Mariana Nadalin (Fintexa) propuso armar un calendario de ventanas de despliegue anticipado para los próximos pasajes (empezando por la v73, sin fecha exacta todavía — fines de septiembre o principios de octubre), para poder avisar a las entidades con antelación de que habrá una actualización sin comprometer todavía una fecha exacta, en vez de definir y comunicar la fecha recién en cada reunión de riesgo puntual. Matias Alzogaray (PM de desarrollo, Fintexa) aceptó "probarlo" — **no es una decisión cerrada**, es una prueba a evaluar con la v73.

**Estado:** Propuesta a probar, sin decisión formal. A confirmar en un próximo barrido si se implementó con la v73.
