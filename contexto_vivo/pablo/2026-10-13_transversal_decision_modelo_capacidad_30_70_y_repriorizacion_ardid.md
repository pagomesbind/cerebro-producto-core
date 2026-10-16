---
id: 2026-10-13_transversal_decision_modelo_capacidad_30_70_y_repriorizacion_ardid
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Roadmap compliance' (2026-10-13, 16:46)"
producto: transversal
tema: Modelo de capacidad 30% mantenimiento / 70% nuevas iniciativas para Onboarding+Wallet+Ardid, y repriorización de Ardid por sobre un pedido de Compliance
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Decisión

Pablo Gomes (con Nicolás Colón) definió un **modelo de capacidad para los carriles de Onboarding, Wallet y Ardid** de cara a noviembre-marzo: tomando una ventana de 3 meses, **30% del rendimiento del equipo se destina a mantenimiento/remediación y 70% a nuevas iniciativas**. La carga estimada actual es de **200-300 puntos de historia** entre Onboarding y Wallet solamente. El criterio explícito: "si me estoy pasando de [la capacidad disponible], es muy probable que lo que estás planificando no va a suceder" — el roadmap se arma contra la capacidad real, no contra el deseo del negocio.

## Repriorización confirmada

Se decidió **priorizar las tareas normativas de Ardid por encima de un requerimiento de Compliance** para diciembre — Emma Vignoles quería un desarrollo de Compliance en noviembre, evaluado como no factible por competencia directa de recursos de Wallet. El ítem de Compliance se reagenda y Ardid (CPF + Coelsa Prevent) pasa a ser la prioridad del período.

## Decisiones complementarias de la misma reunión

- **Enfoque institucional:** abocarse los próximos meses a estabilizar lo existente, pausando la incorporación de desarrollos nuevos no normativos — "lo que no es normativo o no es algo que estoy incumpliendo, pateárselo a febrero/marzo; si no es importante, dejarlo pendiente".
- **Descarte temporal** del requerimiento de "desconocimiento de tarjeta" en Ardid (pedido por Maru, sin demanda activa confirmada) — pasa a pendiente para repriorizar.
- Reuniones de "innovación"/negocio con el área comercial: se evalúa retomarlas una vez por mes (en vez de semanalmente como antes) para que el negocio vea con qué capacidad real cuenta Producto, en vez de asumir que todo entra.
- Se identificó la necesidad de una **herramienta de shaping/estimación gruesa** integrada al roadmap (bocetada conceptualmente: un botón "estimar" por ítem que devuelva una estimación aproximada en puntos) para dejar de depender exclusivamente de Jira, que el PM describe como "siempre desactualizado" para ver qué entra en qué mes — intención, sin desarrollo todavía.

## Normativas con deadline confirmado en esta reunión

- **CPF (Ardid informa alertas fraudulentas a CPF)** e **integración de validación de altas en CPF**: diciembre, con riesgo explícito de no llegar a noviembre ni octubre.
- **Score de riesgo de Coelsa Prevent (norma 8473)**: Coelsa tiene hasta el 1 de enero de 2027 para disponer el servicio; corren luego 60 días para altas y 90 días para monitoreo transaccional — objetivo operativo para **marzo de 2027**.

> Fuente: reunión "Roadmap compliance", 2026-10-13 16:46hs (Pablo Gomes, Nicolás Colón).
