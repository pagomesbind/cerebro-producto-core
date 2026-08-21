# Pedidos de Clientes y Hallazgos Operativos Históricos — Portal Admin

> Estado: mezcla de en producción y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde 4 archivos-cola de `detalle_productos/transversal/` (`pedidos_puntuales_de_clientes.md`, `dolores_soporte_y_administracion.md`, `defectos_encontrados_en_qa.md`, `reporteria_operativa.md`) que mezclaban pedidos de varios productos y del Portal Comercio en un solo archivo — ver [`portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md`](../portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md) para lo específico del portal de comercios.

## Pedidos puntuales por cliente

- **Spena**: totalizadores de volumen/cantidad de transacciones filtrados en el Admin.
- **Desarrollo del Litoral**: ocultar comisiones e impuestos del Portal para roles Supervisor y Operador (permisos granulares por rol), y mostrar el ID Coelsa del split en el Admin (Pendiente).

## Herramientas de recuperación manual de transacciones (pedidos de Soporte)

- Endpoint para recuperar (forzar a `ACREDITADO`) una transacción `RECHAZADA`, recalculando fechas para que liquide en el próximo ciclo.
- Poder recuperar y reintentar una transacción de POS que "no está en TRX" (se perdió en el camino) — mismo patrón de herramienta para Botón Simple.
- Endpoint para **eliminar transacciones** (la herramienta más drástica del cluster, nunca cerrada — quedó en "Refinar").
- Rehabilitar completo un comercio (+ su cuenta Wallet) que quedó deshabilitado.

## Access Management y seguridad operativa (mecánica funcional — el hardening de seguridad vive en arquitectura_sistema)

- **Gestión de bloqueos** por múltiples accesos fallidos: se construyó una pantalla de gestión de bloqueos (front+back) porque Soporte no podía atender bien el reclamo de un usuario bloqueado.
- Ver el rol de un usuario en la grilla y el detalle de usuarios del Admin (antes no era visible, dificultaba el soporte de permisos).
- "Olvidé mi contraseña" en el login de Admin, y bugs de recuperación de contraseña (se permitía cambiar a una que no cumplía requisitos de seguridad; no redirigía al login tras completar el cambio).
- Auditoría de APIs de comercio: persistir en una tabla de auditoría cada alta/baja/modificación de datos sensibles de comercio, con fecha, endpoint, url, body, response, JWT y usuario de Access Management.
- **AccessManagement 2.0**: migración de modelo de permisos 1:1 por Organización a modelo de plantillas reutilizables (RolTemplate/PermisoTemplate) + esquema Miembro-MiembroOrganizacion-MiembroRol; ABM de roles/usuarios por Entidad desde el Admin; soporte multi-aplicación (antes hardcodeado a una sola app). Ver también hardening de seguridad relacionado en [3_recursos/arquitectura_sistema/hardening_y_remediacion_de_pentests.md](../../arquitectura_sistema/hardening_y_remediacion_de_pentests.md).

## Trazabilidad de datos ("que se vea X")

Patrón repetido de campos que existían en el sistema pero no eran visibles donde Soporte los necesitaba: marca de tarjeta + tipo de cuota en el detalle de transacción, columna de Nombre/Razón Social del comprador, Descripción/Razón Social en la grilla de comercios, nombre de fantasía en perfil y en grilla de comercios, ID Split visible en el Admin y en un archivo descargable, primeros 6 y últimos 4 dígitos de la tarjeta en POS, versión del POS agregada al ticket de soporte.

## Motor de reportería operativa (CSV y HTML)

Reportes de **Transacciones, Movimientos, Comercios y Cuentas** para Admin. No confundir con la reportería regulatoria BCRA/Worldsys (ver [`3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md`](../../cumplimiento_normativo/reporteria_worldsys_bcra.md)) — esto es reportería operativa interna.

- **Arquitectura**: servicio genérico de generación de reportes CSV con ABMs de `ReporteTemplate`/`Parámetros`/`Pasos`, con 3 dominios integrados en orden (Movimientos → Comercios → Transacciones) y generación **asíncrona** obligatoria para reportes grandes (no podían resolverse en el ciclo de un request HTTP síncrono).
- **Pendiente sin cerrar**: Reportes CSV de Cuentas quedó en "Refinar", no llegó a desarrollarse como los otros 3 dominios.

