---
id: 2026-08-26_dato_reporte_metricas_semanales_202634
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_metrics — análisis y reporte semanal, semana 202634 (17 al 24 de agosto de 2026)"
producto: transversal
tema: Reporte narrado de métricas semanales (NSM) — semana 202634
tipo: dato
destino_propuesto: 3_recursos/datos/metricas_semanales.md
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Contenido final y completo del archivo `3_recursos/datos/metricas_semanales.md`, con la entrada de la
semana 202634 antepuesta al histórico existente (que se conserva íntegro debajo, sin alterar). El archivo
completo resultante ya está generado en
`wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/metricas_semanales_completo.md` —
`/context_merge` copia ese archivo, byte a byte, sobre `3_recursos/datos/metricas_semanales.md`.

**Resumen de la entrada nueva (semana 202634, 17 al 24 de agosto de 2026):**

- NSM#1 (Volumen API BANK): $179.788 M, WoW −36,9%, vs. promedio 4 semanas −32,4%, vs. baseline 13 semanas
  −26,2%, tendencia ventana móvil −0,1% (casi plana).
- NSM#2 (Volumen Payway): $7.659 M, WoW −35,0%, vs. promedio 4 semanas −27,5%, vs. baseline 13 semanas
  +3,7% (prácticamente en línea con su nivel típico), tendencia ventana móvil +18,3%.
- 6 hallazgos: (1) la caída WoW fuerte en ambas NSM se explica en gran parte por el feriado nacional del
  lunes 17 de agosto (Paso a la Inmortalidad del Gral. San Martín, un día hábil menos) y por la vuelta a la
  normalidad de Payway tras el pico de cobro de servicios de las dos semanas previas — no es una señal
  estadísticamente inusual (z-score dentro de rango); (2) Terra Blockchain profundiza su caída en Wallet
  por **cuarta semana consecutiva** (−83,6% vs. promedio 4 semanas; verificado con una segunda
  metodología en −86,9%, confirma que es real); (3) BSF (Carrefour) concentra el 61,5% del volumen de
  Wallet; (4) **corrección de lectura sobre Tarjeta Sucredito** — el −60,7% reportado inicialmente en
  Payway era ruido de una semana floja, no una caída sostenida (recalculado con ventana móvil 4×4 semanas:
  −9,7%, consistente con el dashboard mensual de Comercial); (5) La Virginia sostiene por cuarta semana un
  ritmo de altas de comercios fuera de lo habitual (77% de las altas de la semana); (6) las transferencias
  entrantes del Agente de Cobros vienen creciendo sostenido hace 6 semanas (+9,2% semanal).

**Corrección post-envío (2026-08-26, mismo día):** el usuario cuestionó el hallazgo de Sucredito cruzándolo
contra un dashboard mensual propio de Comercial — la revisión confirmó que la comparación semana-vs-
promedio sobreestimaba el ruido en un cliente con alta volatilidad semanal. Se corrigió el hallazgo (wiki
y email) y se retiró a Sucredito de la escalación a Comercial. El mismo ejercicio, aplicado a Terra
Blockchain, confirmó que esa caída sí es real. Se registró la decisión de migrar el detector de "caída de
cliente" del pipeline a la metodología de ventana móvil 4×4 semanas — ver
`2026-08-26_decision_metodologia_caida_cliente_ventana_movil`.

Los hallazgos 2 y 5 son continuación de gaps ya abiertos en `2_areas/gaps_y_preguntas.md` (Terra
Blockchain/Sucredito desde 2026-08-04, La Virginia desde 2026-08-04) — ver las actualizaciones propuestas
en los items de gap de esta misma corrida (incluye el cierre de la mitad del gap referida a Sucredito).
Además se creó la tarea personal T-036 en `1_proyectos/tareas.md` para escalar formalmente a
Soporte/Comercial el estado de Terra Blockchain (ya corregida para no mencionar a Sucredito), dado que el
patrón de cuatro semanas consecutivas ya supera el umbral de "esperar una semana más" que se venía
aplicando.

Se generó también el email semanal (`email.html`, mismo `palancas.json`/`hallazgos.json` que alimentan
esta entrada) y quedó como borrador en Gmail — el primer borrador se perdió (gotcha conocido de la skill,
ver `SKILL.md`) y se recreó con el contenido ya corregido; confirmado con `list_drafts`.
