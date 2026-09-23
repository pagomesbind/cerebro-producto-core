---
id: 2026-09-21_transversal_conocimiento_capacidad_desarrollo_100sp_vs_300sp
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_meetings — reunión \"Producto\" (14:01, con Emma Vignoles/Nicolás Colón), 2026-09-21"
producto: transversal
tema: Entrega mensual de Producto/desarrollo bajó de ~300 a ~100 puntos de historia — posible dato medido para reemplazar la restricción de capacidad hardcodeada retirada de estado_actual.md
tipo: conocimiento
destino_propuesto: 2_areas/direccion/estado_actual.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

**Hallazgo (reunión "Producto", 2026-09-21):** al discutir la capacidad reducida del equipo de producto/desarrollo, se mencionó que la entrega actual promedia **~100 puntos de historia mensuales**, frente a **~300 anteriores** — sin especificar el período exacto de comparación ("antes" no tiene fecha), ni si el dato surge de un reporte formal (Jira/velocity) o es una estimación conversacional de quien habló en la reunión (identificado en la minuta solo como "alguien en 7F (Plaza San Martin, 7)", posible error de transcripción de Gemini sobre el nombre real del hablante).

**Por qué puede ser relevante para el canon:** el 2026-09-10 se capturó un item (`2026-09-10_contexto_fijo_correccion_restriccion_capacidad_estado_actual`, todavía en cola/régimen D) que retira de `estado_actual.md` la restricción de capacidad hardcodeada (~1 IDEA cada 3 meses vs. ~6 abiertas) por ser "un decir coloquial, no un dato medido" — dejando pendiente (T-083) reemplazarla por un dato real de `/sync_releases`. Este hallazgo (100 vs. 300 SP/mes) podría ser ese reemplazo, o un dato complementario — pero **no viene de `/sync_releases` ni de un reporte verificado**, viene de una mención al pasar en una reunión. No se cuantificó a qué se atribuye la caída (¿bajas de personal, foco en soporte/mantenimiento, cambio de metodología de estimación?) ni el rango de fechas exacto.

**Contexto adicional de la misma reunión:** se mencionó también que la capacidad reducida está generando que Producto se involucre más directamente en pruebas y puesta en producción de iniciativas (ej. "pagos efectuados y visores") por limitaciones operativas del equipo de desarrollo, y que hay múltiples frentes en curso en paralelo (Ardid, comprobantes, validaciones).

**Pregunta para el usuario:** ¿este dato (100 vs. 300 SP/mes) es el reemplazo que busca T-083, o hace falta esperar el dato formal de `/sync_releases`? Si se usa, falta precisar el período de comparación y la fuente (¿Jira, estimación informal?).