### ⚠️ Filtro por Entidad roto — bug recurrente (3 apariciones confirmadas)

Un usuario logueado como Entidad no ve sus reportes de Comercios/Movimientos filtrados correctamente — falla repetida en más de un reporte, indicando que la lógica de scoping por entidad **no está centralizada** sino reimplementada por reporte. Confirmado 3 veces de forma independiente: reporte de Movimientos, reporte de Comercios, y en QA antes de producción un reporte de Transacciones filtrado por la Entidad PCQA devolvió datos de TODAS las entidades. **Si se plantea una refactorización de scoping/autorización por Entidad, este historial es evidencia de que conviene centralizarlo en una sola capa en vez de seguir parchando reporte por reporte.**

### Otros bugs recurrentes de reportería
- Formato de datos regional incorrecto: importes con separador de miles en punto en vez de coma, fechas ordenadas ascendente en vez de descendente, caracteres rotos (encoding) en el reporte de comercios.
- Campos que no traen datos: campo "procesador" vacío, campo "comercio" vacío en un caso puntual al generar con usuario de Entidad.
- UX: falta ícono más descriptivo para el botón de reporte; "Generar reporte" no redirige tras completarse; "TRANSACCIONES" aparecía duplicada en el menú de Admin.

## Refactorización de permisos (mantenimiento)

Ticket XL de refactorización de permisos del Portal, el más grande de la muestra relevada de la Epic de mejoras técnicas — quedó "Listo para desarrollo" al cierre del relevamiento.

## Parametrización manual y fragmentada de entidades (reunión "Parámetros de entidades", 2026-08-19)

> Estado: en producción / discovery — el problema es operativo hoy, la solución (orquestador vía API) todavía no está construida ni priorizada formalmente por Producto (ver nota más abajo).

**Problema identificado:** los incidentes frecuentes en producción derivan de configuraciones manuales y fragmentadas entre entidades — no hay documentación clara y centralizada de qué parámetros hace falta configurar por producto/entidad, lo que complica la gestión operativa y compromete el aseguramiento de calidad (QA).

**Caso concreto:** Mastercard (integración cross-border/pagos al exterior) es de los productos de alto volumen que hoy se configuran manualmente sin plantilla documentada — mientras no exista una API de configuración, se van a elaborar plantillas documentadas con los parámetros necesarios para su configuración manual, como paliativo.

**Dirección técnica discutida en la reunión:** desarrollar un orquestador vía APIs para automatizar la configuración de entidades, usando ~50 parámetros estandarizados, en lugar de invertir en modificar directamente el panel de administración actual. **Nota (2026-08-20):** esta dirección se discutió en una reunión técnica sin participación formal de Producto — no corresponde leerla como decisión de roadmap vigente; ver la entrada del 2026-08-19/2026-08-20 en [`2_areas/direccion/decisiones.md`](../../../2_areas/direccion/decisiones.md) para el detalle de la corrección.

**Próximos pasos acordados en la reunión:**
- Unificar toda la documentación de configuración de entidades en un repositorio centralizado.
- Relevar los pasos necesarios para parametrizar cada producto con los referentes de cada área.
- Definir una rutina estándar de alta de entidades ejecutable por API o interfaz.
- Recopilar los requerimientos operativos por canal y convenio para reducir la complejidad actual.
- Investigar qué falta en el panel de administración actual para poder crear y configurar entidades correctamente en producción.

## Ver también
- [portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md](../portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md) — mismo tipo de contenido, para el Portal de Comercios.
- [3_recursos/arquitectura_sistema/hardening_y_remediacion_de_pentests.md](../../arquitectura_sistema/hardening_y_remediacion_de_pentests.md) — remediaciones de seguridad sobre Access Management derivadas de pentests.

---
*Fuente: Epics Notion "Dolores de clientes", "Dolores de Soporte y administración", "Defectos encontrados en QA" y "Reporting" (111 SP, 39 tickets) — ingesta 2026-07-06.*
*Última actualización: 2026-08-19 — nueva sección "Parametrización manual y fragmentada de entidades" (reunión "Parámetros de entidades").*
*Última actualización anterior: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Portal Admin de 4 archivos-cola de `detalle_productos/transversal/`.*
