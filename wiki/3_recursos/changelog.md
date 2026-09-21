# Changelog de `3_recursos/`

> Resumen corto de cada merge que tocó esta capa — qué cambió, sin el detalle (eso está en el archivo). **Solo lo escribe `/context_merge`**, una línea por archivo tocado, agrupadas por fecha de merge. Incluye los items `tipo: dato` aplicados por copia a `datos/`. Vive en el core y viaja con el espejo, así que se lee desde el install sin tocar el clon compartido. Rotación anual a `wiki/4_archivos/`.
>
> Distinto del manifiesto de cada merge (`manifiestos/YYYY-MM-DD.md` en el core): el manifiesto es el recibo operativo completo y lo lee `/context_pull`; esto es el resumen humano.

## 2026

### 2026-09-21 (nicolas) — corrida automática (scheduled task, sin usuario presente)

- `detalle_productos/adquirencia/boton_simple_2_0.md` — nueva §11.1: criterio de saneamiento de `pago_unico` cerrado y `pago_unico=1` obligatorio para Botón Simple 2.0 confirmado en AD V73, caso FAVACARD (2.562 accounts) (nicolas).
- `detalle_productos/agente_cobros_y_pagos/masividad_generacion_qr.md` — resuelto el debate abierto de "colas diferenciadas por cliente": gestión inteligente de cola por umbral de 200 req/min implementada en AD V73 (nicolas).
- `detalle_productos/adquirencia/desconocimientos_de_tarjeta.md` — archivo nuevo: extraído de `devoluciones_y_contracargos.md §0` por umbral de tamaño; suma la separación de desconocimientos/devoluciones en PDF y liquidación confirmada para AD V73 (nicolas).
- `detalle_productos/adquirencia/devoluciones_y_contracargos.md` — §0 reemplazada por puntero a `desconocimientos_de_tarjeta.md`.
- 1 item duplicado (bug de zona horaria GMT-3 en webhook QR, nicolas) marcado `ingestado` sin reescritura — ya cubierto por el item equivalente de Pablo ingerido el 2026-09-18.
- Items en régimen D pendientes de permiso explícito del usuario (quedan `en_cola`, ver manifiesto `2026-09-21.md`) — backlog sin cambios este merge, 20 items.

### 2026-09-18 (pablo + nicolas) — corrida automática (scheduled task, sin usuario presente)

- `detalle_productos/ardid/integracion_con_productos_bind.md` — nueva §18: identificación de transacciones ante Ardid por `PaymentId` de Botón Simple, no por el ID interno de Cobro (nicolas).
- `detalle_productos/adquirencia/devoluciones_y_contracargos.md` — §0: contrato técnico del endpoint de "desconocimiento" (`POST /api/v1/Transactions/refund`, confianza Verbal, nicolas); nueva §5: regla de devolución R por T (ventana de un mes, presión de clientes institucionales, pablo).
- `detalle_productos/adquirencia/pos_multiadquirencia.md` — nueva §1.1bis: cierre confirmado del Epic "POS con PRISMA: Admin" (AD-430) — la mayoría de la configuración self-service ya está en Producción desde junio-agosto 2026, corrige el estado "bloqueada" del backfill de julio (pablo).
- `detalle_productos/adquirencia/webhooks_y_notificaciones.md` — nueva sección: bug de zona horaria en el webhook de pagos QR (falta desfase GMT-3 desde el 31/08, decisión pendiente, pablo).
- `detalle_productos/adquirencia/mecanica_qr_coelsa.md` — nueva subsección: mecánica de split (débito/crédito automático) y falla reproducida en Homologación para PCP 531/532, escalada a Coelsa (pablo).
- `detalle_productos/onboarding/onboarding_personas_juridicas.md` — nueva §8.1: detalle funcional real de la consola de referencia "AVA Compliance" (pablo); nueva §9: estructura real de la pantalla de solicitud en el backoffice (pablo).
- `arquitectura_sistema/nfr_y_slas.md` — nueva §3: iniciativa en discovery para exponer salud/latencia de APIs a clientes vía API nueva de Kipi en el APIM (pablo).
- Items en régimen D pendientes de permiso explícito del usuario (quedan `en_cola`, ver manifiesto `2026-09-18.md`).

### 2026-09-16 (pablo + nicolas) — corrida automática (scheduled task, sin usuario presente)

- `cumplimiento_normativo/reporteria_worldsys_bcra.md` — actualizado §2: criterio de integridad de `LAVADOOPERACIONES` (comprobantes vs. reversas) resuelto, entra en vigencia 2026-10-01 (nicolas).
- `datos/log_performance_desarrollo.md` — reemplazado byte a byte: export histórico consolidado de tickets (oct'25-ago'26), 942 tickets / 2.891 SP acumulados (pablo, `/dashboard_delivery`).
- `datos/log_costos_desarrollo.md` — reemplazado byte a byte: sumado stock de horas jul'26 y ago'26 (pablo, `/dashboard_delivery`).

