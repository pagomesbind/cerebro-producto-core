# Log de Iniciativas de Producto

> **Propósito**: registro permanente y consolidado de toda iniciativa/idea de producto ya ingerida al Segundo Cerebro — sea un Epic del Notion histórico o una IDEA del tablero de Producto en Jira (`PRD`). Existe porque el conocimiento de cada iniciativa **no** vive en una página propia: se mergea dentro de los archivos temáticos de `detalle_productos/<producto>/`. Sin este log se perdería la trazabilidad de "qué iniciativa aportó qué" y "cuándo se entregó".
>
> A diferencia de `4_archivos/ingesta_epics_notion.md` (ya completado y rotado, 93/93 Epics) e `1_proyectos/ingesta_jira_producto.md` (archivos de **control de proceso** de cada barrido — checklists, fases, mapeos técnicos — que rotan a `4_archivos/` una vez completado el barrido inicial de su fuente), **este log nunca se archiva**: es responsabilidad continua (`2_areas/`) y se sigue alimentando para siempre, con cada iniciativa nueva que se ingiera de ahí en adelante (directamente, ya sin pasar por un archivo de control dedicado una vez que ambos barridos iniciales terminen).

## Protocolo de actualización (obligatorio)

Cada vez que se ingiera una iniciativa nueva (Epic de Notion o IDEA de Jira, en cualquier estado que ya tenga conocimiento consolidado o desarrollo real), agregar una fila acá como parte del paso de cierre del pipeline correspondiente — mismo momento en que se actualizan índices y `5_control/changelog.md`. Columnas:

