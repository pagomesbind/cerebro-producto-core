# Pedidos de Clientes y Hallazgos Operativos Históricos — Portal Comercio

> Estado: mezcla de en producción y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde 3 archivos-cola de `detalle_productos/transversal/` (`pedidos_puntuales_de_clientes.md`, `dolores_soporte_y_administracion.md`, `reporteria_operativa.md`) que mezclaban pedidos de varios productos y del Portal Admin en un solo archivo — ver [`portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md`](../portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md) para lo específico del Admin.

## Rollout Portal 2.0 (mayo 2026) — bugs de QA

> Fuente: Jira bindpsp.atlassian.net, versiones AD Portal 2.0 V1 (publicada 2026-05-21, 18 tickets, incluye AD-593) y AD Portal 2.0 V2 (publicada 2026-05-21, 2 tickets) — ambas ingeridas retroactivamente el 2026-08-15 por un gap del backfill de 2026-07-13 (nomenclatura no secuencial, ver `2_areas/gaps_y_preguntas.md`). "Portal 2.0" es el rediseño del Portal Comercio (autogestión) que se estaba migrando cliente por cliente en STG/PROD en mayo 2026, con una variante adicional "Mayorista" (`MayoristaBS`) para comercios agrupadores. Estos 20 tickets son observaciones de QA levantadas durante ese rollout — primera cobertura del tema en esta wiki. La skill `/sync_releases` no cruza contra `1_proyectos/` — si alguna de estas observaciones toca un PRD vivo de Portal 2.0, el PM debe verificarlo aparte.