### 2026-09-15 (pablo + nicolas) — corrida automática (scheduled task, sin usuario presente)

- `detalle_productos/adquirencia/validacion_bines_tarjetas.md` — archivo nuevo: mecanismo transversal de identificación de BINs de tarjeta — investigación Fintexa (mail 2026-05/08), causa raíz confirmada (6 vs. 8 dígitos), discovery completo PRD-251 (cruce BIN a BIN, bug de datos en override a Prepaga) (pablo); reclasificación de `pos_multiadquirencia.md §6` a este archivo por ser transversal, no específico de POS.
- `detalle_productos/adquirencia/pos_multiadquirencia.md` — actualizado: §6 removido (contenido movido a `validacion_bines_tarjetas.md`), agregada referencia cruzada.
- `detalle_productos/adquirencia/boton_simple_2_0.md` — actualizado: referencia cruzada a `validacion_bines_tarjetas.md` (canal de mayor impacto por volumen hoy).
- `detalle_productos/wallet/crossborder_manteca_billetera_internacional.md` — archivo nuevo: billetera internacional crossborder vía Manteca, casos Tienda Nube/Despegar, propiedad de PM sin confirmar (nicolas).
- `detalle_productos/wallet/organizaciones_y_configuracion.md` — actualizado: §0.1, avance de actualización masiva de domicilios faltantes (491.495 cuentas) sobre el gap normativo de CPA ya documentado (nicolas).
- `detalle_productos/wallet/transferencias_red_interna.md` — actualizado: §4, uso indebido del comprobante de transferencia interna por el cliente Copel (nicolas).

### 2026-09-14 (pablo) — corrida automática (scheduled task, sin usuario presente)

- `datos/metricas_semanales.md` — reemplazado byte a byte: entrada de la semana 202637 antepuesta al histórico (pablo, `/sync_metrics`).
- `datos/datos_metricas_semanales/*.csv` (9 archivos: dim_collectors, dim_entidades, dim_organizaciones, fact_comercios, fact_cuentas, fact_operaciones, fact_transacciones, fact_transferencias_agente_cobro, semanas) — reemplazados byte a byte con el store acumulado tras la ingesta de la semana 202637 (pablo, `/sync_metrics`).

### 2026-09-11 (pablo + nicolas)

