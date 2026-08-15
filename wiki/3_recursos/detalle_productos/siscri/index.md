# Detalle de Producto — SISCRI

> Conocimiento detallado de producto: mecánica interna, manuales de configuración/integración y hacks operativos de SISCRI. **No es la API pública oficial de Bind PSP** — Siscri no tiene API pública propia expuesta a clientes (accesorio interno de Adquirencia/Wallet).

## Qué es SISCRI

SISCRI es el **motor de cálculo de impuestos** interno de Bind PSP. Corre el cálculo de impuestos (IVA, IIBB, retenciones/percepciones según CUIT, domicilio, forma de pago y agente de retención) que precede al proceso de liquidación diaria a comercios. Conoce cada comercio/entidad porque estos se replican en SISCRI al crearse.

**Aplica tanto a Adquirencia como a Wallet, cada uno con su propia instancia de SISCRI** — no es una instancia única compartida, sino el mismo motor desplegado por separado para cada producto. Ver [wiki/0_direccion/producto/adquirencia_overview.md](../../../2_areas/overview_productos/overview_adquirencia.md#liquidaciones-e-impuestos-siscri) para el rol de SISCRI dentro del flujo de liquidación de Adquirencia.

## Archivos de este módulo

| Archivo | Contenido |
|---|---|
| [configuracion_entidades.md](configuracion_entidades.md) | Alta de parámetros por entidad en SISCRI vía Swagger (`alta_parametros`), casos de alta según CUIT (dos CUITs propios de Bind PSP documentados con bodies completos), configuración de parámetros por provincia (IIBB percepción/retención), verificación en base de datos (`SharedImpuestoDB_prd`), y body de ejemplo para alta de comercio. |
| [integracion_wallet.md](integracion_wallet.md) | Integración SISCRI↔Wallet (instancia orientada a Persona): modelo asíncrono no bloqueante, tipos de comprobante de impuesto (IMPD/IMPC/IMPS), reversa de impuestos por operación rechazada, retenciones (BD+API dedicada), y cluster de bugs de padrones provinciales desactualizados. Ingesta de la Epic histórica "Impuestos en Wallet". |
| [calculo_impuesto_online_qr.md](calculo_impuesto_online_qr.md) | Diagnóstico ad-hoc (2026-07-06) del flujo Transaccion→ServiceProcess→LIQ_IMP para QR + Plazo 0: mínimo real de segundos pero mediana ~1,71h y máximo 5,38h (alta varianza, no "casi instantánea"), con evidencia de ráfagas de backlog puntuales y cadencia tipo batch/cron; 4 transacciones ACREDITADO sin cálculo de impuesto y 1 DEVUELTA con cálculo indebido; más análisis de volumen/throughput (tx por minuto, pico vs. valle horario) para dimensionar el procesamiento por lotes. **§7: decisión de diseño confirmada para el caso PedidosYa** (2026-07-16) — modelo por lotes parametrizable, prioridad a transacciones online, pago diferido fuera de alcance, alcance técnico de AD-1383. |
| [volumetria_transaccional_dimensionamiento_lotes.md](volumetria_transaccional_dimensionamiento_lotes.md) | Análisis ad-hoc (2026-07-07) de volumetría sobre muestra de 100.000 transacciones sin filtrar: distribución tx/minuto total vs. Plazo=0 vs. Plazo≠0 (percentiles, ventanas de 5/15 min, pico/valle horario), hallazgo de que `FormadePago=50` es una carga masiva de archivo (no tráfico real, cliente en baja) que distorsiona el cálculo si no se separa, con ambos escenarios documentados: "limpio" (sin F50, vigente a mediano plazo) y "transitorio" (con F50, picos de hasta ~3.041 tx/min mientras ese cliente siga activo). |

| [hallazgos_operativos_historicos.md](hallazgos_operativos_historicos.md) | Sincronización con comercios (bug provincia Santa Fe por defecto), certificados de retenciones, CSV para PMC, spikes de investigación de RabbitMQ/creación de comercios. Consolidado desde 2 archivos-cola de `detalle_productos/transversal/` (2026-08-12). |

## Ver también

- [detalle_productos/adquirencia/](../adquirencia/) — usa SISCRI para el cálculo de impuestos previo a la liquidación de comercios.
- [detalle_productos/wallet/](../wallet/) — tiene su propia instancia de SISCRI (contraparte de este módulo del lado Wallet).

---
*Última actualización: 2026-07-17 — `/sync_mails`: `calculo_impuesto_online_qr.md` §7 — decisión de diseño confirmada para PedidosYa (modelo por lotes parametrizable, prioridad online) que cierra el diagnóstico de latencia con una resolución concreta.*
*Última actualización anterior: 2026-07-07 — Agregado `volumetria_transaccional_dimensionamiento_lotes.md` (análisis de tx/minuto total vs. Plazo=0 sobre muestra de 100k, para dimensionar lotes).*
