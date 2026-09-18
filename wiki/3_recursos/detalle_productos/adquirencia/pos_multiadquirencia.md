# POS — multiadquirencia, vínculo por login y app intent

> Estado: en producción.

> Fuente: Notion histórico, 5 Epics: **"POS con PRISMA"** (18 tickets, ~45 SP), **"Asociar POS con primer login"** (14 tickets), **"Cambios mensajería GP POS"** (Normativo), **"APK con intent"** y **"DATA2000 funcionalidades APK"**.

## 1. Multiadquirencia: integración con PRISMA como segundo procesador de POS

Hasta esta Epic, el POS de Bind PSP procesaba únicamente contra **GlobalProcessing (GP)**. Se integró **PRISMA** (otro switch/procesador de tarjetas argentino) como **segundo procesador** disponible para el canal POS — de ahí "multiadquirencia".

- **Trabajo de integración típico de un nuevo procesador de tarjetas** (patrón reutilizable para futuros procesadores): creación de repositorio/arquetipo dedicado para el protocolo **ISO 8583** de Prisma, pre-homologación y homologación formal con Prisma, integración al **Centralizador** (el componente interno que orquesta entre procesadores — ya visto en otras Epics de la wiki) en dos etapas (integración pura, luego lógica de orquestación), e integración de la **reversa** de transacciones.
- **Multiadquirencia a nivel de seguridad**: se requirió soportar **distintas llaves de Maestro PIN por procesador** — el cifrado de PIN de una transacción con tarjeta de débito no es genérico, depende de qué procesador la va a validar.
- **Bugs de habilitación real**: un comercio no podía asignarse a una caja/serial de POS si no estaba dado de alta en GP — indica que, pese a integrar Prisma, el alta en GP seguía siendo un prerequisito técnico no siempre necesario; y un caso donde el sistema indicaba "comercio sin convenio" cuando el convenio con Prisma sí existía (bug de validación).
- **Cambios de protocolo forzados por el procesador**: hubo que adaptar campos ISO 8583 y códigos de respuesta de reversos por un cambio unilateral de fecha límite impuesto por el procesador (ticket "Cambios en ISO para el 20/06/2025") — recordatorio de que la integración con un procesador de tarjetas no es "una vez y listo": el procesador puede forzar cambios de protocolo con fecha límite.

### 1.1 Segunda fase — habilitar PRISMA desde el Admin (Jira, Epic "POS con PRISMA: Admin", AD-430 — ✅ cerrada, ver §1.1bis)

