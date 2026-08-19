---
id: 2026-08-15_portal_comercio_rollout_portal20
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versiones AD Portal 2.0 V1 (publicada 2026-05-21, 18 tickets, incluye AD-593) y AD Portal 2.0 V2 (publicada 2026-05-21, 2 tickets) — ambas gap del backfill de 2026-07-13 (nomenclatura no secuencial)"
producto: adquirencia
tema: Rollout de Portal 2.0 (Entidad y Mayorista) — bugs de QA en staging/producción
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9306bc6b7cffeb57db264f132b0e0e6a1ec53d8e
---

**Contexto general:** "Portal 2.0" es el rediseño del Portal Comercio (autogestión) que se estaba migrando cliente por cliente en STG/PROD en mayo 2026, con una variante adicional "Mayorista" (`MayoristaBS`) para comercios agrupadores. Estas 20 tickets son observaciones de QA levantadas durante ese rollout — no se encontró documentación previa de "Portal 2.0" en la wiki, así que esto es la primera cobertura del tema. La skill `/sync_releases` no cruza contra `1_proyectos/` — si alguna de estas observaciones toca un PRD vivo de Portal 2.0, el PM debe verificarlo aparte.

Nueva sección "Rollout Portal 2.0 (mayo 2026) — bugs de QA":

**Autenticación y accesos:**
- **reCAPTCHA bloqueaba credenciales válidas detrás de VPN (AD-1131):** el login de Portal 2.0 rechazaba usuarios con credenciales correctas cuando accedían con VPN activa, porque reCAPTCHA interpretaba el patrón de tráfico como bot/scam. Sin VPN el login funcionaba.
- **Usuario ADMIN recién creado veía menú reducido (AD-1117):** al crear un usuario con rol ADMIN desde el portal (flujo: alta → mail → creación de contraseña → login), el usuario quedaba con permisos/menú de un rol inferior, persistente incluso 20+ minutos después.

**Mayorista (`MayoristaBS`) — funcionalidad específica:**
- **Alta de usuario Operador no permite asignar caja (AD-1133):** al crear un usuario con rol Operador, el desplegable de "caja" no abría tras elegir sucursal; al guardar, vuelve a la página anterior sin crear el usuario.
- **Detalle de transacciones expone campos que no debería (AD-1132):** la sección Transacciones mostraba Comisión/Neto/Retención en las vistas de Mayorista — esa información no debe verse a ese nivel (perfil mayorista agrupa varios comercios).
- **Sección QR carga con error (AD-1120):** en Mayorista, ingresar a la sección QR tira error de carga — el resto de las secciones del portal cargaban bien.
- **Sección Transacciones no trae datos (AD-1121):** para un usuario Mayorista, la sección Transacciones respondía "No se encontraron resultados" pese a existir transacciones reales en `dbo.Transaccion` para ese comercio.
- **Opción "Devolver" deshabilitada sin motivo (AD-1129):** en Mayorista, la opción de devolución aparece griseada en la sección Transacciones.
- **Usuario Operador no ve datos para cobrar con QR (AD-1118):** un usuario con rol Operador, al entrar a "Cobrar con QR", no ve datos para efectuar el cobro y recibe pop-ups de error.

**Portal Entidad (no-Mayorista) — funcional:**
- **Transferencias fallan si el concepto no es "Varios" (AD-1119):** al transferir, cualquier concepto distinto de "Varios" devuelve "Solicitud inválida: los datos de la solicitud no coinciden con lo de la intención" — comparado contra el portal viejo (no 2.0), donde sí se podían usar otros conceptos.
- **Saldo no se actualiza tras pago QR, bloqueando la devolución (AD-845):** un pago de $15 con QR no impactó el saldo mostrado en Movimientos (quedó en $0,49 sin cambios); al intentar devolver, "Error en la devolución: el importe de la devolución es incorrecto". Nota aparte: la sección Transacciones muestra "Total acreditados" de forma que puede confundirse con saldo disponible.
- **Ícono de "ticket" en Movimientos no debería mostrarse para comprobantes (AD-841):** el Cobro con QR interoperable es un comprobante, no una operación (como sí lo es una transferencia) — no debería generarse ni mostrarse el ícono de ticket. Al clickearlo, siempre da "ticket no disponible".
- **Pop-up de error falso al cambiar de caja para cobrar QR (AD-838):** cambiar de caja, generar QR y cobrar funciona bien, pero igual aparece el pop-up "Error al cargar las cajas. Intente nuevamente." sin que haya ocurrido ningún error real.
- **PDF de liquidaciones no abre (AD-1114):** exportar liquidaciones a PDF desde Portal 2.0 descarga el archivo pero da "No podemos abrir este archivo" al intentar abrirlo (reproducido con varias liquidaciones distintas); en el portal viejo (no migrado a 2.0) el mismo PDF abre sin problemas.
- **Columna "Devolución" vacía al exportar Transacciones (AD-988):** el Excel exportado desde Transacciones no trae la fecha de devolución en esa columna.
- **UI menor:** columnas de la sección Usuarios no centradas con sus títulos (AD-1130); pop-ups informativos no se cierran automáticamente y quedan visibles hasta ~3 minutos o cierre manual (AD-837, Portal 2.0 PROD).

**Pagos FX Portal (variante específica del Portal Web, ver también `wallet/dolar_fx.md`):**
- **Etiqueta "IBAN" incorrecta para esquema BAN (AD-1316, Portal 2.0 V2):** en la confirmación de pago, el frontend siempre muestra la etiqueta fija "IBAN" para el número de cuenta del beneficiario, incluso cuando el corredor no es SEPA y el dato es un BAN (cuenta local + SWIFT, ej. transferencias a Canadá). El campo backend `recipient_account_uri` ya distingue el esquema por prefijo (`ban:`/`iban:`) — el fix propuesto es renderizar la etiqueta según ese prefijo ("BAN/IBAN" dinámico) en vez de un texto fijo.
- **Filtro de países en Beneficiario queda pegado (AD-1262, Portal 2.0 V2):** al filtrar por país en la sección Beneficiario, el filtro queda seteado en la última búsqueda incluso al navegar a otra sección o volver a loguearse — no vuelve a "todos los países".

**CITYGAS — pedido de UX (AD-593, Portal 2.0 V1, estado "Con defecto"):** el cliente City Gas, con gran volumen de sucursales/cajas configuradas, pidió que el desplegable de filtro "Sucursales" en Transacciones se muestre ordenado alfabéticamente (A-Z) en vez de sin orden — ver también el pedido ya documentado de CITYGAS sobre totalizador y datos del pagador en el canal QR.
