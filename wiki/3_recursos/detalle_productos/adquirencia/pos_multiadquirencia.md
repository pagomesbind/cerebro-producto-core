# POS — multiadquirencia, vínculo por login y app intent

> Estado: en producción.

> Fuente: Notion histórico, 5 Epics: **"POS con PRISMA"** (18 tickets, ~45 SP), **"Asociar POS con primer login"** (14 tickets), **"Cambios mensajería GP POS"** (Normativo), **"APK con intent"** y **"DATA2000 funcionalidades APK"**.

## 1. Multiadquirencia: integración con PRISMA como segundo procesador de POS

Hasta esta Epic, el POS de Bind PSP procesaba únicamente contra **GlobalProcessing (GP)**. Se integró **PRISMA** (otro switch/procesador de tarjetas argentino) como **segundo procesador** disponible para el canal POS — de ahí "multiadquirencia".

- **Trabajo de integración típico de un nuevo procesador de tarjetas** (patrón reutilizable para futuros procesadores): creación de repositorio/arquetipo dedicado para el protocolo **ISO 8583** de Prisma, pre-homologación y homologación formal con Prisma, integración al **Centralizador** (el componente interno que orquesta entre procesadores — ya visto en otras Epics de la wiki) en dos etapas (integración pura, luego lógica de orquestación), e integración de la **reversa** de transacciones.
- **Multiadquirencia a nivel de seguridad**: se requirió soportar **distintas llaves de Maestro PIN por procesador** — el cifrado de PIN de una transacción con tarjeta de débito no es genérico, depende de qué procesador la va a validar.
- **Bugs de habilitación real**: un comercio no podía asignarse a una caja/serial de POS si no estaba dado de alta en GP — indica que, pese a integrar Prisma, el alta en GP seguía siendo un prerequisito técnico no siempre necesario; y un caso donde el sistema indicaba "comercio sin convenio" cuando el convenio con Prisma sí existía (bug de validación).
- **Cambios de protocolo forzados por el procesador**: hubo que adaptar campos ISO 8583 y códigos de respuesta de reversos por un cambio unilateral de fecha límite impuesto por el procesador (ticket "Cambios en ISO para el 20/06/2025") — recordatorio de que la integración con un procesador de tarjetas no es "una vez y listo": el procesador puede forzar cambios de protocolo con fecha límite.

### 1.1 Segunda fase — habilitar PRISMA desde el Admin (Jira, Epic "POS con PRISMA: Admin", ⚠️ EN DESARROLLO/BLOQUEADA a la fecha de esta ingesta)

