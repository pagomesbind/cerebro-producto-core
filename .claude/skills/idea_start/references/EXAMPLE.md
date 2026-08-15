<!--
Ejemplo ilustrativo de una sesión de /idea_start de punta a punta, resumida (una sesión real
tiene más rondas). Cifras y nombres ficticios — no son datos reales de Bind PSP. Muestra:
(a) el PM llega con problema + solución (Modo A), (b) el estacionamiento funcionando,
(c) un cierre en 🟡 Diferido en el Gate 2.
-->

## El pedido del PM

> "Che, necesitamos un botón en el portal de comercios para que puedan reintentar un alta que
> falló por timeout de AFIP. Los de soporte están hartos de hacerlo a mano por Jira."

## Paso 0 — Clasificación

- **Señal de problema:** soporte resuelve manualmente altas que fallaron por timeout de AFIP → Fase 1.
- **Estacionamiento:** "botón de reintentar en el portal de comercios" → tabla 🅿️, congelado.

## Paso 1 — Barrido (resumen)

- `direccion/estado_actual.md`: sin mención de este dolor en los KRs vigentes.
- `procesos/criterios_de_priorizacion.md`: soporte operativo pesa bajo salvo que haya SLA comprometido.
- `datasets/metricas_semanales.md`: sin métrica de altas fallidas por timeout — gap.
- `2_areas/tareas.md`: **T-050** ya documenta un problema de certificado AFIP en staging — distinto pero mismo proveedor, se cita como antecedente.
- `arquitectura_sistema/integraciones_externas.md`: AFIP es dependencia externa conocida, sin SLA propio documentado.

Descartado tras abrir el índice: `cumplimiento_normativo/` (no toca datos personales ni KYC nuevo, solo reintento de una llamada ya autorizada) — motivo anotado en el anexo.

## Paso 1.6 — Pedido de material

*"¿Tenés el conteo de tickets de soporte por este motivo, aunque sea aproximado? Y si hay un ticket tipo de Jira de soporte, tirámelo — no hace falta para arrancar, seguimos igual."*

## Paso 2 — Nombre y creación

`reintento_alta_afip/` — nombra el problema (el reintento de una operación que falla), no la solución (no es `boton_reintentar_portal`). Anunciado, no preguntado.

## Fase 1 — Ronda 1 (resumida)

```
❓ Q1 - Segmento afectado: ¿quién sufre esto — el comercio que espera el alta, o el equipo de
soporte que la resuelve a mano?

➡️ Ambos, pero el dolor primario es de soporte: son quienes ejecutan el reintento hoy.

❓ Q2 - Frecuencia: ¿tenés una cifra, aunque sea estimada?

➡️ Sin dato en el Cerebro — pregunto directo.
```

PM responde: soporte, ~15 casos/semana, cada uno 10-15 min manuales.

**Gate 1 confirmado:** *"Soporte pierde ~3-4 horas/semana reintentando manualmente altas de comercio que fallaron por timeout de AFIP, sin visibilidad de cuántas veces reintentó antes de escalar."*

## Fase 2 — Tabla de evidencia (resumida)

| Dimensión | Qué dice el Cerebro | Veredicto |
|---|---|---|
| Encaje NSM | No mueve volumen operado — es fricción operativa, no de negocio | No mueve |
| Encaje en foco | No cae en Onboarding/Pagos FX/Ardid — es BAU de soporte | BAU |
| Tamaño real | ~15 casos/semana × 12 min ≈ 3h/semana de soporte. Sin cifra de comercios que abandonan por esto (gap) | Confirmado, acotado |
| Costo de oportunidad | Desplazaría capacidad de Onboarding (foco Ahora) | Compite mal |
| Generalización | Afecta a cualquier comercio que dé de alta, no a uno puntual | Producto entero, pero bajo impacto individual |

**Veredicto: 🟡 Vale la pena, no ahora.** Compite mal contra el foco vigente por 3 horas/semana de fricción operativa sin evidencia de pérdida de negocio. Se difiere hasta tener el dato de abandono, o hasta que el volumen crezca.

**Gate 2 confirmado por el PM.**

## Paso 9 — Cierre

- `proyecto.md`: `**Estado:** 🟡 Diferido — falta evidencia de impacto en negocio (abandono de altas), retomar si supera 30 casos/semana o si aparece un caso de churn atribuible`.
- `gaps.md`: pregunta abierta sobre el dato de abandono.
- `decisiones.md`: entrada del Gate 2 con la tabla completa.
- El ítem del estacionamiento (el botón) queda `⬜ Congelado` — nunca se llegó a discutir, correctamente: no hizo falta evaluar la solución para saber que el problema no competía todavía.
