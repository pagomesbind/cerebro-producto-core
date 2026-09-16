---
id: 2026-09-15_iniciativa-ardid-desconocimientos-problem-statement
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Sesión /idea_problem sobre ardid_desconocimientos (PRD-248), 2026-09-15"
producto: ardid
tema: ardid_desconocimientos — problem statement formal escrito
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: cb58cfd53c7f3d391017622178663faa33c1c2b8
proyecto: ardid_desconocimientos
---

Novedad sobre el proyecto `ardid_desconocimientos` (PRD-248, foco Ardid de Nicolás Colón): se escribió el problem statement formal vía `/idea_problem`, profundizando la medida e impacto que el discovery inicial no había llegado a cuantificar.

- **Corrección de dato:** la carga manual al motor antifraude no es semanal como se había registrado en el discovery original — es cada 1-2 semanas (en el mejor de los casos, semanal). Esto sube la ventana de exposición real (tiempo entre que se confirma un fraude y que la tarjeta queda bloqueada) a **hasta ~14 días**, no ~7 como se asumía antes.
- **Impacto sin cuantificar en plata:** se buscó una cifra propia de pérdida económica o un caso confirmado de reincidencia de fraude durante esa ventana — el PM confirmó que ya se consultó y no existe ese dato. El equipo coincide en que el riesgo es real de todos modos; queda como gap no bloqueante (ver `1_proyectos/ardid_desconocimientos/gaps.md`).
- **Meta acordada:** bajar la ventana de exposición a prácticamente inmediata (mismo día) y las ~2h cada 1-2 semanas de trabajo manual del equipo de Fraude a 0 — plazo concreto a definir recién en la mesa de estimación técnica.

El proyecto sigue sin gaps bloqueantes para pasar a diseño de solución/estimación. Detalle completo en `1_proyectos/ardid_desconocimientos/artefactos/ardid_desconocimientos-problem.md`.