> Fuente: Jira, tickets [AD-432](https://bindpsp.atlassian.net/browse/AD-432) y [AD-431](https://bindpsp.atlassian.net/browse/AD-431) (7 SP c/u, "Bloqueado" en Jira, taggeados a la versión AD 70.1 aunque no cerrados) + [AD-1071](https://bindpsp.atlassian.net/browse/AD-1071, "En curso"). Backfill vía `/sync_releases`, 2026-07-13.

Objetivo: permitir habilitar/configurar PRISMA como procesador POS **desde el Admin** (por comercio o por defecto a nivel entidad), sin depender de configuración manual en base de datos como hasta ahora. **Estado real a la fecha de esta ingesta: no completado.**

- **Modelo elegido, en 2 etapas**: Etapa 1 — el canal POS sigue con GP marcado por defecto en `CanalEntidad`/`CanalComercio`, conviviendo obligatoriamente con PRISMA (deuda técnica reconocida explícitamente). Etapa 2 (fuera de alcance, ticket futuro AD-992) — permitir habilitar POS **solo con PRISMA** sin pasar primero por GP.
- **Restricción de negocio descubierta durante el análisis**: PRISMA no puede configurarse como **primer** procesador porque el código de GP está hardcodeado como paso previo obligatorio — hoy en día es obligatorio dar de alta primero en GP y luego (opcionalmente) en PRISMA; el workaround documentado en el ticket es crear la configuración manualmente en base y simular que GP habilitó PRISMA.
- **Bloqueo activo al momento del backfill**: los nuevos endpoints v2 de alta de comercio exigen el campo `fecha de nacimiento del titular` en ambientes bajos (no obligatorio aún en producción) — bloquea las pruebas de alta de comercios con canal POS en QA/STG. Sin resolución confirmada a la fecha.
- **Lectura para consultas de estado de producto**: pese a que estos tickets están etiquetados con versiones AD 70.1/POS 65 en Jira, **no representan una funcionalidad productiva completa** — la integración base con PRISMA (§1, Notion histórico) sí está en producción, pero la configuración self-service desde el Admin sigue bloqueada/en desarrollo.

### 1.2 Cierre de la épica y posible "Post con Prisma Plus" (2026-07-30)

> Fuente: reunión "Análisis COBRO" (2026-07-30), minuta Gemini.

La épica **"Post con Prisma"** (9 tickets en curso a esta fecha — no confundir con el conteo histórico de 18 tickets/~45 SP de la integración original documentada en §1) llegó al punto de cierre: el equipo decidió **cerrarla en su estado actual** y evaluar crear una segunda versión ("Post con Prisma Plus" o v2) para trasladar ahí los pendientes — en particular la **orquestación de procesadores** que quedó fuera del corte original. Sin fecha ni alcance formal todavía para la v2; queda priorizada para agosto 2026 en el roadmap del área (ver [`decisiones.md`](../../../2_areas/direccion/decisiones.md)).

Relacionado, en la misma reunión: **gestión de IDs de sitio (site IDs) de Prisma según el rubro del comercio** — se identificó el riesgo de asignar mal el site ID según rubro comercial (posible motivo de multas de Prisma); el plan es cargar una tabla de parámetros rubro→site ID y eventualmente exponerla en el Admin.

## 2. Cambios de mensajería GP POS — bug real de cuotas (Normativo)

**Bug de negocio confirmado, no solo técnico**: los SmartPOS enviaban el **mismo código de plan de cuotas** para "3 cuotas TNA normal" y "3 cuotas TNA cuota simple" (debían ser `3` y `13` respectivamente; igual para 6/16) — el procesador (GlobalProcessing) **no podía distinguir la tasa aplicada**, con impacto directo en tasas, contabilidad financiera y riesgo de reclamos. Se corrigió la lógica de mensajería del POS y se coordinó formalmente con GlobalProcessing para que aceptase los nuevos códigos. **Lección reutilizable**: cualquier variante comercial de un mismo "tipo" de operación (ej. cuotas con distinta tasa) necesita su **propio código diferenciado end-to-end** — enviar el mismo código para dos condiciones comerciales distintas es indetectable hasta que alguien audita tasas o cobros.

## 3. Asociar POS con primer login — vínculo "zero-touch" del dispositivo

Mecanismo para vincular un **POS virgen** (sin configurar) a un comercio simplemente logueándose con un usuario válido del sistema — sin proceso de alta manual del dispositivo:

- Si el usuario que loguea es **admin de comercio**: se crea automáticamente una sucursal y una caja, y el POS queda asociado a esa caja nueva.
- Si es **supervisor de comercio**: se crea una caja en su sucursal y el POS queda asociado.
- Si es **operador de comercio**: el POS queda asociado directamente a la caja para la que ese operador ya estaba configurado.
- Una vez asociado, cualquier otro usuario con permisos sobre esa misma caja puede loguearse en el mismo POS.

**Limitaciones conocidas al momento del lanzamiento** (anunciadas explícitamente por el propio equipo, no bugs ocultos):
- No hay forma de **desasociar** un POS para reutilizarlo en otra Entidad — solo puede reasignarse a otro comercio de la misma Entidad inicial.
- El botón "cerrar sesión" en la práctica solo minimiza la app (la sesión se cierra recién si además se fuerza el cierre manual de la app).
- Sin la opción "Recordar usuario" activada, el dispositivo desloguea solo tras bloqueo/inactividad — comportamiento heredado, no introducido por esta Epic.

## 4. APK con intent (integración Posberry) y DATA2000

- **"Intent e integración con Posberry"** (ticket XL): integración vía **Android Intent** con **Posberry** — un dispositivo/plataforma POS de bajo costo (nombre sugiere una base tipo Raspberry Pi). Permite que otra app dispare la apertura del cobro de Bind PSP pasándole los parámetros por intent, en vez de que el usuario opere la app manualmente.
- **"DATA2000 funcionalidades APK"**: conjunto de endpoints de **préstamos** (cálculo de cuota, otorgamiento, resumen, simulador) embebidos en la APK del POS — sugiere que "DATA" es un cliente/proveedor de crédito que ofrece micro-préstamos a comercios directamente desde el mismo dispositivo POS que usan para cobrar. Distinto del discovery de Lending de Wallet ([wallet/lending_discovery.md](../wallet/lending_discovery.md), nunca construido) — este sí llegó a producción, del lado Adquirencia/POS.

## 5. Errores en POS (22 tickets — cola de mantenimiento, cierra el grupo Adquirencia/POS)

> Fuente: Epic Notion "[EPIC] Errores en POS" (Tipo Dolor). Ingesta MANT, 2026-07-06.

Bugs y mejoras puntuales de la APK POS y su BFF, todos ya resueltos ("En Producción"):
- **Comprobantes/tickets**: agregar ID de orden en el ticket impreso, que el ID de orden del ticket de devolución coincida con el del pago original, reimpresión de comprobante de pago (aprobado/rechazado) y de devolución, imprimir automáticamente el ticket al momento de la devolución.
- **Bugs funcionales**: la devolución no actualizaba su valor en pantalla, el login indicaba error pero igual iniciaba sesión, no se tomaba el monto ingresado (mensaje de error con `$null` en vez del mínimo real), fallaba el pago con tarjetas de crédito Mastercard.
- **Filtros de movimientos**: faltaba la forma de pago "Tarjeta Prepaga" como opción de filtro, faltaba el acento en "débito"/"crédito", no se podía filtrar por fecha + medio de pago a la vez, corrección de márgenes en el popup de búsqueda avanzada.
- **Otros**: no se enviaba el comprobante por mail en producción, ocultar el botón de devolución cuando el comercio no puede usarla, agregar botón "No" en el popup de confirmación de devolución, loguear el momento del deslogueo y la versión de la app (para diagnóstico), endpoint para modificar los procesadores de pago habilitados de un comercio, timeout de respuesta del BFF de creación de pago (bug de mayor tamaño, L).

**Lectura para estimaciones futuras**: cola de mantenimiento típica de un dispositivo físico con app embebida — mayoría de tickets sin tamaño individual asignado (arreglos puntuales de UI/mensajes) salvo el timeout de BFF (L), que es el único con causa raíz de backend real.

**Versiones de publicación** (vía `/sync_releases`, backfill XML): tanda de UX menores de POS en **AD 65** (2025-11-17, lanzamiento del tracking Jira) — [AD-14](https://bindpsp.atlassian.net/browse/AD-14) (falta tilde en logout), [AD-15](https://bindpsp.atlassian.net/browse/AD-15) (círculo del calendario desplazado), [AD-17](https://bindpsp.atlassian.net/browse/AD-17) (QR queda cargando sin mostrar resultado), [AD-31](https://bindpsp.atlassian.net/browse/AD-31)/[AD-32](https://bindpsp.atlassian.net/browse/AD-32) (filtros de movimientos), [AD-33](https://bindpsp.atlassian.net/browse/AD-33) (comprobante por email ilegible). Bugs de **Reporting del Admin** (Epic "Reporting", **AD 66** 2025-12-16): [AD-85](https://bindpsp.atlassian.net/browse/AD-85) (reporte de comercios con caracteres rotos), [AD-86](https://bindpsp.atlassian.net/browse/AD-86) (CSV con fechas ordenadas ascendente, debían ser descendente), [AD-93](https://bindpsp.atlassian.net/browse/AD-93) (columnas de importe sin formato consistente), [AD-136](https://bindpsp.atlassian.net/browse/AD-136) (importe con punto en vez de coma decimal).

## 6. Desalineación entre la base de BINES de Payway y lo que responde Decidir al rechazar — investigación abierta

> Fuente: hilo de mail "Análisis BINES Payway/Decidir", Fintexa (Agustín Grau, CTO), mensajes 2026-05-20 a 2026-08-19. Ticket de soporte Fintexa [AD-681](https://fintexa.atlassian.net) asociado.

Investigación técnica de Fintexa sobre rechazos de transacciones con tarjeta relacionados a la identificación de BINES, cruzando tres fuentes: la configuración/identificación de BINES propia de Bind PSP, la base de datos de BINES de **Payway** (provista por Gonzalo Rivera) y lo que responde **Decidir** cuando rechaza una transacción (Decidir/Payway/Prisma son el mismo gateway, ver [`2_areas/direccion/decisiones.md`](../../../2_areas/direccion/decisiones.md) 2026-07-17).

**Primer análisis (2026-05-20, muestra de un día):** no se pudo concluir que los rechazos se expliquen por las diferencias entre bases — hay transacciones con los mismos atributos que sí están aprobadas. Hace falta ajustar la base de BINES propia, pero no está claro qué cambiar: lo que dice Decidir no coincide con la BD de BINES de Payway, y además hay BINES obtenidos de Global Processing (GP) que sí coinciden con los de Payway.

**Segundo análisis (2026-08-19, muestra completa de aprobadas y rechazadas de un día completo, 18/08):** a diferencia del primero (muestra parcial), este análisis concluye que **hay acciones concretas que se pueden tomar ya y que darían mejoras instantáneas** — pendiente de una reunión para definirlas e implementarlas.

**Estado:** sin cierre — pendiente que Bind PSP acepte la reunión propuesta por Fintexa. El informe interactivo con el detalle de "qué BINES corregir" está en un adjunto HTML no leído en el flujo de ingesta.

## Ver también

- [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) — mecánica de Centralizador y multiPSP en el canal QR (mismo concepto de orquestación multi-procesador).
- [wallet/lending_discovery.md](../wallet/lending_discovery.md) — iniciativa de crédito embebido del lado Wallet (discovery, nunca construida) — contrastar con DATA2000, que sí se construyó del lado POS.
