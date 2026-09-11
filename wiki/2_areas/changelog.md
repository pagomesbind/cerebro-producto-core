# Changelog de `2_areas/`

> Resumen corto de cada merge que tocó esta capa — qué cambió, sin el detalle (eso está en el archivo). **Solo lo escribe `/context_merge`**, una línea por archivo tocado, agrupadas por fecha de merge. Vive en el core y viaja con el espejo, así que se lee desde el install sin tocar el clon compartido. Rotación anual a `wiki/4_archivos/`.
>
> Distinto del manifiesto de cada merge (`manifiestos/YYYY-MM-DD.md` en el core): el manifiesto es el recibo operativo completo (qué items consumió, qué permisos pidió, qué contradicciones abrió) y lo lee `/context_pull`; esto es el resumen humano.

## 2026

### 2026-09-11 (pablo + nicolas)

- `direccion/iniciativas.md` — actualizadas 3 filas: PRD-202 (Jira resincronizado tras backlog drift, contrato v7.0); bajar-tiempos-pagos-qr (nuevo informe de tiempos post-despliegue de Keep IT Simple); onboarding_shared_kyc_worsis (novedad de Nicolás Colón — deadline duro 1/oct del directorio, monto en duda, segmentación ARDID sin resolver; `pm_destino: pablo`, ver sección propia del manifiesto).
- `direccion/decisiones.md` — 2 entradas nuevas: Confluence diferido como solución a límites de Jira, no contratado por licencia (pablo); contradicción sin resolver sobre el monto del límite operativo de personas jurídicas ($1.000 canon vs. $10.000 reportado en 2 reuniones independientes) — ambas versiones documentadas, sin elegir ganador.
- `gaps_y_preguntas.md` — 1 gap nuevo: contradicción del monto del límite operativo de personas jurídicas, escalado a Pablo Gomes/Compliance.
- `riesgos.md` — 2 riesgos nuevos: falta de controles en onboardings gestionados por el integrador Gallo (Terra Blockchain ya dado de baja); error de endpoint impide validar conciliación Cashout post W72.2 (Cencosud/Coto).
- Items en régimen D pendientes de permiso explícito del usuario (quedan `en_cola`, ver manifiesto `2026-09-11.md`): 13 items — 3 arrastrados de corridas anteriores + 10 nuevos (cronograma septiembre, corrección estado_actual, transcripción PNET no descargable, decisión Fintexa→Nicolás, 2 gaps de cliente sin ficha, La Virginia x2, ventana de comunicación de fechas, 2 gaps de cliente Biwi/Global Loan) — más 1 item sin producto dueño clasificable (API VATA de Modo).

### 2026-09-10 (pablo)

- `direccion/iniciativas.md` — actualizada 1 fila (PRD-66: causa raíz de la demora de QR confirmada en vivo con Provincia Net, plan de mitigación acordado); creada 1 fila nueva (PRD-247: vulnerabilidad Renaper Datos, discovery cerrado en Gate 2 como 🟡 Diferido, consolida las 2 novedades del 09-09 y 09-10 en una sola fila).
- `riesgos.md` — creado 1 riesgo nuevo: escalamiento de la contención de cola QR por crecimiento del segmento de clientes individuales de Provincia Net.
- Items en régimen D pendientes de permiso explícito del usuario (quedan `en_cola`, ver manifiesto): 5 arrastrados de corridas anteriores (decisión tickets Fintexa → `procesos/gestion_jira.md`; 3 gaps/conocimiento de cliente sin ficha → `clientes/log_clientes.md`/`casos_de_uso_clientes.md`; cronograma de despliegues septiembre → `procesos/`) + 1 nuevo (corrección de la restricción de capacidad hardcodeada → `direccion/estado_actual.md`, pablo).

### 2026-09-09 (pablo + nicolas)

