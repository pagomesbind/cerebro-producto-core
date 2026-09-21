---
id: 2026-09-21_wallet_conocimiento_w73_qa_externo_delay_w74_w75
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_mails — mail 'Informe Estado Proyectos Emisión al 18/09/2026' (threadId 1a0b6242d50cbb44), Nicolas Pomponio (Fintexa), 2026-09-18"
producto: wallet
tema: Wallet W73 pasó a PROD; entrega a QA Externo se retrasa de lunes 21/09 a miércoles; split confirmado en W74 (fin octubre)/W75
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/index.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Continuación/actualización del estado ya capturado en `2026-09-16_wallet_estado_epicasepocas_reformulacion_w73` (todavía en cola, sin mergear) — este item no lo reemplaza, lo completa con el informe semanal siguiente de Fintexa (18/09):

- **17/09/2026:** se pasó a PROD la versión **W72.3**, con el MVP2 de Pagos FX y la puesta en PROD de Apibuffer para la organización DEMO.
- **Split confirmado en dos versiones quincenales** (acordado con Bind PSP en la reunión de refinamiento): **W74** (objetivo de salida fin de octubre) y **W75**.
  - W74 incluye los desarrollos de FCI que habían quedado pateados de W73 (ya desarrollados, pendiente completar QA). A partir de ahora **FCI deja de informarse en el informe semanal** de Fintexa porque ya está en PROD y estable.
  - W75 incluye el desarrollo de Worldsys (solución de KYC en LATAM), pedido por Bind PSP de cara al cierre de mes.
  - Se empieza a taggear en Jira los tickets candidatos al alcance final de W74 — Bind PSP se compromete a revisar y confirmar el alcance.
- **Retraso de entrega a QA Externo:** por la carga de la versión W73, no se llega a entregar a QA Externo el lunes 21/09 como estaba previsto. Se aprovecha que QA Externo va a estar probando la versión del equipo de Cobros y se extiende el QA interno hasta el miércoles, liberándose a medida que se van terminando las historias.

**Épica Mastercard Move (Pagos Crossborder) — pasos operativos pendientes para que el MVP2 funcione:** anular todos los beneficiarios actuales (script compartido con el negocio), forzar la fecha de actualización de corredores (script compartido), correr nuevamente el proceso de actualización de corredores, dar de alta nuevos beneficiarios bajo el nuevo modelo, y repasar todo el flujo (documento paso a paso ya compartido).

> Fuente: mail "Informe Estado Proyectos Emisión al 18/09/2026" (Nicolas Pomponio, Fintexa, threadId `1a0b6242d50cbb44`), 2026-09-18.
