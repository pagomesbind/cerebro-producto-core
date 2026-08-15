# API Pública Expuesta — Wallet

> **ADVERTENCIA:** Este directorio contiene EXCLUSIVAMENTE las APIs públicas expuestas al cliente en el portal web (`psp.bind.com.ar/developers`). Dominio exclusivo de la skill `/sync_web` — ningún otro flujo de ingesta escribe, reclasifica ni elimina nada acá. Reubicado desde `3_recursos/documentacion_api/apis_expuestas/wallet/` en la reestructuración PARA en cascada (2026-08-12) — la API pública ahora vive junto al resto del conocimiento de cada producto.
>
> Ver [3_recursos/arquitectura_sistema/entornos_y_autenticacion_oauth2.md](../../../arquitectura_sistema/index.md) para OAuth2/entornos/TLS, comunes a toda la API pública.

15 funcionalidades:

### Cuentas — `cuentas/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_cuentas.md](cuentas/guia_cuentas.md) | Guía | Conceptos, reglas de negocio, flujo de alta |
| [endpoint_post_crear.md](cuentas/endpoint_post_crear.md) | POST | Crear cuenta nueva |
| [endpoint_patch_habilitar_deshabilitar.md](cuentas/endpoint_patch_habilitar_deshabilitar.md) | PATCH | Cambiar estado de cuenta |
| [endpoint_put_modificar.md](cuentas/endpoint_put_modificar.md) | PUT | Actualizar datos de cuenta |
| [endpoint_get_consultar_id.md](cuentas/endpoint_get_consultar_id.md) | GET | Consultar por ID interno |
| [endpoint_get_consultar_cuit.md](cuentas/endpoint_get_consultar_cuit.md) | GET | Consultar por CUIT |
| [endpoint_get_consultar_email.md](cuentas/endpoint_get_consultar_email.md) | GET | Consultar por email |
| [endpoint_get_consultar_celular.md](cuentas/endpoint_get_consultar_celular.md) | GET | Consultar por número de celular |
| [endpoint_event_cuenta_deshabilitada.md](cuentas/endpoint_event_cuenta_deshabilitada.md) | EVENT | Webhook: cuenta deshabilitada |

### CVU — `cvu/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_cvu.md](cvu/guia_cvu.md) | Guía | Conceptos y flujo CVU |
| [endpoint_post_crear_cvu.md](cvu/endpoint_post_crear_cvu.md) | POST | Crear CVU |
| [endpoint_delete_eliminar_cvu.md](cvu/endpoint_delete_eliminar_cvu.md) | DELETE | Eliminar CVU |
| [endpoint_patch_asignar_alias.md](cvu/endpoint_patch_asignar_alias.md) | PATCH | Asignar alias a CVU |
| [endpoint_get_consultar_por_cbu_cvu_alias.md](cvu/endpoint_get_consultar_por_cbu_cvu_alias.md) | GET | Consultar por CBU/CVU/alias |
| [endpoint_get_listar_cuentas_cvu.md](cvu/endpoint_get_listar_cuentas_cvu.md) | GET | Listar cuentas CVU |

### Saldo en Pesos — `saldo_pesos/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_saldo_pesos.md](saldo_pesos/guia_saldo_pesos.md) | Guía | Comprobantes y saldos |
| [endpoint_post_crear_comprobante.md](saldo_pesos/endpoint_post_crear_comprobante.md) | POST | Crear comprobante |
| [endpoint_get_consultar_tipos_comprobante.md](saldo_pesos/endpoint_get_consultar_tipos_comprobante.md) | GET | Listar tipos de comprobante |
| [endpoint_post_crear_tipo_comprobante.md](saldo_pesos/endpoint_post_crear_tipo_comprobante.md) | POST | Crear tipo de comprobante |
| [endpoint_delete_eliminar_tipo_comprobante.md](saldo_pesos/endpoint_delete_eliminar_tipo_comprobante.md) | DELETE | Eliminar tipo de comprobante |
| [endpoint_get_consultar_comprobante_id.md](saldo_pesos/endpoint_get_consultar_comprobante_id.md) | GET | Consultar comprobante por ID |
| [endpoint_get_consultar_comprobante_id_externo.md](saldo_pesos/endpoint_get_consultar_comprobante_id_externo.md) | GET | Consultar comprobante por ID externo |
| [endpoint_get_consultar_saldo_actual_id.md](saldo_pesos/endpoint_get_consultar_saldo_actual_id.md) | GET | Saldo actual por ID de cuenta |
| [endpoint_get_consultar_saldo_actual_cvu.md](saldo_pesos/endpoint_get_consultar_saldo_actual_cvu.md) | GET | Saldo actual por CVU |
| [endpoint_get_listar_saldos_actuales.md](saldo_pesos/endpoint_get_listar_saldos_actuales.md) | GET | Listar saldos actuales |
| [endpoint_get_consultar_saldo_historico_id.md](saldo_pesos/endpoint_get_consultar_saldo_historico_id.md) | GET | Saldo histórico por ID |
| [endpoint_get_consultar_saldo_historico_cvu.md](saldo_pesos/endpoint_get_consultar_saldo_historico_cvu.md) | GET | Saldo histórico por CVU |
| [endpoint_get_listar_saldos_historicos.md](saldo_pesos/endpoint_get_listar_saldos_historicos.md) | GET | Listar saldos históricos |

