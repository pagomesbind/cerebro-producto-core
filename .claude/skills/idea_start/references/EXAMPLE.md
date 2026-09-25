<!--
Ejemplo ilustrativo de /idea_start de punta a punta, resumido (una sesión real tiene más rondas).
Cifras y nombres ficticios — no son datos reales de Bind PSP. Muestra: (a) Modo A (problema +
solución), (b) el estacionamiento, (c) magnitud propuesta por el Cerebro con nivel de evidencia y
descuento por incertidumbre, (d) el abanico de 4 carriles con tamaño por analogía, (e) una
recomendación defendida donde gana una combinación con el carril operativo.
-->

## El pedido del PM

> "Che, necesitamos un botón en el portal de comercios para que puedan reintentar un alta que
> falló por timeout de AFIP. Los de soporte están hartos de hacerlo a mano por Jira."

## Paso 0 — Clasificación

- **Señal de problema:** soporte resuelve a mano altas que fallaron por timeout de AFIP. Workaround actual: ticket de Jira + reintento manual. → Fase 1.
- **Estacionamiento:** S1 "botón de reintentar en el portal de comercios" → congelado.

## Paso 1 — Barrido (resumen)

- `estado_actual.md`: sin mención de este dolor en los KRs vigentes. Restricción de capacidad: el foco Onboarding absorbe el 70% del equipo de Wallet.
- `criterios_de_priorizacion.md`: el soporte operativo pesa bajo, salvo SLA comprometido.
- `metricas_semanales`: altas de comercios ~600/mes. No hay métrica de fallas por timeout.
- `log_iniciativas_producto.md`: "reintento automático de validación de CUIT" (2025) costó **9 SP reales**. "Pantalla de reintento de pagos en portal" costó **14 SP reales**.
- `arquitectura_sistema/integraciones_externas.md`: AFIP es dependencia externa sin SLA documentado.
- Descartado tras abrir el índice: `cumplimiento_normativo/` (reintento de una llamada ya autorizada, no toca KYC nuevo).

## Paso 2 — Carpeta e IDEA

`reintento_alta_afip/` creado. Mostrada al PM la IDEA a crear ("Reintento de altas de comercio que fallan por timeout de AFIP", Categoría BAU, Producto Cobro). Con su OK: **PRD-9XX creada en DISCOVERY**, asignada al PM.

## Fase 1 — Problema esencial (resumida)

**Síntoma vs. problema esencial.** El síntoma es "soporte reintenta a mano". El porqué: AFIP tira timeout en picos y el alta no reintenta sola. El problema esencial es que **un alta que falla por una causa transitoria no se recupera sola, y el comercio queda esperando sin saberlo**. El botón resolvería el síntoma de Soporte, pero no la espera del comercio.

**Magnitud propuesta por el Cerebro:**

| Magnitud | Valor | Cómo se obtuvo | Nivel | ¿El PM lo valida? |
|---|---|---|---|---|
| Altas fallidas por timeout | ~15/semana | El PM lo dice de memoria; el Cerebro lo contrasta: 600 altas/mes × ~10% de fallas en un caso análogo (validación CUIT 2025) ≈ 60/mes ≈ 15/semana | 🔶 | No: no quiere pedir el export ahora |
| Tiempo de soporte | 10-15 min/caso → ~3 h/semana | PM | ⚪ | No |
| Abandono de comercios por la espera | ⚪ Supuesto: 5% de los fallidos ≈ 3 comercios/mes | Sin dato en el Cerebro; supuesto razonado | ⚪ | No |

→ Tres incertidumbres a `gaps.md`, con la evidencia que las cerraría (export de tickets de Soporte; cruce de altas fallidas vs. comercios activos a 30 días).

**Gate 1 confirmado:** *"Los comercios que se dan de alta necesitan que un alta caída por un timeout transitorio de AFIP se recupere sin intervención, porque hoy quedan esperando sin saberlo mientras Soporte (~3 h/semana ⚪) las reintenta a mano."*

## Fase 2 — ¿Vale la pena? + foco (resumida)

