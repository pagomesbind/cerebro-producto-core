---
id: 2026-09-29_conocimiento-worldsys-reversas-prueba-captura-ok-falta-listado-tipos-operacion
pm: nicolas
fecha_captura: 2026-09-29
fuente: "Mail 'RE: Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas.' — María Victoria Simonetti (BIND PLA/FT/FP) y Pablo Stach (Worldsys), 2026-09-28"
producto: transversal
tema: Reversas/comprobantes en LAVADOOPERACIONES — la prueba de captura de Worldsys salió bien en un ambiente bajo; falta que Bind mande el nuevo listado de tipos de operación para cargarlo en producción antes del 01/10
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md
tipo_destino: actualizar
contradice: "no — completa la cronología de §2 (punto 6, plan del 15/09): suma el resultado de la prueba de captura y el prerequisito pendiente para la entrada en vigencia"
confianza: alta
estado: ingestado
---

**Novedad sobre §2 de `reporteria_worldsys_bcra.md`** (nuevo esquema de reversas con monto negativo + `IdComprobante` + interfaz `TiposComprobantes`, con entrada en vigencia prevista para el procesamiento del 01/10/2026):

7. **Prueba de captura OK (28/09/2026, Pablo Stach — Worldsys).** María Victoria Simonetti (Analista Sr PLA/FT/FP de BIND) pidió novedades de las pruebas que se habían autorizado. Pablo Stach respondió que la prueba de captura **ya se hizo con éxito en un ambiente bajo**. Es la prueba en ambiente controlado (QA) que Leandro Competiello había comprometido el 15/09 para "la semana próxima". El mail no dice qué fecha exacta se corrió.
8. **Prerequisito pendiente del lado de Bind.** En el mismo mensaje, Worldsys pide a Bind (Vicky y Nicolás Colón) el **nuevo listado de tipos de operación** para empezar a cargarlo en el **ambiente productivo**. Es el cambio (b) del archivo de ejemplo del 01/09: la lista fija de `TIPOOPERACION` se reemplaza por la interfaz `TiposComprobantes`. Hasta que ese listado llegue y se cargue en producción, la entrada en vigencia del 01/10 depende de que Bind lo mande a tiempo.

Lo que el hilo no aclara todavía:
- si el documento de alcance/horas que Worldsys había prometido el 15/09 (por ser una "evolución") llegó y se aprobó;
- si Worldsys confirma que el 01/10 sigue en pie o si se corre por el listado pendiente.

> Fuente: Mail "RE: Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas." — María Victoria Simonetti (2026-09-28 18:31 ART) y Pablo Stach (2026-09-28 19:04 ART).
