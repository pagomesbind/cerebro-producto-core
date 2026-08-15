# Producto Liquidador — API, Traditum y Newpay PMC

> Estado: en producción. Reubicado desde `detalle_productos/adquirencia/liquidaciones_y_devoluciones.md` en la reestructuración PARA en cascada (2026-08-12) — es un producto distinto (Liquidador, para clientes que cobran por su cuenta), separado de devoluciones/contracargos del cobro propio de Bind PSP. Ver [devoluciones_y_contracargos.md](devoluciones_y_contracargos.md) para ese otro tema.

## 1. API — Informar Nueva Transacción para Liquidar

> Alcance: dirigido exclusivamente a los equipos de desarrollo e integración técnica de entidades y comercios que operan como **Liquidadores** dentro del ecosistema de Bind PSP. Aplica solo para el producto **Liquidador**.

**Objetivo:** instruir al desarrollador de la Entidad que quiere integrarse a la solución de Bind PSP para informar transacciones externas en estado definitivo, para que el sistema procese esa notificación, persista la transacción y posteriormente realice la liquidación al comercio.

> ⚠️ Solo deben informarse pagos que tengan un estado aprobado definitivo.

El cuerpo de la petición se divide en tres objetos: `Operacion`, `Vendedor` y `Comprador`.

**`Operacion`:** `idMensaje` (opcional), `identificadorProcesador`/`identificadorTransaccion`/`identificadorOrdenVenta`/`identificadorReferencia` (requeridos, IDs del sistema externo), `pagoUnico` (boolean), `tipoTransaccion`="Liquidador", `rubroMovimiento`="PAGO", `rubroTransaccion`="Liquidador", `procesadorPago`="DECIDIR", `formaPago` ("TTDD"/"TTCC"), `fechaNegocio`/`fechaProceso` (ISO 8601 UTC0), `moneda`="ARS", `importeBruto` (double), `estadoTransaccion` ("ACREDITADO"/"RECHAZADA"/"DEVUELTA").

**`Vendedor`:** `cuentaVendedor` (CBU/CVU o número de cuenta), `identificadorVendedor` (CUIT del comercio), `codigoCaja`, `informacionesAdicionales` (obligatorio incluir `{"Key":"MCC","Value":"xxxx"}`).

**`Comprador`:** `identificadorPagador` (DNI/CUIT, opcional), `cuentaPagador` (últimos 4 dígitos del PAN o cuenta, opcional), `descripcionPagador` (opcional).

Ejemplo de request:
```json
{
   "Operacion":{
      "idMensaje":"{{guidV4}}", "identificadorProcesador":"GUID-BS20LIQ-{{guidV4}}",
      "identificadorTransaccion":"0000532608700006408432", "identificadorOrdenVenta":"0000532608700006408432",
      "identificadorReferencia":"766b6119-fcd2-4fff-bd76-f1b3109ef48743", "pagoUnico":false,
      "tipoTransaccion":"Liquidador", "rubroMovimiento":"PAGO", "rubroTransaccion":"Liquidador",
      "procesadorPago":"DECIDIR", "formaPago":"TRANSFER",
      "fechaNegocio":"2026-01-09T18:45:34.302Z", "fechaProceso":"2026-01-09T18:45:36.2256636Z",
      "moneda":"ARS", "importeBruto":3512.0, "estadoTransaccion":"ACREDITADO"
   },
   "Vendedor":{
      "cuentaVendedor":"322-20-1-735135-8-5", "identificadorVendedor":"20322678275",
      "codigoCaja":"B00000623451", "informacionesAdicionales":[{"Key":"MCC", "Value":"3333"}]
   },
   "Comprador":{
      "identificadorPagador":"20415865091", "cuentaPagador":"0000532609240002744097",
      "descripcionPagador":"Nicolás Colón"
   },
   "InformacionAdicional":[]
}
```

Ejemplo de response:
```json
{
    "liquidador_id_trx": "1323519", "id_procesador": "GUID-BS20LIQ-ea09305d-37de-46b6-abc3-59ff3b79b3f2",
    "id_billetera": 0, "fecha_negocio": "2026-01-13T00:00:00",
    "validation_data": { "payment_reference": "YY0113T0001323519O0000000000", "codigo_postal": "C1006ACT", "mcc": "5734" },
    "transaction_status": { "status": "PASS", "on_error": null }
}
```

## 2. Qué es el Liquidador — histórico de clientes (Traditum y Newpay PMC)

> Relevado de 2 Epics históricas de Notion: "Liquidador para traditum" y "Newpay PMC MVP". El producto **Liquidador** sirve a clientes que **cobran por su cuenta** (con su propio procesador/medio) y le piden a Bind PSP **únicamente el cálculo de impuestos/comisión y la liquidación neta al comercio** — Bind nunca procesa el cobro en sí, solo recibe el aviso de la transacción ya definitiva.

