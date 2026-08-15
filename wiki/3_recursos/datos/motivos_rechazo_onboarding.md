# Motivos de Rechazo de Onboarding — tabla de referencia (Id → Descripción)

> Provista por el usuario (2026-07-16) para decodificar el campo `MotivoRechazo` del dataset [Solicitudes de Onboarding](ficha_solicitudes_onboarding.md). No es PII — metadata de sistema, segura para el repo.

| Id | Descripción |
|---|---|
| 1 | DOCUMENTO_NO_ENCONTRADO |
| 2 | PDF417_NO_ENCONTRADO |
| 3 | INTENTOS_EXCEDIDOS |
| 4 | PERSONA_NO_ENCONTRADA |
| 5 | PERSONA_FALLECIDA |
| 6 | EJEMPLAR_NO_VALIDO |
| 7 | PRUEBA_VIDA_INTENTOS_EXCEDIDOS |
| 8 | RECHAZO_MATRIZ_DE_RIESGO |
| 9 | SOLICITUD_PREVIA_APROBADA |
| 10 | INTENTOS_EXCEDIDOS_OTP_EMAIL |
| 11 | INTENTOS_EXCEDIDOS_OTP_SMS |
| 12 | SOLICITUD_NO_ENCONTRADA |
| 13 | ENTIDAD_NO_ENCONTRADA |
| 14 | DATOS_INCOMPLETOS |
| 15 | OTP_INCORRECTO |
| 16 | VALIDACION_FACIAL_INCOMPLETA |
| 17 | PRUEBA_VIDA_INCOMPLETA |
| 18 | DOCUMENTO_NO_VIGENTE |
| 19 | CREAR_CLIENTE_INCOMPLETO |
| 20 | ERROR_ALTA_PRODUCTOCC |
| 21 | ERROR_ALTA_PRODUCTOCA |
| 22 | CREDENCIALES_INCOMPLETAS |
| 23 | ERROR_ALTA_CUENTA_VISTA |
| 24 | ERROR_ALTA_TARJETA_DEBITO |
| 25 | ERROR_AUTORIZAR_TARJETA_DEBITO |
| 26 | ERROR_NOSIS |
| 27 | PENDIENTE_BINDID |
| 28 | DNI_INVALIDO_CARTA_CIUDADANIA |
| 29 | ERROR_NO_EXISTE_PERSONA |
| 30 | FALLO_PARCIAL_RECONOCIMIENTO_FACIAL |
| 31 | FALLO_FINAL_RECONOCIMIENTO_FACIAL |
| 32 | PENDIENTE_CONTACTAR_PERSONA |
| 33 | ERROR_STEP |

## Nota de calidad de dato (2026-07-16)

En la extracción de solicitudes desde mayo-2026, aparecen los códigos `36`, `37`, `38` y `43` con volumen no despreciable (juntos ~8,4% de los rechazos) que **no están en esta tabla de 33 códigos** — pendiente de confirmar con desarrollo si hay códigos adicionales no incluidos en este legend, o si se trata de otro tipo de identificador.

## Uso en el hallazgo del 2026-07-16

Ver [`hallazgos_2026-07-16_onboarding_vs_wallet.md`](hallazgos_2026-07-16_onboarding_vs_wallet.md) §0 — clasifica los motivos observados en fricción técnica/UX (`PDF417_NO_ENCONTRADO`, `INTENTOS_EXCEDIDOS*`) vs. administrativo (`SOLICITUD_PREVIA_APROBADA`) vs. riesgo/compliance real (`RECHAZO_MATRIZ_DE_RIESGO`, `PERSONA_NO_ENCONTRADA`) para [PRD-202](../../1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/proyecto.md).
