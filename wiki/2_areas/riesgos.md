# Riesgos del Contexto Fijo — Bind PSP

> Riesgos que afectan a la plataforma o al negocio en general, no a un proyecto puntual — esos viven en la sección de riesgos de su propio `proyecto.md`. Compartido entre los tres PM/PO: **solo lo escribe `/context_merge`**. Cada PM aporta un riesgo de este alcance como item `tipo: riesgo` en `contexto_vivo/`.

## Capacidad del proveedor de infraestructura (Fintexa)

Dos reducciones de dotación consecutivas en el equipo de Fintexa asignado a Bind PSP (julio y agosto 2026 — Soporte, QA, SRE, Dev Wallet/Adquirencia/Mobile POS). Ver detalle en [3_recursos/arquitectura_sistema/relacion_con_fintexa.md](../3_recursos/arquitectura_sistema/relacion_con_fintexa.md).

## Seguridad — Ardid no aísla datos entre clientes (multi-tenencia)

Fintexa confirmó que Ardid no aísla datos entre organizaciones — clientes como Coto y BIN podrían ver operaciones ajenas entre sí. Sin fecha de resolución confirmada, del lado de Pentass. Ver [3_recursos/arquitectura_sistema/incidentes_de_plataforma.md §4](../3_recursos/arquitectura_sistema/incidentes_de_plataforma.md).

## Compliance — integridad de `LAVADOOPERACIONES` sin resolver

Conflicto de diseño abierto hace ~2 meses (a la fecha del hallazgo) sobre si la fuente de verdad del reporte antilavado a Worldsys/BCRA debe ser la tabla de comprobantes o de movimientos, y cómo tratar reversas. Bloquea desarrollo de Nicolás Colón. Ver [3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md §2](../3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md).

## PCI DSS del proveedor Fintexa — certificación sin confirmar en el texto narrativo del documento de arquitectura

La única mención de PCI DSS v4.0 Level 1 en el documento de arquitectura del proveedor es un diagrama; el texto narrativo y el resumen ejecutivo no lo listan entre los estándares de compliance. Ver [3_recursos/arquitectura_sistema/modelo_de_seguridad.md](../3_recursos/arquitectura_sistema/modelo_de_seguridad.md) y [gaps_y_preguntas.md](gaps_y_preguntas.md).

## Desalineación entre comisión facturada a la entidad y comisión real cobrada por el procesador

Si una configuración de comisión queda mal cargada en el sistema interno de Bind PSP y Soporte no lo detecta a tiempo, Bind PSP puede seguir facturando a una entidad/comercio con un arancel más bajo del real mientras el procesador (Coelsa u otro) le cobra a Bind PSP el arancel completo por cada transacción — la diferencia es pérdida neta directa, no solo un problema de UX/proceso. Precedente cuantificado (causa distinta, mismo patrón): pérdida de **$15.000.000 ARS en un solo mes**, sin fecha exacta ni detalle técnico registrado — solo como referencia de magnitud. Cualquier mecanismo de configuración de comisiones (convenios, arancel reducido/Coelsa, futuros orquestadores) debería incluir una forma de detectar automáticamente esta divergencia, no depender de que Soporte la note manualmente. Capturado 2026-08-20, sin ticket ni dueño de mitigación general asignado todavía.

## Saturación de la base de datos de impuestos por CUIT compartido entre entidades comerciales

La vista `RET_IIBB_REC_ACUM_LOTE` hace un `INNER JOIN` de `LIQ_IMP` contra `COMERCIO` por CUIT; como un mismo CUIT puede pertenecer a hasta ~200 sucursales/comercios distintos, cada transacción real se multiplica en el join (fan-out). Medido: 10 transacciones → 53 scans sobre `COMERCIO` y ~9,8M logical reads sobre `LIQ_IMP` (28,4 min reales); estimado a 500 transacciones → ~2.650 scans y ~490M logical reads (probablemente varias horas) — no ocurre en ambientes bajos por no tener ese volumen ni esa repetición de CUITs. Fintexa evalúa qué filtro agregar (acordado: filtro por código de comercio) sin romper la lógica de negocio. Ver detalle técnico en [3_recursos/detalle_productos/siscri/calculo_impuesto_online_qr.md §8](../3_recursos/detalle_productos/siscri/calculo_impuesto_online_qr.md) y [3_recursos/detalle_productos/agente_cobros_y_pagos/integracion_procesadores_pago.md](../3_recursos/detalle_productos/agente_cobros_y_pagos/integracion_procesadores_pago.md). Detectado 2026-08-20/21 (Julieta Gimenez/Ariel Profitti, Fintexa).

