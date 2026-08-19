# Changelog de `3_recursos/`

> Resumen corto de cada merge que tocó esta capa — qué cambió, sin el detalle (eso está en el archivo). **Solo lo escribe `/context_merge`**, una línea por archivo tocado, agrupadas por fecha de merge. Incluye los items `tipo: dato` aplicados por copia a `datos/`. Vive en el core y viaja con el espejo, así que se lee desde el install sin tocar el clon compartido. Rotación anual a `wiki/4_archivos/`.
>
> Distinto del manifiesto de cada merge (`manifiestos/YYYY-MM-DD.md` en el core): el manifiesto es el recibo operativo completo y lo lee `/context_pull`; esto es el resumen humano.

## 2026

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
