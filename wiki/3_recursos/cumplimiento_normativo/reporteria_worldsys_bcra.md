# Reportería Antilavado a Worldsys (BCRA)

> Estado: en producción. Contenido destilado de 2 Epics de Notion del grupo Transversal/Normativo (integración base + bug de mapeo de datos), más una actualización desde reunión de 2026-07-29. Reubicado desde `detalle_productos/transversal/cumplimiento_normativo.md §1-2` en la reestructuración PARA en cascada (2026-08-12).

## 1. Integración base — qué se informa y cómo

Bind PSP debe informarle diariamente al banco (vía **Worldsys**, un proveedor/canal intermedio hacia BCRA) un conjunto de archivos CSV con novedades de "prevención de lavado de dinero" (PLD), tanto del lado **Wallet** (cuentas) como del lado **Adquirencia** (comercios de cobro). Esta es la integración original (MVP); la Epic histórica "Worldsys etapa 2: separar SUR FIN" extendió este mismo mecanismo para reportar a SUR FINANZAS como entidad normativamente separada (ver ficha de cliente en [2_areas/clientes/](../../2_areas/clientes/index.md)).

### Mecánica común a los 5 tipos de archivo

Cada uno de los 5 reportes se genera **por separado para comercios (Adquirencia) y para cuentas (Wallet)** — 10 combinaciones en total:

| Reporte | Contenido | Nombre de archivo |
|---|---|---|
| LAVADOOPERACIONES | Transacciones de cobro del día anterior | `LAVADOOPERACIONESCOMERCIOS` |
| LAVADOCLIENTES | Altas/modificaciones/bajas de comercios o cuentas | `LAVADOCLIENTESCOMERCIOS` / `LAVADOCLIENTESCUENTAS` |
| LAVADONOMINAS | Nómina de titulares de comercios/cuentas | `LAVADONOMINASCOMERCIOS` |
| LAVADODOMICILIOS | Domicilios de comercios/cuentas | `LAVADODOMICILIOSCOMERCIOS` |
| LAVADOACTIVIDADES | Actividad económica de comercios/cuentas | `LAVADOACTIVIDADESCOMERCIOS` / `LAVADOACTIVIDADESCUENTAS` |

- **Cadencia**: se genera un archivo todos los días a la madrugada, informando la fecha de negocio del día anterior (`Fecha de generación = X`, `Fecha de negocio = X-1`).
- **Formato**: CSV con columnas separadas por punto y coma; si un dato no está disponible, la columna queda vacía; se debe respetar longitud máxima y formato de cada campo según el diseño de Worldsys.
- **Entrega**: el archivo se deja en un **FTP de Worldsys**; internamente se conserva además una copia con fecha para trazabilidad propia, distinta de la copia sin fecha que se sube al FTP.
- **Origen técnico previo**: un Spike ("Generación de csv") de investigación/POC precedió al desarrollo real de los generadores de archivo.

### Enriquecimiento de datos para la Matriz de Riesgo

A pedido del equipo de PLD (prevención de lavado) del banco, se agregaron campos adicionales a comercios y cuentas para poder completar los archivos correctamente:
- **País/nacionalidad** de comercio y de cuenta (formato ISO, opcional en el alta, default `AR` si no se envía).
- **Condición PEP, UIF y FATCA** de cuenta (booleanos, default `false` si no se envía).

### Ajustes post-revisión con el banco

- Los campos de importe de `LavadoOperaciones` (`EspecieTransadaCantidad`, `MontoMonedaLocal`) debían aceptar tanto separador decimal punto como coma (se recomendó seguir usando punto).
- El campo `FormaJuridica` de `LavadoClientes` pasó a ser opcional (se envía vacío).
- El código postal de `LavadoDomicilio` se extrae de fuentes distintas según el dominio: `WalletCuentaDB.dbo.CuentasDomicilios.[CP]` para cuentas, `SharedComercioDB.dbo.Direcciones.[CodigoPostal]` para comercios — con lógica para detectar si el valor es un CP simple (4 dígitos) o un CPA (letra + 4 dígitos + 3 letras), extrayendo en ese caso solo los 4 dígitos numéricos.

