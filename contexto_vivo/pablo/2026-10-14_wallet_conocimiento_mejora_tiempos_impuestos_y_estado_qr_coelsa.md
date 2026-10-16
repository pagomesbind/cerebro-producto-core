---
id: 2026-10-14_wallet_conocimiento_mejora_tiempos_impuestos_y_estado_qr_coelsa
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reuniones 'Join Soporte Clientes' y 'Bind Global66, proximos pasos' (2026-10-14)"
producto: wallet
tema: Plan confirmado de reducción del recycle de impuestos (Circupa) de 2 minutos a 30-40 segundos, y nuevo endpoint de consulta directa a Coelsa ante caídas de APIBank
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Mecanismo de recálculo/recycle de impuestos (Circupa)

Confirmado en dos reuniones del mismo día (interna y con el cliente Global66):

- El cálculo de impuestos (Circupa) es **siempre asincrónico** porque consulta padrones externos al ecosistema de Bind — no puede volverse síncrono en el corto plazo.
- **Mecanismo de recycle**: el sistema monitorea continuamente la cuenta deudora; al registrarse un nuevo crédito, intenta ejecutar el débito pendiente de impuesto **antes** de que el dinero quede disponible para el cliente, validando saldo contra el sistema propio de Bind (no el core bancario del cliente, ej. Mambu de Global66). Si el recycle falla por falta de fondos, se puede volver a reintentar (reciclar) tantas veces como sea necesario — se notifica por webhook tanto el cobro inicial como cada caso de recycle, de forma independiente.
- **Tiempo actual: ~2 minutos** (configurado así, considerado "altísimo"). **Plan confirmado: bajarlo a 30-40 segundos en un plazo de 1-2 semanas** (estimación repetida en ambas reuniones). El proceso corre en bloques (cada 30-40s), por lo que el tiempo real de espera de un cliente puntual puede ser menor al máximo configurado.
- Se descartó (al menos por ahora) un bloqueo preventivo de saldo de 1-2 minutos como mitigación alternativa — afecta negativamente la experiencia de usuario, decisión de negocio del cliente (Global66) de no implementarlo.
- Caso Global66 específico: escenarios de borde sobre diferencias de saldo entre el sistema de Bind y el core bancario del cliente (Mambu) — aclarado que el recycle valida siempre contra el sistema de Bind, no el del cliente.

## Consulta directa a Coelsa ante caída de APIBank (pagos QR)

Gonzalo Rivera confirmó el mecanismo de fondo de las demoras de pago QR >6-7 segundos: Bind va directo a Coelsa para QR (no por APIBank), pero Coelsa avisa al banco sponsor (APIBank) para que acredite/debite de la cuenta recaudadora — si APIBank falla o responde tarde, Coelsa tampoco puede confirmar el estado definitivo a Bind, generando transacciones que quedan en estado "a consultar"/"auditar" hasta que el banco responde (se han visto casos de hasta 40 minutos).

**Solución en desarrollo**: un endpoint propio en Coelsa que permite **consultar directamente el estado de la transacción**, sin depender del aviso del banco sponsor — reduce drásticamente el tiempo en escenarios de caída de APIBank, aunque sin un tope máximo definido todavía (se comunicará cuando esté desarrollado). En paralelo, se sigue afinando el tiempo normal de resolución QR (ver también el incidente autoinflingido del 13/10, `2026-10-13_wallet_riesgo_incidente_qr_autoinflingido_war_room`).

## Pendiente sin fecha confirmada

Bloqueo automático de CBU corta al pasar un cliente a estado "blocked" por fraude/compliance — Global66 lo pide con urgencia (visita de C-level a Argentina), Bind sigue "terminando de definir internamente" sin fecha de producción.

> Fuente: reuniones "Join Soporte Clientes" (10:01hs) y "Bind Global66, proximos pasos" (17:00hs), ambas 2026-10-14.
