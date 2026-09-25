---
id: 2026-09-24_transversal_riesgo_discrepancia_sp_fintexa
pm: pablo
fecha_captura: 2026-09-24
fuente: "/sync_mails — mail 'Comparativa SP Fintexa - Bind Psp', Matías Alzogaray, threadId 1a0d56c7e8ec2911, 2026-09-24"
producto: transversal
tema: discrepancia sistemática de Story Points entre el Jira propio de Bind y lo que reporta/factura Fintexa — riesgo de sobrefacturación
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 2bc1252
---

## Descripción del hallazgo

Matías Alzogaray (PM) comparó los Story Points cargados en el Jira de Bind (AD/WS) contra los que reporta Fintexa por los mismos tickets, sobre una muestra que encontró **35 registros con diferencias** (20 en Adquirencia, 15 en Wallet/Onboarding — sigla WS), resultando en **+53.75 SP netos a favor de Fintexa** (es decir, Fintexa reporta/factura más SP de los que Bind tiene cargados). Adjunta el detalle completo en `Comparación SP Fintexa y Bind Sept 2026.xlsx` (no procesado automáticamente por esta skill — ver nota de adjuntos).

**Composición del desvío:**

1. **Aumentos injustificados de puntos (+100.5 SP, 28 tickets):** Fintexa subió el SP de 28 tickets respecto al valor original en Jira. Los saltos más grandes: 5 tickets duplicaron el esfuerzo de 7→15 SP (`AD-509`, `AD-860` —aparece duplicado en el registro de Fintexa—, `WS-80`, `WS-181`, `WS-1313`; +48 SP solo estos 5). Saltos medios de 3→7 SP en `AD-621`, `AD-647`, `AD-985`, `WS-817` (+4 SP c/u). Micro-aumentos de 1→3 SP en 8 tickets chicos (`AD-700`, `AD-807`, `AD-453`, `AD-845`, `AD-820`, `AD-1103`, `AD-50`, `WS-738`).
2. **Tickets "fantasma" (+13.5 SP, 7 tickets):** tickets que en el Jira de Bind figuran con 0 SP (probablemente tareas administrativas o bugs sin costo) a los que Fintexa les asignó puntos igual. Casos principales: `AD-1006`, `WS-218`, `WS-1314`, `WS-1364` (0→3 SP c/u); fracciones menores en `WS-1311` (0→0.25), `WS-1470` (0→0.25), `WS-1441` (0→1).
3. **Disminuciones/"descuentos" (-46.75 SP, 7 tickets):** en sentido contrario, Fintexa se asignó menos SP de los que Jira tenía en algunos tickets — `AD-688` 15→1 (-14), `WS-565` 15→0.5 (-14.5), `WS-560` 15→7 (-8), entre otros.

**Lectura de Matías Alzogaray (textual):** "los tickets más complejos sufren reducciones extrañas (quizás por no haberlos terminado o por cambio de alcance), pero esto es compensado agresivamente inflando muchos tickets medianos y pequeños (subiéndolos de 1 a 3, de 3 a 7 y de 7 a 15) e inventando puntos en tickets que valían 0" — el balance neto, incluso descontando las reducciones, sigue siendo desfavorable para Bind (+53.75 SP).

## Por qué es un riesgo

Fintexa es el proveedor tecnológico externo que ejecuta el desarrollo de Bind PSP (ver relación documentada en discovery de varios proyectos del Cerebro). Si la facturación o el reporte de capacidad de Fintexa se basa en SP propios distintos de los que Bind tiene cargados en su propio Jira, hay riesgo de sobrepago o de distorsión en el cálculo de capacidad real del equipo — este mismo cálculo es insumo pendiente de T-083 (reemplazo de la restricción de capacidad hardcodeada retirada de `2_areas/direccion/estado_actual.md`, ver `contexto_vivo/2026-09-10_contexto_fijo_correccion_restriccion_capacidad_estado_actual.md`). Una comparación de SP que no concilia entre ambas partes también sugiere que el proceso de medición Build vs. BAU (`2_areas/procesos/`) podría no estar aplicándose de forma consistente del lado de Fintexa.

## Nota de adjuntos (pendiente)

El detalle fila por fila (los 35 registros) vive en el Excel adjunto (`Comparación SP Fintexa y Bind Sept 2026.xlsx`), no procesado automáticamente — ver T-128 en `tareas.md` para el seguimiento.