- `direccion/decisiones.md` — creadas 5 decisiones nuevas: freeze de webhook de arancel neto de Adquirencia (pablo); freeze de webhook en el marco de Shared KYC/Worsis, alcance sin precisar (nicolas); límite operativo $1.000 para altas PJ sin documentación (nicolas); Bind PSP/BIN asume administración de la PCAB + apetito de riesgo GB/DinX (pablo); `/idea_us` exige revisión cruzada de reglas de negocio transversales + `/idea_estimate` suma Modo Proyecto (pablo).
- `direccion/oportunidades.md` — creadas 5 oportunidades nuevas (OP-021 a OP-025): Manteca como riel de pagos regionales (pablo); evaluación de riesgos formal pre-lanzamiento de producto (pablo); marco de gestión de reclamos (pablo); panel de visibilidad de APIs de Fintexa (pablo); proceso formal de desarrollo de productos (pablo) — las últimas 4 del assessment de auditoría del banco tras el fraude de Transferencias Pull.
- `riesgos.md` — actualizado el riesgo Getnet/circuito viejo (entrega a QA Externo confirmada 21/09, W73 reformulado sin correr el deadline 30/09, nicolas); creados 2 riesgos nuevos: Combi (15/09) sin compromiso de Ipsa + Mastercard Move (17/09) (pablo); dependencia de Techfin para la creación del saldo virtual sin control interno documentado (pablo).
- `direccion/iniciativas.md` — actualizadas 2 filas (PRD-66: investigación en curso sobre volumen PNET; PRD-202: PRD reescrito v7.0 + solution regenerado v2.0, hallazgo de PATCH sin priorizar); creadas 3 filas nuevas: cola_verificacion_manual, visibilidad_error_alta (ambas nicolas) y onboarding_shared_kyc_worsis (novedad de nicolas para pablo).
- `gaps_y_preguntas.md` — creados 2 gaps nuevos (abiertos por el propio merge): alcance de webhook congelado sin precisar; límite $1.000 PJ sin reconciliar contra tope UIF/ROS ya documentado.
- Items en régimen D pendientes de permiso explícito del usuario (quedan `en_cola`, ver manifiesto): 4 arrastrados de la corrida anterior (decisión tickets Fintexa, 2 gaps de cliente sin ficha, alta comitente La Virginia sin ficha) + 1 nuevo (cronograma de despliegues septiembre → `procesos/`, pablo).

### 2026-09-08 (pablo + nicolas)

- `riesgos.md` — creados 3 riesgos nuevos: capacidad de QA insuficiente frente a múltiples prioridad 1 (nicolas); segregación de fondos/cuenta operativa PSPCP (Com. "A" 7825) sin verificación explícita (pablo); reportes sistemáticos UIF RMTC/RTE (Res. 200/2024) sin evidencia de cobertura, ya con IDEA de discovery propia PRD-244 (pablo).
- `direccion/iniciativas.md` — creada 1 fila nueva: PRD-244 (reportes sistemáticos UIF RMTC/RTE, discovery) (pablo).
- Items en régimen D pendientes de permiso explícito del usuario (quedan `en_cola`, ver manifiesto): decisión "tickets Fintexa deben pasar por Nicolás Colón" (`procesos/gestion_jira.md`, nicolas); 2 gaps de cliente sin ficha en `clientes/log_clientes.md` ("GCT"/posible GST, y "Tienda Nube"/"Pago Nube", nicolas).

### 2026-09-07, segunda corrida (pablo + nicolas)

