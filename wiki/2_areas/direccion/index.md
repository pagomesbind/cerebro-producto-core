# Dirección — Punto de Entrada del Cerebro

> **Esta es la primera carpeta que el Bibliotecario lee en toda sesión de Producto, antes que [`wiki/index.md`](../../index.md).** Reúne todo lo que hace falta para razonar estrategia sin abrir el resto del repositorio: hacia dónde va Bind PSP, cómo viene, con qué equipo y qué vende, y cómo se decide. Es la "capa 0" que le faltaba al modelo PARA original — nace de una reforma estructural pedida por el PM (ver `decisiones.md`, 2026-07-20), inspirada en cómo otros PMs (ej. Nacho Bassino) organizan su propio cerebro, pero adaptada a que este Cerebro es un knowledge base operativo con ingesta automática, no un context pack estático.
>
> **Escritura restringida:** salvo `oportunidades.md` y `decisiones.md` (que se alimentan de las skills de sync como parte de su función), esta carpeta se escribe con decisión explícita del PM, no como destino automático de una ingesta de `raw/` — mismo criterio que ya regía para los overviews de producto.

## Qué es Bind PSP, en una pantalla

Bind PSP es un PSP (Proveedor de Servicios de Pago) fintech que opera 5 líneas de producto — **Wallet** (billetera digital as a service), **Adquirencia** (cobro a comercios vía QR/tarjeta/transferencia), **Agente de Cobros y Pagos** (capa multi-collector sobre API BANK), **Onboarding** (alta con KYC/KYB) y **Ardid/Akurtech** (antifraude) — más productos accesorios (Siscri, Servicios, Conciliador). Contexto de negocio completo en [empresa.md](../overview_empresa/overview_empresa_general.md); quién hace qué en [equipo.md](../overview_empresa/overview_equipo.md); qué es y qué vale cada producto en [producto/index.md](../overview_productos/index.md).

## Hacia dónde vamos

Dos North Star Metrics fijadas por el CEO gobiernan todo: ser **top 2 en volumen operado por API BANK** y **top 6 adquirentes en volumen operado con Payway**. El contexto actual (post-fraude de marzo 2026, remediación exigida por Grupo BIND) reordenó la ejecución en **3 focos estratégicos con OKR propio**: **Onboarding** (Pablo Gomes, KR1 en foco), **Pagos FX** (Luciana Rudaz, OKR pendiente) y **Ardid** (Nicolás Colón, OKR pendiente). Detalle completo en [north_star.md](north_star.md) y [estrategia/index.md](estrategia/index.md).

## Cómo venimos

[estado_actual.md](estado_actual.md) — el valor actual de cada NSM y cada KR, con su gap contra el target. Empieza honesto: varias métricas no tienen baseline todavía, y eso está declarado explícitamente en vez de omitido.

## Patrones estacionales conocidos

[estacionalidad_metricas.md](estacionalidad_metricas.md) — calendario de negocio (no cálculo estadístico)
que `/sync_metrics` consulta al escribir hallazgos, para no marcar como "sin explicar" un movimiento que
en realidad es estacional conocido (ej. pico de cobro de servicios los días 1-10 del mes en NSM#2).

## Cómo decidimos

[criterios_priorizacion.md](../procesos/criterios_de_priorizacion.md) — el criterio de priorización que el equipo ya usa de hecho (compliance primero, las 2 NSM como marco, capacidad real del equipo, simplicidad de OKR), destilado de decisiones reales. [decisiones.md](decisiones.md) es el registro histórico completo de decisiones tomadas (trimestre vivo; histórico en `historico/`).

## Qué podría venir después

[oportunidades.md](oportunidades.md) — candidatas a IDEA nueva detectadas en reuniones/mails/sesiones que todavía no tienen Jira ni proyecto propio. Se alimenta automáticamente desde `/sync_meetings`, `/sync_mails` y `/debrief`.

## Referencia rápida

[glosario.md](../glosario.md) — términos, siglas y errores de transcripción recurrentes (PSP≠PCP, CVU≠"CBU corta", Decidir=Payway=Prisma, etc.).

## Ver también, fuera de esta carpeta

- [`2_areas/clientes/patrones_transversales.md`](../../2_areas/clientes/patrones_transversales.md) — patrones de comportamiento repetidos entre clientes (el equivalente de `feedback_intelligence`). Se queda en `2_areas/` porque es parte de la base de clientes mantenida por `/sync_customers`, no se duplica acá.
- [`2_areas/tareas_producto.md`](../tareas.md) — backlog operativo del equipo (distinto de `oportunidades.md`: acá son acciones a resolver, ahí son ideas de producto a evaluar).
- [`../gaps_y_preguntas.md`](../gaps_y_preguntas.md) — vacíos de información y decisiones pendientes del PM.

---
*Creado: 2026-07-20 — punto de entrada de la reforma estructural del Cerebro. Ver `decisiones.md` para el contexto completo de por qué se creó esta capa.*