- **Iniciativa**: nombre tal cual la fuente.
- **Fuente**: `Notion` o `Jira <KEY>` (la IDEA, ej. `Jira PRD-115`).
- **Fecha de entrega**: para Jira, la `releaseDate` de la versión (`fixVersions`) más antigua entre los tickets de Entrega asociados (US/Error) — es la fecha real de pasaje a producción, no la de creación del ticket. Para Notion, **no se calculó retroactivamente** (decisión del usuario 2026-07-06) — queda `—`.
- **Tamaño (Story Points)**: para Jira, el campo real de Story Points de la IDEA (`customfield_10107`). Para Notion, se deriva aplicando la **convención de conversión Talle de camiseta → SP** confirmada por el usuario (2026-07-06, ver [gestion_jira.md §1.4](../../2_areas/procesos/gestion_jira.md#14-prioridad-versión-y-story-points)): `S=1 · M=3 · L=7 · XL=15`.
  - Regla de cómputo (2026-07-06): se suman únicamente los tickets con un **conteo explícito por talle** en `referencia_estimaciones.md` (ej. "3×XL, 9×L"). Todo ticket sin talle registrado, o cuyo talle exacto no se puede atribuir individualmente (ej. "resto M/S" sin desglosar cuántos son M y cuántos S), **cuenta como 0 SP** — por indicación del usuario, para no inventar un split que la fuente no da.
  - **⚠️ "0 SP" no significa "sin esfuerzo real"**: varias Epics con **0 SP** en este log tuvieron decenas de tickets reales (ej. OB Personas Jurídicas MVP tuvo 91 tickets) — simplemente el Notion histórico no registró talle de camiseta en esos tickets. El conteo de tickets (visible en `referencia_estimaciones.md`) es la señal de volumen real en esos casos, no el SP.
- **Conocimiento en**: archivo§sección donde vive el conocimiento destilado. `—` si la iniciativa no generó contenido (caso vacío, ver PRD-168 abajo).

---

## Wallet

| Iniciativa | Fuente | Fecha de entrega | Tamaño (SP) | Conocimiento en |
|---|---|---|---|---|
| Compra CCL MVP | Notion | — | **151 SP** (3×XL+9×L+11×M+10×S; 9 tickets sin talle) | `wallet/dolar_ccl.md §3` |
| Venta CCL MVP | Notion | — | **29 SP** (1×XL+2×L; 13 tickets restantes "resto M/S" sin desglose exacto) | `wallet/dolar_ccl.md §3.7` |
| Compra/Venta CCL Combi: precio fijo y fuera de horario | Notion | — | **10 SP** (1×L+1×M) | `wallet/dolar_ccl.md §3.8` |
| Dolar FX | Notion | — | ~100 SP (estimado directo en la fuente) | `wallet/dolar_fx.md §1` |
| Pagos FX - deprecado | Notion | — | ~100 SP-equivalente (discovery, nunca desarrollado — 0 tickets) | `wallet/dolar_fx.md §2` |
| FCI - Cuentas Remuneradas - APIs | Notion | — | **165 SP** (la más grande relevada en Wallet) | `wallet/cuenta_remunerada_fci.md §0` |
| API crypto: Compra/venta | Notion | — | 120 SP | `wallet/crypto.md §1` |
| DIRECTA Crypto | Notion | — | 55 SP | `wallet/crypto.md §2` |
| APP: Transferir a contacto celular | Notion | — | **22 SP** (1×XL+1×L; 2 tickets sin talle) | `wallet/otros_manuales.md §0` |
| Debin Recurrente en APP | Notion | — | ~45 SP | `wallet/debin_y_fondeo.md §5` |
| Fondear cuenta recaudadora con DEBIN | Notion | — | **0 SP** (2-3 tickets, ninguno con talle registrado) | `wallet/debin_y_fondeo.md §1-4` |
| Consulta DEBIN COELSA directo | Notion | — | **30 SP** (2×L+1×XL+1×S; no ejecutada) | `wallet/debin_y_fondeo.md §7` |
| Debin Recurrente CVU-CBU por API | Notion | — | ~40 SP | `wallet/debin_y_fondeo.md §6` |
| Endpoint Wallet: Consulta enfocada en conciliar | Notion | — | **7 SP** (1×L; 2 bugs sin talle) | `wallet/conciliacion_y_totalizadores.md §0` |
| Cuentas para menores - MVP Arcos | Notion | — | **0 SP** (4 tickets "L/XL" sin desglose exacto por talle) | `wallet/cuentas_menores_y_eco_cerrado.md §0` |
| Impuestos en Wallet | Notion | — | ~97 SP | `siscri/integracion_wallet.md` |
| Alimentar CPA en cuentas wallet | Notion | — | 0 SP (discovery, sin desarrollo) | `wallet/organizaciones_y_configuracion.md §0` |
| Seguridad (foco APP Wallet) | Notion | — | **0 SP** (12 casos QA, no historias con talle) | `wallet/otros_manuales.md §-1` |
| PIX Rol Emisor | Notion | — | ~100 SP | `wallet/pix_rol_emisor.md` |
| APK para wallet básica | Notion | — | **0 SP** (sin desglose exacto por talle) | `wallet/clientes_white_label.md §3` |
| Astropay Wallet | Notion | — | **0 SP** (sin desglose exacto por talle) | `wallet/clientes_white_label.md §1` |
| WICO | Notion | — | **0 SP** (sin desglose exacto por talle) | `wallet/clientes_white_label.md §2` |
| Api bank transferencias red interna | Notion | — | 30 SP (estimado, no ejecutada) | `wallet/transferencias_red_interna.md` |
| Lending - Pagar QR con línea de crédito | Notion | — | 0 SP (discovery, sin desarrollo) | `wallet/lending_discovery.md §3` |
| Lending - Préstamos individuales | Notion | — | 0 SP (discovery, sin desarrollo) | `wallet/lending_discovery.md §2` |
| Que pagos con QR pasen por Ardid | Jira PRD-115 | **2026-04-29** (WS 69) | **5 SP** | `ardid/integracion_con_productos_bind.md §7` |
| ASTROPAY: Consulta directa a Coelsa para contingencia | Jira PRD-45 | **2025-11-26** (W 65.1) | **4 SP** | `wallet/debin_y_fondeo.md §7` (resuelve gap: Notion decía "no ejecutada", Jira confirma que sí se construyó) |
| ASTROPAY: Consulta directa a Coelsa por un solo id Coelsa o cvu | Jira PRD-105 | **2025-12-18** (W 66.1) | **5 SP** | `wallet/conciliacion_y_totalizadores.md §5` (contenido ya documentado por Notion; solo se agregó atribución de fuente) |
| API Cripto: MVP - Compra, venta y tenencia de cualquier moneda | Jira PRD-9 | **2025-12-15** (W 66) | **2 SP** | `wallet/crypto.md §1.3` (mantenimiento post-MVP; MVP en sí ya documentado por Notion) |
| Impuestos wallet ajustes para integrarse | Jira PRD-61 | **2025-11-26** (W 65.1) | **5 SP** | `siscri/integracion_wallet.md §3.1` |
| Cuentas para menores - MVP Arcos Dorados | Jira PRD-17 | **2025-11-26** (W 65.1) | **4 SP** | `wallet/cuentas_menores_y_eco_cerrado.md §0.1` (MVP ya documentado por Notion; agrega cardinalidad tutor/menor, deshabilitación en cascada, y aclaración de diseño del endpoint de habilitar-menor) |
| ECO Cerrado | Jira PRD-69 | **2025-12-16** (AD 66) | **3 SP** | `wallet/cuentas_menores_y_eco_cerrado.md §3.1` (API técnica ya documentada por Notion; agrega origen de negocio, lógica de comprobantes neto/bruto y cluster de bugs) |
| Consulta totalizadores CBU/CVU Coelsa - APIs | Jira PRD-56 | **2026-02-19** (W 67.4) | **4 SP** (IDEA) — 20,25 SP reales en los tickets de desarrollo (WS-58=7, WS-59=7, WS-275=3, WS-596=3, WS-590=0,25) | `wallet/conciliacion_y_totalizadores.md §3.1` (API ya documentada por Notion; agrega norma exacta COM A 8298, fechas de compromiso BCRA, multi-PSP real y cluster de bugs) |
| FCI Cuenta remunerada | Jira PRD-103 | **2025-11-17** (W 65) | **5 SP** (IDEA) — ≈87 SP reales en los 58 tickets de desarrollo retenidos de la Epic WS-1 (~17x el estimado; Epic no es una entrega puntual sino ~8 meses de mantenimiento) | `wallet/cuenta_remunerada_fci.md §4` (mecánica ya documentada por Notion; agrega historial completo de mantenimiento: bugs de fórmula, robustez del proceso, cluster de Cuenta Comitente, y nuevo endpoint de Liquidaciones por Usuario en desarrollo) |
| Validar misma titularidad de Suscripciones de Debin | Jira PRD-185 | **2026-07-15** (W 71) | **0 SP** (IDEA sin SP cargado) — 1 SP real (WS-1296) | `wallet/debin_y_fondeo.md §8` (corrección de vulnerabilidad de fraude — validación samename fail-closed, pedida por Emma Vignoles) |

**Total SP — Wallet: 1.138 SP** (usando el SP de la IDEA para PRD-56 y PRD-103, consistente con el resto del log; ver SP real de tickets en cada fila; PRD-185 suma 0 por no tener SP de IDEA cargado).

### TIN (Wallet white-label con app mobile propia)

| Iniciativa | Fuente | Fecha de entrega | Tamaño (SP) | Conocimiento en |
|---|---|---|---|---|
| TIN: MVP | Notion | — | 43 SP | `wallet/tin_tarjetero.md §1` |
| TIN: APP Tarjetero en Wallet MVP cash in | Notion | — | ~89 SP | `wallet/tin_tarjetero.md §2` |
| TIN: APP Opción ingresar dinero | Notion | — | 13 SP (conjunto con Historial de destinatarios frecuentes) | `wallet/tin_tarjetero.md §3` |
| TIN: Historial de destinatarios frecuentes | Notion | — | ver fila anterior (13 SP conjunto, no se duplica en el total) | `wallet/tin_tarjetero.md §3` |
| TIN (bolsa de bugs menores) | Notion | — | **0 SP** (sin desglose por talle en la fuente) | `wallet/tin_tarjetero.md §4` |
| Desconocimientos de tarjeta | Notion | — | **0 SP** (sin desglose por talle en la fuente) | `adquirencia/liquidaciones_y_devoluciones.md §0` (reclasificada a Adquirencia) |
| TIN: Mantenimiento | Notion | — | **108 SP** (22×M+4×L+14×S; 11 tickets sin talle) | `wallet/tin_tarjetero.md §5` |

**Total SP — TIN: 253 SP** (43+89+13+108; el conjunto 13 SP se cuenta una sola vez).

---

## SUR FINANZAS (transversal)

| Iniciativa | Fuente | Fecha de entrega | Tamaño (SP) | Conocimiento en |
|---|---|---|---|---|
| SUR FINANZAS: MVP | Notion | — | **0 SP** (sin desglose por talle en la fuente) | `transversal/sur_finanzas.md` |
| SUR FINANZAS: Requerimientos | Notion | — | **0 SP** (sin desglose por talle — 91 tickets reales, la Epic con más tickets de toda la ingesta) | `transversal/sur_finanzas.md` |
| SUR FINANZAS: APK Wallet MVP | Notion | — | **0 SP** (sin desglose por talle) | `transversal/sur_finanzas.md` |
| SUR FINANZAS: Links de pago en portal comercio | Notion | — | **0 SP** (sin desglose por talle) | `transversal/sur_finanzas.md` |
| SUR FINANZAS (bolsa de dolores) | Notion | — | **0 SP** (sin desglose por talle) | `transversal/sur_finanzas.md` |
| Worldsys etapa 2: separar SUR FIN | Notion | — | **0 SP** (sin desglose por talle) | `transversal/sur_finanzas.md §3` |

**Total SP — SUR FINANZAS: 0 SP** (ninguna de las 6 iniciativas tiene desglose por talle en la fuente — grupo con más tickets reales de toda la ingesta, ver conteos en `referencia_estimaciones.md`).

---

## Adquirencia

| Iniciativa | Fuente | Fecha de entrega | Tamaño (SP) | Conocimiento en |
|---|---|---|---|---|
| Cuotas CFT cliente: POS | Notion | — | **43 SP** (1×XL+1×L+7×M; 2 tickets sin talle) | `adquirencia/cuotas_y_campanias.md` |
| Botón Simple 2.0 | Notion | — | **0 SP** (78 tickets reales, ~50 bugs, sin desglose exacto por talle) | `adquirencia/boton_simple_2_0.md §1-3` |
| Devoluciones para botón simple | Notion | — | **0 SP** (sin desglose por talle) | `adquirencia/boton_simple_2_0.md §4` |
| Cambios DECIDIR Boton por marcas | Notion | — | **0 SP** (sin desglose por talle) | `adquirencia/boton_simple_2_0.md §5` |
| APIs para buscar deuda y cobrarla con BS2.0 | Notion | — | **0 SP** (sin desglose por talle) | `adquirencia/boton_simple_2_0.md §6` |
| Deuda QR | Notion | — | **0 SP** (sin desglose por talle) | `adquirencia/boton_simple_2_0.md §6` |
| QR tarjeta (en desarrollo al freeze) | Notion | — | **0 SP** (sin desglose por talle) | `adquirencia/boton_simple_2_0.md §8` |
| Pago Facil: Multicredencial BS y no liquidar | Notion | — | **0 SP** (sin desglose por talle) | `adquirencia/boton_simple_2_0.md §7` |
| QRI PSP 184 acreditación en wallet | Notion | — | **0 SP** (49 tickets reales, ~30 bugs, sin desglose exacto por talle) | `adquirencia/mecanica_qr_coelsa.md` (Parte 3) |
| Tardan mucho en resolver estado de tx con QR | Notion | — | 0 SP (sin desarrollo, nota operativa) | `referencia_estimaciones.md` |
| POS con PRISMA | Notion | — | 45 SP (estimado conjunto del lote A4: PRISMA+Asociar+Mensajería+APK intent+DATA2000) | `adquirencia/pos_multiadquirencia.md §1` |
| Cambios mensajería GP POS | Notion | — | ver "POS con PRISMA" (45 SP conjunto, no se duplica en el total) | `adquirencia/pos_multiadquirencia.md §2` |
| Asociar POS con primer login | Notion | — | ver "POS con PRISMA" (45 SP conjunto, no se duplica en el total) | `adquirencia/pos_multiadquirencia.md §3` |
| APK con intent | Notion | — | ver "POS con PRISMA" (45 SP conjunto, no se duplica en el total) | `adquirencia/pos_multiadquirencia.md §4` |
| DATA2000 funcionalidades APK | Notion | — | ver "POS con PRISMA" (45 SP conjunto, no se duplica en el total) | `adquirencia/pos_multiadquirencia.md §4` |
| Agrupador mayorista: Alta de entidades | Notion | — | **21 SP** (3×L; 4 tickets restantes sin talle) | `adquirencia/agrupador_mayorista.md §1` |
| Agrupador mayorista: ABM de canales de cobro | Notion | — | **100 SP** (mayor estimación agregada del lote A5) | `adquirencia/agrupador_mayorista.md §2` |
| Agrupador mayorista: ABM de roles y usuarios | Notion | — | **86 SP** | `adquirencia/agrupador_mayorista.md §3` |
| Mejora modelo agrupador | Notion | — | **40 SP** (2×XL+1×L+1×M; 49 tickets restantes sin talle exacto) | `adquirencia/agrupador_mayorista.md §6-7` |
| Parche agrupador mayorista | Notion | — | **77 SP** (11×L de 20 tickets; resto sin talle exacto) | `adquirencia/agrupador_mayorista.md §4-5` |
| Liquidador para traditum | Notion | — | **0 SP** ("todos L o sin tamaño", sin desglose exacto) | `adquirencia/liquidaciones_y_devoluciones.md §Liquidador histórico` |
| Integración RxT con Centralizador | Notion | — | **22 SP** (1×L+1×XL; resto "mayormente S/M" sin desglose exacto) | `adquirencia/webhooks_y_notificaciones.md §CVUCollect` |
| Newpay PMC MVP | Notion | — | **43 SP** (1×XL+4×L; resto "M/S" sin desglose exacto) | `adquirencia/liquidaciones_y_devoluciones.md §Liquidador histórico` |
| DESA: Botón cancelar y filtros en apis | Jira PRD-87 | **2026-02-10** (AD 67.2) | **3 SP** | `adquirencia/boton_simple_2_0.md §9` |
| COTO: Acomodar devoluciones parciales | Jira PRD-81 | **2025-12-16** (AD 66) | **5 SP** | `adquirencia/liquidaciones_y_devoluciones.md §1.1` |
| Errores en POS | Notion | — | **19 SP** (4×M+1×L; 17 tickets sin talle) | `adquirencia/pos_multiadquirencia.md §5` |
| PMC: Mantenimiento | Notion | — | **36 SP** (5×M+3×L; 1 ticket sin desarrollar) | `adquirencia/liquidaciones_y_devoluciones.md §PMC: Mantenimiento` |
| MOPAGOS: requerimientos específicos | Jira PRD-51 | **2025-11-17** (AD 65) | **2 SP** | `adquirencia/webhooks_y_notificaciones.md §Tipos de evento` (solo 1 de los 3 requerimientos pedidos llegó a construirse; cliente ya no activo) |
| HIPÓDROMO: Orden de venta con códigos externos | Jira PRD-112 | **2026-02-19** (AD 67.3) | **3 SP** (IDEA) — ≈29 SP reales en los 17 tickets de desarrollo retenidos (AD-518=7, AD-621=3, AD-677=3, AD-651=3, resto 0-1) | `adquirencia/botones_de_pago_y_qr.md §Origen de negocio` (funcionalidad técnica ya documentada por Notion; agrega origen de negocio y cluster de bugs) |
| Mejoras para integraciones y soporte | Jira PRD-88 | **2025-11-17** (AD 65) | **5 SP** (IDEA) — no aplica un total real: 7 Epics combinadas (~147 tickets), triage agresivo sobre muestra representativa, no fetch exhaustivo (a diferencia del resto de esta ingesta) | `adquirencia/configuracion_entidades_y_comercios.md §Mejoras y bugs de Admin/Backoffice` (rediseño de canales `canal_entidad`/`canal_comercio`, Alta de Entidad, AccessManagement — este último ya documentado por Notion en `agrupador_mayorista.md §3`) — también `wallet/organizaciones_y_configuracion.md §6` (ABM Especificaciones/Aceptadores, mensajes de error en alta de cuenta) |

**Total SP — Adquirencia: 550 SP.**

---

## Agente de Cobros y Pagos

| Iniciativa | Fuente | Fecha de entrega | Tamaño (SP) | Conocimiento en |
|---|---|---|---|---|
| Astro: Agente de cobros y pagos en USD | Notion | — | 19 SP | `cobros/cuenta_recaudadora_usd.md §1-2` |
| Astro: Consulta de saldo. Agente en ARS | Notion | — | **3 SP** (1×M; 1 bug sin talle) | `cobros/cuenta_recaudadora_usd.md §3` |
| Creación masiva de cajas con cvu | Notion | — | 27 SP | `cobros/carga_masiva_cajas.md` |
| API: TRX PULL cons tacito | Notion | — | **18 SP** (2×L+1×M+1×S; 5 tickets restantes sin talle) | `cobros/transferencias_pull.md` |
| Motor general de recycle | Notion | — | **75 SP** | `wallet/recycle_cobro_automatico.md §3` (reclasificada a Wallet) |
| Parche de recycles de viajes | Notion | — | **14 SP** (2×L; 9 bugs "S/M" sin desglose exacto) | `wallet/recycle_cobro_automatico.md §2` (reclasificada a Wallet) |
| Recurrencia en cobros | Notion | — | 0 SP (discovery, sin desarrollo) | `transversal/pagos_recurrentes_discovery.md` (reclasificada a transversal) |

**Total SP — Agente de Cobros y Pagos: 156 SP.**

---

## Onboarding

| Iniciativa | Fuente | Fecha de entrega | Tamaño (SP) | Conocimiento en |
|---|---|---|---|---|
| OB Personas Jurídicas MVP | Notion | — | **0 SP** (91 tickets reales, ninguno con talle registrado en Notion) | `onboarding/onboarding_personas_juridicas.md` |
| Onboarding en partes por API | Notion | — | **0 SP** (6 tickets, sin talles registrados) | `onboarding/onboarding_por_api.md` |
| Onboardings para el BIND | Notion | — | **0 SP** (24 tickets, mayoría sin tipo ni talle registrado) | `onboarding/onboarding_bind_sucursal.md` |
| Mejora OB PJ - Cambios de wordings | Jira PRD-168 | — (sin ticket de Entrega vinculado) | 0 SP | — *(sin contenido: IDEA sin `issuelinks` ni descripción)* |

**Total SP — Onboarding: 0 SP** (los 121 tickets reales del grupo — 91+6+24 — no tienen talle de camiseta registrado en el Notion histórico).

---

## Ardid

| Iniciativa | Fuente | Fecha de entrega | Tamaño (SP) | Conocimiento en |
|---|---|---|---|---|
| Ardid para wallet: Transferencias | Notion | — | **0 SP** (21 tickets reales, "mayormente L con algunos M/S", sin desglose exacto) | `ardid/integracion_con_productos_bind.md §1` |
| Ardid para botón simple MVP | Notion | — | **0 SP** (11 tickets reales, "predominantemente L", sin desglose exacto) | `ardid/integracion_con_productos_bind.md §2` |
| Ardid - Bóveda: integrar | Notion | — | 7 SP | `ardid/integracion_con_productos_bind.md §4` |
| Reparar Ardid+Wallet: Alta de cuentas y de segmentos | Notion | — | 50 SP | `ardid/integracion_con_productos_bind.md §5` |
| Ajustes Ardid+Wallet: Informar datos de localización | Notion | — | 20 SP (discovery, nunca construida) | `ardid/integracion_con_productos_bind.md §6` |
| Ajustes Ardid+Botón: localización y devoluciones | Notion | — | 15 SP (discovery, nunca construida) | `ardid/integracion_con_productos_bind.md §6` |

**Total SP — Ardid: 92 SP.**

---

## Transversal / Normativo

| Iniciativa | Fuente | Fecha de entrega | Tamaño (SP) | Conocimiento en |
|---|---|---|---|---|
| Integración con Worldsys MVP | Notion | — | **7 SP** (1×Spike L; 43 tickets restantes "M a XL" sin desglose exacto) | `transversal/cumplimiento_normativo.md §1` |
| Más datos en las cuentas para BCRA y Worldsys | Notion | — | **1 SP** (1×S, único ticket de la Epic) | `transversal/cumplimiento_normativo.md §2` |
| PCI: Recertificación | Notion | — | **13 SP** (2×M+1×L) | `transversal/cumplimiento_normativo.md §3` |
| Seguridad | Notion | — | **94 SP** (1×XL+3×L+16×M+10×S; 37 tickets de checklist de hardening sin talle) | `transversal/seguridad_y_webhooks.md §3` |
| Conteo de pegadas a API Bank | Notion | — | **16 SP** (3×M+1×L) | `transversal/seguridad_y_webhooks.md §4` |
| Reporting | Notion | — | **111 SP** (Tamaño estimado de la Epic; sin desglose por talle en todos los tickets) | `transversal/reporteria_operativa.md` |
| PSI — Proveedor de Servicios de Iniciación de Pagos | Notion | — | **104 SP** (Tamaño estimado; discovery, nunca construido) | `transversal/psi_discovery.md` |
| Grupo DESA: requerimientos para salir a prod | Notion | — | **52 SP** (Tamaño estimado de la Epic; 2×S+4×M de los tickets con talle) | `transversal/pago_facil.md` (sección Grupo DESA) |
| Modelo desacoplado transferencias | Notion | — | **0 SP** (Epic vacía, sin backlog ni Definiciones) | `transversal/referencia_estimaciones.md` (nota) |
| PSP Grupo BIND | Notion | — | **0 SP** (Epic vacía, sin backlog ni Definiciones) | `transversal/referencia_estimaciones.md` (nota) |

**Total SP — Transversal/Normativo: 398 SP.**

---

## Multi-producto (cola final — Epics-contenedor de bugs/mejoras)

| Iniciativa | Fuente | Fecha de entrega | Tamaño (SP) | Conocimiento en |
|---|---|---|---|---|
| Dolores de clientes | Notion | — | **~50 SP** (aprox. 10×M+6×S+2×L de los tickets con talle) | `transversal/pedidos_puntuales_de_clientes.md` |
| Dolores de Soporte y administración | Notion | — | **0 SP** (~93 tickets, sin patrón de talle dominante, sin desglose exacto) | `transversal/dolores_soporte_y_administracion.md` |
| Defectos encontrados en QA | Notion | — | **0 SP** (139 tickets, ~66% buckets de regresión sin contenido) | `transversal/defectos_encontrados_en_qa.md` |
| Mejoras e Iniciativas Técnicas | Notion | — | **0 SP** (~208 tickets, la Epic más grande del proyecto — triage agresivo sobre muestra) | `transversal/mejoras_e_iniciativas_tecnicas.md` |

**Total SP — Multi-producto: ~50 SP.**

---

## Total general (todas las fuentes, todos los productos)

**≈ 2.637 SP.** Suma de los subtotales de cada sección (Wallet 1.138 + TIN 253 + SUR FINANZAS 0 + Adquirencia 550 + Agente de Cobros y Pagos 156 + Onboarding 0 + Ardid 92 + Transversal/Normativo 398 + Multi-producto ~50). **Con este lote se completó el barrido inicial de las 15 IDEAs `Finalizada` de Jira** (ver [1_proyectos/ingesta_jira_producto.md](../../2_areas/1_proyectos/ingesta_jira_producto.md)). **Es un piso, no el esfuerzo real total**: varias de las Epics con más tickets de toda la ingesta (SUR FINANZAS: Requerimientos con 91, OB PJ MVP con 91, Botón Simple 2.0 con 78, Mejoras e Iniciativas Técnicas con ~208, Defectos encontrados en QA con 139) aportan 0 SP acá porque el Notion histórico no les registró talle de camiseta (o porque el volumen hizo inviable un triage exhaustivo) — el conteo de tickets de `referencia_estimaciones.md` es la señal de volumen real en esos casos. **Con este lote se completó el proyecto de ingesta: 93/93 Epics del Notion histórico.**

## Relación con otros documentos de la wiki

- [4_archivos/ingesta_epics_notion.md](../../2_areas/4_archivos/ingesta_epics_notion.md) — archivo de control del barrido de Notion, ya completado y rotado a `4_archivos/` (93/93 Epics ingeridas); este log sigue vivo después.
- [1_proyectos/ingesta_jira_producto.md](../../2_areas/1_proyectos/ingesta_jira_producto.md) — archivo de control del barrido inicial de Jira (mapeo de custom fields, pipeline IDEA→Epic→US). Rota a `4_archivos/` al completar el barrido inicial planeado; de ahí en adelante, cada IDEA nueva de Jira se ingiere directo a este log sin pasar por un archivo de control dedicado.
- [3_recursos/detalle_productos/transversal/referencia_estimaciones.md](../../2_areas/procesos/referencia_estimaciones.md) — fuente de los valores de Story Points y de los desgloses por talle usados para derivarlos.
- [3_recursos/detalle_productos/transversal/gestion_jira.md §1.4](../../2_areas/procesos/gestion_jira.md#14-prioridad-versión-y-story-points) — convención de conversión Talle→SP.
- [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md) — gaps abiertos sobre iniciativas puntuales de este log (ej. Epics "Lanzadas" en Notion sin ejecución real confirmada).

---
*Última actualización: 2026-08-10 — `/sync_jira_ideas`: fila nueva PRD-185 (Finalizada, W 71) en Wallet.*
*Última actualización anterior: 2026-07-06 — Backfill completo de la columna Tamaño (SP) aplicando la convención Talle→SP (S=1·M=3·L=7·XL=15) sobre los desgloses de `referencia_estimaciones.md`. Tickets sin talle registrado, o con desglose ambiguo entre dos talles (ej. "resto M/S"), cuentan como 0 SP por indicación explícita del usuario. Agregado "Total general" al pie del log.*
