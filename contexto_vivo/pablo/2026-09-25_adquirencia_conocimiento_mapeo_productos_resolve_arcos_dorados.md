---
id: 2026-09-25_adquirencia_conocimiento_mapeo_productos_resolve_arcos_dorados
pm: pablo
fecha_captura: 2026-09-25
fuente: "Proyecto PRD-216 (Arcos Dorados: mapear productos de la orden de venta en items del Resolve), finalizado 2026-09-25 — cierre vía /idea_finish. Contenido técnico extraído del comentario de QA en AD-1434 (2026-08-07, nunca antes volcado a la wiki) y de proyecto.md §3"
producto: adquirencia
tema: mecánica real del mapeo de productos de la orden de venta en el /resolve (lectura de QR), incluyendo la validación de cuadratura y las limitaciones conocidas descubiertas en QA
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/botones_de_pago_y_qr.md, sección "Gap de mapeo en la lectura de QR: productos, sucursal y terminal (cliente Arcos Dorados, 2026-07-22)" — agregar como subsección "Resultado final (2026-08-31) — corrección entregada" a continuación de la nota "Próximo paso" existente, antes del separador
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9fbee64
---

> Fuente: Proyecto PRD-216, finalizado 2026-09-25. Detalle técnico real extraído del comentario de QA en el ticket de desarrollo AD-1434 (2026-08-07) — nunca antes reflejado en la wiki, solo descubierto al hacer el relevamiento completo de Jira para el cierre formal.

La sección existente sobre el gap de Arcos Dorados (2026-07-22) documenta el descubrimiento y la decisión de arreglarlo, pero no el resultado. Agregar lo siguiente a continuación de esa sección, antes de archivar el proyecto:

### Resultado final (2026-08-31) — corrección entregada en AD-1434

El mapeo de productos del `/resolve` (`PaymentAcceptor.Iep`) se corrigió y liberó en la versión AD 72 (2026-08-31). En vez de devolver un único ítem sintético hardcodeado, ahora itera `ov.Productos` y arma un `Item` por producto (1:1), solo para órdenes en estado `closed_amount` (en `open_amount`/`pending` sigue devolviendo `items = []`, no `null` como describía el criterio de aceptación original — el payload real siempre lleva array, según especifica CIMPRA 525).

**Mapeo de campos:**

| Campo del item | Origen | Nota |
|---|---|---|
| `title` | `p.Codigo` si tiene valor | Fallback si null/vacío: `"Producto " + (caja.NombreFantasia ?? caja.Nombre)` |
| `description` | `p.Descripcion` | |
| `unit_price` | `(double)p.Monto` | Cast decimal→double |
| `quantity` | `p.Cantidad` | |
| `currency_id` | `"ARS"` | Hardcode |
| `picture_url` | `null` | Viaja como `null` explícito en el JSON (por especificación de CIMPRA), no se omite del payload |

**Cambio de comportamiento no anticipado en el análisis original (descubierto en QA, 2026-08-07):** `ValidarYProcesarProductos` dejó de descartar en silencio los productos inválidos cuando `RequiereProductos=false`. Ahora valida siempre (descripción no vacía, monto > 0, y que `sum(Monto × Cantidad) == MontoTotal`) y **rechaza la creación de la orden con HTTP 422** si no cuadra — antes la orden se creaba igual con los productos inválidos descartados. Aplica con cualquier valor de `RequiereProductos`. Sin problemas detectados en clientes tras casi un mes en producción (verificado al cierre, 2026-09-25) — decisión explícita de no comunicar este cambio a Soporte ni a los comercios, por ser el comportamiento correcto reemplazando al bug.

**Efecto colateral en un endpoint de consulta relacionado:** `GET .../ultima-orden-venta` cambia su respuesta aunque no se tocó su código — con `RequiereProductos=false` pasa de devolver `productos: []` a devolver el detalle completo. Los otros 3 `GET` de orden de venta no cambian.

**Limitaciones conocidas (confirmadas por QA, no van a corregirse — no confundir con "pendiente"):**
- **Truncado a 50 caracteres:** por especificación de CIMPRA, `title` y `description` se cortan a 50 caracteres sin aviso al emisor si el `Codigo`/`Descripcion` original del producto es más largo.
- **QR de Deuda no lee productos:** a diferencia de la Orden de Venta, la lectura de QR de Deuda no lee `Deuda.ProductosJson` — sintetiza un único item con el motivo y el monto de la deuda. Fuera de alcance de esta corrección.
- **`POST /orden-venta` con múltiples productos:** las órdenes creadas por ese endpoint devuelven N items en el `/resolve`, pero todos con el mismo `title` y sin `quantity` — inconsistente con el mapeo de arriba, discutir con negocio si amerita alinearse a futuro.

**Defectos colaterales detectados en QA, migrados a otro proyecto:** 2 defectos del webhook de pago (no informa `CodigoProducto`; omite el array `Productos` si el código/descripción es muy largo) se migraron al cierre (2026-09-25) al proyecto Ministerio de Justicia (Epic AD-374, PRD-134) por ser el mismo mecanismo de productos en transacciones — seguimiento ahí, no en este proyecto ya archivado.

**Testing:** 7 casos de test explícitos como subtareas de AD-1434 (un producto, múltiples productos, fallback de `Codigo` faltante, estados no cerrados devuelven `items` vacío, independencia de `RequiereProductos`, validación 422 de cuadratura, truncado a 50 caracteres) — todos Finalizados, sin regresiones detectadas.

Ver también la entrada de esfuerzo real en `2_areas/procesos/referencia_estimaciones.md` (item de contexto_vivo del mismo cierre, `2026-09-25_adquirencia_esfuerzo_real_prd216`).