## Proyecto Servicios — continuidad de equipo y bloqueo de pruebas con tarjetas prepagas

Dos riesgos sobre el "Proyecto Servicios" (BPG/Pago Fácil, incorporado al pipeline de Wallet — ver [3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md §4](../3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md)): (1) **continuidad de conocimiento** — Pablo Serra (Fintexa) informó (2026-08-21) la baja del integrante identificado como quien más conocía el proyecto, sin plan de traspaso de conocimiento documentado; (2) **bloqueo de pruebas con tarjetas prepagas** (severidad media-alta, impacto directo en clientes) — el ambiente de staging no tiene tarjetas prepagas ni datos de prueba válidos provistos por Pago Fácil o el procesador Decidir, pese a rechazos recurrentes ya reportados por clientes; Andrea Orsini y Adriana Endzeliz gestionan con Decidir/Payway conseguir una tarjeta de prueba válida, sin fecha de resolución confirmada al 2026-08-25.

## Reprogramaciones reiteradas de pases a producción erosionan la confianza de clientes

En la reunión "Adquirencia V 72: Pre-Despliegue" (2026-08-27) se reprogramó el pase a producción para la noche del lunes 31/08 (12 tickets de QA con errores críticos detectados). Gonzalo Rivera expresó malestar propio y de los clientes ante los cambios constantes y postergaciones de fechas de implementación — genera **percepción de falta de profesionalismo** y afecta los avisos previos que las entidades ya comunicaron a sus propios clientes (caso citado: APIBank). El equipo reconoció la frustración pero sostuvo que posponer busca evitar errores críticos en producción; Melisa Belpassi (QA) señaló que ya había advertido la imposibilidad de llegar con los tickets y que su propuesta de coordinar documentación conjunta no se gestionó a tiempo — QA opera como cuello de botella por acumulación de tareas, con necesidad de reformular la coordinación entre equipos. Mitigación propuesta: calendario de lanzamientos anticipado desde la v73 (ver nota de reforma del ciclo de despliegues, pendiente de permiso explícito para `procesos/`).

## Multa de $75 millones por errores en pruebas de bloqueo de transacciones de Ardid

Confirmada una multa de **$75 millones** a Bind PSP originada por errores en las pruebas de bloqueo de transacciones de Ardid (motor antifraude) — transacciones que debían bloquearse no se bloquearon. Mencionada al pasar en la minuta de "Repaso Semanal líderes" (2026-09-01) como parte del diagnóstico que motivó la reforma del ciclo de despliegues (ver `2_areas/procesos/`, pendiente de permiso). El monto fue redactado en la minuta oficial (enviada a Fintexa/Tecnológica Financiera) por sensibilidad ante destinatarios externos, y se completó cruzando la minuta de Gemini de la misma reunión (interna). Sin confirmar la entidad que aplicó la multa, el ticket/versión de Ardid involucrado, ni si ya está resuelta. Señal de que Ardid quedó fuera del loop de coordinación de despliegues — el equipo sumó como acción incorporar a un referente de Ardid a las reuniones de coordinación (Hernán Clarich). Capturado 2026-09-02, confianza media (mención al pasar en ambas fuentes, sin ticket ni informe de causa raíz propio).

## Getnet deprecará su arquitectura actual de POS a fin de trimestre — afecta ~5% de la lectura de QR de Bind

Getnet (dispositivos POS provistos por Santander) reiteró que la migración a una nueva arquitectura, en curso desde el año pasado, tiene plazo estimado de adecuación para **fines de este trimestre**; al llegar esa fecha, la arquitectura actual queda deprecada y las operaciones que sigan dependiendo de ella se verían afectadas. Pablo Gomes estimó que esto podría afectar a un **~5%** de los QR que Bind lee actualmente (sin confirmar qué clientes puntuales dependen de esos dispositivos). Podría requerirse una versión intermedia de código QR para no perder capacidad de lectura. Mitigación: se irá levantando en las reuniones periódicas con Wallet (dos por semana) apenas haya definición adicional — clasificado con prioridad 1 interna para tenerlo en el radar, pero deliberadamente **sin fecha de resolución "confirmada"** en el tablero hasta tener más certeza. Capturado 2026-09-04 (reunión "Producto - Prioridades"), confianza baja (mail de un tercero reenviado, sin confirmación técnica propia del alcance).

## Getnet deprecará el circuito viejo de la Billetera Bind Pago como socio/APM — deadline duro 30/09

