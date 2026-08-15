# Referencia de Estimaciones — Historial de esfuerzo por iniciativa (Notion histórico)

> Reubicado desde `detalle_productos/transversal/referencia_estimaciones.md` en la reestructuración PARA en cascada (2026-08-12) — es proceso interno de estimación, no conocimiento de producto. Los links de este documento a archivos de `detalle_productos/<producto>/` pueden apuntar todavía a nombres de archivo previos a esa misma reestructuración; si un link no resuelve, buscar el tema por nombre en el índice del producto correspondiente.
>
> **Propósito:** estimar desarrollos nuevos por analogía con lo que costaron desarrollos similares del pasado. Cada entrada resume una Epic del Notion histórico (pre-Jira): qué se construyó, cuántos tickets llevó y de qué tamaño (`Tamaño`: S / M / L / XL / XXL — la escala de sizing del equipo), con los tickets representativos y su esfuerzo. Alimentado por el proyecto de ingesta de Epics de Notion (completado, 93/93, archivo de control en `4_archivos/`). Desde 2026-07-06 también recibe entradas del tablero de Producto en Jira (ver sección "Jira" al final).
>
> Fechas de cierre: mes/año; con `*` = aproximada (derivada del mes de creación de la versión, no de la fecha real de pasaje a producción — solo disponible desde mediados de 2025).
>
> **Conversión Talle de camiseta → Story Points** (convención vigente del proceso de Jira, ver [gestion_jira.md §1.4](gestion_jira.md#14-prioridad-versión-y-story-points)): `S=1 · M=3 · L=7 · XL=15`. Cuando una Epic solo tiene distribución de talles (sin SP agregado en la fuente original), se puede derivar un total aplicando esta tabla — dejar explícito si la cobertura es parcial (tickets sin talle registrado no se pueden sumar).

---

## Wallet

### Compra CCL MVP (Epic Negocio — cierre core ~2025-03\*, ajustes hasta ~2025-08\*)

**Qué se construyó:** producto API-first de compra de dólar CCL para organizaciones (primer cliente Inter/Banza): wrapper sobre API Broker IVSA-Poincenot, flujo intención→ejecución con dos patas bursátiles, modelo de precios X+Y, cuenta comitente como nueva entidad, onboarding integrado y webhooks a la organización. Detalle funcional: [wallet/dolar_ccl.md §3](../../3_recursos/detalle_productos/wallet/dolar_ccl.md).

**Esfuerzo total:** 42 tickets — aprox. 3×XL, 9×L, 11×M, 10×S (9 sin tamaño registrado). Desarrollo core distribuido en ~11 versiones de Wallet (W 37 → W 48).

**Tickets representativos (para estimar por analogía):**

| Ticket | Tamaño | Tipo |
|---|---|---|
| Wrapper API Broker IVSA-Poincenot (integración completa con un proveedor bursátil nuevo) | XL | No funcional |
| Ejecutar compra CCL (orquestación de operación con comprobantes, webhooks y contingencias) | XL | Funcional |
| Onboarding flujo Inter (endpoint alta cuenta+CVU+cuenta comitente, entidad nueva) | XL | Funcional |
| Iniciar compra CCL — intención (endpoint nuevo con modelo de datos completo y validaciones) | L | Funcional |
| Consulta cotización +X+Y (endpoint + parametrización por organización/operación) | L | Funcional |
| Bug de días no hábiles en cambios de estado (lógica de calendario bursátil) | L | Bug |
| Readaptar cálculo X+Y en cotizaciones (refactor de cálculo core) | L | No funcional |
| Debitar por separado cargo Bind PSP y montoOrdenado (cambio contable con reversas) | M | Funcional |
| Consultar/cachear cotización en paralelo cada X min | M | No funcional |
| Ajustes de exposición de campos en un endpoint existente (ocultar/agregar atributos) | S | Funcional |

**Lectura para estimaciones futuras:** una integración nueva con proveedor financiero externo + flujo transaccional de dos fases ≈ 3 XL + ~9 L + cola de M/S; el MVP funcional tomó ~8 versiones quincenales de calendario y siguió generando bugs de producción (timing/webhooks) durante ~4 versiones más.

### Api bank transferencias red interna (Epic Normativo — NO ejecutada en Notion, migró a Jira)

**Qué se definió:** cursar transferencias entre CVUs del mismo PSP (o PSPs con BIND como sponsor) por red interna del banco, sin pasar por Coelsa/Link. Detalle: [wallet/transferencias_red_interna.md](../../3_recursos/detalle_productos/wallet/transferencias_red_interna.md).

**Esfuerzo:** estimación de Epic = **30 SP** (6 US: webhook entrante, saliente, conciliación, consultas, statemonitor, batch de movimientos — sin tamaño individual asignado). Sin ejecución registrada en Notion (todas las US quedaron Pendientes); útil como referencia de estimación para adaptaciones de circuito de transferencias con premisa de transparencia hacia el cliente.

---

## Adquirencia

### Cuotas CFT cliente: POS (Epic Negocio — cierre ~2024-11\*)

**Qué se construyó:** pago en cuotas con tarjeta de crédito en POS con CFT a cargo del cliente, vía módulo de Campañas (multi-dimensión: cuotas/canal/medio de pago/BIN/vigencia, herencia entidad→comercio) + API Promociones + adaptación de SDK, APK POS, liquidaciones y devoluciones. Detalle: [adquirencia/cuotas_y_campanias.md](../../3_recursos/detalle_productos/adquirencia/cuotas_y_campanias.md).

**Esfuerzo total:** 11 tickets — 1×XL, 1×L, 7×M (2 sin tamaño).

**Tickets representativos:**

| Ticket | Tamaño | Tipo |
|---|---|---|
| Campaña CFT a cargo del cliente — motor de cálculo e inserción en transacción | XL | Funcional |
| Armar API Promociones (API nueva) | L | Funcional |
| Nuevo medio de pago: tarjeta de crédito en cuotas (forma de pago contable separada) | M | Funcional |
| Pantallas en APK POS para cuotas | M | Funcional |
| Mostrar info de cuotas en detalle de transacción (por cada vista: Admin/Portal/POS) | M c/u | Funcional |
| Adaptar SDK para cuotas | M | Spike |

**Lectura para estimaciones futuras:** un módulo de pricing/campañas nuevo con impacto en 4 superficies (API, POS, portal, liquidaciones) ≈ 1 XL (motor) + 1 L (API) + ~7 M de superficies; sin bugs relevantes registrados en el backlog de la Epic.

---

## Wallet (lote W1 — cambio de divisas)

### Venta CCL MVP (cierre ~2024-12\*/2025-01\*, complemento de Compra CCL MVP)

**Qué se construyó:** mecánica espejo de Compra CCL (§ ver Compra CCL arriba): flujo intención→ejecución de venta de bono en dólares para obtener pesos, soporte multi-entidad. Detalle: [wallet/dolar_ccl.md §3.7](../../3_recursos/detalle_productos/wallet/dolar_ccl.md).

**Esfuerzo:** 16 tickets — 1×XL (Ejecutar venta), 2×L, resto M/S.

**Bug real con causa raíz:** intenciones `APROBADA` sin `montoInvertido`/`montoObtenido` — 36 de 61 intenciones relevadas tenían ambos atributos completos pese a que ambos webhooks de IVSA sí llegaban; el valor de un webhook no se estaba persistiendo. Lección: en flujos de dos webhooks secuenciales, verificar que CADA webhook persista su propio campo, no asumir que "llegó el webhook" implica "se guardó el dato".

### Compra/Venta CCL Combi: precio fijo y fuera de horario (cierre ~2025-03\*)

**Qué se construyó:** modo alternativo para organizaciones `combi=true` — sin caché de cotización, con `priceHash` de precio fijo con expiración propia, válido tanto compra como venta. Detalle: [wallet/dolar_ccl.md §3.8](../../3_recursos/detalle_productos/wallet/dolar_ccl.md).

**Esfuerzo:** solo 2 tickets — 1×L (lógica de negocio combi) + 1×M (wrapper agrega apis combi). Ejemplo de cuánto cuesta agregar un "modo alternativo" a un flujo ya construido: mucho menor que construir el flujo base.

### Dolar FX — MULC (Epic Negocio, ~100 SP estimados)

**Qué se construyó:** acceso al dólar oficial (mercado MULC/BCRA) vía cuenta CBU USD "shadow", con flujo intención→ejecución sin concepto de vuelto (precio no aproximado). Detalle: [wallet/dolar_fx.md §1](../../3_recursos/detalle_productos/wallet/dolar_fx.md).

**Esfuerzo:** 17 tickets — 2×XL (wrapper integración + ejecutar compra), varios L (crear intención compra/venta, ejecutar venta, monitorear estado, consultar intención), resto M. Circuito de compra/venta completo; **circuito de mover los dólares obtenidos (transferir/conciliar/saldo multimoneda) quedó sin cerrar** (3-4 tickets en refinamiento al freeze).

**Lectura para estimaciones futuras:** un segundo mercado de cambio de moneda sobre el mismo proveedor (IVSA-Poincenot) que uno ya existente (CCL) cuesta similar en order de magnitud (2×XL + ~5×L) — no es gratis reutilizar el proveedor, cada mercado (bonos vs. MULC) tiene su propio set de endpoints y reglas.

### Pagos FX — deprecado (solo discovery, nunca construido)

**Qué se definió:** pagos cross-border (COMEX) para PyMEs/empresas restringidas del mercado tradicional, vía Mastercard Move + cash in con DEBIN + compra de USD con CCL Combi. Detalle: [wallet/dolar_fx.md §2](../../3_recursos/detalle_productos/wallet/dolar_fx.md).

**Esfuerzo:** 0 tickets de desarrollo — 9 documentos de Definiciones (PRD completo, análisis de mercado, casos de uso). Referencia útil para dimensionar el **costo de discovery puro** de una iniciativa de este tamaño (~100 SP-equivalente en alcance) antes de decidir no construirla.

## Wallet (lote W2 — crypto y FCI)

### API crypto: Compra/venta + DIRECTA Crypto (Epics Negocio, 120 + 55 SP estimados)

**Qué se construyó:** motor genérico de compra/venta de cualquier criptomoneda con ARS (proveedor Lirium) compensado internamente contra el circuito de Dólar CCL; más el caso DIRECTA (Astropay) — expatriación de fondos de apuestas online vía cripto por restricción de Cumplimiento a la expatriación directa con CCL, con modelo de titularidad especial (cuentas a nombre de DIRECTA, address cripto a nombre del usuario final). Detalle: [wallet/crypto.md](../../3_recursos/detalle_productos/wallet/crypto.md).

**Esfuerzo:** ~41 tickets (API crypto) + ~17 tickets (DIRECTA, ~11 compartidos con la Epic genérica) = una de las integraciones más grandes relevadas hasta ahora, comparable a FCI.

**Lectura para estimaciones futuras:** una Epic "genérica" (motor) + una Epic "cliente específico" que reutiliza ~65% de sus tickets es un patrón recurrente (ver también SUR FINANZAS/TIN) — al estimar un cliente nuevo sobre una integración ya construida, contar principalmente los tickets no compartidos (para DIRECTA fueron ~6 de 17).

### FCI - Cuentas Remuneradas - APIs (Epic Negocio, ~165 SP — la más grande relevada en Wallet)

**Qué se construyó:** inversión automática de saldos en Fondo Común de Inversión (Money Market, IVSA/Poincenot) con suscripción/rescate diario automático y rendimiento acreditado como comprobante de crédito. Detalle completo (mecánica operativa + contexto de producto): [wallet/cuenta_remunerada_fci.md](../../3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md).

**Esfuerzo:** ~49 tickets, 165 SP estimados — la Epic de mayor tamaño estimado relevada hasta ahora en todo el proyecto de ingesta.

**Clientes reales del producto:** Astropay, WICO, TIN, CENCO (con OB/CVU en otro PSP — SBS), Globant/La Virginia — 5 clientes de lanzamiento para un único desarrollo, patrón "una integración, muchos clientes" a diferencia de DIRECTA/Cripto (una integración, un cliente con reglas especiales).

**Lectura para estimaciones futuras:** ~165 SP es el techo relevado hasta ahora para "un producto financiero nuevo completo con proceso batch diario + conciliación + múltiples clientes de lanzamiento". Útil como ancla superior de la escala.

## Wallet (lote W3 — transferencias y DEBIN)

### APP: Transferir a contacto celular (4 tickets)

**Qué se construyó:** transferencia por número de celular en vez de CBU/CVU/alias. Detalle: [wallet/otros_manuales.md §0](../../3_recursos/detalle_productos/wallet/index.md).

**Esfuerzo:** 4 tickets — 1×XL (integración con lista de contactos del dispositivo), 1×L (transferir con celular), resto sin tamaño. Ejemplo de referencia: una mejora de UX simple sobre un motor ya existente, cuando toca APIs nativas del dispositivo (contactos), puede saltar a XL igual que una integración backend compleja.

### Debin Recurrente en APP (~45 SP, 8 tickets)

**Qué se construyó:** cash-in personal del usuario final vinculando su propio CBU. Detalle: [wallet/debin_y_fondeo.md §5](../../3_recursos/detalle_productos/wallet/debin_y_fondeo.md).

**Esfuerzo:** 8 tickets — 1×XL (integración final a BFF), 2×L, resto M. Construida y en producción pero **nunca publicada en los stores** — recordatorio de que "en producción" no siempre significa "disponible al usuario final": puede quedar detrás de una decisión comercial/de lanzamiento.

### Fondear cuenta recaudadora con DEBIN (2-3 tickets)

**Qué se construyó:** cash-in a nivel organización reutilizando DEBIN recurrente de API Bank. Detalle: [wallet/debin_y_fondeo.md §1-4](../../3_recursos/detalle_productos/wallet/debin_y_fondeo.md) (ya documentado con detalle operativo completo antes de esta ingesta).

**Esfuerzo:** bajo — 2-3 tickets sin tamaño relevado, funcionalidad acotada (crear + consultar DEBIN, reutilizando endpoints de API Bank ya existentes de la solución de Cobro).

### Consulta DEBIN COELSA directo (~5 tickets, NO ejecutada en Notion)

**Qué se definió:** contingencia de bypass directo a Coelsa para Astropay ante degradación de Bind. Detalle: [wallet/debin_y_fondeo.md §7](../../3_recursos/detalle_productos/wallet/debin_y_fondeo.md).

**Esfuerzo:** 5 tickets, todos "Listo para desarrollo" al freeze — 2×L + 1×XL + 1×S sin ejecutar. Tercer caso relevado (junto con Api bank red interna y Pagos FX) de Epic "Lanzada" en Notion sin evidencia real de desarrollo — patrón a tener en cuenta al usar el catálogo de Epics como fuente de verdad de qué se construyó.

### Debin Recurrente CVU-CBU por API (~40 SP, 12 tickets)

**Qué se construyó:** gestión completa de suscripciones DEBIN por API (alta/baja/consulta) + cluster de bugs de idempotencia de ciclo de vida. Detalle: [wallet/debin_y_fondeo.md §6](../../3_recursos/detalle_productos/wallet/debin_y_fondeo.md).

**Esfuerzo:** 12 tickets, la mayoría (7 de 12) son bugs de idempotencia post-lanzamiento — **patrón de estimación importante**: funcionalidades de gestión de un recurso con soft-delete (alta/baja/consulta de suscripciones, tokens, credenciales, etc.) tienden a generar una cola de bugs de validación de estado proporcional o mayor al esfuerzo de construcción inicial. Presupuestar tiempo de hardening después del MVP para este tipo de funcionalidad.

### Endpoint Wallet: Consulta enfocada en conciliar (3 tickets)

**Qué se construyó:** endpoint de conciliación optimizado para Astropay (paginado grande, campos mínimos). Detalle: [wallet/conciliacion_y_totalizadores.md §0](../../3_recursos/detalle_productos/wallet/conciliacion_y_totalizadores.md).

**Esfuerzo:** 3 tickets — 1×L (endpoint nuevo) + 2 bugs chicos corregidos de paso en el endpoint genérico existente. Ejemplo de esfuerzo bajo cuando se apalanca en un endpoint ya existente en vez de construir desde cero.

## Wallet (lote W4 — cuentas menores, impuestos, CPA, seguridad)

### Cuentas para menores - MVP Arcos (4 tickets)

**Qué se construyó:** alta de cuenta de menor (deshabilitada, sin CVU hasta aprobación del tutor) + segmentación de riesgo diferenciada en ARDID con "graduación" automática a los 18 años. Detalle: [wallet/cuentas_menores_y_eco_cerrado.md §0](../../3_recursos/detalle_productos/wallet/cuentas_menores_y_eco_cerrado.md).

**Esfuerzo:** 4 tickets, todos L/XL (alta de cuenta, aprobación tutor, adaptaciones OB, segmentación) — sin bugs. Ejemplo de feature con reglas de negocio no triviales (edad, aprobación, segmentación de riesgo) resuelta en pocos tickets grandes en vez de muchos chicos.

### Impuestos en Wallet (~97 SP, ~42 tickets — la Epic normativa más grande relevada)

**Qué se construyó:** integración completa Wallet↔SISCRI para cálculo de impuestos por comprobante, asíncrona y no bloqueante, con reversa (no confirmada) y retenciones (BD+API dedicada). Detalle: [siscri/integracion_wallet.md](../../3_recursos/detalle_productos/siscri/integracion_wallet.md).

**Esfuerzo:** ~42 tickets — patrón muy distinto a otras Epics grandes: **~15 son bugs**, y de esos, la mayoría (5-6) son el mismo problema raíz repetido (padrones provinciales desactualizados) contado como tickets separados. **Lectura para estimar integraciones normativas con datos externos por jurisdicción** (padrones fiscales, tablas BCRA, etc.): presupuestar una cola de mantenimiento recurrente, no un costo único — cada jurisdicción nueva o cada actualización de padrón es, en la práctica, un ticket de bug futuro si no hay proceso de sincronización automática.

### Alimentar CPA en cuentas wallet (0 tickets — discovery puro, gap normativo abierto)

**Qué se investigó:** por qué el 72% de las cuentas con domicilio no logra completar el CPA (Código Postal Argentino). Diagnóstico completo (integración rota con Google Maps, sin fallback entre proveedores) pero **nunca priorizado para desarrollo**. Detalle: [wallet/organizaciones_y_configuracion.md §0](../../3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md).

**Esfuerzo:** 0 tickets de desarrollo. Referencia de cuánto discovery de datos (análisis cuantitativo con CSVs reales) puede completarse antes de decidir no priorizar un fix.

### Seguridad (foco APP Wallet) — remediación de pentest (12 tickets, todos casos QA)

**Qué se construyó:** remediación de hallazgos de un pentest mobile externo — invalidación de sesiones concurrentes vía endpoint centralizado de validación de token (consumido también por Admin), y reflejo de la política de contraseñas de Access Management en la APK. Detalle: [wallet/otros_manuales.md §-1](../../3_recursos/detalle_productos/wallet/index.md).

**Esfuerzo:** 12 casos de prueba (no historias de desarrollo per se) atados 1 a 1 a observaciones numeradas de un informe de pentest. Patrón de estimación: un pentest externo con hallazgos de sesión/autenticación en mobile genera trabajo cross-cutting (backend + cada front que consume el mismo mecanismo de sesión).

## Wallet (lote W5-W6 — PIX, clientes white-label, Lending — cierre de Wallet)

### PIX Rol Emisor (~100 SP estimados, 18 tickets)

**Qué se construyó:** pago en ARS leyendo QR PIX en BRL (proveedor PagBrasil), compensado internamente vía compra/venta de dólar CCL. Detalle: [wallet/pix_rol_emisor.md](../../3_recursos/detalle_productos/wallet/pix_rol_emisor.md).

**Esfuerzo:** 18 tickets sobre un alcance MVP acotado (lectura QR + pago + confirmación; devolución y Chave Pix quedaron fuera). Tercer caso relevado (junto a DIRECTA Crypto) del patrón "canal de pago internacional nuevo que se apalanca en el motor CCL ya construido" — señal fuerte de que ese motor es infraestructura reutilizable madura, no un desarrollo puntual.

### Astropay Wallet, WICO, APK wallet básica (setup de clientes, no features)

**Qué se hizo:** dimensionamiento y stress test dedicado para el cliente de mayor volumen (Astropay: 2M tx/mes, 500K cuentas simuladas); configuración de marca white-label (WICO, solo ajustes de UI); app básica para un caso de uso de transporte/pasajero con login offline y biométrico (APK básica). Detalle: [wallet/clientes_white_label.md](../../3_recursos/detalle_productos/wallet/clientes_white_label.md).

**Esfuerzo:** bajo por ticket individual, pero **Astropay ameritó un proyecto de stress test con prioridad sobre todo lo demás en Wallet Service** — lectura para estimar: un cliente de escala similar (millones de tx/mes) justifica presupuestar un stress test dedicado como parte del onboarding, no como opcional.

### Lending (Préstamos individuales + Pagar QR con línea de crédito) — 0 tickets, discovery puro

**Qué se definió:** dos modelos de crédito embebido (originación puntual vs. línea revolving) con Bind PSP como middleware sobre un scorer externo (Credicuotas). Detalle: [wallet/lending_discovery.md](../../3_recursos/detalle_productos/wallet/lending_discovery.md).

**Esfuerzo:** 0 tickets — journey maps y análisis funcional completos, pero la variante revolving quedó con preguntas de diseño financiero sin resolver (cómo consolidar cuotas de múltiples préstamos sobre la misma línea) que probablemente explican por qué nunca pasó a desarrollo. Lectura para futuros discovery de crédito: resolver el modelo de cobranza/consolidación de cuotas ANTES de pasar a Priorización, no durante.

---

## TIN (lote T1-T2 — Wallet white-label con app mobile propia)

### TIN: MVP + TIN: APP Tarjetero (43 + ~89 SP / 58 tickets — el ticket-set más grande relevado en una sola Epic)

**Qué se construyó:** wallet white-label con app propia para un cliente de escala masiva (hasta 1M CVU potenciales), con tarjetero para cash-in con tarjeta guardada (reutilizando el ecosistema de Cobro/Adquirencia como procesador). Detalle: [wallet/tin_tarjetero.md](../../3_recursos/detalle_productos/wallet/tin_tarjetero.md).

**Esfuerzo:** dado el volumen (101 tickets combinados) y la pérdida de cuota SQL de Notion durante esta ingesta, estas dos Epics se documentaron a nivel de mecánica y riesgos principales, sin triage ticket-por-ticket exhaustivo — señalado explícitamente en el archivo de control. **Lectura para estimar clientes de wallet white-label con app propia**: requieren equipos mixtos (interno + proveedores externos, ej. "KeepIT"+"TF" en este caso) y traen riesgos recurrentes de terceros (credenciales de biometría, tiempos de aprobación de stores) que no dependen del propio equipo.

### TIN: APP Opción ingresar dinero + Historial de destinatarios frecuentes (7 + 9 tickets, ambas chicas)

**Qué se construyó:** mejoras de UX de bajo esfuerzo sobre flujos ya existentes (botón de cash-in en home con visibilidad configurable por organización, transferencia rápida desde el detalle de un movimiento). Detalle: [wallet/tin_tarjetero.md §3](../../3_recursos/detalle_productos/wallet/tin_tarjetero.md).

**Esfuerzo:** 13 SP + tickets chicos sin estimar — ejemplo de referencia para "mejoras incrementales de UX sobre una wallet ya construida": bajo esfuerzo individual, alto volumen de tickets pequeños.

### TIN: Mantenimiento (51 tickets: 31 Funcional/No funcional, 20 Bug — cierra el grupo TIN)

**Qué se construyó:** cola de mejoras UX y bugs post-lanzamiento sin tema único (performance de arranque de app, hardening de seguridad — screen recording/contraseña en predictivo, integración Ardid/Recycle, parametrización multi-tenant). Detalle: [wallet/tin_tarjetero.md §5](../../3_recursos/detalle_productos/wallet/tin_tarjetero.md).

**Esfuerzo:** 22×M + 4×L (performance de arranque, esquema de reintentos Ardid, adaptación a Recycle genérico) + 14×S + 11 sin tamaño = **108 SP**. **Lectura para estimar**: una Epic "Mantenimiento" de una app con ~2 años en producción trae ratio Funcional/Bug de ~60/40 — más cerca de "cola de deuda técnica menor" que de problemas estructurales nuevos.

---

## SUR FINANZAS (6 Epics — plataforma white-label multi-comercio, Wallet+Adquirencia)

### SUR FINANZAS: MVP + Requerimientos + APK + Links de pago + Dolor + Worldsys etapa 2 (34+91+... tickets)

**Qué se construyó:** plataforma multi-comercio con canales (QR/POS/Botón) configurables por comercio, multi-credencial/multi-cuenta, transferencias con costos propios, Access Management centralizado, portal con grilla de movimientos muy iterada, y reportería normativa separada vía Worldsys. Casos de uso reales: venta de entradas de eventos (incluida la Selección Argentina de fútbol), links de pago. Detalle: [transversal/sur_finanzas.md](../../3_recursos/detalle_productos/ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md).

**Esfuerzo:** "SUR FINANZAS: Requerimientos" es la **Epic con más tickets de todo el proyecto de ingesta (91)** — pero a diferencia de Epics igual de grandes en Wallet (FCI, Impuestos), la enorme mayoría son mejoras incrementales chicas (M/S) sobre la grilla de movimientos, no piezas de arquitectura nueva. **Lectura para estimar**: un módulo de reportería/grilla usado intensamente por un cliente grande genera un flujo constante de pedidos de filtros/columnas/exports — hay que presupuestarlo como mantenimiento continuo, no como una fase cerrada del proyecto.

**Deuda normativa pendiente real** (no confirmado si se resolvió): facturación automática contra AFIP y automatización de Régimen Informativo BCRA/AFIP — ambas quedaron en estado Pendiente en el histórico.

---

## Adquirencia (lote A1)

### Botón Simple 2.0 + Devoluciones + Cambios DECIDIR (78 + 3 + 2 tickets)

**Qué se construyó:** checkout unificado de link de pago soportando tarjeta+QRI+RxT bajo un mismo objeto "Deuda", con pool de CVUs pre-creados para el medio transferencia. Detalle: [adquirencia/boton_simple_2_0.md](../../3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md).

**Esfuerzo:** 78 tickets, **segunda Epic con más tickets de toda la ingesta** (detrás de SUR FINANZAS: Requerimientos) — pero a diferencia de esa, acá el volumen es mayormente bugs (~50) de un patrón muy consistente: desincronización de estado/webhooks/liberación de recursos al agregar medios de pago nuevos sobre un modelo (`Deuda`) pensado originalmente solo para tarjeta. **Lectura de estimación central del proyecto**: integrar un 2do/3er medio de pago sobre un objeto de negocio ya construido cuesta significativamente más en QA/bugs que en desarrollo inicial — auditar explícitamente cada efecto secundario (webhooks, recursos reservados, devoluciones) por cada medio de pago nuevo, no solo el camino feliz de creación.

### APIs buscar deuda BPG + Multicredencial ThirdPartyStore + QR Tarjeta (Pago Fácil / MODO)

**Qué se construyó:** pago de impuestos/servicios externos (BPG) vía BS2.0 con imputación de vuelta al sistema externo; modalidad "ThirdPartyStore" donde Bind opera como plataforma pura sin ser comercio de registro (sin impuestos ni liquidación propia) para clientes con procesador propio; aceptación de pago con tarjeta en el QR interoperable para wallets terceras (cliente: MODO). Detalle: [adquirencia/boton_simple_2_0.md §6-8](../../3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md).

**Esfuerzo:** volumen validado con spike de estrés temprano (60.000 operaciones/día de crear+consultar deuda). **Lectura de modelo de negocio, no solo de esfuerzo**: "ThirdPartyStore" es el único caso relevado en todo el proyecto donde Bind PSP no es responsable fiscal ni liquidador de una transacción que corre sobre su propia plataforma — patrón de referencia si se evalúan futuras integraciones tipo "payment facilitator as a service" con clientes que ya tienen su propio acuerdo con un procesador.

### QRI PSP 184 acreditación en wallet (~49 tickets)

**Qué se construyó:** acreditación en tiempo real de cobros QR en la cuenta wallet del comercio (neto de comisiones/impuestos), reutilizando el CVU de la cuenta wallet existente en vez de crear uno nuevo. Detalle: [adquirencia/mecanica_qr_coelsa.md](../../3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md#mecánica-de-comprobantes-y-cluster-de-bugs-de-acreditación-en-línea-epic-histórica-qri-psp-184-acreditación-en-wallet).

**Esfuerzo:** ~30 bugs, mismo patrón que Botón Simple 2.0 (§ Adquirencia A1): integrar una funcionalidad nueva (acreditación en línea) sobre un flujo de alta de comercio ya maduro deja comercios a medio camino (sin CVU, sin habilitar, sin SISCRI) y genera asimetrías contables (devolución de bruto vs. acreditación de neto). **Tercer caso confirmado** del patrón "2da funcionalidad sobre flujo maduro cuesta más en bugs que en desarrollo" — junto con BS2.0 (medios de pago) y el cluster de padrones de Impuestos en Wallet.

### Tardan mucho en resolver estado de tx con QR (Epic Dolor, sin desarrollo — nota operativa)

Epic vacía salvo la nota "levantar ticket en Coelsa" — indica un reclamo operativo hacia Coelsa por demoras en resolver el estado definitivo de transacciones QR, sin desarrollo propio de Bind PSP asociado. Sin esfuerzo a registrar.

---

## Adquirencia (lote A4 — POS multiadquirencia)

### POS con PRISMA + Asociar POS primer login + Cambios mensajería GP POS + APK intent + DATA2000 (18+14+2+2+5 tickets)

**Qué se construyó:** segundo procesador de POS (Prisma, protocolo ISO 8583) con llaves de PIN por procesador; vínculo "zero-touch" de POS virgen por login (sin alta manual); corrección de códigos de cuotas mal diferenciados hacia GlobalProcessing; integración Android Intent con Posberry; préstamos embebidos en la APK (cliente DATA). Detalle: [adquirencia/pos_multiadquirencia.md](../../3_recursos/detalle_productos/adquirencia/pos_multiadquirencia.md).

**Esfuerzo:** ~45 SP para integrar un segundo procesador de POS completo (repositorio+arquetipo, homologación, Centralizador, reversa, llaves de PIN) — **primera referencia de esfuerzo relevada para "agregar un procesador de tarjetas nuevo al canal POS"**, útil para estimar un tercer procesador futuro. Aprendizaje transversal reutilizable: cualquier variante comercial de una misma operación (cuotas con distinta tasa) necesita código diferenciado end-to-end — el bug de GP POS (mismo código para TNA normal y "cuota simple") es un caso concreto de qué pasa cuando no se hace esto desde el principio.

---

## Adquirencia (lote A5 — Agrupador mayorista)

### Alta de entidades (7 tickets: 3F/3B/1O, piloto de la Epic)

**Qué se construyó:** especificaciones completas de creación de entidad (backend + grilla de detalle en Admin) y sección de asignación de convenios/reglas por herencia a comercios. Detalle: [adquirencia/agrupador_mayorista.md §1](../../3_recursos/detalle_productos/adquirencia/agrupador_mayorista.md).

**Esfuerzo:** 2×L (back/front de especificaciones) + 1×L (convenios y reglas). Bugs (3) todos detectados en regresión de Staging antes del pase a Producción, no en Producción — patrón sano de QA temprano.

### ABM de canales de cobro (33 tickets: 24F/6B/3O)

**Qué se construyó:** cascada `canal_entidad`→`canal_comercio` para QR/POS/Botón Simple/RxT, con estados (Configurado/Pre-Configurado/No Configurado/Configurado con Error), reintentos diferenciando error interno vs. externo, y **refactor de alto riesgo** para desacoplar la creación automática de QR de la habilitación general de un comercio. Detalle: [adquirencia/agrupador_mayorista.md §2](../../3_recursos/detalle_productos/adquirencia/agrupador_mayorista.md).

**Esfuerzo:** Epic de **100 SP estimados** (la de mayor estimación agregada de todo el lote A5) — mezcla de funcionalidades grandes (XL: habilitar canal por defecto en alta de comercio para BS/QR/POS/RXT) con bugs de integración con procesadores externos (GP: errores no registrados; Decidir/CardBusinessRules: edición de canal no sincroniza tabla de reglas). **Lectura de estimación**: un sistema de habilitación de canales con 4 procesadores distintos (QR-Coelsa, POS-GP, BS-Decidir, RxT) multiplica la superficie de bugs de sincronización entre la tabla de estado del comercio y la tabla de reglas de negocio del procesador — mismo patrón que Botón Simple 2.0 (Adquirencia A1) pero del lado de configuración en vez de transacción.

### ABM de roles y usuarios / AccessManagement 2.0 (16 tickets, todos Funcional)

**Qué se construyó:** migración de modelo de permisos 1:1 por Organización a modelo de plantillas reutilizables (RolTemplate/PermisoTemplate) + esquema Miembro-MiembroOrganizacion-MiembroRol; ABM de roles/usuarios por Entidad desde el Admin; soporte multi-aplicación en AccessManagement (antes hardcodeado a una sola app). Detalle: [adquirencia/agrupador_mayorista.md §3](../../3_recursos/detalle_productos/adquirencia/agrupador_mayorista.md).

**Esfuerzo:** 86 SP estimados. Incluye 1 Spike (M) + 2 tareas XL ("ABM roles: BACK apis para abms roles" y "Tareas de migración AccessManagement2.0") — **refactor de modelo de datos de identidad/permisos de esta magnitud es de las tareas más caras relevadas en todo el proyecto** (comparable en riesgo a la migración de Impuestos en Wallet). Útil como referencia si se evalúa tocar de nuevo el modelo de permisos: la migración de datos existentes (remapear Rol 1:1 a Rol reutilizable, sin duplicar plantillas donde el rol era idéntico entre organizaciones) fue la pieza de mayor riesgo, no el desarrollo de los endpoints nuevos.

### Mejora modelo agrupador (53 tickets: 8F/7B/38O)

**Qué se construyó:** bolsa de mejoras incrementales de portal marca blanca, filtros/columnas de grilla de Transacciones, reglas de pago administrables desde Admin (Botón Simple), onboarding marca blanca para Sur Finanzas. Detalle: [adquirencia/agrupador_mayorista.md §7](../../3_recursos/detalle_productos/adquirencia/agrupador_mayorista.md).

**Esfuerzo:** triage agresivo (38 tickets "otros" sin tipo son filtros/columnas/textos menores, no requirieron fetch completo). De los 15 tickets con contenido sustantivo: 2×XL (reglas de pago admin, back+front), 1×L (templates de mail), 1×M (OB Sur Finanzas). **Hallazgo transversal, no de esfuerzo**: dos bugs independientes de este lote (BOTONLIQ con cantidad de tx mal y liquidaciones de fin de semana mal calculadas) comparten la misma causa raíz — manejo de timezone `-03:00` vs. UTC en `FechaProceso` — ver nota de alerta en [agrupador_mayorista.md §6](../../3_recursos/detalle_productos/adquirencia/agrupador_mayorista.md).

### Parche agrupador mayorista (20 tickets: 15F/1B/1S/1O/2 cancelados)

**Qué se construyó:** rol "Admin comercio mayorista" sin acceso a Liquidaciones/Usuarios; soporte multi-aplicación en AccessManagement (spike+back+front) descubierto como necesidad durante el desarrollo del rol anterior; ocultamiento de datos sensibles a roles mayoristas (parche Frontend + intento de backend con permisos, 2 tareas canceladas); reporte consolidado de liquidaciones por Entidad (3 partes: modificación de tabla, CSV, grilla). Detalle: [adquirencia/agrupador_mayorista.md §4-5](../../3_recursos/detalle_productos/adquirencia/agrupador_mayorista.md).

**Esfuerzo:** predominantemente L (11 de los 20 tickets). **Lectura de proceso, no solo de esfuerzo**: esta Epic es un caso de libro de "parche que destapa una limitación de arquitectura" — un pedido puntual (nuevo rol sin ver Liquidaciones) escaló a un Spike + 2 tareas de desarrollo para generalizar AccessManagement a multi-aplicación, que después se reutilizó en la Epic completa de ABM de roles (A5, arriba). Al estimar un "pedido simple de rol nuevo", presupuestar el riesgo de que dispare un spike de arquitectura si el modelo de permisos no soporta el caso de uso todavía.

---

## Adquirencia (lote A6 — Liquidador y RxT/CVUCollect)

### Liquidador para traditum (6 tickets, primer cliente del producto)

**Qué se construyó:** endpoint de aviso de transacción externa ya definitiva (ACREDITADO, luego DEVUELTA/RECHAZADA) con plazo/comisión configurable por medio de pago y comercio, y archivos `BNF.TXT`/`OPG.TXT` para que el banco Macro pague a los comercios de Traditum. Detalle: [adquirencia/liquidaciones_y_devoluciones.md §Liquidador — histórico de clientes](../../3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md#liquidador-histórico-de-clientes-traditum-y-newpay-pmc).

**Esfuerzo:** 4 tickets con desarrollo real (todos L o sin tamaño registrado) + 2 cancelados (archivo de Beneficiarios, archivo de Retenciones). **Primera referencia de esfuerzo para "dar de alta un cliente nuevo del producto Liquidador"**: el costo real no está en el endpoint de aviso (genérico, ya existía el patrón de Botón Simple) sino en el archivo de salida a medida del banco del cliente — variable de cliente a cliente.

### Integración RxT con Centralizador / CVUCollect (15 tickets, 14 Funcional + 1 Pendiente sin desarrollar)

**Qué se construyó:** vínculo Entidad→Collector (`idCollector` como especificación)→Caja→CVU con alias, ABM completo (crear/eliminar CVU y alias de una caja, con propagación estricta de errores de CVUCollect sin desincronizar), endpoint de transferencias entrantes con dos modalidades (monto abierto/cerrado), y filtrado de estados no definitivos antes de informar a Pago Externo. Detalle: [adquirencia/webhooks_y_notificaciones.md §Mecánica CVUCollect](../../3_recursos/detalle_productos/adquirencia/webhooks_y_notificaciones.md#mecánica-cvucollect-vínculo-entidadcollectorcajacvu--epic-histórica-integración-rxt-con-centralizador).

**Esfuerzo:** mayormente S/M (tickets de endpoints CRUD acotados: crear/eliminar/consultar CVU o alias de una caja, ~S-M cada uno) + 1 L (asignar alias) + 1 XL (nuevo flujo de Pago Externo sin convenio, en la Epic hermana de PMC). **Lectura de estimación**: una integración de "vincular un sistema externo de CVUs a la jerarquía Entidad/Comercio/Caja" se descompone en varios endpoints CRUD pequeños e independientes — el costo total es la suma de piezas chicas, no una pieza grande, a diferencia de refactors como AccessManagement 2.0.

### Newpay PMC MVP (36 tickets, triage no exhaustivo por volumen — 10 de 36 relevados con contenido)

**Qué se construyó:** segundo cliente del producto Liquidador, con mecánica más compleja que Traditum: archivo de entrada propio (transacciones + alta de entes/comercios), mapeo de códigos externos por comercio/entidad, cálculo de impuestos por lote (Canal+Entidad), procesamiento batch asíncrono en cola dedicada (`LQ_PMC`) corrido a la tarde, y diseño de liquidación en HTML en vez de PDF estándar. Detalle: [adquirencia/liquidaciones_y_devoluciones.md §Liquidador — histórico de clientes](../../3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md#liquidador-histórico-de-clientes-traditum-y-newpay-pmc).

**Esfuerzo:** 1×XL (nuevo flujo de Pago Externo sin convenio), 4×L (input de archivo mock, archivo de salida HTML, cálculo de impuestos por lote, carga masiva del batch de la tarde), resto M/S. **Lectura de esfuerzo — confirma el patrón de Traditum**: para un segundo cliente del mismo producto, el endpoint de aviso ya existía; el esfuerzo grande estuvo en adaptarse al **formato de archivo propio del cliente** (entrada y salida) y en la robustez del proceso batch/async (probado explícitamente a 10 tx/seg antes de habilitar en Producción) — no en el motor de liquidación en sí, que se reutilizó del producto genérico. Rollout operativo no trivial documentado aparte de tickets: alta de ~300 comercios vía Excel curado a mano, con proceso de "borrado completo" para poder reprocesar archivos cargados por error.

---

## Adquirencia (lote MANT — cierra el grupo Adquirencia)

### Errores en POS (22 tickets)

**Qué se construyó:** cola de bugs y mejoras de la APK POS y su BFF (comprobantes/tickets, filtros de movimientos, bugs de pago con Mastercard/monto/login). Detalle: [adquirencia/pos_multiadquirencia.md §5](../../3_recursos/detalle_productos/adquirencia/pos_multiadquirencia.md#5-errores-en-pos-22-tickets--cola-de-mantenimiento-cierra-el-grupo-adquirenciapos).

**Esfuerzo:** 4×M + 1×L (timeout de BFF de creación de pago, el único con causa raíz de backend) = **19 SP**; 17 de 22 tickets sin tamaño. **Lectura**: mantenimiento típico de un dispositivo físico con app embebida — el alto ratio de tickets sin tamaño sugiere que se trataban como fixes rápidos, no como desarrollo planificado.

### PMC: Mantenimiento (9 tickets)

**Qué se construyó:** mejoras sobre el producto Liquidador para el cliente PMC — deduplicación de transacciones, retenciones/percepciones en liquidación a empresas, liquidaciones por comercio, procesamiento de Transacciones Externas más robusto. Detalle: [adquirencia/liquidaciones_y_devoluciones.md §PMC: Mantenimiento](../../3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md#pmc-mantenimiento-9-tickets--cola-de-mejoras-sobre-el-liquidador-cierra-el-grupo-adquirencia).

**Esfuerzo:** 5×M + 3×L (endpoint SISCRI+comercio, 2 tickets de Procesamiento TE) = **36 SP**; 1 ticket sin desarrollar (automatización de TLE, quedó Pendiente). **Lectura**: igual que con Newpay PMC MVP, el esfuerzo de mantenimiento de un cliente del Liquidador se concentra en el detalle del formato/mapeo de datos (deduplicación, retenciones), no en el motor de liquidación en sí.

---

## Cobros (Agente de Cobros y Pagos — lote C1)

### Astro: Agente de cobros y pagos en USD (19 SP, 18 tickets relevados)

**Qué se construyó:** extensión del Agente de Cobros y Pagos con cuenta recaudadora en dólares por entidad (cliente Astropay), reutilizando el circuito CVUCollect pensado originalmente para ARS. Detalle: [cobros/cuenta_recaudadora_usd.md §1-2](../../3_recursos/detalle_productos/agente_cobros_y_pagos/cuenta_recaudadora_usd.md).

**Esfuerzo:** feature base de tamaño moderado (19 SP totales), pero generó un cluster largo de ~12 bugs de post-producción (`CBU_INVALID_CURRENCY`, webhook saliente no enviado, formato de webhook USD≠ARS, conciliación sin soporte USD, StateMonitor inconsistente, entre otros), todos M o sin tamaño, típicos de "producto multi-moneda construido sobre un circuito mono-moneda". **Lectura para estimaciones futuras**: al extender un circuito ARS existente a una nueva moneda, presupuestar una cola de bugs de post-producción comparable en cantidad al desarrollo base — la causa raíz repetida es que partes del código asumían ARS de forma implícita (formato de fecha, tipo de transacción en conciliación, moneda en balance).

### Astro: Consulta de saldo. Agente de cobros y pagos en ARS (2 tickets)

**Qué se construyó:** endpoint simple de consulta de saldo de cuenta recaudadora + 1 bug de diseño de API (pedía el collector_id explícito en vez de inferirlo del token). Detalle: [cobros/cuenta_recaudadora_usd.md §3](../../3_recursos/detalle_productos/agente_cobros_y_pagos/cuenta_recaudadora_usd.md).

**Esfuerzo:** M (feature) + sin tamaño (bug). Epic más chica del lote — referencia de piso para "un endpoint GET de consulta simple sobre un circuito ya existente".

### Creación masiva de cajas con cvu (27 SP, 20 tickets relevados)

**Qué se construyó:** herramienta interna (no expuesta a clientes) de alta masiva de cajas+CVU+alias por CSV, diseñada en 3 entregas incrementales (creación en proceso → completitud+consulta → API genérica de cargas masivas) + 2 features transversales relacionadas (idExterno en cajas, nombreCaja=nombreCVU). Detalle: [cobros/carga_masiva_cajas.md](../../3_recursos/detalle_productos/adquirencia/carga_masiva_cajas_rxt.md).

**Esfuerzo:** 27 SP en el desarrollo base (3 tickets L cada uno) + cola de ~10 bugs de estabilización (S/M, mayormente sin tamaño), casi todos de la misma familia: validaciones de CSV insuficientes (alias duplicado/largo/faltante, nombre faltante) y falta de atomicidad por registro (un registro con error no debía afectar a los demás del lote). **Lectura para estimaciones futuras**: en herramientas de carga masiva por CSV, presupuestar explícitamente el costo de validación por-registro y de aislar fallas — es donde se concentró la mayoría de los defectos, no en el mecanismo de creación en sí.

### API: TRX PULL cons tacito (9 tickets del backlog, 2 con 404/blank)

**Qué se construyó:** habilitación de consentimiento tácito (sin token) en transferencias pull/débito directo, tanto para el rol CRÉDITO (Bind PSP cobrándose de una cuenta same-name) como DÉBITO (banco/PSP externo debitando una cuenta de Bind PSP), + 2 adecuaciones de formato de request/moneda pedidas por Coelsa. Detalle: [wallet/transferencias_pull.md](../../3_recursos/detalle_productos/wallet/transferencias_pull.md).

**Esfuerzo:** 2×L (ajustes CRÉDITO y DÉBITO, con lógica de reversa vía comprobante de crédito), 1×M (adecuación de formato de request), 1×S (ajuste de moneda). Epic más antigua del lote (2023-2024, `wallet back`) — normativa de cumplimiento de Coelsa más que iniciativa de negocio.

---

## Wallet (lote C2 — reclasificado de "Cobros" por etiqueta explícita `wallet back`/`wallet app`)

### Motor general de recycle (75 SP estimados, 19 tickets)

**Qué se construyó:** rediseño completo del motor de cobro automático de deudas pendientes de Wallet como microservicio event-driven (`Shared.Recycle`), generalizando el mecanismo (nacido para TIN) a cualquier tipo de comprobante. Diseño documentado en 11 pasos incrementales (modelo de datos → detección de créditos → priorización FIFO → ejecución → verificación → cierre de monitoreo → auditoría → manejo de errores → anti-concurrencia → job diario de expiración) + webhook `COMPROBANTE_RECICLADO`. Detalle: [wallet/recycle_cobro_automatico.md §3](../../3_recursos/detalle_productos/wallet/recycle_cobro_automatico.md).

**Esfuerzo:** 75 SP repartidos en 11 pasos secuenciales con dependencias explícitas entre sí (cada paso declara el anterior como `Dependencia`) — tamaños mayormente L/XL en los pasos de lógica de negocio (priorización, ejecución, verificación, auditoría, anti-concurrencia) y M en los de infraestructura/cierre. Sumó 1 paso de "Revisión" post-hoc (XL) para un caso no cubierto originalmente (más de un crédito simultáneo por cuenta) y 3 bugs de regresión de formato del webhook nuevo. **Lectura para estimaciones futuras**: un motor de reglas de negocio con máquina de estados explícita (11 pasos con dependencias documentadas 1→11) es el patrón más grande y mejor documentado de todo lo relevado hasta ahora — sirve de plantilla de cómo descomponer un rediseño de motor complejo en entregas secuenciales verificables.

### Parche de recycles de viajes (13 tickets — Recycle V1, específico TIN)

**Qué se construyó:** primera versión de Recycle, acotada a los viajes QR de TIN: débito automático ante cash-in con orden FIFO y sin pagos parciales, y límite configurable de viajes pendientes (antifraude offline). Detalle: [wallet/recycle_cobro_automatico.md §2](../../3_recursos/detalle_productos/wallet/recycle_cobro_automatico.md).

**Esfuerzo:** 2 features L (forzar débito ante cashin, límite de viajes pendientes) + 9 bugs de estabilización S/M, casi todos del mismo patrón: paridad incompleta entre el circuito online y el offline (límite online vs. oflfine distinto, bypass de seguridad vía desconexión) y errores de sincronización de estado/fecha entre el comprobante de deuda y la entidad de negocio (Viaje QR). **Lectura para estimaciones futuras**: cuando un límite o regla de negocio tiene una variante "online" y otra "offline"/asíncrona, verificar explícitamente que ambas leen el mismo valor configurado — la mitad de los bugs de este lote vinieron de esa discrepancia, no de la lógica central.

### Recurrencia en cobros (discovery, sin desarrollo)

**Qué se relevó:** alianza propuesta con DEBI (débito automático/pagos recurrentes) — modelo de revenue sharing 80/20, integración a RxT, cuenta recaudadora propia. Detalle: [transversal/pagos_recurrentes_discovery.md](../../3_recursos/detalle_productos/adquirencia/pagos_recurrentes_discovery.md).

**Esfuerzo:** no aplica — Epic nunca salió de discovery de producto, sin backlog de desarrollo ni tickets con tamaño. Se registra solo como contexto de negocio, no como referencia de esfuerzo.

---

## Onboarding (lote O1)

### OB Personas Jurídicas MVP (91 tickets — la Epic con más tickets del grupo Onboarding)

**Qué se construyó:** flujo completo de alta de sociedades sobre la base del onboarding de personas físicas existente (dependencia PJ↔PF), con documentación variable por tipo de sociedad, cumplimiento normativo (PEP/OFAC/SO, Beneficiario Final, Propietario Directo) y gestión desde Backoffice. Detalle: [onboarding/onboarding_personas_juridicas.md](../../3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md).

**Esfuerzo:** sin campo `Tamaño` registrado en ninguno de los 91 tickets (a diferencia de la mayoría de las Epics de Wallet/Adquirencia relevadas) — no hay base para estimar por Story Points este lote. **Lectura de volumen, no de tamaño**: la distribución de tipos es ~70% `Error` (bugs de validación/UX/documentación descubiertos en QA) contra ~20% `🚀 Funcional` (features de cumplimiento agregadas sobre la marcha) — patrón de un formulario largo y con muchas reglas de negocio cruzadas (tipo de sociedad × documento × validación) que generó una cola larga de defectos de detalle en vez de pocos bugs grandes.

### Onboarding en partes por API (6 tickets, con PRD completo)

**Qué se construyó:** producto de onboarding customizable e invocable por API en pasos independientes (caso de uso principal: solo Renaper Datos), con OAuth2, externalId y legajo parcial — cliente ancla COTO CICSA. Detalle: [onboarding/onboarding_por_api.md](../../3_recursos/detalle_productos/onboarding/onboarding_por_api.md).

**Esfuerzo:** sin tamaños registrados; MVP acotado explícitamente en el PRD a "crear solicitud + consultar Renaper Datos" con 1 mes de desarrollo estimado, resto del producto en el mes siguiente. **Hallazgo de seguridad**: bug de aislamiento entre entidades (una Entidad podía consultar solicitudes de otra vía su propio consumer OAuth2) — relevante como antecedente de riesgo en cualquier producto que expone datos de onboarding multi-tenant vía API.

### Onboardings para el BIND (24 tickets, triage superficial por falta de contenido)

**Qué se construyó:** variantes de onboarding para el canal sucursal/banco de BIND (Zafiro, Mercado Abierto, Socialnet) + reempadronamiento "Júbilo". Detalle: [onboarding/onboarding_bind_sucursal.md](../../3_recursos/detalle_productos/onboarding/onboarding_bind_sucursal.md).

**Esfuerzo:** no estimable — la mayoría de los 24 tickets son cambios de texto/UI sin tipo ni tamaño registrado en Notion, ni descripción más allá del título. Se documentó igual por el valor de mapear las variantes de canal existentes, no por su costo de desarrollo.

---

## Ardid (lote AR1 — integración con Wallet/Adquirencia/SurFin, lado Bind PSP)

### Ardid para wallet: Transferencias (21 tickets)

**Qué se construyó:** integración completa de Ardid en el circuito de transferencias de Wallet (salientes con/sin intención, entrantes, interpretación de 2FA, sincronización de alta/segmento de cliente) + requisitos de seguridad en la app (huella obligatoria, método de seguridad obligatorio iOS/Android) + patrón de fallback "esquivar Ardid" ante error 500 o cliente inexistente. Detalle: [ardid/integracion_con_productos_bind.md §1](../../3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md).

**Esfuerzo:** mayormente L (alta de clientes, actualización de segmento, integración de transferencias salientes, huella obligatoria) con algunos M/S en ajustes puntuales (fallbacks, cuit destino enmascarado). **Hallazgo de mayor severidad de este lote**: un bug de regresión permitía que transacciones pasaran aunque hubiera reglas restrictivas creadas en Ardid — bypass del control antifraude. **Lectura de diseño, no de esfuerzo**: el patrón de fallback "esquivar a Ardid" ante error o desincronización es una decisión consciente de priorizar disponibilidad sobre bloqueo antifraude — a tener en cuenta como tensión de diseño recurrente en cualquier integración con un motor de reglas de terceros.

### Ardid para botón simple MVP (11 tickets)

**Qué se construyó:** integración de Ardid en Botón Simple vía un endpoint centralizado de "business rules" en Centralizador (wrapper de Analyze + NotRealized), con alta automática de Entity en Ardid al crear una entidad nueva, y ajustes de payload (comercio id, email, hash de tarjeta con PAN+expiración, link de pago con DNI/email/idExternoCliente). Detalle: [ardid/integracion_con_productos_bind.md §2](../../3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md).

**Esfuerzo:** predominantemente L en la infraestructura del wrapper (endpoint de business rules, refactor de business rules, wrapper Analyze/NotRealized) y M/S en los ajustes puntuales de payload. **Lectura para estimaciones futuras**: cuando dos o más productos (Wallet, Botón Simple, SurFin) necesitan la misma integración con un motor externo, centralizar la llamada en un componente compartido (Centralizador) evita repetir el costo de integración por producto — patrón reutilizable para futuras integraciones con proveedores externos usados por múltiples productos.

### Ardid - Bóveda: integrar (3 tickets, 7 SP)

**Qué se construyó:** integración de los pagos de Bóveda (credenciales guardadas en Botón Simple) al análisis de Ardid. Detalle: [ardid/integracion_con_productos_bind.md §4](../../3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md).

**Esfuerzo:** 7 SP totales — 1×L (integración) + 1×M (bug de visibilidad en portal) + 1 sin tamaño (bug de Cash In sin resolver). Epic más chica del lote, referencia de piso para "sumar un canal de pago existente al análisis de un motor antifraude ya integrado".

### Reparar Ardid+Wallet: Alta de cuentas y de segmentos (50 SP estimados, 11 tickets)

**Qué se construyó:** segunda ronda de estabilización de la sincronización Wallet↔Ardid en alta de cuentas/segmentos/organizaciones — corrige gaps del desarrollo original de "Ardid para wallet: Transferencias" (no se creaban `ClientType`/`ClientProduct`, error 400 por campo faltante, activación de creación de cuentas acoplada a la de transferencias salientes). Detalle: [ardid/integracion_con_productos_bind.md §5](../../3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md).

**Esfuerzo:** 50 SP — mayormente L (informar email en analyze, crear segmento en Ardid al crearlo en Wallet, alta de parámetros de Ardid al crear organización en 2 partes) y M/S en bugs puntuales de payload. **Lectura para estimaciones futuras**: una integración de sincronización de alta (cuenta/segmento/organización) entre dos sistemas casi nunca queda completa en la primera Epic — presupuestar una segunda ronda de "reparación" con volumen de esfuerzo comparable al desarrollo original cuando el flujo tiene varios eventos de sincronización distintos (alta, segmento, organización, producto).

### Ajustes Ardid+Wallet: Informar datos de localización en operaciones (20 SP estimados, discovery, sin desarrollo)

**Qué se relevó:** pedido de cumplimiento/investigación (probablemente PLAFT) para exponer datos de conexión (IP, fecha/hora con huso horario, producto/domicilio de recepción, dispositivo/software usado, geo-referencia). Detalle: [ardid/integracion_con_productos_bind.md §6](../../3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md).

**Esfuerzo:** no aplica — Epic quedó en Status "Discovery - Priorización", nunca se priorizó su desarrollo pese a estar estimada en 20 SP.

### Ajustes Ardid+Botón: Informar localización e informar devoluciones (15 SP estimados, discovery, sin desarrollo)

**Qué se relevó:** mismo objetivo que la Epic de Wallet de arriba pero para Botón Simple/Adquirencia — informar motivo en NotRealized, informar return en devoluciones, informar IP/dispositivo. Detalle: [ardid/integracion_con_productos_bind.md §6](../../3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md).

**Esfuerzo:** no aplica — Epic también quedó en discovery, sus 3 tickets nunca se refinaron (plantillas vacías). **Lectura conjunta de ambas Epics de discovery**: el enriquecimiento de contexto (IP/dispositivo/geo-referencia) para el análisis antifraude fue pedido para Wallet ya en 2024 y nunca se construyó ni ahí ni en su réplica para Botón Simple — gap de producto persistente, útil para priorizar si se retoma el tema.

---

## Transversal / Normativo (lote N1 — cumplimiento)

### Integración con Worldsys MVP (44 tickets, triage no exhaustivo por volumen/repetitividad)

**Qué se construyó:** integración base de reportería antilavado (PLD) hacia BCRA vía Worldsys — 5 tipos de archivo CSV diario (Operaciones, Clientes, Nóminas, Domicilios, Actividades), duplicados para Adquirencia (comercios) y Wallet (cuentas), más enriquecimiento de datos (país/nacionalidad, PEP/UIF/FATCA) para la Matriz de Riesgo del banco. Detalle: [transversal/cumplimiento_normativo.md §1](../../3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md).

**Esfuerzo:** los 10 generadores de archivo base van de M a XL (el de "Informar transacciones cobro" es XL, el resto mayormente M/L), más 1 Spike L de investigación previa (Generación de CSV) y una cola de ajustes M/S post-revisión con el banco (separador decimal, campo opcional, extracción de CP vs. CPA). **Lectura para estimaciones futuras**: un mismo patrón de reporte regulatorio (archivo CSV diario a un FTP externo) multiplicado por N dominios de datos (acá: 5 tipos × 2 dominios) es más barato de estimar por unidad una vez resuelto el primero — el costo real está en el mapeo de datos y los ajustes de formato post-revisión con el organismo, no en la mecánica de generación/entrega en sí (ya cubierta también en [sur_finanzas.md §3](../../3_recursos/detalle_productos/ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md) para la extensión a SUR FINANZAS).

### Más datos en las cuentas para BCRA y Worldsys (1 ticket)

**Qué se construyó:** corrección de mapeo de códigos de actividad/ocupación en el archivo `LAVADOACTIVIDADESCUENTAS` (bug puntual sobre la integración de arriba). Detalle: [transversal/cumplimiento_normativo.md §2](../../3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md).

**Esfuerzo:** S — Epic más chica de todo el relevamiento junto con las de discovery.

### PCI: Recertificación (3 tickets)

**Qué se construyó:** ajustes de continuidad operativa (replicación de pago presente en otro cluster) y reducción de alcance PCI (TTL de 60 min para tarjetas temporales en Bóveda). Detalle: [transversal/cumplimiento_normativo.md §3](../../3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md).

**Esfuerzo:** 1×M (replicación de cluster) + 1×L (TTL en CardTemp) + 1×M sin contenido adicional (reajustes generales). **Lectura para estimaciones futuras**: los proyectos de recertificación PCI tienden a generar tickets de infraestructura/resiliencia (alta disponibilidad, minimización de retención de datos) más que features de producto — presupuestar este tipo de trabajo como carga técnica recurrente, no como desarrollo de negocio.

## Transversal / Normativo (lote N2 — seguridad, sanidad de plataforma)

### Seguridad (67 tickets, triage por título — remediación de pentests + hardening de Access Management)

**Qué se construyó:** ver detalle completo en [hardening_y_remediacion_de_pentests.md](../../3_recursos/arquitectura_sistema/hardening_y_remediacion_de_pentests.md). Remediación de ~15 hallazgos de pentest (control de acceso vulnerable por falta de validación de header, JWT que no vencía al cerrar sesión, credenciales/tráfico en texto plano, falta de SSL/certificate pinning, exposición de datos en logs/RAM) + hardening proactivo de Access Management (MFA, geolocalización/geobloqueo, rate limiting, políticas de contraseña, captcha).

**Esfuerzo:** de los ~30 tickets con tamaño registrado: 1×XL (Pentest APP Fase 1 completa), 3×L, ~16×M, ~10×S; el resto (~37) son tareas de checklist de hardening sin tamaño individual asignado en Notion. **Lectura para estimaciones futuras**: un pentest completo de una app mobile + su backend genera un backlog de remediación de ~15-20 tickets de severidad Alta/Crítica, mayormente M/S por ítem (arreglos puntuales de validación), más 1 XL si se cuenta el pentest en sí como ticket.

### Conteo de pegadas a API Bank (4 tickets, 16 SP)

**Qué se construyó:** header `x-internalclientid` propagado a través de todos los MS que invocan a la API Bank (Wallet, Aceptador/Adquirencia, CvuCollect), para poder reportar comercialmente el volumen de pegadas discriminado por app y organización/entidad. Detalle: [conteo_de_pegadas_api_bank.md](../../3_recursos/arquitectura_sistema/conteo_de_pegadas_api_bank.md).

**Esfuerzo:** 2×M + 1×L + 1×M = 16 SP repartidos casi por igual entre 4 sistemas consumidores del mismo cambio (mismo patrón de header, 4 implementaciones).

### Reporting (39 tickets, Tamaño estimado 111 SP)

**Qué se construyó:** motor de generación de reportes CSV/HTML (Transacciones, Movimientos, Comercios, Cuentas) para Portal Comercio y Admin, con generación asíncrona para archivos grandes y un extracto de movimientos HTML personalizable (logo/domicilio de la organización) de emisión mensual automática. Detalle: [portal_admin/index.md](../../3_recursos/detalle_productos/portal_admin/index.md).

**Esfuerzo:** mezcla de M/L/XL en el desarrollo core (el modelo de extracto HTML es XL, la integración de cada dominio de datos L/M) + cola de ~13 bugs post-lanzamiento mayormente M, concentrados en un mismo defecto recurrente: el filtro por Entidad no propagaba correctamente al reporte. **Lectura para estimaciones futuras**: un motor de reportería genérico (ABM de templates/parámetros) amortiza el costo de agregar nuevos dominios de datos, pero cada dominio igual requiere su propio ticket de integración + su propia versión asíncrona — no asumir que el 2do/3er dominio es gratis solo porque el motor ya existe.

## Transversal / Normativo (lote N3)

### PSI — Proveedor de Servicios de Iniciación de Pagos (Tamaño estimado 104 SP, discovery nunca construido)

**Qué se definió:** modelo para que fintechs clientes de Bind PSP (vía alianza con Banco Industrial) puedan abrir y vincular cuentas bancarias reales (CBU ARS/USD) dentro de su propia wallet, sin ser un banco — acceso a productos hoy exclusivos de CVU. Detalle: [transversal/psi_discovery.md](../../3_recursos/detalle_productos/wallet/psi_discovery.md).

**Esfuerzo:** 104 SP estimados a nivel Epic; las 16 US de desarrollo nunca se ejecutaron (todas quedaron "Pendiente", sin tamaño individual). **Lectura para estimaciones futuras**: un PRD de este nivel de madurez (bench competitivo + módulos MVU/Should/Could + notas técnicas de integración con curl de ejemplo) es la señal de que el discovery estaba completo y listo para pasar a desarrollo — que no haya arrancado responde a priorización de negocio, no a falta de definición.

### Grupo DESA: requerimientos para salir a prod (7 tickets, Tamaño estimado 52 SP)

**Qué se construyó:** ver detalle en [transversal/pago_facil.md — sección Grupo DESA](../../3_recursos/detalle_productos/servicios/pago_facil.md). Personalización de marca blanca (RIPSA) + campo `ClientReference` + marca de tarjeta + timer de expiración en el formulario de Link de Pago, más reportería exportable de transacciones y liquidaciones (reemplaza a la plataforma externa MacroClick que usaba el cliente).

**Esfuerzo:** 52 SP (Tamaño estimado de la Epic); de los tickets con talle individual: 2×S + 4×M. **Lectura para estimaciones futuras**: pedidos de personalización de un cliente sobre infraestructura de checkout ya existente (campos adicionales, marca blanca, reportería) tienden a ser Epics chicas (S/M por ticket) comparadas con el desarrollo original del motor — el costo real recurrente en este tipo de pedido es la reportería exportable, que casi siempre aparece como ítem adicional.

### Modelo desacoplado transferencias / PSP Grupo BIND (sin contenido — Epics vacías)

Ambas Epics están en estado "Discovery - Producto" pero sin ningún ticket de backlog ni documento de Definiciones cargado en Notion — probablemente placeholders creados para reservar el nombre de una iniciativa futura, nunca avanzaron a discovery real. Sin esfuerzo que registrar.

---

## Multi-producto (cola final — Epics-contenedor de bugs/mejoras, cierran la Fase 2 completa del proyecto)

### Dolores de clientes (38 tickets: 28 Funcional/No funcional/Requerimiento, 2 Bug, 8 otros)

**Qué se construyó:** cola de pedidos puntuales de ~15 clientes nombrados (Spena, DESA, Astropay, COTO, ProvinciaNET, TINSA, CITYGAS, Mopagos, Pagos Digitales, Desarrollo del Litoral, Banza, PLD/Worldsys), mayormente sobre POS, RxT, Deuda QR y Wallet. Detalle: [transversal/pedidos_puntuales_de_clientes.md](pedidos_puntuales_de_clientes.md).

**Esfuerzo:** ~50 SP sobre los tickets con talle registrado (aprox. 10×M + 6×S + 2×L; el resto sin talle). **Lectura para estimaciones futuras**: no es esfuerzo de "un desarrollo" sino la señal de volumen de pedidos ad-hoc por cliente que hay que presupuestar de forma recurrente — el tema recurrente de idempotencia (3 apariciones independientes entre esta Epic y "Dolores de Soporte") es la única pieza de arquitectura común identificable.

### Dolores de Soporte y administración (~93 tickets: 62 Funcional/No funcional/Requerimiento, 19 Bug/Error/Defecto, 1 Spike, 11 otros)

**Qué se construyó:** cola de pedidos internos del equipo de Soporte/Administración — herramientas de recuperación manual de transacciones, Access Management operativo, trazabilidad de datos en Admin, idempotencia de Pago Externo (BS/RxT), onboarding/KYC/fraude, SISCRI/impuestos. Detalle: [transversal/dolores_soporte_y_administracion.md](dolores_soporte_y_administracion.md).

**Esfuerzo:** **0 SP registrado** — mezcla amplia de talles sin patrón dominante claro (ver desglose de tickets en el archivo temático); volumen de 93 tickets es la señal real. **Lectura para estimaciones futuras**: Access Management y trazabilidad de datos en Admin concentran la mayoría del esfuerzo real, más que features de cara al cliente final.

### Defectos encontrados en QA (139 tickets: 10 Funcional/No funcional/Requerimiento, 37 Bug/Error/Defecto, 92 otros)

**Qué se construyó:** ver detalle en [transversal/defectos_encontrados_en_qa.md](defectos_encontrados_en_qa.md). El ~66% del backlog son buckets `[REGRESIONES]` sin contenido propio (uno por versión) — salteados por regla del pipeline. De los bugs reales muestreados, el hallazgo de mayor valor es la **tercera confirmación independiente** del bug de filtro por Entidad roto (ver `reporteria_operativa.md §3`).

**Esfuerzo:** **0 SP registrado** — Epic dominada por placeholders de regresión sin talle; no representativa de esfuerzo de desarrollo real.

### Mejoras e Iniciativas Técnicas (~208 tickets: 85 No funcional, 57 Bug, 31 Funcional, 12 Spike, 7 Error, 5 Soporte, 1 Defecto, 1 Requerimiento, 9 sin tipo — la Epic más grande de todo el proyecto)

**Qué se construyó:** migración multi-servicio a .NET 8 (Bind Aceptador, CvuCollect, Wallet), cluster de confiabilidad de Astropay (transferencias entrantes/notificaciones/auditoría de operaciones), resiliencia del backend de eventos de Wallet (comprobantes/operaciones sin comprobante, contingencia de duplicidad), y estabilidad de la APK POS (crasheos, sospecha de caché). Detalle: [transversal/mejoras_e_iniciativas_tecnicas.md](mejoras_e_iniciativas_tecnicas.md).

**Esfuerzo:** **0 SP registrado** — triage agresivo sobre muestra de 45/208 tickets (Funcional+Spike+Requerimiento+Defecto), sin desglose exhaustivo de talles sobre el total. **Lectura para estimaciones futuras**: la migración de plataforma (.NET 8) se ejecutó en paralelo al roadmap de producto, servicio por servicio — patrón a repetir para futuras migraciones de infraestructura sin bloquear entregas de negocio. Los clientes de mayor volumen (Astropay) generan su propio cluster recurrente de tickets de confiabilidad proporcional a su volumen transaccional.

---

## Jira (`bindpsp.atlassian.net`) — IDEAs de Producto

> A partir de acá, la fuente deja de ser el Notion histórico y pasa a ser el tablero de Producto en Jira (espacio `PRD`, Jira Product Discovery). Alimentado por [ingesta_jira_producto.md](../../4_archivos/ingesta_jira_producto.md). **Diferencia de escala**: Jira registra Story Points numéricos reales por IDEA/ticket (no el sizing S/M/L/XL/XXL usado en el Notion histórico) — no mezclar ambas escalas al comparar esfuerzo.

### Que pagos con QR pasen por Ardid — IDEA PRD-115 (Finalizada, Go Live 2026-04-28)

**Qué se construyó:** integración del canal de Pago QR de Wallet al análisis antifraude de Ardid (hasta entonces solo cubría transferencias) — mismo endpoint `/Analyze`, scope propio, NOT_REALIZED ante fallo/devolución total. Detalle: [ardid/integracion_con_productos_bind.md §7](../../3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md).

**Esfuerzo:** 5 Story Points (IDEA) + 3 Historias hijas (WS-549 análisis, WS-550 not-realized por falla, WS-551 not-realized por devolución) sin story points individuales cargados. **Lectura para estimaciones futuras**: extender un motor antifraude ya integrado (Ardid) a un canal de pago adicional que reutiliza el mismo endpoint de análisis es una Epic chica (5 SP) — referencia de piso para este tipo de extensión incremental, similar en magnitud a "Ardid - Bóveda: integrar" (7 SP, Notion).

### DESA: Botón cancelar y filtros en apis — IDEA PRD-87 (Finalizada)

**Qué se construyó:** botón "Cancelar" + redirección a `errorUrl` en Botón Simple 1.0, filtro por `codigoComercio`, y nuevo endpoint `GET /api/v1/Deudas` con paginación/filtros — pedidos por cliente RIPSA. Detalle: [adquirencia/boton_simple_2_0.md §9](../../3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md).

**Esfuerzo:** 3 Story Points (IDEA) + Epic AD-260 con 10 tickets con contenido (2 Test/Xray excluidos), de los cuales 4 fueron bugs de QA (paginación no expuesta, `fechaDePago` faltante, camelCase). **Lectura para estimaciones futuras**: mismo patrón que PRD-81 (abajo) — tocar una API de "Deuda" ya construida genera una cola de bugs de QA proporcionalmente grande frente al tamaño chico de la IDEA.

### COTO: Acomodar devoluciones parciales — IDEA PRD-81 (Finalizada)

**Qué se construyó:** más info del contracargo en el webhook de devolución, endpoint para consultar un contracargo por id, filtro de transacciones por hora/minuto/segundo — acelerado por la salida a producción del cliente COTO. Detalle: [adquirencia/liquidaciones_y_devoluciones.md §1.1](../../3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md).

**Esfuerzo:** 5 Story Points (IDEA) + Epic AD-61 con 12 tickets (11 Finalizados + 1 aún Asignado), de los cuales **8 de 12 fueron bugs de QA** sobre el webhook de contracargo/devolución (formato de fecha, estado prematuro, id incorrecto, caso QR parcial rechazado sin webhook). **Lectura para estimaciones futuras**: cuando Producto acelera una funcionalidad por presión de salida de un cliente grande (acá: 5 SP originales), el costo real termina siendo mucho mayor por la cola de bugs de estabilización del webhook — mismo patrón que el cluster de "Deuda" en Notion (Botón Simple 2.0) y que PRD-87 arriba: un webhook de evento de negocio expuesto a múltiples medios de pago tiende a acumular bugs de campo/estado/caso no contemplado proporcional a esa variedad, no al tamaño original de la Epic.