- `detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md` — actualizado: 5ª línea de exploración, cola de QR exclusiva por cliente para Provincia Net propuesta por Arquitectura, complementaria a la investigación ya en curso (pablo).
- `detalle_productos/adquirencia/coelsa_nueva_api_comercio_cbu_cvu.md` — archivo nuevo: nueva API "Comercio" de Coelsa (ABM unificado con CBU/CVU), no integrada aún por Bind (pablo).
- `detalle_productos/adquirencia/coelsa_qr_catalogo_apis_tecnico.md` — archivo nuevo: catálogo de endpoints/códigos de error/Notification Push/firma EMVCo de la API QR de Coelsa, desdoblado de `mecanica_qr_coelsa.md` por umbral de fisión (pablo).
- `detalle_productos/adquirencia/mecanica_qr_coelsa.md` — actualizado: seguimiento post-despliegue de tiempos de PagosQR y referencias cruzadas a los 2 archivos nuevos (pablo).
- `detalle_productos/adquirencia/boton_simple_2_0.md` — actualizado: icono de confirmación confuso en Link Botón 2.0, clasificado como mejora técnica (nicolas).
- `detalle_productos/adquirencia/pagos_fx_portal_beneficiarios.md` — actualizado: MVP mayormente en QA externo salvo alta de beneficiarios (nicolas).
- `detalle_productos/adquirencia/index.md` — actualizado: filas de los 2 archivos nuevos y changelog interno.
- `detalle_productos/wallet/coelsa_cvu_api_referencia.md` — archivo nuevo: referencia técnica completa de la API CVU de Coelsa (PSP→Cuenta Recaudadora→CVU, screening, Comercios CVU, SFTP masivo, payloads literales) (pablo).
- `detalle_productos/wallet/coelsa_debin_api_referencia.md` — archivo nuevo: referencia técnica de la API DEBIN de Coelsa (auth, ambientes, API Bancos, transferencia pull JWT, contracargo, scoring) (pablo).
- `detalle_productos/wallet/coelsa_debin_api_payloads.md` — archivo nuevo: anexo de payloads reales de DEBIN, desdoblado de la referencia por umbral de fisión (pablo).
- `detalle_productos/wallet/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: Global 66, reactivar CVU eliminada crea CVU nueva por tratarse de cuentas migradas (nicolas).
- `detalle_productos/wallet/index.md` — actualizado: filas de los 2 archivos nuevos y changelog interno.
- `cumplimiento_normativo/coelsa_cpf_central_prevencion_fraude.md` — archivo nuevo: Central de Prevención de Fraude de Coelsa (base compartida del ecosistema, API REST, RabbitMQ) (pablo).
- `cumplimiento_normativo/coelsa_prevent_scoring_y_on_hold.md` — archivo nuevo: COELSA.PREVENT (scoring, umbrales de rechazo, servicio ON HOLD) (pablo).
- `cumplimiento_normativo/identificacion_personas_juridicas_vinculados.md` — actualizado: documentación exigida por BCRA para Wallet Data Service (nicolas).
- `cumplimiento_normativo/index.md` — actualizado: filas de los 2 archivos nuevos.
- `detalle_productos/portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: ticket histórico AD132, roles de usuario desaparecían por caché+endpoint recursivo, ya aprobado su desarrollo (nicolas).
- `detalle_productos/ardid/integracion_con_productos_bind.md` — actualizado: falta de segmentación automática de personas jurídicas por CUIT, discovery sin resolver (nicolas).
- `detalle_productos/ardid/despliegues_y_operacion.md` — actualizado: seguimiento post-despliegue del fix de estados de tarjetas, solución temporal en Mongo (nicolas).
- `detalle_productos/agente_cobros_y_pagos/masividad_generacion_qr.md` — archivo nuevo: arquitectura secuencial de generación masiva de QR, tiempos medidos, debate de colas diferenciadas (nicolas).
- `detalle_productos/agente_cobros_y_pagos/index.md` — actualizado: fila del archivo nuevo.
- `detalle_productos/portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: falta de devoluciones parciales, solo disponible desde el Admin (nicolas).
- `arquitectura_sistema/integraciones_externas.md` — actualizado: registro de la primera ingesta completa de documentación pública de Coelsa (baseline de changelog para futuras ingestas) (pablo).
- Items pendientes de permiso explícito (régimen D) o sin producto dueño claro: quedan `en_cola` — ver manifiesto `2026-09-11.md`.

### 2026-09-10 (pablo)

- `detalle_productos/adquirencia/automatizacion_creacion_masiva_qr.md` — archivo nuevo: mecánica técnica completa (SFTP→ETL→SP Orquestador→webhook) de la creación masiva de QR de Provincia Net, en producción desde 2026-08-13.
- `detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md` — actualizado: causa raíz confirmada directamente por Ingeniería de Bind y Provincia Net (cola única compartida + retry storm de reintentos), plan de mitigación corto/largo plazo, líneas de exploración nuevas, contexto de negocio/crecimiento de Provincia Net.
- `detalle_productos/adquirencia/index.md` — actualizado: fila nueva del archivo de mecánica, nota ampliada del incidente.
- `cumplimiento_normativo/identificacion_personas_fisicas_cvu.md` — actualizado: 4ta DDJJ obligatoria (cooperación tributaria internacional OCDE/CRS + FATCA, §4/§4bis/§5), confianza subida para los puntos ya confirmados contra fuente primaria BCRA (1.3, 4.13.1.1).
- `cumplimiento_normativo/index.md` — actualizado: nota de contenido del archivo de arriba.
- Item `contexto_fijo_correccion_restriccion_capacidad_estado_actual` (pablo) — régimen D (`direccion/estado_actual.md`), queda `en_cola` pendiente de permiso explícito del usuario (ver manifiesto).

### 2026-09-09 (pablo + nicolas)

- `detalle_productos/adquirencia/incidente_qr_masivo_provincia_net.md` — archivo nuevo: saturación de cola de generación de QR por carga masiva de Provincia Net, decisión de convivencia de dos sistemas, y análisis de datos propio del PM que confirma el volumen de PNET pero deja la causa raíz de la ventana de reclamos sin confirmar (pablo).
- `detalle_productos/adquirencia/index.md` — actualizado: fila nueva del archivo de arriba.
- `detalle_productos/portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: búsqueda por referencia en el Admin solo exacta, no parcial (workaround vía CSV) (nicolas).
- `detalle_productos/ardid/integracion_con_productos_bind.md` — actualizado: nueva §14.5, confirmación de qué entra en W73 (mapeo de rechazo, habilitación global, rechazo por caída) y qué queda afuera (state monitor, pasa a W74), con riesgo funcional explícito (nicolas).
- `detalle_productos/wallet/interoperabilidad_qr_getnet.md` — actualizado: alcance confirmado dentro de W73, entrega a QA Externo 21/09 (nicolas).
- `detalle_productos/servicios/pago_facil_mantenimiento.md` — actualizado: §5, seguimiento semanal del Piloto Productivo Bind-SEPSA (nuevas entidades UAT, puntos operativos resueltos/en curso) (nicolas).
- `detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md` — actualizado: nueva §6.1, prueba de vida y concordancia facial (face match) son dos validaciones biométricas distintas, la norma exige ambas (pablo).
- Item `cumplimiento_bcra_com_8471_fraude` (pablo) procesado sin escritura — contenido ya cubierto en profundidad por `cumplimiento_normativo/gestion_riesgo_fraude_bcra.md` (mergeado 2026-09-07).