## 2. Integridad de `LAVADOOPERACIONES`: comprobantes vs. movimientos, y tratamiento de reversas (sin resolver, 2026-07-16)

> Fuente: reunión "Producto" (2026-07-16), minuta Gemini.

Surgió un conflicto de diseño sin resolver sobre qué universo de datos debe alimentar `LAVADOOPERACIONES`:
- **Postura interna (Pablo Gomes):** la tabla de **comprobantes** debe ser la única fuente de verdad — es la que efectivamente registra el 100% de los movimientos que alteran el saldo de una CVU. La propuesta es informar el 100% de los comprobantes y dejar que el área de PLD decida qué excluir, en vez de que Bind PSP pre-filtre qué reportar (riesgo de omitir información crítica por una selección propia).
- **Lo que el área de PLD dijo textualmente en una reunión previa (según Emma Vignoles):** que quieren **movimientos de dinero**, no comprobantes — sugiere que su modelo mental no incluye el concepto de reversa (ej. tratan cualquier registro como definitivo, sin lógica de neteo).
- **Problema técnico concreto:** Worldsys (vía SOS) **no puede interpretar una reversa referenciando el ID de comprobante original** — la propuesta explorada es reportar el mismo ID de comprobante original con el monto en negativo para netear, pero el equipo lo considera riesgoso (con volumen alto, es fácil que falte un registro de reversa y quede un saldo negativo fantasma sin explicación). Se está evaluando en cambio agregar **un campo nuevo con el ID de comprobante relacionado** para poder identificar la reversa sin alterar el monto de la transacción original.
- **Casos que complican la definición:** ajustes de saldo virtuales sin movimiento de dinero real (ajustes BCF), transferencias entrantes que generan débito automático (BCF), y transacciones fallidas al instante (no deberían informarse, a diferencia de una reversa el día siguiente).
- **Estado:** sin resolver — pendiente coordinar una reunión conjunta entre Producto, PLD/Compliance y el equipo de Worldsys/Word para definir el criterio de integridad de una vez. Bloquea el avance de Nicolás Colón en el ticket que detalla el archivo de comprobantes de Worldsys — lleva ~2 meses sin poder avanzar por falta de esta definición.

## 3. Bug de mapeo — códigos de actividad/ocupación

El archivo `LAVADOACTIVIDADESCUENTAS` no mapeaba correctamente los códigos de actividad/ocupación de ciertas cuentas — por ejemplo, no se enviaba el código 9 ("Ama de casa") ni el código 12 ("Desocupado") para cuentas que sí tenían esa condición. Bug puntual sobre la mecánica descrita en §1, no una funcionalidad nueva.

## Ver también

- [limites_operativos_uif_ros.md](limites_operativos_uif_ros.md) — topes operativos que Compliance usa para decidir cuándo pedir documentación adicional, mismo dominio normativo.
- [pci_dss_recertificacion.md](pci_dss_recertificacion.md) — otra obligación normativa de Bind PSP, independiente de esta.
- [2_areas/direccion/decisiones.md](../../2_areas/direccion/index.md) — decisión relacionada a límites de segmento de cliente.

---
*Fuente: Notion histórico, Epics "Integración con Worldsys MVP" (44 tickets) y "Más datos en las cuentas para BCRA y Worldsys" (1 ticket) — ingesta 2026-07-06. Triage de "Integración con Worldsys MVP" no exhaustivo por volumen y alta repetitividad de los tickets (mismo patrón de archivo diario replicado 10 veces); varias URLs del backlog de la Epic resultaron ser páginas de Pruebas/QA o páginas eliminadas (404), no tickets de desarrollo reales.*
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/cumplimiento_normativo.md §1-2` (reestructuración PARA en cascada). Contenido sin cambios.*
