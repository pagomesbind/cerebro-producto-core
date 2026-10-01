---
id: 2026-09-29_arquitectura_conocimiento_costos_infra_rate_limit_entidad
pm: pablo
fecha_captura: 2026-09-29
fuente: "/sync_meetings — reunión \"Repaso Semanal líderes\" (2026-09-29 11:00, compartida por evignoles), minuta Gemini"
producto: transversal
tema: "Costo de infraestructura productiva supera USD 50.000/mes por consumo inestable de entidades (Credicuota) — propuesta de rate limiting por entidad en 4 perfiles"
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/nfr_y_slas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

En "Repaso Semanal líderes" (2026-09-29): Emma Vignoles planteó que el costo de infraestructura en el ambiente productivo **supera los USD 50.000/mes**, atribuido en gran parte al consumo inestable de ciertas entidades — **Credicuota** fue señalada explícitamente como caso concreto.

**Propuesta/mecanismo en desarrollo (Hernán Clarich):** implementar **rate limiting por entidad**, con perfiles de consumo escalonados — **bronce, plata, oro, platino** — operando mediante políticas en **API Management** y claves de suscripción (subscription keys). Los valores de corte definitivos por perfil todavía están pendientes de análisis (no definidos en esta reunión). **Decisión acordada:** Hernán Clarich activará el rate limit por entidad en producción, previo análisis de los límites por cada producto y categoría.

> Fuente: reunión "Repaso Semanal líderes", 2026-09-29 (`/sync_meetings`), minuta de Gemini (docId `1yvPrMP0eehP2qw4fUey7i8eISz5rKtZtlWaXpB_LLCI`).
