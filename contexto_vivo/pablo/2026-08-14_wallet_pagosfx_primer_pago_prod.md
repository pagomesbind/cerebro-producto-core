---
id: 2026-08-14_wallet_pagosfx_primer_pago_prod
pm: pablo
fecha_captura: 2026-08-17
fuente: "/sync_mails — mail \"Informe Estado Proyectos Emisión al 14/08/2026\" (threadId 1a001fd354c0211d), Nicolás Pomponio (Fintexa), 2026-08-14"
producto: wallet
tema: Primer PagoFX productivo real (Mastercard Move) — sin webhooks de estado, resuelto por consulta BGS
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_fx.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: capturado
merge_commit:
---

**Fuente:** informe semanal recurrente de Fintexa sobre el proyecto Wallet (Nicolás Pomponio), 14/08/2026. Épica "Mastercard Move (Pagos Crossborder)" — destino natural es `dolar_fx.md` §2, que ya documenta el wrapper de Mastercard Move y las APIs publicadas hasta W70 (PRD-10, iniciativa de Luciana Rudaz).

**Hito:** se realizó el **primer PagoFX productivo real** (primera transacción crossborder de Pagos FX en ambiente PROD).

**Hallazgo operativo:** no se observó la llegada de webhooks por cambios de estado de pago del lado de Mastercard — se solicitó información al proveedor. El pago terminó resolviéndose por **consulta de estado vía BGS**, no por webhook. Se sigue dando soporte al negocio y analizando resultados del ambiente productivo, detectando ambigüedades y levantando nuevos tickets para el MVP2.

**Avance en STG (MVP2):** se detectaron ajustes al flujo de alta de beneficiario a partir de diferencias observadas en PROD. Fixes en curso:
- Contemplar campos opcionales con obligatoriedad condicional (special notes) en la consulta del Endpoint Guide.
- Obtener datos del sender para asociarlos al alta de beneficiario.
- Excluir `purpose_of_payment` de la validación y persistencia en el alta de beneficiario.
- Validar `purpose_of_payment` en la ejecución de un pago FX.

**Alerta de alcance:** se agregaron 4 nuevas historias de usuario al MVP2 no contempladas en el alcance inicial de la versión W 72.1 — riesgo sobre los plazos comprometidos, señalado explícitamente por el equipo.

**Próximos pasos:** esperar respuesta de Mastercard sobre los webhooks faltantes; colaborar con el front del portal en soporte de configuraciones.

> Nota: Pagos FX/Mastercard Move es del foco estratégico liderado por Luciana Rudaz — Pablo Gomes está en copia del informe semanal por ser PM de Wallet, no como owner de esta iniciativa.
