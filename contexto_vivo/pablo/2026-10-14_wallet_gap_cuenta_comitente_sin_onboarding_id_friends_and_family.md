---
id: 2026-10-14_wallet_gap_cuenta_comitente_sin_onboarding_id_friends_and_family
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Join Soporte Clientes' (2026-10-14, 10:01)"
producto: wallet
tema: Clientes históricos de 'Friends and Family' dados de alta manualmente carecen de onboarding ID, bloqueando el alta de cuenta comitente
tipo: gap
destino_propuesto: 3_recursos/detalle_productos/wallet/
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## Gap operativo

Un cliente antiguo proveniente del programa **"Friends and Family"** fue dado de alta de forma manual en su momento y **carece de un `onboarding ID`**, requisito indispensable en el sistema actual para dar de alta su cuenta comitente (ver proceso de automatización de alta de cuenta comitente vía Onboarding, en curso — `resiliencia_api_bank/proyecto.md`). Hacer una nueva incorporación generaría una CVU y cuenta distintas a las que el cliente ya usa, lo cual no es una solución real.

## Resolución acordada (parche puntual, no estructural)

Franco (equipo que gestiona estos casos) va a consultar directamente con Gómez y con Pablo Gomes para resolver manualmente este caso atípico — vía intervención directa del equipo o un script de Fintexa que dé de alta la cuenta comitente por fuera del flujo estándar.

## Por qué queda como gap

No está claro cuántos clientes históricos similares (dados de alta antes de que existiera el flujo con `onboarding ID`) podrían chocar con la misma limitación a medida que avance la automatización de cuentas comitentes — no se dimensionó el universo de casos en la reunión, solo se resolvió el caso puntual reportado.

> Fuente: reunión "Join Soporte Clientes", 2026-10-14 10:01hs (Adriana Endzeliz, Gonzalo Rivera, Pablo Gomes y otros).