- `direccion/decisiones.md` — creadas 2 decisiones nuevas: IDEA de Jira desde el arranque del discovery (2026-09-07) y reforma del ciclo de despliegues a quincenal con Release Candidates (2026-09-01, contradice `procesos/publicaciones_mensuales.md`); creada 1 decisión nueva: Getnet impone migración OAuth2 de su API Resolve, deadline 30/09 (2026-09-04, con corrección del PM del 2026-09-07) (pablo).
- `direccion/iniciativas.md` — actualizada 1 fila (alias_cvu_checkout: creación completa en Jira, PRD-239); creadas 2 filas nuevas: PRD-238 (gestión de riesgo de fraude, Com. "A" 8471/8473 BCRA) y getnet_oauth2_resolve (migración OAuth2 de Getnet, PRD-237) (pablo).
- `riesgos.md` — creado 1 riesgo nuevo: Getnet deprecará el circuito viejo de la Billetera Bind Pago como socio/APM, deadline 30/09 — con nota de posible superposición sin confirmar con `getnet_oauth2_resolve/` (nicolas).
- `3_recursos/cumplimiento_normativo/gestion_riesgo_fraude_bcra.md` — creado: Comunicaciones "A" 8471 y 8473 del BCRA (pablo).
- `3_recursos/detalle_productos/wallet/interoperabilidad_qr_getnet.md` — creado: especificación técnica OAuth2 del circuito interoperable QR de Getnet (nicolas).
- `3_recursos/arquitectura_sistema/api_bank/` — módulo nuevo, 11 archivos: relevamiento completo de la API pública de Banco Industrial (pablo).
- `3_recursos/datos/datos_metricas_semanales/` y `log_metricas_semanales.md` — reemplazados con el store de la semana 202636 (pablo).
- `3_recursos/datos/metricas_semanales.md` — creada entrada semana 202636 (pablo).
- `clientes/casos_de_uso_clientes.md` — actualizadas 8 fichas: Maxiconsumo, Global 66 (pablo+nicolas), La Virginia, Peak Travel/Terramundi (pablo+nicolas), RIPSA, Depay, INTER, OCTAGON (pablo + nicolas).
- `gaps_y_preguntas.md` — creados 4 gaps nuevos: PedidosYa sin ficha en log_clientes.md, Pago Fácil/Western Union sin ficha en log_clientes.md, criterio de hotfix sin definir, tensión publicaciones_mensuales.md vs. reforma quincenal (pablo + nicolas).
- `procesos/criterios_de_priorizacion.md` — nueva sección: criterio de clasificación Build vs. Bau (pablo + nicolas).
- `procesos/comunicacion_de_lanzamientos.md` — nueva sección: formato estándar del contenido de cada aviso (pablo + nicolas).
- `procesos/analisis_de_riesgo_de_despliegue.md` — nueva sección: gap de criterio hotfix vs. despliegue estándar (nicolas).
- `procesos/publicaciones_mensuales.md` — nota de contradicción con la reforma quincenal (protocolo de contradicción aplicado, ver gap) (pablo).
- `overview_empresa/overview_empresa_general.md` — nueva sección: roles adquirente vs. agrupador (pablo).

### 2026-09-07, primera corrida (pablo + nicolas)

- `direccion/oportunidades.md` — creadas 2 filas nuevas: OP-019 (Agente de Cobros y Pagos sin consulta de cuenta por CBU/CVU/alias, paridad con Wallet) y OP-020 (migrar transferencias de Link a Coelsa para reducir tasa de rechazo) (pablo + nicolas). 1 item de nicolas (`oportunidad-refactor-segmentos-wallet-autonomia-clientes`) evaluado como duplicado de OP-017 ya existente (mismo hecho, misma reunión) — no se creó fila nueva.
- `direccion/iniciativas.md` — actualizadas 2 filas: PRD-202 (contrato v6.0 aplicado — modelo de palancas simplificado, renombres, precisión de alcance) y bajar-tiempos-pagos-qr (reunión Global66 acota causa de discrepancia de medición, nuevo hallazgo de transferencias no acreditadas) (pablo + nicolas).
- `tareas.md` — creada 1 fila nueva (T-108): desarrollar skill de automatización de comunicaciones de novedades de producto (nicolas).
- `direccion/decisiones.md` — creada 1 decisión nueva: exclusión del ticket Siscri (AD-1383/PRD-205) de la versión D73 (nicolas).
- `riesgos.md` — creado 1 riesgo nuevo: deprecación de la arquitectura actual de POS de Getnet a fin de trimestre, ~5% de la lectura de QR de Bind (nicolas).

### 2026-09-03 (pablo + nicolas)

- `direccion/oportunidades.md` — creadas 2 filas nuevas: OP-017 (autonomía de clientes sobre segmentos de Wallet, caso Credicuotas) y OP-018 (Onboarding no expone motivo de rechazo por totalizadores) (pablo).
- `direccion/iniciativas.md` — actualizadas 2 filas existentes (PRD-223: fecha de Etapa 2 sin confirmar, propuesta de demo en Staging; bajar-tiempos-pagos-qr: informe entregado a Depay) y creadas 2 filas nuevas (PRD-208: confirmado en alcance v73; PRD-116: hallazgo que reduce esfuerzo, servicio ya integrado) (pablo).
- `gaps_y_preguntas.md` — creado 1 gap nuevo (cliente "PG" en estimación de volumen BPG sin ficha); actualizado 1 gap existente (contradicción TPay vs. BSF/Global66 — nueva evidencia que refuerza el lado Global66, sin cerrar la pregunta) (pablo).
- `direccion/decisiones.md` — creada 1 decisión nueva: migración de transferencias salientes de CBU larga de Link a Coelsa (piloto) (pablo).