### Transferencias — `transferencias/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_transferencias.md](transferencias/guia_transferencias.md) | Guía | Flujo de transferencias salientes/entrantes |
| [endpoint_post_transferir.md](transferencias/endpoint_post_transferir.md) | POST | Ejecutar transferencia |
| [endpoint_post_conciliar_entrante.md](transferencias/endpoint_post_conciliar_entrante.md) | POST | Conciliar transferencia entrante |
| [endpoint_get_consultar_operacion_id.md](transferencias/endpoint_get_consultar_operacion_id.md) | GET | Consultar operación por ID |
| [endpoint_event_transferencia_saliente.md](transferencias/endpoint_event_transferencia_saliente.md) | EVENT | Webhook: transferencia saliente |
| [endpoint_event_transferencia_entrante.md](transferencias/endpoint_event_transferencia_entrante.md) | EVENT | Webhook: transferencia entrante |

### Pago QR — `pago_qr/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_pago_qr.md](pago_qr/guia_pago_qr.md) | Guía | Flujo de pago con QR |
| [endpoint_get_leer_qr.md](pago_qr/endpoint_get_leer_qr.md) | GET | Leer/decodificar QR |
| [endpoint_post_pagar_qr.md](pago_qr/endpoint_post_pagar_qr.md) | POST | Ejecutar pago QR |
| [endpoint_get_consultar_operacion_id.md](pago_qr/endpoint_get_consultar_operacion_id.md) | GET | Consultar operación por ID |
| [endpoint_get_consultar_operacion_id_ext.md](pago_qr/endpoint_get_consultar_operacion_id_ext.md) | GET | Consultar por ID externo |
| [endpoint_event_pago_qr.md](pago_qr/endpoint_event_pago_qr.md) | EVENT | Webhook: pago QR completado |
| [endpoint_event_devolucion_qr.md](pago_qr/endpoint_event_devolucion_qr.md) | EVENT | Webhook: devolución QR |

### DEBIN Recurrente — `debin_recurrente/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_debin_recurrente.md](debin_recurrente/guia_debin_recurrente.md) | Guía | Flujo de suscripción y cobro DEBIN |
| [endpoint_post_crear_suscripcion.md](debin_recurrente/endpoint_post_crear_suscripcion.md) | POST | Crear suscripción DEBIN |
| [endpoint_post_crear_debin.md](debin_recurrente/endpoint_post_crear_debin.md) | POST | Crear débito DEBIN |
| [endpoint_event_debin_recurrente.md](debin_recurrente/endpoint_event_debin_recurrente.md) | EVENT | Webhook: resultado DEBIN |

### Recycle — `recycle/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_recycle.md](recycle/guia_recycle.md) | Guía | Flujo de reciclado de comprobantes |
| [endpoint_event_comprobante_reciclado.md](recycle/endpoint_event_comprobante_reciclado.md) | EVENT | Webhook: comprobante reciclado |
| [endpoint_event_comprobante_pendiente.md](recycle/endpoint_event_comprobante_pendiente.md) | EVENT | Webhook: comprobante pendiente |

