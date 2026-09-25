---
id: 2026-09-25_gap-copel-contrato-qr-y-bcf-onboarding
pm: nicolas
fecha_captura: 2026-09-25
fuente: "Reunión 'Join Soporte Clientes' (2026-09-23) — resumen del mail de Gemini (Drive no disponible, sin minuta detallada)"
producto: transversal
tema: Copel (sin ficha) avanza a firma de contrato de cobros QR; "BCF" con análisis de riesgo por fraude — identidad a confirmar (¿Carrefour BSF?)
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: baja
estado: ingestado
merge_commit: 2bc1252
---

Dos novedades de clientes que no se pueden rutear a una ficha sin confirmar identidad:

1. **Copel — contrato de "solución de cobros con Copel QR" en firma.** Mauro Suppan hará el seguimiento de la firma. Es coherente con la decisión comercial ya capturada (2026-09-17: freeze de integraciones hasta tener contrato firmado, pricing elevado). Copel **sigue sin fila en `log_clientes.md`** — gap ya abierto en canon; esta es nueva evidencia de que la relación avanza y la ficha va a hacer falta. Para `/sync_customers`.
2. **"BCF" — análisis de riesgo por fraudes y pedido de su instructivo de onboarding.** Adriana Endzeliz le pedirá a BCF el instructivo actualizado de su proceso de onboarding para revisión interna. "BCF" no matchea ningún cliente en `log_clientes.md`; el candidato más probable es **Carrefour (BSF)** (fila existente, Wallet), que ya tiene un item de fraude en transferencias por app móvil (2026-09-17) — probable error de transcripción BSF→BCF. A confirmar antes de fusionarlo en la ficha de Carrefour.

Además, en la misma reunión Adriana Endzeliz quedó en consultar "la prioridad y estado del límite de ingreso de dinero para los onboardings menores" — posible cruce con los límites operativos de cuentas (ver gap abierto de $1.000 vs. $10.000 para PJ), sin detalle suficiente para capturarlo aparte.

> Fuente: Reunión "Join Soporte Clientes" (2026-09-23), resumen del mail de Gemini.
