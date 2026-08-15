# Strategy Brief: Onboarding — H2 2026

> **Versión 1 — 2026-07-20.** Brief ejecutivo para presentación a gerencia. Sintetiza [foco_onboarding.md](foco_onboarding.md) (fuente completa, con roadmap detallado por IDEA, riesgos y decisiones). Preparado por Pablo Gomes con el Cerebro (`/strategy_brief`).
> **Deck:** [strategy_deck_onboarding.pptx](strategy_deck_onboarding.pptx) — 9 slides ejecutivas sobre la plantilla institucional de Grupo Bind, mismo contenido de este brief.

## 1. Decisión estratégica

Hoy tenemos tres frentes de problema abiertos en el ingreso de clientes a Bind PSP. El primero: la enorme mayoría de las cuentas nuevas se crean sin pasar por ninguna validación real — no sabemos quién es esa gente al momento de darles una cuenta. El segundo: no tenemos dimensionado cuántas de las cuentas que ya existen tienen su documentación completa, y todo indica que es prácticamente ninguna. El tercero: de las pocas solicitudes que sí pasan por el proceso de validación hoy, casi la mitad termina rechazada — y la mayoría de esos rechazos no es por fraude, sino por una falla técnica al capturar el documento del cliente, es decir, estamos perdiendo gente legítima por un problema de producto, no de riesgo.

No tenemos todavía una fecha límite impuesta desde afuera — lo que el banco exige es que **nosotros mismos presentemos el plan** de cuándo y cómo vamos a regularizar la situación. Eso vuelve la urgencia una urgencia de definición, no de reloj: cuanto antes tengamos una dirección clara y accionable, antes dejamos de estar expuestos. Por eso elegimos, dentro de esa definición, primero cubrir la mayor cantidad de cuentas posible (ancho) antes que sumar más controles de validación a las que ya pasan por el proceso (profundidad) — abrir la cobertura a todo el flujo nuevo pesa más que perfeccionar lo que ya se valida. Y de los tres frentes, elegimos atacar primero el flujo de cuentas nuevas: es la única palanca que corta el problema en el momento exacto en que se genera. Mientras sigamos sumando cuentas nuevas sin control, ni el stock viejo ni la experiencia del proceso se pueden resolver bien. Stock y experiencia no se descartan: se posponen a próximos ciclos, con la lógica de encadenamiento en la sección 3.

## 2. Foco del Now

**Validar toda cuenta nueva de billetera antes de crearla**, con documentación completa. El punto de partida es crudo: sobre las últimas cuentas creadas, solo 1 de cada 20 pasó por una validación aprobada — el resto, más de 280 mil cuentas, se dio de alta sin control. La meta es llevar esa cobertura a más del 80% para fin de año. Es la prioridad estratégica número uno porque es, a la vez, el mandato de cumplimiento del banco y la puerta de entrada de todo el volumen de negocio futuro. *(Corre en paralelo, y de forma independiente, un ajuste regulatorio de corto plazo sobre límites de cuentas bancarias por titular, con fecha de cumplimiento muy próxima — importa cumplirlo, pero no resuelve el problema de cobertura: es un parche puntual, no el objetivo del año.)*

## 3. Roadmap — cómo atacamos el Now

- **Primer paso (en curso):** construir la capacidad de validar, en el momento del alta, a personas físicas adultas que se integran de forma directa — el segmento que concentra prácticamente todo el volumen actual (ver el desglose en la sección 4). Es deliberadamente el punto de partida más angosto y de mayor impacto: sin esto, no hay base para nada más.
- **Seguido de:** incorporar un control normativo puntual pedido explícitamente por el banco, antes que otros gaps detectados internamente — un pedido externo pesa más que un hallazgo propio.
- **Después:** extender la misma validación a menores de edad — volumen hoy marginal, pero con un cliente concreto esperando esa capacidad.
- **Más adelante en el año:** cubrir personas jurídicas y comercios, y resolver los controles fiscales adicionales que todavía faltan — se dejan para el final porque no compiten en volumen ni en urgencia con lo anterior.
- **Fuera de esta secuencia pero corriendo en paralelo:** el ajuste normativo de corto plazo mencionado en la sección 2, y la limpieza técnica de la falla de captura de documento que hoy genera la mayoría de los rechazos — esta última es justamente el problema que decidimos posponer, aunque su causa raíz ya está identificada y lista para atacar cuando llegue su turno.
- **Ciclo siguiente (no este año):** una vez resuelto el flujo, se retoma la regularización del stock de cuentas existentes.

