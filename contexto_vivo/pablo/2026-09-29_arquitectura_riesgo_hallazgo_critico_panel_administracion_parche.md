---
id: 2026-09-29_arquitectura_riesgo_hallazgo_critico_panel_administracion_parche
pm: pablo
fecha_captura: 2026-09-29
fuente: "/sync_meetings — reunión \"Repaso Semanal líderes\" (2026-09-29 11:00, compartida por evignoles), minuta Gemini"
producto: transversal
tema: "Hallazgo de alta criticidad en el panel de administración (pentest) — parche urgente programado para 30/09 o 01/10"
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: crear
contradice: "el índice de contexto_vivo (`contexto_vivo/index.md`) lista dos items del 2026-09-28 con id `2026-09-28_transversal_riesgo_vulnerabilidad_control_acceso_admin_centralizador` y `2026-09-28_transversal_decision_hotfix_admin_centralizador`, estado en_cola, aparentemente sobre el mismo hallazgo (Admin Centralizador, CVSS 8.7). Al verificar, ninguno de los dos existe como archivo físico en wiki/1_proyectos/contexto_vivo/ — mismo patrón de anomalía de integridad ya documentado repetidamente en el log de `/context_push` (filas de índice sin archivo real, o viceversa). No se pudo completar el item original; este item se captura de cero con lo que aporta la reunión de hoy, para que el hallazgo no se pierda aunque el original esté inaccesible."
confianza: media
estado: en_cola
merge_commit:
---

En "Repaso Semanal líderes" (2026-09-29): Emma Vignoles exigió a Pablo Vargas (Fintexa) y Hernán Clarich mayor visibilidad sobre los hallazgos de las pruebas de intrusión (pentests), más allá de un correo electrónico. En esa discusión, Hernán Clarich, Melisa Belpassi, Sebastián Ríos y Pablo Serra repasaron un **hallazgo de alta criticidad detectado en el panel de administración** durante pruebas técnicas de calidad — sin más detalle técnico en esta minuta sobre la naturaleza exacta de la falla.

**Acordado:** coordinar una reunión específica sobre el hallazgo y preparar un **parche urgente** para desplegarlo el **miércoles o jueves** siguientes a esta reunión (30/09 o 01/10 de 2026).

**Nota de contexto (ver `contradice`):** el índice de `contexto_vivo/` registra dos items previos del 2026-09-28 sobre, aparentemente, el mismo hallazgo en el "Admin Centralizador" (uno `tipo: riesgo` con CVSS 8.7, otro `tipo: decision` sobre la elección de hotfix vs. V74) — pero ninguno de los dos existe físicamente en el disco. Si este es el mismo hallazgo, este item aporta el dato nuevo (fecha concreta de parche); si el líder confirma que son hallazgos distintos, tratar como riesgo independiente.

> Fuente: reunión "Repaso Semanal líderes", 2026-09-29 (`/sync_meetings`), minuta de Gemini (docId `1yvPrMP0eehP2qw4fUey7i8eISz5rKtZtlWaXpB_LLCI`).
