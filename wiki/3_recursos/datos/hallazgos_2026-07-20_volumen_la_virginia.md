# Hallazgo — Volumen de La Virginia sobre el total de cuentas de Wallet (2026-07-20)

> Motivado por: [riesgos_y_decisiones_onboarding.md §6](../../1_proyectos/proyecto-onboarding-estrategico/artefactos/riesgos_y_decisiones_onboarding.md#6-front-ob-de-la-virginia--tc-de-cuenta-comitente) — pregunta abierta sobre cuánto volumen de personas físicas tiene La Virginia en su Onboarding con Front, para evaluar si conviene construir un paso de T&C de cuenta comitente dedicado ahí.
> Fuente: [Cuentas de Wallet](ficha_cuentas_wallet.md) (`datasets_locales/cuentas wallet desde mayo.csv`, 304.356 filas, desde 2026-05-01) y [Solicitudes de Onboarding](ficha_solicitudes_onboarding.md) (`datasets_locales/solicitudes desde mayo.csv`, 38.152 filas). La Virginia = `OrganizacionId`/`IdOrganizacion` **30** (ver [organizaciones_wallet.md](organizaciones_wallet.md)). Cálculo vía `awk` en línea de comandos — nunca se expusieron filas individuales ni PII.

## Resultado

| Indicador | Valor |
|---|---|
| Total de cuentas de Wallet (todas las organizaciones, desde mayo 2026) | 304.356 |
| Cuentas de La Virginia | **218** |
| % de La Virginia sobre el total | **0,0716%** (~85 cuentas/mes) |
| Cuentas de La Virginia que son persona física (CUIT que no arranca con `30`) | **214 de 218 (98,17%)** |
| Cuentas de La Virginia que son persona jurídica (CUIT que arranca con `30`) | 4 de 218 (1,83%) |
| Solicitudes de Onboarding de La Virginia (`IdOrganizacion=30`) | 214 |
| De esas, aprobadas (`Estado` 2/7/8) | 212 (99,1% de sus propias solicitudes) |

## Lectura

- **Volumen absoluto muy chico:** La Virginia explica menos de 1 de cada 1.000 cuentas creadas en Wallet en la ventana analizada. Cualquier desarrollo dedicado a su Front (como el paso de T&C de cuenta comitente pedido en el tema 6 de `riesgos_y_decisiones_onboarding.md`) tiene que evaluarse contra ese volumen, no contra el volumen total de la plataforma.
- **Casi todo su volumen es persona física** (98,2%) — coherente con que hoy solo tienen circuito de Onboarding armado para ese segmento (personas jurídicas es proceso manual aparte, ver ficha de cliente).
- **La Virginia es un outlier positivo de cobertura KYC:** mientras el promedio general de la base es ~5,2% de cuentas con solicitud de Onboarding aprobada (ver [hallazgos_2026-07-16_onboarding_vs_wallet.md](hallazgos_2026-07-16_onboarding_vs_wallet.md)), en La Virginia ese número es ~97% (212 aprobadas de 218 cuentas). Refuerza que es un buen candidato de piloto para la alta de comitente simplificada (tema 5 del mismo documento): el legajo necesario debería existir para casi todos sus usuarios.

## Nota metodológica

- Ventana de datos: 2026-05-01 en adelante (~2,5 meses), no el histórico completo del cliente — si se necesita el volumen histórico total, hay que pedir una extracción con rango más amplio.
- El campo `IdOrganizacion` del dataset de Solicitudes está en `NULL` en 61,8% de las filas a nivel general (ver ficha) — no afecta este cálculo puntual porque se filtró por un valor específico presente, pero significa que el total general de solicitudes por organización está subestimado para organizaciones con esa falla de dato; no se detectó ese problema en las filas de La Virginia (214 solicitudes vs. 218 cuentas, consistente).
