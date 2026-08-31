---
id: 2026-08-31_wallet_pagos_fx_mvp2_manejo_errores_mastercard_move
pm: pablo
fecha_captura: 2026-08-31
fuente: "/sync_mails — mail 'Informe Estado Proyectos Emisión al 28/08/2026' (threadId 1a04a0a6e8b0e3c7), Nicolás Pomponio (Fintexa), 2026-08-28"
producto: wallet
tema: Pagos FX cross-border (Mastercard Move) MVP2 — hallazgos de manejo de errores detectados durante pruebas en STG
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_fx.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

El informe semanal de Emisión (Fintexa, Nicolás Pomponio) al 28/08/2026 documenta 4 hallazgos de diseño detectados durante las pruebas del MVP2 de Pagos FX cross-border (Mastercard Move), todavía EN DESARROLLO/QA — no son bugs de producción, son gaps de diseño identificados antes de cerrar el contrato:

**1. Validación de cuenta (ASV) mucho menos confiable que la de pago (IVS):**
- De los 6 corredores probados para cuentas tipo **IVS**, los 6 cerraron en `VALIDO`.
- De los 7 corredores probados para cuentas tipo **ASV**, solo 2 cerraron en `VALIDO`; los otros 4 devuelven `CANNOT_CONFIRM` (1 corredor sin resultado reportado).
- Interpretación del equipo: `CANNOT_CONFIRM` no es evidencia de que la cuenta sea inválida, solo de que ese corredor no tiene cobertura de verificación — pero hoy no hay forma de distinguir ambos casos desde el contrato de Mastercard.

**2. `TipoCuenta` no se valida contra el esquema real que declara el corredor:**
- Cada corredor de Mastercard declara su esquema de cuenta implícitamente en el regex de `recipient_account_uri` de su guía (`iban:` → tipo IVS, `ban:` → tipo ASV).
- Hoy es el **front** el que identifica el tipo de cuenta a mostrar/enviar, y Wallet solo valida que el valor recibido sea literalmente `IVS` o `ASV` — no lo cruza contra lo que el corredor realmente espera. Riesgo de que un front mal configurado mande un tipo de cuenta que el corredor rechace silenciosamente distinto a como está pensado.

**3. Un pago exitoso en MVP1 no predice que la validación de cuenta (ASV, MVP2) vaya a funcionar:**
- Son dos capacidades distintas de Mastercard: el pago usa el rail de transferencia; ASV le pregunta directamente al banco destino por el estado de la cuenta. El argumento "si el pago MVP1 llegó a éxito, la cuenta no debería ser problema" **no aplica** — se vieron muchas cuentas que dan `CANNOT_CONFIRM` en la validación pese a que el corredor procesa pagos sin problema.

**4. Gap de manejo de errores en `CreatePayment` — dos casos hoy mal clasificados:**
- **Timeout/corte de red/status ambiguo:** cuando `CreatePayment` falla con timeout, corte de red o un status que no es `SUCCESS`/`PENDING`/`REJECTED`, el pago y la operación van correctamente a **"A auditar"** (resultado incierto, lo revisa una persona) — pero la organización **no recibe ninguna notificación** (`PAGO_EXTERIOR_RESULTADO` no se envía). El pago queda en un cajón interno sin que la organización tenga señal de que dejó de estar "en curso". Gap de soporte/operación, no de lógica de negocio.
- **Un HTTP 500 de Mastercard al crear el pago se trata como rechazo de negocio, y no lo es:** un 500 no indica si el pago nació o no — puede ser un fallo interno (no se creó) o un fallo devolviendo la respuesta (sí se creó y el dinero ya está en camino). Hoy el 500 se agrupa junto con los 400/409: el pago pasa a `Rechazado`, se le informa a la organización `PAGO_EXTERIOR_RESULTADO` con `Rechazada`, y nadie lo manda a "A auditar" — con el riesgo de comunicarle a un cliente que su pago fue rechazado cuando en realidad el dinero puede haber salido igual.

Contexto: MVP2 tiene publicación estimada en STG desde marzo 2026; el ambiente productivo de MVP1 ya está configurado y operando con soporte real al negocio. Los 5 tickets nuevos que cubren estos gaps (`[Pagos FX] Contemplar campos opcionales...`, `Excluir purpose_of_payment...`, `Validación de purpose of payment...`, `Obtener datos del sender...`, `Validación de dirección condicional por corredor...`) ya están EN DESARROLLO/QA — este item documenta el razonamiento detrás para que quede legible fuera de Jira.