### Pago QR PIX — `pago_qr_pix/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_pago_qr_pix.md](pago_qr_pix/guia_pago_qr_pix.md) | Guía | Flujo de pago con QR PIX |
| [endpoint_post_pagar_qr_pix.md](pago_qr_pix/endpoint_post_pagar_qr_pix.md) | POST | Ejecutar pago QR PIX |

### Dólar CCL — `dolar_ccl/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_dolar_ccl.md](dolar_ccl/guia_dolar_ccl.md) | Guía | Flujo de operaciones con Dólar CCL |
| [endpoint_get_consultar_cotizacion.md](dolar_ccl/endpoint_get_consultar_cotizacion.md) | GET | Consultar cotización USD/ARS |
| [endpoint_get_consultar_horario_mercado.md](dolar_ccl/endpoint_get_consultar_horario_mercado.md) | GET | Consultar horario de mercado |
| [endpoint_get_consultar_ddjj.md](dolar_ccl/endpoint_get_consultar_ddjj.md) | GET | Consultar DDJJ |
| [endpoint_post_crear_intencion_compra.md](dolar_ccl/endpoint_post_crear_intencion_compra.md) | POST | Crear intención de compra |
| [endpoint_post_ejecutar_compra.md](dolar_ccl/endpoint_post_ejecutar_compra.md) | POST | Ejecutar compra |
| [endpoint_post_crear_intencion_venta.md](dolar_ccl/endpoint_post_crear_intencion_venta.md) | POST | Crear intención de venta |
| [endpoint_post_ejecutar_venta.md](dolar_ccl/endpoint_post_ejecutar_venta.md) | POST | Ejecutar venta |
| [endpoint_get_consultar_intencion.md](dolar_ccl/endpoint_get_consultar_intencion.md) | GET | Consultar intención |
| [endpoint_get_consultar_operacion_id.md](dolar_ccl/endpoint_get_consultar_operacion_id.md) | GET | Consultar operación por ID |
| [endpoint_get_consultar_operacion_id_externo.md](dolar_ccl/endpoint_get_consultar_operacion_id_externo.md) | GET | Consultar por ID externo |
| [endpoint_event_aviso_dolar_ccl.md](dolar_ccl/endpoint_event_aviso_dolar_ccl.md) | EVENT | Webhook: aviso operación CCL |

### Criptomonedas — `criptomonedas/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_criptomonedas.md](criptomonedas/guia_criptomonedas.md) | Guía | Flujo de operaciones con cripto |
| [endpoint_get_consultar_cotizacion_cripto.md](criptomonedas/endpoint_get_consultar_cotizacion_cripto.md) | GET | Consultar cotización cripto |
| [endpoint_post_crear_intencion_compra_cripto.md](criptomonedas/endpoint_post_crear_intencion_compra_cripto.md) | POST | Crear intención de compra |
| [endpoint_post_ejecutar_compra_cripto.md](criptomonedas/endpoint_post_ejecutar_compra_cripto.md) | POST | Ejecutar compra |
| [endpoint_post_crear_intencion_venta_cripto.md](criptomonedas/endpoint_post_crear_intencion_venta_cripto.md) | POST | Crear intención de venta |
| [endpoint_post_ejecutar_venta_cripto.md](criptomonedas/endpoint_post_ejecutar_venta_cripto.md) | POST | Ejecutar venta |
| [endpoint_get_consultar_intencion_cripto.md](criptomonedas/endpoint_get_consultar_intencion_cripto.md) | GET | Consultar intención |
| [endpoint_get_consultar_saldo_cripto.md](criptomonedas/endpoint_get_consultar_saldo_cripto.md) | GET | Consultar saldo cripto |
| [endpoint_get_consultar_operacion_id_cripto.md](criptomonedas/endpoint_get_consultar_operacion_id_cripto.md) | GET | Consultar operación por ID |
| [endpoint_get_consultar_operacion_id_externo_cripto.md](criptomonedas/endpoint_get_consultar_operacion_id_externo_cripto.md) | GET | Consultar por ID externo |
| [endpoint_event_aviso_cripto.md](criptomonedas/endpoint_event_aviso_cripto.md) | EVENT | Webhook: aviso operación cripto |

### Impuestos — `impuestos/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_impuestos.md](impuestos/guia_impuestos.md) | Guía | Retenciones y percepciones |
| [endpoint_event_aviso_impuesto.md](impuestos/endpoint_event_aviso_impuesto.md) | EVENT | Webhook: aviso de impuesto aplicado |