| Dimensión | Qué dice el Cerebro | Nivel | Veredicto |
|---|---|---|---|
| Encaje NSM | Un alta recuperada es un comercio que empieza a operar antes | — | Mueve poco |
| Tamaño real | ~15/semana 🔶, abandono ⚪ | 🔶/⚪ | **A la baja por falta de evidencia** |
| Costo de oportunidad | Compite con Onboarding (foco Ahora) | ✅ | Solo si es barato |
| Generalización | El mismo patrón de reintento sirve para otras validaciones externas del alta (RENAPER, BCRA) | ✅ | Habilita el carril 3 |

**Veredicto:** ✅ vale la pena **solo si la solución es chica**. Sobre el escenario conservador (sin abandono comprobado) es fricción operativa. Si se validara el abandono, pasaría a problema de negocio. **Gate 2 confirmado.**

**Frontera del foco:**
- **Dentro:** altas que fallan por timeout de AFIP.
- **Fuera:** otras causas de rechazo de AFIP (datos inválidos) y el resto de las validaciones externas. Van al carril 3 como opcionalidad, no como alcance.

## Fase 3 — Abanico

| # | Carril | Alternativa | Cubre | Tamaño + analogía | Tiempo a valor |
|---|---|---|---|---|---|
| A0 | 0 | Convivir | — | ~3 h/semana de Soporte ⚪ + abandono ⚪ | — |
| A1 | 1 · Operativa | Soporte reintenta en lote 2 veces por día desde el backoffice existente, con un aviso estándar al comercio | Espera del comercio: parcial. Soporte: baja a ~1 h/semana | 0 SP · ~1 h/semana de Soporte 🔶 | Inmediato |
| A2 | 2 · Acotada | Reintento automático con backoff en el alta (3 intentos) + aviso al comercio si agota | Total, en el foco | M-L: **7-12 SP** — se parece al reintento de validación CUIT (9 SP reales) 🔶 | ~1 sprint |
| A3 | 3 · Amplia | Motor de reintentos genérico para todas las validaciones externas del alta | Total + otras validaciones | XL+: **20-35 SP** — análogo a la pantalla de reintento de pagos (14 SP) × 2 integraciones más 🔶 | 2-3 sprints |
| S1 | 2 (variante) | Botón de reintento en el portal (lo que trajo el PM) | Soporte sí, espera del comercio no (el comercio tiene que darse cuenta) | L: ~12-16 SP (pantalla + reintento) 🔶 | ~1.5 sprints |

Preguntas para el análisis funcional-técnico:
1. ¿El alta es idempotente frente a un reintento?
2. ¿Qué códigos de AFIP son transitorios?

**Gate 3 confirmado:** el PM no suma opciones.

## Fase 4 — Recomendación y defensa

- **Recomendación:** **A1 ya + A2 en el próximo hueco de capacidad.**
- **Por qué:** A2 resuelve el problema esencial (la recuperación sin intervención), no solo el síntoma de Soporte. A1 alivia desde mañana sin desarrollo.
- **Costo / beneficio (conservador):** 7-12 SP contra ~3 h/semana. Se paga en meses, no en semanas, así que no se justifica desplazar Onboarding: va al próximo hueco.
- **Por qué no las otras:**
  - A0: el dolor es real y A1 cuesta 0 SP.
  - A3: la generalización no tiene demanda validada hoy.
  - S1: cuesta más que A2 y deja al comercio esperando.
- **Qué la invalidaría:** si se valida un abandono >5% de los fallidos, subir A2 de prioridad. Si RENAPER empieza a tirar timeouts, reevaluar A3.
- **Repuesto:** A1 sola, indefinidamente.
- **Sensibilidad:** con el abandono validado en ~3 comercios/mes, A2 pasa a "ahora".

**Gate 4:** el PM aprueba. S1 → ❌ Descartado (lo cubre A2 mejor). `-start.md` en `Aprobado por PM`.

## Cierre

- `artefactos/reintento_alta_afip-start.md` (autocontenido) → descripción de PRD-9XX. SP estimado 10 (preliminar de shaping). Sigue en DISCOVERY.
- `tareas.md`:
  - acordar A1 con Soporte;
  - pedir el export de tickets para validar la magnitud.
- `gaps.md`: las 3 incertidumbres.
- Paso siguiente: `/idea_solution` sobre A2 cuando haya capacidad. A1 se acuerda con Soporte, sin skill.
