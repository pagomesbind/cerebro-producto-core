---
id: 2026-08-21_adquirencia_cbu_corto_csv_deprecado
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_meetings — reunión 'Análisis de riesgos AD V72' (2026-08-21 14:02, docId 1cuABvOG3eEhMaN3XDQtF5ofpEqHmXewlt85OeXfC7EY)"
producto: adquirencia
tema: Retiro del método de carga masiva de CBU Corto por archivo CSV — solo queda activo el pedido "por cantidad"
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/adquirencia/herramientas_operativas_boton_simple.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

En el lote de despliegue de AD V72 (27/08/2026) se retira el método obsoleto de carga masiva de CBU/CBU Corta U mediante archivos CSV (ticket 1139). A partir de este release, la **única vía activa para generar stock de CBU Corto en lote es el pedido "por cantidad"** (el mecanismo ya documentado en `herramientas_operativas_boton_simple.md` — alta de CVU masivo). Cualquier integración o proceso operativo (Soporte, scripts) que todavía dependa del formato CSV deja de funcionar tras el pase.

Clasificado con semáforo verde por el equipo (bajo riesgo, sin clientes activos identificados usando el método CSV al momento de la reunión).

> Fuente: Reunión "Análisis de riesgos AD V72" (2026-08-21), minuta Gemini — sección Decisiones, "Eliminación de carga masiva por CSV" y Detalles ([00:37:40]-[00:38:56]).
