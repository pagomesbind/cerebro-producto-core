# API Pública Expuesta — Adquirencia

> **ADVERTENCIA:** Este directorio contiene EXCLUSIVAMENTE las APIs públicas expuestas al cliente en el portal web (`psp.bind.com.ar/developers`). Dominio exclusivo de la skill `/sync_web`. Reubicado desde `3_recursos/documentacion_api/apis_expuestas/adquirencia/` en la reestructuración PARA en cascada (2026-08-12).
>
> Ver [3_recursos/arquitectura_sistema/entornos_y_autenticacion_oauth2.md](../../../arquitectura_sistema/index.md) para OAuth2/entornos/TLS, comunes a toda la API pública.

7 funcionalidades:

### Comercios y Transacciones — `comercios_transacciones/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_comercios_transacciones.md](comercios_transacciones/guia_comercios_transacciones.md) | Guía | Gestión de comercios |
| [endpoint_post_crear_comercio.md](comercios_transacciones/endpoint_post_crear_comercio.md) | POST | Crear comercio |
| [endpoint_get_consultar_comercio.md](comercios_transacciones/endpoint_get_consultar_comercio.md) | GET | Consultar comercio |
| [endpoint_get_consultar_transaccion.md](comercios_transacciones/endpoint_get_consultar_transaccion.md) | GET | Consultar transacción |
| [endpoint_patch_habilitar_comercio.md](comercios_transacciones/endpoint_patch_habilitar_comercio.md) | PATCH | Habilitar/deshabilitar comercio |

### QR Dinámico — `qr_dinamico/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_qr_dinamico.md](qr_dinamico/guia_qr_dinamico.md) | Guía | Flujo QR Dinámico (deuda) |
| [endpoint_post_crear_deuda.md](qr_dinamico/endpoint_post_crear_deuda.md) | POST | Crear deuda QR |
| [endpoint_get_consultar_deuda.md](qr_dinamico/endpoint_get_consultar_deuda.md) | GET | Consultar deuda |
| [endpoint_delete_eliminar_deuda.md](qr_dinamico/endpoint_delete_eliminar_deuda.md) | DELETE | Eliminar deuda |
| [endpoint_post_crear_devolucion_qr.md](qr_dinamico/endpoint_post_crear_devolucion_qr.md) | POST | Crear devolución |
| [endpoint_get_consultar_devolucion.md](qr_dinamico/endpoint_get_consultar_devolucion.md) | GET | Consultar devolución |
| [endpoint_event_transaccion_qr_deuda.md](qr_dinamico/endpoint_event_transaccion_qr_deuda.md) | EVENT | Webhook: transacción QR dinámico |
| [endpoint_event_devolucion_qr_dinamico.md](qr_dinamico/endpoint_event_devolucion_qr_dinamico.md) | EVENT | Webhook: devolución QR dinámico |

### QR Estático — `qr_estatico/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_qr_estatico.md](qr_estatico/guia_qr_estatico.md) | Guía | Flujo QR Estático |
| [endpoint_get_generar_codigo_qr.md](qr_estatico/endpoint_get_generar_codigo_qr.md) | GET | Generar código QR |
| [endpoint_post_crear_orden_venta.md](qr_estatico/endpoint_post_crear_orden_venta.md) | POST | Crear orden de venta |
| [endpoint_delete_eliminar_orden_venta.md](qr_estatico/endpoint_delete_eliminar_orden_venta.md) | DELETE | Eliminar orden de venta |
| [endpoint_get_consultar_orden_id.md](qr_estatico/endpoint_get_consultar_orden_id.md) | GET | Consultar orden por ID |
| [endpoint_get_consultar_orden_codigo_externo.md](qr_estatico/endpoint_get_consultar_orden_codigo_externo.md) | GET | Consultar por código externo |
| [endpoint_post_crear_devolucion_qr.md](qr_estatico/endpoint_post_crear_devolucion_qr.md) | POST | Crear devolución |
| [endpoint_get_consultar_devolucion.md](qr_estatico/endpoint_get_consultar_devolucion.md) | GET | Consultar devolución |
| [endpoint_event_transaccion_qr_estatico.md](qr_estatico/endpoint_event_transaccion_qr_estatico.md) | EVENT | Webhook: transacción QR estático |
| [endpoint_event_devolucion_qr_estatico.md](qr_estatico/endpoint_event_devolucion_qr_estatico.md) | EVENT | Webhook: devolución QR estático |

