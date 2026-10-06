---
id: 2026-10-02_conocimiento-convencion-camelcase-y-excepcion-pascalcase-webhook-ccl
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Charla directa con el PM durante /idea_solution de inter_trazabilidad_ccl (PRD-259), 2026-10-02"
producto: wallet
tema: Convención de nombres de las APIs (camelCase) y excepción deliberada del webhook de Dólar CCL (PascalCase); diseño aprobado para sumarle fechas
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_ccl.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

**Convención de nombres.** Según Nicolás Colón (2026-10-02), la directiva general de Bind PSP para los campos de las APIs es **camelCase**. El GET de intención de Dólar CCL la cumple (`fechaHoraCreacion`, `montoObtenido`). El **webhook de aviso de Dólar CCL** (`COMPRA_DOLAR_CCL` / `VENTA_DOLAR_CCL`) quedó en **PascalCase** (`MensajeId`, `OperacionId`, `MontoInvertido`, según el portal público de developers). El PM decidió **mantener esa excepción**: los campos nuevos que se le sumen al webhook siguen su estilo actual, para no mezclar estilos en el mismo payload ni romper a los consumidores.

**Diseño aprobado, todavía sin construir (PRD-259, pedido de Inter, lo paga el cliente).** Se van a sumar al final del payload del webhook de Dólar CCL 8 fechas que hoy solo expone el GET de intención: `FechaHoraCreacion`, `FechaHoraVencimiento`, `DdjjAceptadaFechaHora`, `FechaHoraCreacionEnBroker`, `FechaHoraOperacionUltimoStatus`, `FechaHoraFinalizacionIntencion`, `FechaHoraFinalizacion`, `FechaHoraUltimaModificacion`.
- Llevan valor y formato **idénticos al GET**, sin normalizar.
- Usan `null` explícito cuando el dato no existe todavía.
- Aplican a todos los operadores (modelos Standard/INTE y COMBI) y a compra y venta.
- El cambio es aditivo, sin eventos ni estados nuevos.

**Hechos técnicos relevados en el análisis, útiles para la documentación del producto:**
- **El formato de fechas del GET de intención es inconsistente.** En una respuesta real de staging (2026-10-01), 6 fechas vienen en UTC con offset (`+00:00`) y 2 sin offset:
  - `fechaHoraFinalizacion` está en UTC: mismo valor que `fechaHoraFinalizacionIntencion`, y Poincenot devuelve `endOperationDate` en UTC.
  - `ddjjAceptadaFechaHora` es el valor que manda la organización al ejecutar, sin offset; en el ejemplo, en hora Argentina.
- **Ninguna fecha de la intención registra la finalización real.** `fechaHoraFinalizacionIntencion` y `fechaHoraFinalizacion` son el fin *esperado*, calculado al crear la intención a partir del preview del broker. El momento real del cierre lo dan `fechaHoraOperacionUltimoStatus` y `fechaHoraUltimaModificacion`.
- **`fechaHoraOperacionUltimoStatus` viene `null`** en una intención `EN_PROCESO`, antes del primer aviso del procesador.

Al publicarse el cambio, `/sync_web` va a levantar los campos nuevos del portal. Este item documenta el *por qué* del estilo y del formato, que el portal no explica.