Getnet (vía Luisana Noguera, `productoqr@getnet.com.ar`) reclama desde el 2026-09-01 que la Billetera Bind Pago migre del circuito viejo al nuevo circuito tecnológico interoperable ("Interoperabilidad v6 BCRA") para poder seguir operando como medio de pago (APM/socio) dentro de su red de QR — es decir, para que un usuario de la billetera pueda seguir pagando escaneando un QR de un comercio afiliado a Getnet. Bind Pago ya completó una homologación técnica el 17/04 pero solo con pruebas manuales por Postman (confirmado por Alan Martínez, área técnica Bind); nunca hubo integración sistémica real, y el circuito viejo sigue en uso en producción.

**Postura de Getnet (reiterada, última el 03/09):** el circuito antiguo será deprecado "a finales de Q" sin comunicaciones adicionales — no está dispuesta a mantenerlo pese a los pedidos explícitos de Bind de conservarlo mientras se planifica el desarrollo. Escalamiento interno (03/09→04/09): Gonzalo Rivera (Team Leader Integraciones y Soporte) alertó que "nos vamos a quedar sin operar con Getnet"; Emma Vignoles confirmó fecha límite dura: **30/09**. Al 2026-09-05, Fintexa (Agustín Grau) ya levantó el ticket de análisis, asignado a Nico Pomponio — sin fecha de entrega estimada ni confirmación de que el desarrollo llegue a producción antes del 30/09. Especificación técnica completa (OAuth2 `client_credentials`, endpoints `/resolve`/`/orders`/`/payments`) en [3_recursos/detalle_productos/wallet/interoperabilidad_qr_getnet.md](../3_recursos/detalle_productos/wallet/interoperabilidad_qr_getnet.md).

**Posible superposición sin confirmar (marcada explícitamente, no resuelta por este merge):** existe un proyecto de producto activo, `1_proyectos/getnet_oauth2_resolve/` (Pablo Gomes, IDEA PRD-237, EN APROBACION), sobre Getnet migrando la autenticación de su API Resolve de `access_token` fijo a OAuth2 `client_credentials` — mismo proveedor, mismo endpoint `/resolve`, mismo deadline 30/09. No está confirmado si ambos hilos describen la misma migración de fondo (Bind Wallet leyendo/pagando QR de comercios Getnet) vista desde dos fuentes distintas (mail técnico a Integraciones vs. proyecto formal de PM), o si son dos alcances técnicos separados que coinciden en proveedor y ventana. **Pendiente de que Pablo Gomes y Nicolás Colón lo confirmen entre sí** — si es la misma migración, este riesgo debería consolidarse bajo el proyecto `getnet_oauth2_resolve/` en vez de quedar como riesgo general.

**Sin mitigación ni plan de contingencia confirmado** si el desarrollo no llega a tiempo — no hay definición de qué pasaría operativamente con los usuarios de Bind Pago si el circuito viejo se apaga el 30/09 sin el nuevo en producción. Capturado 2026-09-06 (Nicolás Colón), confianza alta.

## Ver también
- [gaps_y_preguntas.md](gaps_y_preguntas.md) — vacíos de información del contexto fijo, distinto de riesgos ya identificados.
- [tareas.md](tareas.md) — backlog operativo, no riesgos.

---
*Última actualización: 2026-09-07 — nuevo riesgo "Getnet deprecará el circuito viejo de la Billetera Bind Pago como socio/APM — deadline duro 30/09" (posible superposición sin confirmar con el proyecto `getnet_oauth2_resolve/`, ver nota en la propia entrada).*
*Última actualización anterior: 2026-09-07 — nuevo riesgo "Getnet deprecará su arquitectura actual de POS a fin de trimestre".*
*Última actualización anterior: 2026-09-02 — nuevos riesgos "Reprogramaciones reiteradas erosionan confianza de clientes" y "Multa de $75M por errores en pruebas de bloqueo de Ardid".*
*Última actualización anterior: 2026-08-27 — nuevos riesgos "Saturación de la base de datos de impuestos por CUIT compartido" y "Proyecto Servicios — continuidad de equipo y bloqueo de pruebas con tarjetas prepagas".*
*Última actualización anterior: 2026-08-20 — nuevo riesgo "Desalineación entre comisión facturada a la entidad y comisión real cobrada por el procesador".*
*Última actualización anterior: 2026-08-12 — Creación del archivo en la reestructuración PARA en cascada, consolidando 4 riesgos ya documentados en la wiki pero sin un lugar propio.*