### Conciliaciones — `conciliaciones/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_conciliaciones.md](conciliaciones/guia_conciliaciones.md) | Guía | Flujo de conciliación wallet |
| [endpoint_get_consultar_comprobantes.md](conciliaciones/endpoint_get_consultar_comprobantes.md) | GET | Consultar comprobantes |
| [endpoint_get_consultar_operaciones.md](conciliaciones/endpoint_get_consultar_operaciones.md) | GET | Consultar operaciones |
| [endpoint_get_consultar_movimientos_cuenta_corriente.md](conciliaciones/endpoint_get_consultar_movimientos_cuenta_corriente.md) | GET | Consultar movimientos de cuenta corriente |
| [endpoint_get_consultar_archivos_wallet.md](conciliaciones/endpoint_get_consultar_archivos_wallet.md) | GET | Listar archivos de conciliación |
| [endpoint_get_descargar_archivo_wallet.md](conciliaciones/endpoint_get_descargar_archivo_wallet.md) | GET | Descargar archivo de conciliación |

### Cuenta Recaudadora — `cuenta_recaudadora/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_cuenta_recaudadora.md](cuenta_recaudadora/guia_cuenta_recaudadora.md) | Guía | Flujo de cuenta recaudadora |
| [endpoint_get_consultar_saldo_recaudadora.md](cuenta_recaudadora/endpoint_get_consultar_saldo_recaudadora.md) | GET | Consultar saldo |
| [endpoint_post_fondear_debin.md](cuenta_recaudadora/endpoint_post_fondear_debin.md) | POST | Fondear vía DEBIN |
| [endpoint_get_consultar_debin.md](cuenta_recaudadora/endpoint_get_consultar_debin.md) | GET | Consultar DEBIN |

### Acreditación de Cobros — `acreditacion_cobros/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_acreditacion_cobros.md](acreditacion_cobros/guia_acreditacion_cobros.md) | Guía | Flujo de acreditación de cobros QR |
| [endpoint_event_comprobante_cobro_qr.md](acreditacion_cobros/endpoint_event_comprobante_cobro_qr.md) | EVENT | Webhook: comprobante de cobro QR |

### Cuenta Remunerada — `cuenta_remunerada/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_cuenta_remunerada.md](cuenta_remunerada/guia_cuenta_remunerada.md) | Guía | Flujo FCI y rendimientos |
| [endpoint_post_crear_cuenta_comitente.md](cuenta_remunerada/endpoint_post_crear_cuenta_comitente.md) | POST | Crear cuenta comitente |
| [endpoint_get_consultar_tna.md](cuenta_remunerada/endpoint_get_consultar_tna.md) | GET | Consultar TNA |
| [endpoint_get_consultar_proceso_fci.md](cuenta_remunerada/endpoint_get_consultar_proceso_fci.md) | GET | Consultar proceso FCI |
| [endpoint_event_rendimiento_fci.md](cuenta_remunerada/endpoint_event_rendimiento_fci.md) | EVENT | Webhook: rendimiento FCI |
| [endpoint_event_conclusion_proceso_fci.md](cuenta_remunerada/endpoint_event_conclusion_proceso_fci.md) | EVENT | Webhook: conclusión proceso FCI |

## Notas técnicas

- **Limitación del portal (Framer SPA):** el HTML estático retornado por scraping no renderiza JS dinámico; URLs de sub-páginas individuales retornan 404 en scraping estático. Payloads JSON completos capturados solo para Dólar CCL y Criptomonedas (datos reales); el resto documenta estructura/parámetros/flujo inferidos del contexto de las guías padre. Campos marcados "pendiente de confirmación con equipo técnico" requieren validación contra la API real en staging.
- **Entornos:** Staging `https://gw-staging-qrbind.epays.services` · Producción `https://api.bindpagos.com.ar`.

## Ver también
- [detalle_productos/wallet/index.md](../index.md) — resto del conocimiento de producto de Wallet (no API pública).

---
*Última actualización: 2026-08-12 — Reubicado desde `documentacion_api/apis_expuestas/wallet/` (reestructuración PARA en cascada). Contenido y estructura sin cambios, solo la ruta.*
*Última actualización anterior: 2026-06-30 — Fuente: https://psp.bind.com.ar/developers*