### 2026-09-08 (pablo + nicolas)

- `detalle_productos/wallet/conciliacion_y_totalizadores.md` — actualizado: nueva §8 (conciliación Coelsa ampliada a tipo CAS + corrección de cuadraturas por saldos en FCI, La Virginia/Coppel) (nicolas).
- `detalle_productos/agente_cobros_y_pagos/devoluciones_y_contracargos.md` — archivo nuevo: bug de contracargos de colectores (Pago Fácil) rechazados por validación de ID de caja vs. ID de colector (nicolas).
- `detalle_productos/agente_cobros_y_pagos/index.md` — actualizado: fila del archivo nuevo.
- `detalle_productos/onboarding/hallazgos_operativos_historicos.md` — actualizado: nueva sección, decisión de no priorizar mejoras de lectura de QR/código de barra (nicolas).
- `detalle_productos/adquirencia/mecanica_qr_coelsa.md` — actualizado: Parte 4, confirmación de que Coelsa calcula el 21% de IVA sobre la comisión del webhook de QR de forma automática y obligatoria (nicolas).
- `detalle_productos/adquirencia/boton_simple_2_0.md` — actualizado: nueva §8.2, integración MODO (QR Tarjeta) completada + requerimiento FAVACARD (PRD-235/ticket 1512) ratificado en máxima prioridad (nicolas).
- `detalle_productos/adquirencia/pagos_fx_portal_beneficiarios.md` — actualizado: nueva §7, estado de QA de Pagos FX tras demora atribuida a Mastercard (nicolas).
- `detalle_productos/adquirencia/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: nuevo hallazgo, Provincia Net incidente crítico sin resolver (ticket 1676/DAD-2943) y decisión de mantener conviviendo el proceso masivo antiguo con el nuevo desarrollo (nicolas).
- `detalle_productos/adquirencia/devoluciones_y_contracargos.md` — actualizado: ratificación de prioridad máxima de PRD-146 (tickets DAD-2209/DAD-2257) (nicolas).
- `cumplimiento_normativo/limites_operativos_uif_ros.md` — actualizado: nueva sección, definiciones de Cumplimiento confirmadas para casos multi-operatoria (caso Pago Fácil — separación de comercios por operatoria, titularidad CUIT) (pablo).
- `cumplimiento_normativo/gestion_riesgo_tecnologia_seguridad_a7724.md` — archivo nuevo: marco de gestión de riesgos de TI/ciberseguridad, Com. "A" 7724 BCRA, aplicabilidad asumida por el PM (pablo).
- `cumplimiento_normativo/index.md` — actualizado: fila del archivo nuevo.
- `cumplimiento_normativo/identificacion_personas_juridicas_vinculados.md` — actualizado: nueva sección, checklist interno de documentación por tipo societario (Res. UIF 200/2024) (pablo).

### 2026-09-07, segunda corrida (pablo + nicolas)

- `arquitectura_sistema/api_bank/` — módulo nuevo (carpeta creada con permiso explícito del usuario), 11 archivos: relevamiento completo de la API pública de Banco Industrial (87 endpoints, 10 grupos) — Autenticación, Cuenta, Billetera, Transferencia, TransferenciaMEP, Debin, Vista, Webhooks, Eventos, Alta de Cuenta (con gap de catálogo PSI embebido), Errores (pablo).
- `arquitectura_sistema/index.md` — actualizado: fila del módulo nuevo.
- `cumplimiento_normativo/gestion_riesgo_fraude_bcra.md` — archivo nuevo: Comunicaciones "A" 8471 y 8473 del BCRA, programa de gestión de riesgo de fraude y score de riesgo por CUIL/CUIT (pablo).
- `cumplimiento_normativo/index.md` — actualizado: fila del archivo nuevo.
- `detalle_productos/wallet/interoperabilidad_qr_getnet.md` — archivo nuevo: especificación técnica OAuth2 del circuito interoperable QR de Getnet (socio/APM), con nota de posible superposición sin confirmar con `getnet_oauth2_resolve/` (nicolas).
- `detalle_productos/wallet/index.md` — actualizado: fila del archivo nuevo.
- `datos/datos_metricas_semanales/*.csv` y `datos/log_metricas_semanales.md` — reemplazados (copia byte a byte, tipo: dato): store semana 202636 (pablo).
- `datos/metricas_semanales.md` — nueva entrada: semana 202636, hallazgos de negocio (versión abreviada — sin tablas 1a-1d completas, ver nota en la propia entrada) (pablo).

### 2026-09-07, primera corrida (pablo + nicolas)

- `detalle_productos/onboarding/integracion_worldsys_listas_informados.md` — archivo nuevo: integración real con "Listas de Informados" (LDI) de Worldsys — endpoints, autenticación, `Evaluate` vs. `SourcesSearch`, parámetro `ConfigurationName` (pablo).
- `detalle_productos/onboarding/validacion_lista_negra_bind.md` — actualizado: referencia cruzada al archivo hermano nuevo de Worldsys LDI.
- `detalle_productos/onboarding/index.md` — actualizado: fila del archivo nuevo.
- `detalle_productos/ardid/integracion_con_productos_bind.md` — actualizado: nueva §16, confirmación en producción del fix de grupo BIN (§15) generando rechazos legítimos en el cliente Terramundi (nicolas).
- `detalle_productos/wallet/conciliacion_y_totalizadores.md` — actualizado: nueva §7, regularización de campos cuenta corriente/movimientos y extensión de conciliación Cash Out vía Coelsa (V72.2) (nicolas).
- `detalle_productos/adquirencia/devoluciones_y_contracargos.md` — actualizado: nueva §4, fix de timeout en contracargo por ID de referencia de transacción sobredimensionado (AD1639, cliente Ripsa) (nicolas).
- `detalle_productos/adquirencia/webhooks_y_notificaciones.md` — actualizado: nueva sección, tres definiciones sobre el webhook de QR Tarjeta (endpoint de devoluciones separado, comisiones de Coelsa, ID Coelsa en comprobantes) (nicolas).
- `detalle_productos/wallet/transferencias_pull.md` — actualizado §6: Coelsa confirma que la URL del PSP registrada no responde a telnet; Bind reporta `ERROR DEBITO` en pruebas propias (nicolas).
- `detalle_productos/adquirencia/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: nueva sección "Hallazgos operativos recientes (septiembre 2026)" — PedidosYa (arancel neto QR) y ProvinciaNET (masividad de QR satura cola general) (nicolas).
- `detalle_productos/wallet/validaciones_y_alias_cvu.md` — sin cambios: 1 item de nicolas (`wallet-reintento-alias-por-delay-registro-cbu-coelsa`) evaluado como duplicado de contenido ya mergeado en la corrida 2026-09-03 (mismos tickets WS-1556/DEM-1828, misma reunión) — no se escribió contenido nuevo.

### 2026-09-03 (pablo + nicolas)

- `detalle_productos/wallet/validaciones_y_alias_cvu.md` — actualizado: reintento de alias confirmado con tickets WS-1556/DEM-1828, detalle de despliegue V72.2 (pablo).
- `detalle_productos/wallet/validacion_totalizadores_cbu_cvu.md` — archivo nuevo: mecánica completa de validación de totalizadores CBU/CVU (PRD-200, mandato BCRA/Banco Industrial) (pablo).
- `detalle_productos/wallet/debin_y_fondeo.md` — actualizado: nueva §9, endpoint de Coelsa para consulta de operación DEBIN/DEBINQR por ID propio (nicolas).
- `detalle_productos/wallet/index.md` — actualizado: filas de los archivos nuevos/tocados.
- `detalle_productos/onboarding/validacion_lista_negra_bind.md` — archivo nuevo: servicio SOAP de Listas Negras (incluye lista 15 de PLD), ya en producción, insumo de PRD-116 (pablo).
- `detalle_productos/onboarding/index.md` — actualizado: fila del archivo nuevo.
- `detalle_productos/adquirencia/mecanica_qr_coelsa.md` — actualizado: Parte 5, evidencia adicional de reclamo activo de Global66 (no cierra la contradicción TPay vs. BSF/Global66) (pablo).
- `detalle_productos/ardid/modulo_transferencias.md` — actualizado: nueva §9, límites de reglas vigentes y limitación de tooling para trazabilidad regla→rechazo, motivada por el incidente de Terramundi (pablo).
- `arquitectura_sistema/relacion_con_fintexa.md` — actualizado: §2 con el corte de agosto 2026 del informe COE (delta vs. julio) (pablo).
- `arquitectura_sistema/modelo_acoplado_vs_desacoplado.md` — actualizado: nueva sección, los dos tracks pendientes reportados por Banco Industrial y su cruce con la decisión de migración CBU Link→Coelsa (pablo).

### 2026-09-02 (pablo + nicolas)

- `cumplimiento_normativo/identificacion_personas_fisicas_cvu.md` — archivo nuevo (⚠️ orientación de diseño, no validada por Compliance): marco regulatorio BCRA/UIF/ARCA/AAIP de identificación para altas CVU de personas físicas (pablo).
- `cumplimiento_normativo/identificacion_personas_juridicas_vinculados.md` — archivo nuevo (⚠️ orientación de diseño, no validada por Compliance): requisitos UIF para personas jurídicas, FCI/Fideicomisos y beneficiario final (pablo).
- `cumplimiento_normativo/index.md` — actualizado: filas de los 2 archivos nuevos.
- `detalle_productos/wallet/validaciones_y_alias_cvu.md` — actualizado: reintento automático de alias ante error de APIBank (§1); nueva §3, nota operativa de baja confianza sobre domicilio real/consulta AFIP en altas 2024 (nicolas).
- `detalle_productos/agente_cobros_y_pagos/transferencia_saliente_mecanica.md` — actualizado: bug de mapeo de transferencias salientes como recibidas, sin desarrollo asociado (nicolas).
- `detalle_productos/adquirencia/boton_simple_2_0.md` — actualizado: nueva §8.1, definiciones técnicas de QR Tarjeta post-payments/terminal ID (fusión de 2 items, pablo + nicolas).
- `detalle_productos/servicios/pago_facil_mantenimiento.md` — actualizado: nueva §6, restricciones de Coelsa sobre alias de CBU (nicolas).
- `detalle_productos/wallet/transferencias_pull.md` — actualizado §6: continuación del circuito de reactivación en Homologación, `PUT` de URL de PSP no se refleja en consulta posterior (nicolas).
- `detalle_productos/ardid/integracion_con_productos_bind.md` — actualizado: nueva §15, bug de grupo BIN mal configurado bloqueaba reglas de pago (cliente Coto) (nicolas).
- `detalle_productos/adquirencia/gestion_convenios_comisiones.md` — actualizado: confirmación de negocio del modelo de herencia (reunión 2026-08-27), no contradice el contrato ya documentado (nicolas).
- `detalle_productos/adquirencia/pos_multiadquirencia.md` — actualizado: nueva §1.4, Decidir vs. Prisma — parametrización distinta para tarjeta QR (nicolas).
- `detalle_productos/wallet/dolar_fx.md` — actualizado: nueva §2.9, PVT de Mastercard Cross-Border (XBS) — Implementation Plan v3.0, deadline 16/09 (pablo).
- `detalle_productos/onboarding/onboarding_por_api.md` — actualizado: nueva §4, modelo de integración "completa" (caso Inter) e incidente de PDF417 asociado (pablo).
- `detalle_productos/adquirencia/mecanica_qr_coelsa.md` — actualizado: nueva Parte 5, parametrización del tiempo de espera de resolución (State Monitor T1/T2) — con contradicción sin resolver sobre el cliente que lo motivó (pablo + nicolas).
- `detalle_productos/adquirencia/webhooks_y_notificaciones.md` — actualizado: nuevos campos de arancel aceptador en el webhook de Cobro QR exitoso (pablo).

### 2026-08-31 (pablo + nicolas)

- `datos/metricas_semanales.md` — actualizado (items `tipo: dato`, aplicado byte a byte): entradas de las semanas 202634 y 202635 antepuestas al histórico (pablo).
- `datos/datos_metricas_semanales/` — actualizado (items `tipo: dato`, aplicado byte a byte): store cumulativo hasta la semana 202635, incluye primera ingesta completa de `dim_collectors.csv` con mapeo confirmado (pablo).
- `detalle_productos/adquirencia/gestion_convenios_comisiones.md` — actualizado: inventario completo de los 16 endpoints (3 hallazgos nuevos H9-H11) y dato de arquitectura sobre el flujo transaccional compartido con el Admin (pablo).
- `detalle_productos/ardid/despliegues_y_operacion.md` — archivo nuevo: protocolo de rollback de dos pasos (imagen + DB) y riesgo de reglas antifraude no aplicadas (caso Coto, AD-1374) (pablo).
- `detalle_productos/ardid/index.md` — actualizado: registro del archivo nuevo.
- `detalle_productos/wallet/dolar_fx.md` — actualizado: nueva §2.6ter con 4 hallazgos de manejo de errores del MVP2 de Pagos FX cross-border (Mastercard Move) (pablo).
- `detalle_productos/wallet/validaciones_y_alias_cvu.md` — actualizado §1: tope de 10 modificaciones de alias/año y formato (6-20 caracteres), confirmado por normativa BCRA — redirigido acá en vez de `apis_expuestas/cvu/guia_cvu.md` (dominio exclusivo de `/sync_web`), con gap señalizado para que esa skill lo aplique a la guía pública (pablo).
- `detalle_productos/servicios/pago_facil.md` — actualizado: nueva sección sobre email obligatorio para envío de comprobante de pago (ticket SER-66) (nicolas).
- `detalle_productos/servicios/pago_facil_mantenimiento.md` — actualizado: nueva §5, Piloto Productivo Bind-SEPSA (plataforma admin, Billers, puntos operativos abiertos) (nicolas).

### 2026-08-27 (pablo + nicolas)

- `datos/changelog_releases.md` — actualizado (item `tipo: dato`, aplicado byte a byte): 4 entradas nuevas (AD 71.3, W 72, W 71.8).
- `datos/log_versiones_publicadas.md` — actualizado (item `tipo: dato`, aplicado byte a byte): cabecera de último barrido + 3 filas nuevas (AD 71.3, W 71.8, W 72 — 18 tickets).
- `detalle_productos/adquirencia/configuracion_de_entidades.md` — actualizado: nueva §7 (hotfix localidades/código postal); nota de contradicción en §4 (ver contrato real de convenios).
- `detalle_productos/adquirencia/boton_simple_2_0.md` — actualizado: nueva §11 (parámetro `pago_unico`) y §12 (eliminación de límite de $9M en links de pago).
- `detalle_productos/adquirencia/pos_multiadquirencia.md` — actualizado: nueva §1.3 (deuda técnica de reglas Prisma/GP → parámetros de canal dinámicos).
- `detalle_productos/adquirencia/devoluciones_y_contracargos.md` — actualizado: nueva §2 (bug de tipo de operación en contracargos POS GP, AD V72); §1.1 (historial COTO) extraída por umbral de tamaño.
- `detalle_productos/adquirencia/cliente_coto_historial_operativo.md` — creado (fisión de `devoluciones_y_contracargos.md`, sin cambio de fondo).
- `detalle_productos/adquirencia/impuestos_iibb_liquidacion_lote.md` — creado: bug de performance (fan-out JOIN) y NULL constraint en la vista de percepción IIBB.
- `detalle_productos/adquirencia/webhooks_y_notificaciones.md` — actualizado: cambio de categorización CBU externo→CBU corto en CBU Collect (AD V72).
- `detalle_productos/adquirencia/herramientas_operativas_boton_simple.md` — actualizado: retiro de carga masiva de CBU Corto por CSV.
- `detalle_productos/adquirencia/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: hallazgo AD-1558 (Apibank, reconsulta indebida TX019/TX021).
- `detalle_productos/adquirencia/mejoras_admin_backoffice_prd88.md` — actualizado: nota de contradicción doble en §2 (Epic AD-8 + contrato real de convenios, ver gaps).
- `detalle_productos/adquirencia/gestion_convenios_comisiones.md` — creado: contrato real OpenAPI de Convenios/Comisiones (Convenio maestro + ComercioConvenio, flag `FromCommerce`).
- `detalle_productos/adquirencia/index.md` — actualizado: filas nuevas de los 3 archivos creados, descripciones ajustadas.
- `detalle_productos/wallet/transferencias_pull.md` — actualizado: nueva §6 (reactivación de Transferencias Pull en homologación, Coelsa).
- `detalle_productos/wallet/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: nota comparativa COTO (payload real vs. documentación) + tramo W72 (eliminar CVU deshabilita cuenta, ventana OperacionByIdExterno a 180 días).
- `detalle_productos/wallet/organizaciones_y_configuracion.md` — actualizado: §7 cerrado (AuthExternal V2 etapa 3/3) + tramo W72 (bug cache Redis, path Ardid en alta de org).
- `detalle_productos/wallet/validaciones_y_alias_cvu.md` — creado (fisión de `organizaciones_y_configuracion.md`): mecánica de alias Coelsa/bloqueo 24hs + hardening de longitud CVU/CBU.
- `detalle_productos/wallet/dolar_ccl.md` — actualizado: §3.6bis cerrado con ticket WS-1351.
- `detalle_productos/wallet/historial_confiabilidad_transferencias_y_comprobantes.md` — actualizado: §10 cerrado (migración EasyNet completa) + reconsulta parametrizable (EN QA).
- `detalle_productos/wallet/debin_y_fondeo.md` — actualizado: 2 fixes de robustez de contracargos DEBIN recurrente (Epic WS-810/PRD-140).
- `detalle_productos/wallet/cuenta_remunerada_fci.md` — actualizado: resiliencia FCI paso 6 ante 502 de PCNT; §4.5 cerrado (2 de 5 defectos de Settlement/Info).
- `detalle_productos/wallet/index.md` — actualizado: fila del archivo nuevo, descripciones ajustadas.
- `detalle_productos/ardid/integracion_con_productos_bind.md` — actualizado: mapeo de motivos de rechazo hacia Onboarding + control de disponibilidad de Ardid en Wallet (discovery).
- `detalle_productos/ardid/modulo_pagos.md` — actualizado: identificación de tarjetas por hash + bloqueo permanente por hash de vencimiento.
- `detalle_productos/ardid/index.md` — actualizado.
- `detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md` — actualizado: Wallet como orquestador de Onboarding (endpoints propuestos); vulnerabilidad de validación Renaper (no cruza imágenes de DNI); contradicción de orden de prioridad (ver gaps).
- `detalle_productos/onboarding/integracion_worldsys_complianceone.md` — actualizado: requisitos de evidencia documental para onboarding delegado a terceros.
- `detalle_productos/onboarding/index.md` — actualizado.
- `detalle_productos/servicios/pago_facil_mantenimiento.md` — actualizado: Proyecto Servicios incorporado formalmente al pipeline de Wallet.
- `detalle_productos/servicios/pago_facil.md` — actualizado: esquema de subagentes para exponer APIs de BPG a integradores externos (discovery).
- `detalle_productos/siscri/calculo_impuesto_online_qr.md` — actualizado: saturación de BD de impuestos por CUIT compartido + regla de liquidación same-day.
- `detalle_productos/agente_cobros_y_pagos/integracion_procesadores_pago.md` — creado: deuda técnica de reglas Prisma/GP, parámetro pago único, regla de liquidación.
- `detalle_productos/agente_cobros_y_pagos/index.md` — actualizado.
- `arquitectura_sistema/mantenimiento_y_capacidad_aks.md` — actualizado: purga periódica de bases históricas en ventana de mantenimiento de Apibank.
- `arquitectura_sistema/incidentes_de_plataforma.md` — actualizado: nueva §8 (repaso semanal — despliegues Wallet 7.2/AuthExternal v2.0, Zero Downtime vs. Sentinela).
- `arquitectura_sistema/index.md` — actualizado.

### 2026-08-21 (pablo)

- `detalle_productos/onboarding/onboarding_personas_juridicas.md` — actualizado: nueva §8 (demo end-to-end a Octagon/Banco Industrial — consola de cumplimiento y potencial de marca blanca).
- `detalle_productos/portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: nueva sección de parametrización manual y fragmentada de entidades (reunión "Parámetros de entidades").
- `detalle_productos/portal_admin/accesos_qa_staging.md` — creado: credenciales de acceso de prueba al Admin en STAGING para sesiones de QA/discovery.
- `detalle_productos/portal_admin/index.md` — actualizado: referencia al archivo nuevo.
- `detalle_productos/portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: nueva sección sobre la retomada del rollout de Portal 2.0 (despliegue piloto por entidad).
- `detalle_productos/adquirencia/pos_multiadquirencia.md` — actualizado: nueva §6 (investigación abierta de desalineación de BINES Payway/Decidir).

### 2026-08-19 (pablo)

- `detalle_productos/wallet/conciliacion_y_totalizadores.md` — actualizado: archivos de Cuadratura (nuevo §6), totalizadores expuestos en BFF de onboarding, límite de 30 iteraciones V72.
- `detalle_productos/wallet/cuenta_remunerada_fci.md` — actualizado: nueva §4.6 (estado MVP2, webhook FCI faltante en PROD, duplicados por condición de carrera W71).
- `detalle_productos/wallet/dolar_fx.md` — actualizado: primer PagoFX productivo real (nueva §2.6bis).
- `detalle_productos/adquirencia/botones_de_pago_y_qr.md` — actualizado: mejoras al Monitor de carga masiva de deudas ProvinciaNET (AD 71.2 FIX).
- `detalle_productos/ardid/integracion_con_productos_bind.md` — actualizado: atribución de versión ARD-32 al hotfix de reintentos de SP ya documentado (§10/§11).
- `detalle_productos/portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: nueva sección "Rollout Portal 2.0" (20 tickets, primera cobertura del tema).
- `detalle_productos/wallet/organizaciones_y_configuracion.md` — actualizado: nueva §7 (altas de organización y AuthExternal V2, tramo W71).
- `detalle_productos/wallet/dolar_ccl.md` — actualizado: correcciones de venta/comprobantes de cargo (W71) y despliegue V72 pese a regresiones sin cerrar.
- `detalle_productos/wallet/debin_y_fondeo.md` — actualizado: fix de mapeo de `CoelsaId` y endpoint manual de contracargos (W71).
- `detalle_productos/wallet/historial_confiabilidad_transferencias_y_comprobantes.md` — actualizado: nueva §10 (infraestructura y confiabilidad tramo W71) y §10.1 (reducción de microservicios/nodos).
- `detalle_productos/wallet/pedidos_de_clientes_y_hallazgos_operativos.md` — actualizado: bugs y pedidos operativos tramo W71, pedido de GST, deuda técnica de comprobante relacionado.
- `detalle_productos/wallet/recycle_cobro_automatico.md` — actualizado: contracargo de débito recurrente pasa a producción + fix de trazabilidad.
- `datos/changelog_releases.md` — actualizado: 12 entradas nuevas (AD 71.2 FIX, ARDID V1.18.2.1 HF, Portal 2.0 V1/V2, W71 y sus 6 FIX).
- `datos/log_versiones_publicadas.md` — actualizado: header, estado del backfill de AD corregido, 12 filas nuevas de versiones ingestadas.
- `datos/metricas_semanales.md` — reemplazado byte a byte (semana 202633).
- `datos/datos_metricas_semanales/` — reemplazado byte a byte (semana 202633; `dim_collectors` sin refresh, ver gap en `2_areas/gaps_y_preguntas.md`).
- `detalle_productos/onboarding/integracion_worldsys_complianceone.md` — creado: contrato técnico de la API Worldsys/ComplianceOne (auth, personas, documentos, catálogo de tipos, import masivo), desde Swagger público v1.0.0 + hilo de mail con el proveedor (discovery PRD-147).