> Fuente: Jira, tickets [AD-432](https://bindpsp.atlassian.net/browse/AD-432) y [AD-431](https://bindpsp.atlassian.net/browse/AD-431) (7 SP c/u, "Bloqueado" en Jira, taggeados a la versión AD 70.1 aunque no cerrados) + [AD-1071](https://bindpsp.atlassian.net/browse/AD-1071, "En curso"). Backfill vía `/sync_releases`, 2026-07-13.

Objetivo: permitir habilitar/configurar PRISMA como procesador POS **desde el Admin** (por comercio o por defecto a nivel entidad), sin depender de configuración manual en base de datos como hasta ahora.

> ⚠️ **Estado desactualizado — ver §1.1bis.** Lo que sigue es el estado tal como lo describía el backfill original de Jira (2026-07-13), que mostraba el estado "Bloqueado" de 2 tickets como si la funcionalidad siguiera sin completar. Un barrido directo en Jira (2026-09-18) confirmó que la Epic ya cerró y la gran mayoría de estos tickets están en Producción — el estado "Bloqueado" que seguían mostrando en Jira era la aprobación QA interna de Bind PSP, un paso posterior al despliegue real, no evidencia de que el código no estuviera en producción.

- **Modelo elegido, en 2 etapas**: Etapa 1 — el canal POS sigue con GP marcado por defecto en `CanalEntidad`/`CanalComercio`, conviviendo obligatoriamente con PRISMA (deuda técnica reconocida explícitamente). Etapa 2 (fuera de alcance, ticket futuro AD-992) — permitir habilitar POS **solo con PRISMA** sin pasar primero por GP. **Actualización: la Etapa 2 terminó construyéndose y entregándose** dentro del mismo período — ver §1.1bis.
- **Restricción de negocio descubierta durante el análisis**: PRISMA no puede configurarse como **primer** procesador porque el código de GP está hardcodeado como paso previo obligatorio — hoy en día es obligatorio dar de alta primero en GP y luego (opcionalmente) en PRISMA; el workaround documentado en el ticket es crear la configuración manualmente en base y simular que GP habilitó PRISMA. Esta restricción sigue vigente incluso con la Epic cerrada (ver §1.1bis).
- **Bloqueo activo al momento del backfill original**: los nuevos endpoints v2 de alta de comercio exigían el campo `fecha de nacimiento del titular` en ambientes bajos — bloqueaba las pruebas de alta de comercios con canal POS en QA/STG. Sin confirmación de si sigue bloqueando a la fecha del cierre de Epic (2026-09-18).

### 1.1bis Cierre del Epic "POS con PRISMA: Admin" (AD-430) — confirmado 2026-09-18

> Fuente: `/idea_prd` (PRD-70, POS con PRISMA) — barrido directo de los 15 tickets de la Epic AD-430 en Jira (`bindpsp.atlassian.net`), incluidos `fixVersion` publicada y comentarios de cierre de cada historia. Capturado 2026-09-18.

De los 15 tickets que componen la Epic, la gran mayoría ya está en Producción, con **2 defectos abiertos** y **una pieza de deuda técnica sin iniciar**.

**Qué se confirmó como entregado (verificado por `fixVersion` publicada, no solo por el estado de Jira):**
- **Configuración por defecto a nivel Entidad y habilitación a nivel Comercio** (los dos tickets que motivaban la nota "bloqueada"), más el flujo de cobro adaptado a tomar los valores parametrizados: en Producción desde el **2026-06-24** (versión AD 70.1).
- **Jerarquía de reglas de pago y promociones entre Comercio y Entidad**: en Producción desde el **2026-08-03** (versión AD 71). Resuelve el caso donde un comercio tenía reglas propias de promociones pero ninguna de procesador, y el pago fallaba en vez de escalar a buscar el procesador en la Entidad padre. Resolución independiente por tipo de regla: `ReglasFinales.Procesador = Comercio.Procesador ?? Entidad.Procesador`, igual para promociones — un comercio puede heredar una regla y tener la otra propia al mismo tiempo.
- **Devolución con el mismo procesador que hizo el cobro original**: en Producción desde el **2026-08-31** (versión AD 72). Quedó bloqueada varias semanas en Jira porque no se podía probar en Staging (sigue sin permitir pagos/devoluciones de POS con Prisma) hasta validar directo en Producción. Regla de negocio: una devolución del mismo día en que se cobró se trata como anulación; una devolución de un cobro de un día anterior se trata como devolución propiamente dicha — misma distinción que ya regía para GP. **Deuda técnica reconocida por el propio desarrollo:** las devoluciones con Prisma envían el tipo de lectura de tarjeta como "MANUAL" fijo, sin distinguir CHIP/BAND/CONTACTLESS como sí hace el proceso de pago — ya existe el enumerador necesario, falta aplicarlo también acá.
- **Habilitar un comercio para operar exclusivamente con Prisma ("solo Prisma"), sin convivencia obligatoria con GP** (la Etapa 2 de §1.1, antes diferida sin ticket ni fecha): **terminó construyéndose y entregándose** en el mismo período (Producción desde el 2026-08-31, cierre formal del ticket el 2026-09-08). Durante el desarrollo se descubrió una dependencia no prevista: el mecanismo que asigna el número de serie de un POS a una caja en su primer login también filtraba exclusivamente por el procesador GP (código 2000) — sin corregirlo, un comercio "solo Prisma" no podría ni vincular su primer dispositivo POS. Producto (Pablo Gomes) amplió el alcance de la misma historia para incluir esa corrección. Sin deuda técnica asociada según el propio desarrollo.
- **Dos bugs de producción corregidos, no documentados hasta ahora:** (1) el alta de un canal POS con Prisma no creaba correctamente las reglas de negocio del comercio en el motor de reglas (`cardbusinessrules`) por cruzar mal las columnas de valor y código de comercio al insertar la especificación — corregido, en Producción desde el 2026-08-03; (2) cambiar el orden de prioridad entre GP y Prisma en un comercio ya habilitado dejaba el canal POS en estado de error ("GP: Error al dar de alta el subcomercio") — corregido, en Producción desde el 2026-08-31, con advertencia del propio desarrollo de que "el código que maneja altas y modificaciones para GP sigue estando lejos de lo ideal".

**Qué sigue sin resolver a la fecha de esta ingesta (2026-09-18):**
- **2 defectos abiertos**, detectados después del último release (AD 72), sin comentario de seguimiento del proveedor: (1) cambiar la prioridad de procesadores de un comercio ya configurado (de GP a Prisma, mostrado en el Admin como "Payway") no aplica el cambio — el comercio queda con GP como principal; (2) un comercio que hereda el canal POS con Prisma como principal desde la Entidad falla su alta porque no se genera el CVU correspondiente.
- **Deuda técnica de fondo sobre el motor de reglas de pago:** el motor no trata el **Canal** de cobro (presencial, Botón Simple, QR, etc.) como dimensión propia de las reglas, del mismo modo en que sí distingue reglas de procesador de reglas de descuento. Hoy, para el procesador, el canal es solo un filtro puntual — si el comercio tiene una regla de procesador en un canal distinto al evaluado, se descarta entera en vez de convivir con la regla de la Entidad en el canal correcto; para los descuentos, el canal ni siquiera se mira en ese punto del código. Resultado: no existe hoy forma de que un comercio acumule, por ejemplo, una regla de procesador propia del canal presente con una regla de descuento heredada de otro canal. Solución propuesta (sin construir): cambiar la llave de resolución de "tipo de regla" a "tipo de regla + canal" — antes hace falta confirmar contra la base real qué valores tiene cargado el campo Canal, dado que la migración que restringe sus valores válidos (`PRESENTE`, `BOTON_SIMPLE`, `QR`, `QR_TARJETA`) corrió solo en el ambiente interno del proveedor, nunca en Staging ni Producción.
- Sin desarrollo iniciado, consistente con lo ya documentado: orquestación/failover automático entre procesadores (decisión explícita de no priorizarlo), gestión de la tabla de parámetros de Prisma por rubro desde el Admin, y alta en Prisma con identificador de adquirente distinto al de Bind PSP.

**Nota de nomenclatura:** en las pantallas del Admin, Prisma se muestra como "Payway" — varios defectos (incluidos los 2 abiertos) están redactados por QA usando ese nombre visible, no "Prisma". Cualquier guía de soporte/capacitación sobre esta configuración debería usar el mismo nombre que ve el usuario.

**Por qué importa más allá de este archivo:** el scope de la métrica de volumen por gateway (NSM #2) excluía el canal POS con la nota de que "ese proyecto no se shippeó" (`2_areas/direccion/north_star.md §2`, 2026-07-21) — este cierre confirma que la nota está desactualizada; ver gap capturado sobre esto, pendiente de permiso de usuario para tocar `north_star.md`.

### 1.2 Cierre de la épica y posible "Post con Prisma Plus" (2026-07-30)

> Fuente: reunión "Análisis COBRO" (2026-07-30), minuta Gemini.

La épica **"Post con Prisma"** (9 tickets en curso a esta fecha — no confundir con el conteo histórico de 18 tickets/~45 SP de la integración original documentada en §1) llegó al punto de cierre: el equipo decidió **cerrarla en su estado actual** y evaluar crear una segunda versión ("Post con Prisma Plus" o v2) para trasladar ahí los pendientes — en particular la **orquestación de procesadores** que quedó fuera del corte original. Sin fecha ni alcance formal todavía para la v2; queda priorizada para agosto 2026 en el roadmap del área (ver [`decisiones.md`](../../../2_areas/direccion/decisiones.md)).

Relacionado, en la misma reunión: **gestión de IDs de sitio (site IDs) de Prisma según el rubro del comercio** — se identificó el riesgo de asignar mal el site ID según rubro comercial (posible motivo de multas de Prisma); el plan es cargar una tabla de parámetros rubro→site ID y eventualmente exponerla en el Admin.

### 1.3 Deuda técnica de reglas Prisma/GP — decisión de pasar a parámetros de canal dinámicos (2026-08-20)

> Fuente: Reunión "Análisis COBRO" (2026-08-20), minuta Gemini. Invitados: Luciana Rudaz, Pablo Gomes, Nicolás Colón, Matías Alzogaray, Daniela Collia, Melisa Belpassi, Flavia Salmerón, Marcos Sánchez, Cristian Medina, Julieta Giménez (Fintexa).

**Deuda técnica confirmada:** el sistema convive con dos procesadores de pago (Prisma y GP) usando grupos de reglas de procesador mal estructurados para la coexistencia — genera problemas operativos al intentar operar con ambos simultáneamente (Daniela Collia, Fintexa). Este hallazgo complementa el modelo de 2 etapas ya documentado en §1.1 (Etapa 1: GP por defecto conviviendo obligatoriamente con PRISMA, deuda técnica reconocida) — ahora se define **cómo** resolver esa deuda.

**Decisión acordada (2026-08-20):** en vez de mantener grupos de reglas rígidos por procesador, el proceso pasará a tomar los valores de los **parámetros del canal** directamente — evita ciclos repetitivos de modificación de reglas cada vez que cambia algo. Alcance del ajuste aceptado: adaptar el proceso de lectura de parámetros, no rediseñar la estructura de reglas de cero.

**Acciones de seguimiento (no asignadas a Producto):** Daniela Collia (Fintexa) va a compartir el detalle de la deuda técnica de reglas con Nicolás Colón para que la cargue como ticket formal en el sistema de Bind PSP.

**Despliegue de un ticket de Prisma sin completar su configuración en el admin (misma reunión):** se decidió proceder con el despliegue pese a que la funcionalidad de configuración desde el panel administrativo (que permitiría seleccionar Prisma como procesador único, hoy el sistema habilita GP por defecto) no está terminada — Cristian Medina y Daniela Collia (Fintexa) confirman que el backend está preparado pero la interfaz de administración no permite esa configuración flexible. El ticket no cumple todos los requisitos de Definition of Done, pero se aprueba el despliegue para no atrasar el cronograma, dejando la limitación de la interfaz administrativa para abordar por separado. Es consistente con la limitación ya documentada en §1.1 de que Prisma no puede configurarse hoy como primer procesador (GP hardcodeado como paso previo obligatorio).

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

## 1.4 Decidir (no presencial) vs. Prisma (presencial) para tarjeta QR — parametrización distinta (2026-08-27)

> Fuente: reunión "Análisis COBRO" (2026-08-27, Daniela Collia/Fintexa, Pablo Gomes, Nicolás Colón). Continuación del análisis de tarjeta QR priorizado para la versión de septiembre — ver [boton_simple_2_0.md §8.1](boton_simple_2_0.md) para las definiciones de post-payments/terminal ID de la misma iniciativa.

Daniela Collia planteó que Decidir se usa para ventas no presenciales y Prisma para presenciales, y que ambos procesadores piden datos distintos:

- **Decidir**: solo requiere un identificador de sitio (**site ID**), descrito como un agrupador de establecimientos. En producción se usa habitualmente el código `00130250`, que agrupa establecimientos por marca de tarjeta — valor que no figura en la tabla de reglas de negocio de Prisma (`Business Rules`, processor ID 2003) que el equipo venía analizando.
- **Prisma**: requiere múltiples parámetros detallados — identificador de establecimiento e identificador de terminal, exigidos por MODO.

Al revisar el panel de administración (configuración de procesador), se confirmó la misma asimetría en el canal presente con Payway: Prisma pide terminal+establecimiento, Decidir opera principalmente con site ID + un terminal configurado como código de comercio. Hipótesis sin confirmar: el site ID actuaría como nivel de agrupación de establecimientos (ej. el rubro/MCC 5541 tiene un único comercio, mientras que el 4813 agrupa varios — 691 y 992).

Quedó pendiente para Nicolás Colón: unirse a la sesión de integración de Decidir para resolver las dudas, definir la configuración exacta (site ID / establishment ID) y contactar a Gonzalo Rivera para la información técnica que destrabe el desarrollo — ver `1_proyectos/tareas.md` T-010.

## Ver también

- [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) — mecánica de Centralizador y multiPSP en el canal QR (mismo concepto de orquestación multi-procesador).
- [wallet/lending_discovery.md](../wallet/lending_discovery.md) — iniciativa de crédito embebido del lado Wallet (discovery, nunca construida) — contrastar con DATA2000, que sí se construyó del lado POS.
- [validacion_bines_tarjetas.md](validacion_bines_tarjetas.md) — mecanismo de identificación/validación de BINs de tarjeta (antes §6 de este archivo, reclasificado 2026-09-14 por ser transversal a cualquier canal de tarjeta, no específico de POS).

---
*Última actualización: 2026-09-18 — `/context_merge`: cierre confirmado del Epic "POS con PRISMA: Admin" (AD-430, nueva §1.1bis) — la configuración self-service desde el Admin, marcada "en desarrollo/bloqueada" desde el backfill de 2026-07-13, en realidad está mayormente en Producción desde junio-agosto 2026.*