### Botón Simple — `boton_simple/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_boton_simple.md](boton_simple/guia_boton_simple.md) | Guía | Flujo Botón Simple (link de pago) |
| [endpoint_post_crear_link_pago.md](boton_simple/endpoint_post_crear_link_pago.md) | POST | Crear link de pago |
| [endpoint_get_consultar_link_pago.md](boton_simple/endpoint_get_consultar_link_pago.md) | GET | Consultar link de pago |
| [endpoint_event_transaccion.md](boton_simple/endpoint_event_transaccion.md) | EVENT | Webhook: transacción completada |
| [endpoint_event_devolucion.md](boton_simple/endpoint_event_devolucion.md) | EVENT | Webhook: devolución |

> Ver también `boton_simple_10/` y `boton_simple_20/` — versiones adicionales del mismo producto documentadas por separado en el portal.

### Conciliaciones — `conciliaciones/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_conciliaciones.md](conciliaciones/guia_conciliaciones.md) | Guía | Flujo conciliación adquirencia |
| [endpoint_get_consultar_archivos_cobro.md](conciliaciones/endpoint_get_consultar_archivos_cobro.md) | GET | Listar archivos de cobro |
| [endpoint_get_descargar_archivo_cobro.md](conciliaciones/endpoint_get_descargar_archivo_cobro.md) | GET | Descargar archivo de cobro |

### Recaudación por Transferencia — `recaudacion_transferencia/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_recaudacion_transferencia.md](recaudacion_transferencia/guia_recaudacion_transferencia.md) | Guía | Flujo CVU caja recaudadora |
| [endpoint_post_crear_cvu_caja.md](recaudacion_transferencia/endpoint_post_crear_cvu_caja.md) | POST | Crear CVU caja |
| [endpoint_patch_asignar_alias_cvu_caja.md](recaudacion_transferencia/endpoint_patch_asignar_alias_cvu_caja.md) | PATCH | Asignar alias a CVU caja |
| [endpoint_delete_deshabilitar_cvu_caja.md](recaudacion_transferencia/endpoint_delete_deshabilitar_cvu_caja.md) | DELETE | Deshabilitar CVU caja |
| [endpoint_event_transaccion_rxt.md](recaudacion_transferencia/endpoint_event_transaccion_rxt.md) | EVENT | Webhook: transacción RxT |

### Eco Cerrado — `eco_cerrado/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_eco_cerrado.md](eco_cerrado/guia_eco_cerrado.md) | Guía | Flujo ecosistema cerrado |
| [endpoint_post_informar_transaccion.md](eco_cerrado/endpoint_post_informar_transaccion.md) | POST | Informar transacción |
| [endpoint_post_devolver_transaccion.md](eco_cerrado/endpoint_post_devolver_transaccion.md) | POST | Devolver transacción |
| [endpoint_event_transaccion_eco_cerrado.md](eco_cerrado/endpoint_event_transaccion_eco_cerrado.md) | EVENT | Webhook: transacción eco cerrado |

## Ver también
- [detalle_productos/adquirencia/index.md](../index.md) — resto del conocimiento de producto de Adquirencia (no API pública).

---
*Última actualización: 2026-08-12 — Reubicado desde `documentacion_api/apis_expuestas/adquirencia/` (reestructuración PARA en cascada). Contenido y estructura sin cambios, solo la ruta.*
*Última actualización anterior: 2026-06-30 — Fuente: https://psp.bind.com.ar/developers*
