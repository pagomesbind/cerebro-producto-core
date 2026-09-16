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

## 2. Integridad de `LAVADOOPERACIONES`: comprobantes vs. movimientos, y tratamiento de reversas (resuelto, entra en vigencia 2026-10-01)

> Fuente: reunión "Producto" (2026-07-16), minuta Gemini; hilo de mail "Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas." (2026-06-04 a 2026-09-15).

Surgió un conflicto de diseño sobre qué universo de datos debe alimentar `LAVADOOPERACIONES`:
- **Postura interna (Pablo Gomes):** la tabla de **comprobantes** debe ser la única fuente de verdad — es la que efectivamente registra el 100% de los movimientos que alteran el saldo de una CVU. La propuesta es informar el 100% de los comprobantes y dejar que el área de PLD decida qué excluir, en vez de que Bind PSP pre-filtre qué reportar (riesgo de omitir información crítica por una selección propia).
- **Lo que el área de PLD dijo textualmente en una reunión previa (según Emma Vignoles):** que quieren **movimientos de dinero**, no comprobantes — sugiere que su modelo mental no incluye el concepto de reversa (ej. tratan cualquier registro como definitivo, sin lógica de neteo).
- **Problema técnico concreto:** Worldsys (vía SOS) **no puede interpretar una reversa referenciando el ID de comprobante original** — la propuesta explorada es reportar el mismo ID de comprobante original con el monto en negativo para netear, pero el equipo lo considera riesgoso (con volumen alto, es fácil que falte un registro de reversa y quede un saldo negativo fantasma sin explicación). Se está evaluando en cambio agregar **un campo nuevo con el ID de comprobante relacionado** para poder identificar la reversa sin alterar el monto de la transacción original.
- **Casos que complican la definición:** ajustes de saldo virtuales sin movimiento de dinero real (ajustes BCF), transferencias entrantes que generan débito automático (BCF), y transacciones fallidas al instante (no deberían informarse, a diferencia de una reversa el día siguiente).

**Resolución (cronología completa, discovery técnico con Worldsys 2026-06-04 a 2026-09-15):**

1. **Reunión inicial (03/06/2026, minuta de Leandro Competiello — Worldsys/PMO):** se acuerda evaluar cómo incorporar ~500 nuevos tipos de comprobante y cómo distinguir reversiones/devoluciones/contracargos/rechazos de operaciones originales, sin duplicar impacto en los acumuladores de alertas PLD.
2. **Intercambio técnico (09/06 y 06/07/2026, Pablo Stach — Worldsys):** se descarta la opción de matchear la reversión contra el registro original ya persistido y restarle el monto — Compliance One (el motor de ingesta de Worldsys) **no soporta operaciones aritméticas contra registros ya cargados**, solo importa lo que viene en el archivo de entrada. Se confirma como única vía viable: **enviar la reversión como un registro nuevo e independiente, con monto negativo**, siempre que viaje el CUIT/CUIL. No hace falta que el sistema catalogue el registro como "reversión" — alcanza con que el monto negativo figure en el listado para que el acumulador dé el neto correcto. Riesgo de timing reconocido y aceptado: si la reversión se informa después del cierre del procesamiento mensual de alertas, ese período no la descuenta (queda para el siguiente).
3. **Archivo de ejemplo (01/09/2026, Nicolás Colón):** se envía a Worldsys el archivo con los 3 cambios esenciales acordados — (a) cambio de `IdOperacion` por `IdComprobante` en el campo `NUMEROOPERACION` (imperceptible para Worldsys), (b) reemplazo de la lista fija de `TIPOOPERACION` por la nueva interfaz `TiposComprobantes` (alimentada periódicamente), (c) inserción de registros de devolución con monto negativo.
4. **Confirmación de recepción (10/09/2026, Pablo Stach):** Worldsys confirma que recibió el archivo de ejemplo y arranca pruebas de ingesta.
5. **Escalamiento de urgencia (10/09/2026, Diego Scaldaferri, Gerente de Cumplimiento y Prevención de LA/FT/FP de BIND):** mientras el cambio no esté en producción, las reversas/devoluciones siguen sin netearse en los acumuladores de alertas PLD (riesgo de falsos positivos, o de que el criterio de "movimientos de dinero" que pedía PLD nunca haya distinguido una reversa de una operación real).
6. **Plan de implementación (15/09/2026, Leandro Competiello):** Worldsys confirma que el tema lo toma él junto con el Account Manager Gonzalo Quintana; es una evolución, no un cambio menor; coordinarán una prueba de captura en ambiente QA la semana del 21/09; **el nuevo esquema entra en vigencia a partir del procesamiento del 01 de octubre de 2026** (primera corrida del mes).

**Mecanismo final adoptado:** conviven dos piezas — el **monto negativo** (punto 2, netea el acumulador) y un **campo nuevo con el ID de comprobante relacionado**, `IdComprobanteRelacionado` (da trazabilidad al analista sobre cuál es la reversa de qué comprobante). Coincide con la alternativa que ya estaba documentada arriba como "se está evaluando".

> Fuente adicional: hilo de mail "Nuevo Requerimiento BIND (PSP) - Monitoreo de TRXs reversadas." (lcompetiello@worldsys.com.ar, pstach@worldsys.io, msimonetti@bind.com.ar, dscaldaferri@bind.com.ar, ncolon@bind.com.ar — 2026-06-04 a 2026-09-15).

## 3. Bug de mapeo — códigos de actividad/ocupación

El archivo `LAVADOACTIVIDADESCUENTAS` no mapeaba correctamente los códigos de actividad/ocupación de ciertas cuentas — por ejemplo, no se enviaba el código 9 ("Ama de casa") ni el código 12 ("Desocupado") para cuentas que sí tenían esa condición. Bug puntual sobre la mecánica descrita en §1, no una funcionalidad nueva.

## Ver también

- [limites_operativos_uif_ros.md](limites_operativos_uif_ros.md) — topes operativos que Compliance usa para decidir cuándo pedir documentación adicional, mismo dominio normativo.
- [pci_dss_recertificacion.md](pci_dss_recertificacion.md) — otra obligación normativa de Bind PSP, independiente de esta.
- [2_areas/direccion/decisiones.md](../../2_areas/direccion/index.md) — decisión relacionada a límites de segmento de cliente.

---
*Fuente: Notion histórico, Epics "Integración con Worldsys MVP" (44 tickets) y "Más datos en las cuentas para BCRA y Worldsys" (1 ticket) — ingesta 2026-07-06. Triage de "Integración con Worldsys MVP" no exhaustivo por volumen y alta repetitividad de los tickets (mismo patrón de archivo diario replicado 10 veces); varias URLs del backlog de la Epic resultaron ser páginas de Pruebas/QA o páginas eliminadas (404), no tickets de desarrollo reales.*
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/cumplimiento_normativo.md §1-2` (reestructuración PARA en cascada). Contenido sin cambios.*
