---
id: 2026-10-06_arquitectura_decision_escalado_bd_proyecto_independiente
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_meetings — reunión 'Repaso Semanal líderes' (2026-10-06 10:59, compartida evignoles), minuta Gemini"
producto: transversal
tema: Escalado automático de base de datos / objetivo "Zero Downtime" se trata como proyecto arquitectónico independiente, no como tarea de infraestructura menor
tipo: decision
destino_propuesto: 3_recursos/arquitectura_sistema/index.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

En "Repaso Semanal líderes" (2026-10-06), al repasar un pendiente de infraestructura, Daniel Zalazar (Fintexa) aclaró que el objetivo de lograr cero interrupciones ("Zero Downtime") mediante el escalado automático de bases de datos no es únicamente un tema de infraestructura puntual, sino un proyecto arquitectónico integral que requiere mayor tiempo de desarrollo que el que se le venía dando. Se concluyó en la reunión que el escalado de base de datos se tratará de acá en más como un proyecto independiente (no una tarea suelta dentro de otro proyecto o del mantenimiento general de infraestructura).

No se asignó owner de Producto, fecha ni alcance formal en esta reunión — es una decisión de encuadre/gobernanza técnica (cómo se va a trackear el esfuerzo), no el arranque de un discovery. Se relaciona con el contexto ya conocido de alto costo de infraestructura (>USD 50.000/mes, con propuesta de rate limiting por entidad) capturado el 2026-09-29 en la misma reunión recurrente.

> Fuente: reunión "Repaso Semanal líderes" (2026-10-06), minuta Gemini.
