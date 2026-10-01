---
id: 2026-09-29_arquitectura_decision_waf_geolocalizacion_y_secretos_codigo
pm: pablo
fecha_captura: 2026-09-29
fuente: "/sync_meetings — reunión \"Repaso Semanal líderes\" (2026-09-29 11:00, compartida por evignoles), minuta Gemini"
producto: transversal
tema: "Reglas de WAF por geolocalización (bloqueo China/Rusia) en camino a producción, nuevo procedimiento para secretos hallados en código fuente"
tipo: decision
destino_propuesto: 3_recursos/arquitectura_sistema/seguridad_de_plataforma.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

En "Repaso Semanal líderes" (2026-09-29), con Fintexa (Pablo Vargas, Hernán Clarich y equipo):

**Reglas de WAF por geolocalización — acordada:** ya aplicadas y monitoreadas en **staging**, con el fin de restringir tráfico de países como **China y Rusia**. Si funcionan bien esta semana, pasan a **producción**. Responsable de la implementación productiva: Pablo Vargas (Fintexa).

**Procedimiento de secretos en código fuente:** Fintexa expuso un nuevo procedimiento sobre cómo actuar ante el hallazgo de secretos (credenciales, tokens, etc.) en el código fuente — cuenta con acuerdo general del equipo y se comunica en una capacitación al área de desarrollo el viernes siguiente a esta reunión (2026-10-02).

**Pendiente relacionado, sin resolver en esta reunión:** Emma Vignoles exigió mayor visibilidad y priorización sobre los hallazgos de **pentests** (pruebas de intrusión) más allá de recibirlos solo por correo — se acordó coordinar una reunión específica de visibilidad (sin fecha fijada todavía).

> Fuente: reunión "Repaso Semanal líderes", 2026-09-29 (`/sync_meetings`), minuta de Gemini (docId `1yvPrMP0eehP2qw4fUey7i8eISz5rKtZtlWaXpB_LLCI`).
