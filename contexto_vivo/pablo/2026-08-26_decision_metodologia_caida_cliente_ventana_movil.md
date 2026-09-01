---
id: 2026-08-26_decision_metodologia_caida_cliente_ventana_movil
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_metrics — sesión de revisión del reporte, semana 202634"
producto: transversal
tema: Detector de "caída de cliente" debe migrar a la misma metodología de ventana móvil 4x4 semanas que ya usan las NSM y las palancas
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

**Contexto/Problema:** el detector de "caída de cliente" de `/sync_metrics` (`detectar()` en `pipeline.py`)
mide comparando la última semana cerrada contra el promedio de las 4 semanas previas (sin incluir la
semana actual). Esta métrica es sensible a que la última semana de un bloque sea floja para una entidad en
particular (patrón conocido, señalado por el usuario) — en clientes con alta volatilidad semanal, una sola
semana débil genera una caída porcentual muy alta que no refleja una tendencia real.

**Caso concreto que destapó el problema (semana 202634):** el hallazgo "Tarjeta Sucredito cayó −60,7%"
(semana vs. promedio de 4 semanas previas) no cerraba contra un dashboard mensual propio de Comercial, que
mostraba una caída mucho más moderada. Recalculando con la metodología de "Tendencia" que ya usan las NSM
y las palancas (acumulado de las últimas 4 semanas cerradas vs. las 4 previas — la misma semana floja
queda diluida entre las otras 3 del bloque), la caída real fue de solo −9,7%, consistente con el dashboard
de Comercial. En cambio, aplicada al mismo caso de Terra Blockchain (caída ya confirmada como real y
sostenida), la nueva metodología dio −86,9% — prácticamente igual al −83,6% original — confirmando que no
diluye señales reales, solo ruido de una semana puntual.

**Decisión tomada:** migrar el detector de "caída de cliente" (y cualquier detector análogo a nivel de
entidad/collector/organización) de "semana vs. promedio de 4 semanas previas" a "acumulado de últimas 4
semanas cerradas vs. acumulado de las 4 semanas previas" — la misma ventana móvil (`VENTANA_TENDENCIA`,
ya usada en `bloque_movil()` para las NSM y en `medio_palancas()`/`_detectar_palancas` para las palancas).
Unifica el criterio de "caída" en todos los niveles del pipeline (NSM, palanca, cliente) bajo una sola
metodología, ya validada.

**Impacto en el roadmap/producto:** requiere un cambio de código en `pipeline.py` — específicamente en la
función `detectar()` que genera los "candidatos a hallazgo" de caída de cliente (hoy compara semana actual
vs. `estadisticas de las 4 semanas previas`; hay que sumarle el cálculo de ventana 4×4 igual que
`bloque_movil()`, y usarlo como criterio primario de "caída" en vez del semana-vs-promedio, que puede
quedar como dato secundario/WoW igual que ya ocurre con las NSM). El script está espejado desde
`CEREBRO_CORE` en este install — el cambio no puede aplicarse en esta sesión, necesita hacerse en el repo
compartido y propagarse por el mecanismo normal de espejo. No urgente para la operación de la skill (el
piso de materialidad y el criterio editorial del PM siguen filtrando falsos positivos manualmente
mientras tanto), pero sí deseable antes de la próxima corrida con clientes volátiles para evitar repetir
esta alarma falsa.

**Estado:** Aprobado (confirmado por el usuario en la sesión, validado con el caso Sucredito vs.
Terra Blockchain) — pendiente de implementación en `pipeline.py`.
