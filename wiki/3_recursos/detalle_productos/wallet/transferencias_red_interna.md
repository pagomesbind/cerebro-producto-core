# Transferencias por Red Interna del Banco (API Bank) — Wallet

> Estado: documentación desactualizada / en disputa — la Epic figura "Lanzada" en Notion pero todas sus user stories quedaron `Pendiente`; sin confirmar si opera realmente en producción. Ver gap en [`../../../2_areas/gaps_y_preguntas.md`](../../../2_areas/gaps_y_preguntas.md).

> Fuente: Notion histórico, Epic **"Api bank transferencias red interna"** (⭐ Epics, tipo Normativo) + su PRD en 💡 Definiciones. **Atención al estado**: la Epic figura "Lanzada" en Notion pero todas sus user stories quedaron `Pendiente` — la definición se completó en Notion y la ejecución continuó (o debía continuar) en Jira.

## 1. Contexto y motivación (del PRD)

- El **banco BIND exige** que las transferencias entre CVUs del **mismo PSP**, o entre PSPs donde BIND es el **banco sponsor**, se cursen como **"internas"** — es decir, **sin pasar por Coelsa ni Link**.
- Motivaciones: cumplir el requerimiento del banco (estaba presionando para hacerlo), **bajar la latencia** de esas transferencias, y **reducir incidentes por caídas de terceros** (Coelsa) en operaciones que en realidad nunca salen de la red del banco.
- No hay valor directo de negocio: es adaptación normativa/de infraestructura, con beneficio indirecto de menos dolores operativos.
- Aplica a **todas las organizaciones de Wallet**, sean del PSP 184 o de otros PSP.
- **Premisa de diseño explícita**: las organizaciones no deben sufrir el cambio (o lo mínimo posible) — la interpretación de la transferencia interna debe ser transparente para el cliente.

## 2. Alcance definido (MUST del PRD → user stories)

1. **Interpretar transferencias entrantes** por red interna del banco (adaptar la interpretación del webhook de transferencia entrante).
2. **Realizar transferencias salientes** por red interna.
3. **Conciliar** transferencias entrantes de red interna (endpoint Conciliar transferencia entrante).
4. **Consultas**: que los endpoints de consulta de operaciones devuelvan los datos relevantes también en estas transferencias.
5. Adaptar el **statemonitor** (monitoreo de estados) para el nuevo circuito.
6. Adaptar el **archivo batch de movimientos** para contemplar el id de red interna del banco.

**COULD HAVE** (no comprometido): procesar internamente también las transferencias **intra-PSP entre organizaciones distintas** de nuestro propio sistema (entrantes y salientes), sin salir a la red externa.

El banco entregó documentación de referencia: *"Red Interna — Cambios en Reportería Diaria"* (PDF adjunto al PRD en Notion).

## 3. Estado al freeze

Estimación de la Epic: 30 SP. Solo se ejecutó una regresión previa de referencia ("Pruebas antes de hacer cualquier cambio", validada en STG); las 6 US quedaron **Pendientes** en Notion. Verificar el estado real de la implementación en Jira.

## 4. Uso indebido del comprobante de transferencia interna — cliente Copel (2026-09-11)

> Fuente: reunión "W 72.3 (Pagos FX) y Modificaciones en los Proxys de PRD - Análisis de riesgos" (2026-09-11), Gonzalo Damian Rivera.

Gonzalo Damian Rivera reportó que la entidad **Copel** lleva **dos meses** resolviendo sus operaciones internas mediante el **comprobante de transferencia interna** —un tipo de comprobante reservado para uso del sistema— en lugar de generar la operación real. Consecuencia: quedan comprobantes creados pero sin la operación asociada. Bind ya les avisó hace dos meses que debían dejar de hacerlo; Gonzalo propuso bloquearles directamente el uso de ese tipo de comprobante para forzar el corte ("se quedarán sin operar"). No quedó registrada como decisión formal en la minuta (no aparece en la sección "Decisiones" de la reunión) — es una propuesta verbal, a confirmar si se ejecutó.

**Nota:** "Copel" no tiene ficha propia en `2_areas/clientes/log_clientes.md` — ya apareció antes en el Cerebro como mención relacionada a "La Virginia" (endpoint de alta de cuenta comitente compartido). No queda claro si es un cliente propio o una entidad relacionada/interna a otro cliente — a confirmar en el próximo barrido de `/sync_customers`.
