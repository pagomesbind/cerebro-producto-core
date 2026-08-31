---
id: 2026-08-27_transversal_calendario_anticipado_despliegues_propuesto
pm: pablo
fecha_captura: 2026-08-28
fuente: "/sync_meetings — reunión 'Adquirencia V72: Pre-Despliegue' (2026-08-27), minuta Gemini"
producto: transversal
tema: Reprogramaciones recurrentes de pase a producción dañan la relación con clientes — propuesta de calendario de despliegues anticipado
tipo: conocimiento
destino_propuesto: 2_areas/procesos/comunicacion_de_lanzamientos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

En la reunión de pre-despliegue de la versión 72 de Cobro/Adquirencia (2026-08-27), el pase a producción se reprogramó del jueves 27/08 21hs a la noche del lunes 31/08 por 12 tickets con errores críticos de QA sin cerrar (Simpra, CBU collect, webhooks duplicados de DPay, desarrollos en CUAP). Gonzalo Rivera (Integraciones/Soporte) planteó una queja de fondo, no puntual de este release: las reprogramaciones recurrentes de fechas ya comunicadas a clientes generan una percepción de falta de profesionalismo — citó el precedente reciente de APIBank (modificación de fecha la misma semana) y señaló que los clientes ya ponen en marcha sus propios avisos internos (popups en billeteras, personal de control) en base a la fecha que Bind les confirma, y tienen que reavisar cuando esa fecha cambia. Pablo Gomes respondió que el riesgo de postergar es preferible al de pasar a producción algo que después falle, pero reconoció que la comunicación institucional después de la reunión de riesgo debe mejorar.

**Propuesta discutida (sin decisión formal, a probar con la v73):** Mariana Nadalin (Fintexa) propuso armar un calendario de ventanas de despliegue anticipado para los próximos pasajes (empezando por la v73, sin fecha exacta todavía — fines de septiembre o principios de octubre), para poder avisar a las entidades con antelación de que habrá una actualización sin comprometer todavía una fecha exacta, en vez de definir y comunicar la fecha recién en cada reunión de riesgo puntual. Matias Alzogaray (PM de desarrollo, Fintexa) aceptó "probarlo" — no es una decisión cerrada, es una prueba a evaluar. Contexto adicional que explica la recurrencia del problema: esta versión arrancó con 126 tickets (hoy ~30) y viene absorbiendo hotfixes/excepciones (ej. el fix de estados de tarjetas para Coto, tratado aparte y ya desacoplado de este pase) que se suman sobre la marcha.

**Relación con el canon existente:** el proceso ya documentado en `2_areas/procesos/analisis_de_riesgo_de_despliegue.md` define cómo se arma el informe de riesgo y su semáforo, pero no contempla un calendario de ventanas *anticipado* — la fecha de pase hoy se fija recién en la reunión de riesgo puntual (con 4 días hábiles de antelación mínima), lo que no deja margen si aparecen tickets críticos de QA a último momento, como pasó acá. `2_areas/procesos/comunicacion_de_lanzamientos.md` (acordado 2026-08-18) cubre la comunicación *interna* post-lanzamiento ("avisos de producto"), un tema relacionado pero distinto — esta captura es sobre comunicación *externa* (a clientes) y sobre el *calendario* de fechas, no sobre el aviso de que algo ya se lanzó.

**Impacto directo en un proyecto vivo:** este mismo retraso empujó la fecha de pase de PRD-216 (Arcos Dorados, AD-1434) del 27/08 al 31/08 — ver `1_proyectos/prd-216_arcos_dorados_productos_resolve/proyecto.md §7/§8` y `1_proyectos/tareas.md` (T-042).

> Fuente: Reunión "Adquirencia V72: Pre-Despliegue" (2026-08-27), minuta Gemini.