### Cliente: Traditum (primer cliente, PSP Argenpay)

- Traditum cobra con tarjeta por su cuenta y le pide a Bind PSP que le calcule la liquidación; paga a sus comercios por transferencia a través del **banco Macro**, usando la información que Bind le entrega.
- Plazo de liquidación y comisión configurables **por medio de pago y por comercio**.
- Endpoint de aviso soporta `ACREDITADO` desde el MVP; `RECHAZADA`/`DEVUELTA` se agregaron después. Reglas de devolución: si ocurre el mismo día de negocio de la transacción original, se elimina el cálculo y no aparece en el batch `DEVBOTON`; si es otra fecha, sí se incluye. Solo se admiten devoluciones **totales** para canales que no sean QR.
- **Archivos generados para el banco Macro** (misma lógica que `BOTONLIQ`, un registro por liquidación de comercio del día): **`BNF.TXT`** (Beneficiarios: CUIT/razón social/domicilio/código de ente, reenvía todos los comercios cada vez — ticket cancelado, no llegó a implementarse); **`OPG.TXT`** (Órdenes de Pago: formato de longitud variable separado por tabulaciones, incluye CUIT, id de liquidación, importe con coma decimal, CBU, código de método de pago derivado del prefijo del CBU); archivo de **Retenciones** (ticket cancelado, sin desarrollo confirmado).

### Cliente: Newpay PMC (segundo cliente, mismo producto)

Caso más complejo que Traditum: PMC define su propio diseño de archivo de entrada y salida, y el procesamiento corre por lotes.

- **Input**: PMC envía diariamente (10 AM) un archivo con las transacciones a liquidar ya calculadas (Bind no calcula plazo ni comisión) + archivo separado de alta de "entes" (comercios).
- **Mapeo de códigos externos**: diccionario `DominioExterno` por Comercio (código principal/secundario/sucursal/caja/dispositivo) y `EntidadDominioExterno` a nivel Entidad, para que PMC referencie sus propios códigos.
- **Procesamiento por lotes en la tarde**: liquida antes de las 18hs lo recibido a las 10hs, filtrado a transacciones/comercios de PMC, valida que todas tengan el impuesto calculado antes de correr. Genera archivos propios de PMC + archivos batch estándar de Bind (`boton`, `botonliq`, `botontax`).
- **Cálculo de impuestos por lote** (Canal+Entidad): infraestructura nueva para calcular impuestos de un lote completo de una vez, prerequisito del batch de la tarde.
- **Procesamiento asíncrono**: cola dedicada por canal (`LQ_PMC`), validado con pruebas de estrés (10 tx/seg) antes de producción.
- **Salida**: PDF de liquidación en **HTML** (no el PDF estándar), configurable por Entidad.
- **Permitir más de un comercio con el mismo CUIT**: parametrizable por Entidad — necesidad de PMC, que puede tener múltiples "entes" bajo el mismo CUIT.
- **Rollout operativo real**: alta de comercios de PMC vía Excel curado a mano, validación de reglas de impuestos por entidad, y un proceso de "borrado completo" documentado para reprocesar un archivo cargado por error (borra de Transaccion, Liq_imp, ServiceProcess, Pago Externo, Liquidación, Retención, storage del archivo, y lotes de ingreso/egreso de Siscri).

## 3. PMC: Mantenimiento (9 tickets — cola de mejoras)

> Fuente: Epic Notion "[EPIC] PMC: Mantenimiento" (Tipo Dolor). Ingesta MANT, 2026-07-06.

- **Deduplicación de transacciones**: id único por transacción (`idprocesador`), luego mejorado concatenando nombre de archivo + posición/nro de fila (el id original no distinguía todos los casos).
- **Retenciones**: comprobantes de retenciones por rango de fechas, apertura de retenciones/percepciones en liquidación a empresas.
- **Liquidaciones por comercio**: capacidad de generar liquidaciones segmentadas por comercio (no solo agregadas).
- **Procesamiento de Transacciones Externas (TE)**: debía devolver resultados detallados por registro, garantizando que se procesaran todos los registros correctos del lote aunque alguno fallara.
- **Integración con Centralizador/SISCRI**: endpoint para actualizar datos de comercio en ambos dominios en una sola operación.
- **Automatización pendiente**: "Automatizar que generar el TLE genere todo lo demás" quedó Pendiente — el operador todavía dispara varios pasos manuales.

## Ver también
- [devoluciones_y_contracargos.md](devoluciones_y_contracargos.md) — devoluciones/contracargos del cobro propio de Bind PSP (producto distinto).

---
*Última actualización: 2026-08-12 — Extraído de `detalle_productos/adquirencia/liquidaciones_y_devoluciones.md` (reestructuración PARA en cascada) por ser un producto/tema distinto (Liquidador para terceros). Contenido sin cambios de fondo.*