### 2026-09-02 (pablo + nicolas)

- `direccion/iniciativas.md` — creada 1 fila nueva (bajar-tiempos-pagos-qr, con nota de atribución en disputa TPay vs. BSF/Global66) y actualizadas 3 filas (PRD-202: descripción de IDEA refrescada; PRD-223: staging confirmado en fecha; comercios_mayoristas: demo real ejecutada, 3 socios confirmados) (pablo + nicolas).
- `riesgos.md` — creados 2 riesgos: reprogramaciones reiteradas erosionan confianza de clientes (nicolas); multa de $75M por errores en pruebas de bloqueo de Ardid (pablo).
- `gaps_y_preguntas.md` — creados 2 gaps nuevos (contradicción TPay vs. BSF/Global66 sobre el cliente que motivó el ajuste de tiempos QR; TPay sin ficha en `log_clientes.md`); actualizado 1 gap existente (contrato real de Convenios — nueva evidencia confirmatoria, sin cerrar la pregunta) (pablo + nicolas).
- `direccion/oportunidades.md` — sin cambios: 1 item (`oportunidad-alias-cbu-checkout-boton-simple-pago-facil`, nicolas) evaluado como duplicado de OP-016 ya existente, no se creó fila nueva.

### 2026-08-31 (pablo + nicolas)

- `direccion/decisiones.md` — creada 1 entrada: migración del detector de "caída de cliente" de `/sync_metrics` a metodología de ventana móvil 4×4 semanas (pablo).
- `direccion/oportunidades.md` — creada 1 fila (OP-016): alias de CVU visible en checkout de transferencia de Botón Simple 2.0 (pablo).
- `direccion/iniciativas.md` — creada 1 fila nueva (alias_cvu_checkout) y actualizadas 2 filas (PRD-202: 2 novedades; convenios_configuracion: 2 novedades) (pablo).
- `gaps_y_preguntas.md` — creado 1 gap nuevo (guia_cvu.md sin tope anual de modificaciones de alias, señalizado para `/sync_web`); actualizados 4 gaps existentes (dim_collectors, mapeo confirmado/reconfirmado; La Virginia, sexta semana; Pago Fácil sin ficha, ahora con evidencia de producción); cerrado y rotado a `4_archivos/gaps_resueltos.md` el gap de Terra Blockchain/Sucredito (baja por Compliance) (pablo + nicolas).
- `4_archivos/gaps_resueltos.md` e `index.md` — creados (primera rotación de un gap resuelto en el repo compartido).
- `overview_empresa/overview_empresa_general.md` — actualizado: nueva sección sobre la venta del negocio de banca minorista de Grupo BIND a Banco Patagonia (permiso explícito del usuario, régimen D) (pablo).
- `procesos/comunicacion_de_lanzamientos.md` — actualizado: nueva sección sobre la propuesta (sin decisión formal) de calendario de ventanas de despliegue anticipado (permiso explícito, régimen D) (pablo).
- `clientes/patrones_transversales.md` — actualizado: nueva sección 5 (notas de identidad de cliente) — Pago Fácil/Western Union/SEPSA son el mismo grupo comercial (permiso explícito, régimen D) (pablo).

### 2026-08-27 (pablo + nicolas)

