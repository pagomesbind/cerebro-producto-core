---
id: 2026-10-06_transversal_gap_depuracion_registros_wallet_retencion
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_meetings — reunión 'Repaso Semanal líderes' (2026-10-06 10:59, compartida evignoles), minuta Gemini"
producto: transversal
tema: Depuración de registros antiguos de Wallet (>6 meses, programada 13/10) sin verificación explícita contra requisitos de retención regulatoria
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "2_areas/direccion/... (vía contexto_vivo, item 2026-10-05_cumplimiento_conocimiento_res_uif_200_24_art17_conservacion_10_anos, en_cola) — ese item establece un plazo de conservación de 10 años de documentación de clientes (art. 17 Res. UIF 200/24) para Onboarding/Legajo Digital; este hallazgo es sobre depuración de 'registros antiguos de la wallet' (no necesariamente documentación de legajo/KYC, posiblemente datos transaccionales/operativos) y no queda claro en la minuta si ambos conjuntos de datos se superponen o son dominios separados"
confianza: baja
estado: en_cola
merge_commit:
---

En "Repaso Semanal líderes" (2026-10-06) se acordó, sin debate ni objeción, programar la depuración de registros antiguos de la base de datos de Wallet para el martes 13 de octubre, en la ventana horaria de 4:00 a 6:00 a.m. Daniel Zalazar (Fintexa) informó que, en acuerdo con los DBA y Gonzalo Damian Rivera, se depurarán registros anteriores a seis meses de antigüedad, tras confirmar que la operación requiere bajar el ecosistema completo para ejecutarse. Daniel Zalazar asumió la tarea de informar la modalidad operativa a los clientes, y confirmó que no se requieren pruebas posteriores al tratarse de "datos históricos".

**Gap detectado (no mencionado ni discutido en la reunión):** la minuta no especifica qué tipo de registro se depura (¿logs técnicos? ¿transacciones? ¿datos de legajo/onboarding?) ni si se validó contra algún requisito de retención regulatoria antes de fijar la fecha. Esto es potencialmente relevante porque el Cerebro ya tiene capturado (2026-10-05, vía `/sync_mails`, item `tipo: conocimiento` pendiente de merge) un plazo de conservación de 10 años de documentación de clientes según el art. 17 de la Res. UIF 200/24, aplicable a Onboarding/Legajo Digital. Si "registros antiguos de la wallet" incluyera cualquier dato de identificación/legajo de clientes (y no solo logs operativos o historial transaccional de bajo valor regulatorio), depurar a los 6 meses contradiría directamente ese plazo de 10 años.

No hay evidencia en la minuta de que el equipo haya considerado esta distinción — se trata como una tarea puramente técnica de mantenimiento de base de datos (DBA + Fintexa), sin participación de Compliance/PLD en la decisión. Confianza baja porque no está confirmado qué datos concretos se depuran; se registra como gap para que el PM confirme el alcance antes de la fecha programada (13/10).

> Fuente: reunión "Repaso Semanal líderes" (2026-10-06), minuta Gemini.
