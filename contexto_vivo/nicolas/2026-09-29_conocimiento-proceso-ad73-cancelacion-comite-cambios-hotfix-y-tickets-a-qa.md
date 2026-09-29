---
id: 2026-09-29_conocimiento-proceso-ad73-cancelacion-comite-cambios-hotfix-y-tickets-a-qa
pm: nicolas
fecha_captura: 2026-09-29
fuente: "Mail 'MINUTA - Reunión de Pre-despliegue AD 73: Jue, 24 de sept de 2026' — Matías Alzogaray, enviado 2026-09-28 (minuta completa; hasta ahora solo se conocía el resumen del mail de Gemini)"
producto: transversal
tema: Lecciones de proceso del pase cancelado de AD V73 — tickets sumados a último momento, propuesta de comité de cambios (urgencias como hotfix aparte), tickets a QA con documentación completa, filtro de observaciones de QA
tipo: conocimiento
destino_propuesto: 2_areas/procesos/analisis_de_riesgo_de_despliegue.md
tipo_destino: actualizar
contradice: "no — alimenta el '⚠️ Gap abierto — sin criterio explícito para decidir cuándo un ticket es hotfix' de ese archivo con una propuesta nueva, todavía en stand-by (no es una decisión tomada)"
confianza: media
estado: en_cola
---

**Por qué se canceló el pase de AD V73 del 24/09.** La minuta completa de la "Reunión de Pre-despliegue AD 73" (24/09, enviada por mail por Matías Alzogaray el 28/09) da la causa de proceso, además de los errores de liquidaciones ya capturados:
- Entraron **tickets de soporte y requerimientos de alta prioridad (BINes) a último minuto**, y hubo inestabilidad en el ambiente de staging. El equipo no llegó a cerrar todos los tickets de la versión.
- Se dijo que sumar tickets a una versión a pocas horas del pase **sobrecarga a QA y obliga a reiniciar las regresiones**. Hay que mejorar la comunicación y decidir en conjunto.
- Muchos tickets marcados como defecto (sobre todo en **Pagos FX**) eran en realidad **mejoras visuales o componentes despriorizados**. No se consideraron bloqueantes.

**Propuestas en stand-by (no aprobadas todavía):**
1. **Comité de cambios.** Revisar cómo se prioriza y definir si los requerimientos urgentes de último momento se tratan como **hotfixes externos** en vez de forzarlos dentro de un versionado que ya está encaminado. Es el criterio que le falta al gap abierto de `analisis_de_riesgo_de_despliegue.md` sobre cuándo un ticket es hotfix.
2. **Tickets a QA con documentación completa.** Que cada ticket llegue a QA con lo necesario para probarlo (endpoints, colección de Postman, etc.), para no perder tiempo buscando información. Se plantea como mejora continua.
3. **Filtro de observaciones de QA.** Mejorar el criterio para separar rápido los bloqueos reales de las observaciones que son requerimientos nuevos o mejoras funcionales.

**Acción relacionada de la minuta:** Mariela Marin (Fintexa QA) tenía que evaluar para el 25/09 por qué las ejecuciones de tests previas no detectaron las fallas de liquidación. Esta fuente no trae el resultado.

> Fuente: Mail "MINUTA - Reunión de Pre-despliegue AD 73: Jue, 24 de sept de 2026 a las 4:30pm – 5:00pm (GMT-03)" — Matías Alzogaray (2026-09-28).