- `direccion/decisiones.md` — creadas 2 entradas: prioridades de Producto de Cobro/Adquirencia para septiembre 2026 (fusión de 2 items del mismo hecho, Pablo Gomes + Nicolás Colón), y alcance inicial de pagos de servicios BPG (solo botón de pago, sin saldo de wallet).
- `direccion/oportunidades.md` — creadas 6 filas (OP-010 a OP-015): funcionalidades POS/Botón pedidas por Andesmar, rediseño de convenios entidad→comercio, pago de servicios con saldo de wallet de terceros, ecosistema financiero para cámara de supermercados mayoristas, fix de resiliencia de alias CVU (apibank/Coelsa), integración con Cobros con Transferencia (CCT) de Coelsa.
- `direccion/iniciativas.md` — actualizada 1 fila (PRD-147, novedad ZIP consolidado Worldsys) y creadas 6 filas nuevas (PRD-66, PRD-216, comercios_mayoristas con 2 novedades, asignacion_alias_cvu con 2 novedades, convenios_configuracion, PRD-223).
- `riesgos.md` — creados 2 riesgos: saturación de BD de impuestos por CUIT compartido (agente_cobros_y_pagos/siscri), y Proyecto Servicios (continuidad de equipo + bloqueo de pruebas con tarjetas prepagas).
- `gaps_y_preguntas.md` — creados 5 gaps: doc vs. real de `GET /CuentaCorriente` (datosOperacion), Red Link 404 sin dueño de producto identificado, contradicción de prioridad de desarrollo Onboarding (PF/PJ/menores), Epic AD-8 no funciona como documenta el canon, contrato real de API de Convenios contradice documentación previa.
- `clientes/casos_de_uso_clientes.md` — actualizadas 4 fichas: CREDICUOTAS (pedido de 2do factor), GRUPO SLOTS - Jugadon (alerta por cambio de categorización de webhook CBU Collect), COTO CICSA (fix de impuestos QR, semáforo amarillo), ARCOS DORADOS (fix de orden de productos al leer QR, con permiso explícito del usuario).
- `procesos/comunicacion_de_lanzamientos.md` — creado (con permiso explícito del usuario): acuerdo de canal estándar de mail interno para anunciar lanzamientos de producto.
- `procesos/index.md` — actualizado, sumada fila del archivo nuevo.

### 2026-08-21 (pablo)

- `direccion/decisiones.md` — creada 1 entrada con contradicción sin resolver (orquestador de configuración de entidades vía API: ¿decisión de roadmap vigente o no? — dos versiones del mismo PM, escaladas).
- `gaps_y_preguntas.md` — creado 1 gap (contradicción del orquestador de API, ver arriba).
- `direccion/oportunidades.md` — creada 1 fila (OP-009, onboarding propio como producto de marca blanca).
- `direccion/iniciativas.md` — creada 1 fila (PRD-214, primer discovery formal — dimensionamiento de stock actualizado y bifurcación de arquitectura SharedKYC vs. integración directa).
- `riesgos.md` — creado 1 riesgo (desalineación entre comisión facturada a la entidad y comisión real cobrada por el procesador).
- `clientes/casos_de_uso_clientes.md` — actualizada ficha de OCTAGON (cronología: demo de onboarding propio a Octagon y Compliance de Banco Industrial, con permiso explícito del usuario).

### 2026-08-19 (pablo)

- `gaps_y_preguntas.md` — creado 3 gaps (MCC4829 VISA, backfill AD Portal 2.0, dim_collectors sin orden de columnas), actualizados 2 (La Virginia, Terra Blockchain — tercera semana consecutiva de cada patrón).
- `direccion/iniciativas.md` — creado, primeras 2 filas (PRD-147, PRD-202); PRD-147 actualizada con la novedad del 2026-08-19 (problem statement v2.0, sin decisiones/gaps nuevos).
- `direccion/decisiones.md` — creada 1 decisión (liderazgo de gestión de proyecto de Onboarding pasa a Soluciones Andinas — item duplicado de 2 fuentes, fusionado en una sola entrada).
- `tareas.md` — creada 1 tarea (T-107, renovación de contrato de Figma).
- `overview_empresa/overview_equipo.md` — actualizado (nueva Gerente de Operaciones Mariana Nadalin + cronograma presencial Fintexa).
- `CLAUDE.md` (raíz del repo, no `2_areas/` pero mismo régimen de permiso) — actualizado: se suma `riesgos.md` como archivo lazy de proyecto/subproyecto en `1_proyectos/`, con el mismo patrón que `gaps.md`/`decisiones.md` (decisión ya aprobada por el usuario en sesión previa 2026-08-18).
