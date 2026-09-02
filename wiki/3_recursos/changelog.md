# Changelog de `3_recursos/`

> Resumen corto de cada merge que tocó esta capa — qué cambió, sin el detalle (eso está en el archivo). **Solo lo escribe `/context_merge`**, una línea por archivo tocado, agrupadas por fecha de merge. Incluye los items `tipo: dato` aplicados por copia a `datos/`. Vive en el core y viaja con el espejo, así que se lee desde el install sin tocar el clon compartido. Rotación anual a `wiki/4_archivos/`.
>
> Distinto del manifiesto de cada merge (`manifiestos/YYYY-MM-DD.md` en el core): el manifiesto es el recibo operativo completo y lo lee `/context_pull`; esto es el resumen humano.

## 2026

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