## 4. Evidencia vs. apuesta

Lo que sabemos, con datos reales de los últimos meses:

- De las cuentas de billetera creadas recientemente, apenas **1 de cada 20 pasó por una validación aprobada** — el resto se dio de alta sin ningún control.
- El volumen mensual de altas nuevas de billetera ronda las **120.000 cuentas por mes**, y está brutalmente concentrado en un solo segmento: **más del 99% son personas físicas adultas** (~121.600/mes), personas jurídicas apenas **~120/mes** (0,1%) y menores de edad son prácticamente inexistentes (menos de 2 por mes). Esta concentración es la razón concreta por la que el primer paso del roadmap ataca exclusivamente a los adultos: es donde vive casi todo el volumen, así que es donde se gana o se pierde la meta de cobertura.
- De las pocas solicitudes que sí pasan hoy por el proceso de validación, **casi la mitad es rechazada** — y de esos rechazos, **la mitad es por una falla técnica al leer el documento del cliente** (no por una señal real de riesgo: los rechazos por control de riesgo genuino son una fracción mínima, muy por debajo del 1%).
- El volumen también está concentrado del lado de las organizaciones: un puñado de cuentas grandes explica la mayor parte del flujo que hoy no pasa por ningún control.

Lo que todavía es apuesta: asumimos que esas organizaciones grandes van a poder migrar sin fricción severa, porque ya harían su propia verificación antes de llegar a nosotros — eso se valida recién con la conversación comercial directa con cada una, antes de comprometer fechas de desarrollo.

## 5. Riesgos y mitigaciones

- **Diseño técnico sin resolver:** todavía no está definido quién debe orquestar la validación en el momento del alta, lo que bloquea el diseño de la solución central. *Mitigación:* mesa técnica dedicada esta semana para destrabar la definición.
- **Repositorio de documentación en disputa:** hay una discusión abierta sobre cuál es el sistema definitivo donde debe quedar guardada la documentación de cada cliente. *Mitigación:* resolución rápida y priorizada con Compliance, porque afecta tanto al flujo como al stock diferido.
- **Riesgo comercial:** las organizaciones grandes podrían resistirse a migrar si perciben fricción en su integración actual. *Mitigación:* conversación comercial temprana mostrando el flujo propuesto, antes de fijar compromisos de fecha.

## 6. Checkpoints

- Antes de comprometer fechas de desarrollo: cierre de la conversación comercial con las organizaciones dominantes.
- En el corto plazo: resolución de la definición de orquestación técnica y del repositorio de documentación.
- No hay una fecha límite regulatoria impuesta desde afuera — el compromiso es presentarle al banco nuestro propio plan de regularización cuanto antes; este brief es, en los hechos, la base de ese plan.

## 7. Trade-offs explícitos

- **Cubrir todas las cuentas, incluso por encima de** sumar más validaciones a las que ya se controlan — ancho antes que profundidad.
- **Flujo de cuentas nuevas, incluso por encima de** regularizar el stock existente.
- **Cerrar la puerta de entrada, incluso por encima de** arreglar la experiencia de quienes ya pasan por el proceso — se acepta perder gente legítima por fricción técnica un poco más, a cambio de tener cobertura primero.
- **Migrar primero a las organizaciones de mayor volumen, incluso por encima de** resolver todos los casos de uso menores al mismo tiempo.
