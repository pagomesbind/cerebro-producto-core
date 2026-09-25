---
id: 2026-09-25_conocimiento-coelsa-pull-homologacion-requests-llegan-formato-distinto
pm: nicolas
fecha_captura: 2026-09-25
fuente: "Mail 'Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación' — ncolon@bind.com.ar / icm@coelsa.com.ar (Niurka Yamarte), mensajes del 2026-09-23 y 2026-09-24"
producto: wallet
tema: Transferencias Pull en Homologación (ticket Coelsa #456632) — el bloqueo no es de conectividad: los avisos de Coelsa sí llegan a Bind, pero con un formato de request distinto al que espera la implementación de Bind
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/transferencias_pull.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/wallet/transferencias_pull.md §6 — 'Aprendizaje operativo (extiende el hallazgo anterior)' (2026-09-03): hipótesis de que la falta de tráfico en AvisoDebinPendienteCVU y el ERROR DEBITO se explican por una falla de conectividad de red/VPN hacia 172.30.8.62"
confianza: media
estado: en_cola
---

Continuación de §6 de `transferencias_pull.md` (circuito de reactivación de Transferencias Pull en Homologación, ticket Coelsa #456632). **Cambia el diagnóstico del bloqueo.**

**2026-09-23 15:42 (ART) — Bind (Nicolás Colón) a Coelsa:** verificaron que el telnet a la IP del PSP (`172.30.8.62`) efectivamente no está habilitado, **pero las peticiones de Coelsa sí llegan a Bind**. El problema es que internamente no se están interpretando porque **el request que llega es distinto al documentado**. Se le pasó a Coelsa un ejemplo concreto real y el esperado, preguntando si hay un problema de su lado o si la documentación está desactualizada.

Diferencias entre el request real recibido (DEBIN `ORD6LEN8QOL61LG9M1Y30V`, 2026-09-22, importe 1.00, PSP 5071 / KEEP IT SIMPLE SRL) y el "esperado según documentación" que usa Bind como referencia (ejemplo de 2023, PSP 0070 Resimple → BIND PAGOS SA, PSP 0532):

| Campo | Request real (Coelsa, 2026-09-22) | Esperado por Bind |
|---|---|---|
| `operacion.objeto.tipo` | **ausente** | `"TRXPL"` |
| `operacion.vendedor.cuenta_virtual` | **ausente** (vendedor solo con CBU) | presente (`id_psp`, `cuit_psp`, `cvu`, `cuit_cvu`, `titular_cvu`) |
| `operacion.vendedor.cuenta.terminal` | presente (`""`) | ausente |
| `esTitular` | entero (`0`) | booleano (`false`) |
| `EntityID` (raíz) | **ausente** | `0` |
| `debin.estadoComprador` | `01` / `NO ADHERIDO` | `00` / `ADHERIDO` |
| `evaluacion` | `puntaje: 65`, `reglas: "2a,9,1c"` | `puntaje: 0`, `reglas: ""` |
| `fechaExpiracion` | 15 segundos después de `fecha` | 15 segundos después de `fecha` (igual) |

**Observación del Cerebro (no confirmada por Coelsa):** el request real coincide con el esquema estándar de `AvisoDebinPendiente` / `AvisoDebinPendienteCVU` publicado en la documentación pública de Coelsa, ya documentado en `wallet/coelsa_debin_api_payloads.md` (sin `objeto`, sin `cuenta_virtual` del vendedor, `esTitular` entero, `terminal` en la cuenta del vendedor). El formato "esperado" por Bind (con `objeto.tipo: "TRXPL"` y `EntityID`) parece salir de otra especificación — probablemente la específica de transferencias pull con la que se construyó la implementación original en 2023. Es decir: la hipótesis más probable es que **Coelsa está mandando un aviso DEBIN estándar donde Bind espera el aviso específico de transferencia pull**, ya sea por configuración del PSP nuevo (5071) en homologación o por un cambio de Coelsa. A confirmar por Coelsa.

**2026-09-24 10:08 — Coelsa** pide ejecutar una prueba nueva y enviar el ID o el request. **2026-09-24 12:58 — Bind** envía dos IDs de pruebas nuevas: `86VRPQ2GD0P1L0Y2GLY0M1` y `0V1JXON170O5M0GNZ64EL7`. **2026-09-24 17:55 — Coelsa** responde que están validando los mensajes enviados de esos IDs y que compartirán el resultado al terminar. Sin resolución a la fecha de captura.

**Aprendizaje operativo (corrige el de 2026-09-03):** que el telnet a la IP del PSP no responda **no implica** que no haya conectividad para los avisos — el tráfico HTTP de Coelsa llega igual. La falta de "tráfico" en `AvisoDebinPendienteCVU` reportada el 2026-08-28 y el `ERROR DEBITO` que Bind veía en sus pruebas se explican (hipótesis actual) por un **desajuste de contrato del payload**, no por red/VPN. Lección para próximos debugging con Coelsa: antes de escalar un problema de red, revisar los logs de entrada del endpoint del lado de Bind y comparar el payload real contra el esperado.

> Fuente: Mail "Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación" — ncolon@bind.com.ar (2026-09-23 y 2026-09-24) / icm@coelsa.com.ar, Niurka Yamarte (2026-09-24).