**Autenticación y accesos:**
- **reCAPTCHA bloqueaba credenciales válidas detrás de VPN** ([AD-1131](https://bindpsp.atlassian.net/browse/AD-1131)): el login de Portal 2.0 rechazaba usuarios con credenciales correctas cuando accedían con VPN activa, porque reCAPTCHA interpretaba el patrón de tráfico como bot/scam. Sin VPN el login funcionaba.
- **Usuario ADMIN recién creado veía menú reducido** ([AD-1117](https://bindpsp.atlassian.net/browse/AD-1117)): al crear un usuario con rol ADMIN desde el portal (flujo: alta → mail → creación de contraseña → login), el usuario quedaba con permisos/menú de un rol inferior, persistente incluso 20+ minutos después.

**Mayorista (`MayoristaBS`) — funcionalidad específica:**
- **Alta de usuario Operador no permite asignar caja** ([AD-1133](https://bindpsp.atlassian.net/browse/AD-1133)): al crear un usuario con rol Operador, el desplegable de "caja" no abría tras elegir sucursal; al guardar, vuelve a la página anterior sin crear el usuario.
- **Detalle de transacciones expone campos que no debería** ([AD-1132](https://bindpsp.atlassian.net/browse/AD-1132)): la sección Transacciones mostraba Comisión/Neto/Retención en las vistas de Mayorista — esa información no debe verse a ese nivel (perfil mayorista agrupa varios comercios).
- **Sección QR carga con error** ([AD-1120](https://bindpsp.atlassian.net/browse/AD-1120)): en Mayorista, ingresar a la sección QR tira error de carga — el resto de las secciones del portal cargaban bien.
- **Sección Transacciones no trae datos** ([AD-1121](https://bindpsp.atlassian.net/browse/AD-1121)): para un usuario Mayorista, la sección Transacciones respondía "No se encontraron resultados" pese a existir transacciones reales en `dbo.Transaccion` para ese comercio.
- **Opción "Devolver" deshabilitada sin motivo** ([AD-1129](https://bindpsp.atlassian.net/browse/AD-1129)): en Mayorista, la opción de devolución aparece griseada en la sección Transacciones.
- **Usuario Operador no ve datos para cobrar con QR** ([AD-1118](https://bindpsp.atlassian.net/browse/AD-1118)): un usuario con rol Operador, al entrar a "Cobrar con QR", no ve datos para efectuar el cobro y recibe pop-ups de error.

**Portal Entidad (no-Mayorista) — funcional:**
- **Transferencias fallan si el concepto no es "Varios"** ([AD-1119](https://bindpsp.atlassian.net/browse/AD-1119)): al transferir, cualquier concepto distinto de "Varios" devuelve "Solicitud inválida: los datos de la solicitud no coinciden con lo de la intención" — comparado contra el portal viejo (no 2.0), donde sí se podían usar otros conceptos.
- **Saldo no se actualiza tras pago QR, bloqueando la devolución** ([AD-845](https://bindpsp.atlassian.net/browse/AD-845)): un pago de $15 con QR no impactó el saldo mostrado en Movimientos (quedó en $0,49 sin cambios); al intentar devolver, "Error en la devolución: el importe de la devolución es incorrecto". Nota aparte: la sección Transacciones muestra "Total acreditados" de forma que puede confundirse con saldo disponible.
- **Ícono de "ticket" en Movimientos no debería mostrarse para comprobantes** ([AD-841](https://bindpsp.atlassian.net/browse/AD-841)): el Cobro con QR interoperable es un comprobante, no una operación (como sí lo es una transferencia) — no debería generarse ni mostrarse el ícono de ticket. Al clickearlo, siempre da "ticket no disponible".
- **Pop-up de error falso al cambiar de caja para cobrar QR** ([AD-838](https://bindpsp.atlassian.net/browse/AD-838)): cambiar de caja, generar QR y cobrar funciona bien, pero igual aparece el pop-up "Error al cargar las cajas. Intente nuevamente." sin que haya ocurrido ningún error real.
- **PDF de liquidaciones no abre** ([AD-1114](https://bindpsp.atlassian.net/browse/AD-1114)): exportar liquidaciones a PDF desde Portal 2.0 descarga el archivo pero da "No podemos abrir este archivo" al intentar abrirlo (reproducido con varias liquidaciones distintas); en el portal viejo (no migrado a 2.0) el mismo PDF abre sin problemas.
- **Columna "Devolución" vacía al exportar Transacciones** ([AD-988](https://bindpsp.atlassian.net/browse/AD-988)): el Excel exportado desde Transacciones no trae la fecha de devolución en esa columna.
- **UI menor:** columnas de la sección Usuarios no centradas con sus títulos ([AD-1130](https://bindpsp.atlassian.net/browse/AD-1130)); pop-ups informativos no se cierran automáticamente y quedan visibles hasta ~3 minutos o cierre manual ([AD-837](https://bindpsp.atlassian.net/browse/AD-837), Portal 2.0 PROD).

**Pagos FX Portal (variante específica del Portal Web, ver también [`wallet/dolar_fx.md`](../wallet/dolar_fx.md)):**
- **Etiqueta "IBAN" incorrecta para esquema BAN** ([AD-1316](https://bindpsp.atlassian.net/browse/AD-1316), Portal 2.0 V2): en la confirmación de pago, el frontend siempre muestra la etiqueta fija "IBAN" para el número de cuenta del beneficiario, incluso cuando el corredor no es SEPA y el dato es un BAN (cuenta local + SWIFT, ej. transferencias a Canadá). El campo backend `recipient_account_uri` ya distingue el esquema por prefijo (`ban:`/`iban:`) — el fix propuesto es renderizar la etiqueta según ese prefijo ("BAN/IBAN" dinámico) en vez de un texto fijo.
- **Filtro de países en Beneficiario queda pegado** ([AD-1262](https://bindpsp.atlassian.net/browse/AD-1262), Portal 2.0 V2): al filtrar por país en la sección Beneficiario, el filtro queda seteado en la última búsqueda incluso al navegar a otra sección o volver a loguearse — no vuelve a "todos los países".

**CITYGAS — pedido de UX** ([AD-593](https://bindpsp.atlassian.net/browse/AD-593), Portal 2.0 V1, estado "Con defecto"): el cliente City Gas, con gran volumen de sucursales/cajas configuradas, pidió que el desplegable de filtro "Sucursales" en Transacciones se muestre ordenado alfabéticamente (A-Z) en vez de sin orden — ver también el pedido ya documentado de CITYGAS sobre totalizador y datos del pagador en el canal QR, abajo.

## Pedidos puntuales por cliente

- **CITYGAS**: mejora de visualización del totalizador y agregar datos del pagador en el portal Comercio del canal QR (Pendiente).

## Bugs sin cliente específico

- Bug en el botón para devolver una transacción desde el Portal Comercio.
- **SUR FINANZAS: la sección Usuarios no traía información** — el listado de usuarios del portal quedaba vacío para un administrador real (confirmado en QA antes de producción). Ver ficha del cliente en [`ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md`](../ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md).

## Extracto de movimientos HTML (desarrollo en 7 partes)

Extracto de movimientos con formato HTML (no solo CSV) para Portal Comercio:
1. Modelo de extracto (back).
2. Configuración del reporte (back) — incluye logo, comentarios y domicilio de la organización como datos personalizables del extracto.
3. Portal Comercio (front).
4. Generación mensual automática del reporte.
5-6. Procesamiento de archivos grandes en pequeños pasos (batch) — mismo problema de volumen que motivó la generación asíncrona de reportes CSV del Admin.
7. No mostrar reportes expirados en Admin ni en Portal (los reportes generados tienen una vida útil/expiración).

**Pendiente sin cerrar**: "Procesar archivos grandes en pequeños pasos (batch)" para Wallet (ticket separado del de Extracto HTML) quedó en "Refinar".

## Ver también
- [portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md](../portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md) — motor de reportería CSV del Admin (bug recurrente de filtro por Entidad).
- [ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md](../ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md) — grilla de movimientos y particularidades de portal de SUR FINANZAS.

---
*Fuente: Epics Notion "Dolores de clientes", "Dolores de Soporte y administración" y "Reporting" — ingesta 2026-07-06.*
*Última actualización: 2026-08-15 — `/sync_releases`: nueva sección "Rollout Portal 2.0 (mayo 2026) — bugs de QA" (20 tickets, ingesta retroactiva por gap del backfill anterior).*
*Última actualización anterior: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Portal Comercio de 3 archivos-cola de `detalle_productos/transversal/`.*
