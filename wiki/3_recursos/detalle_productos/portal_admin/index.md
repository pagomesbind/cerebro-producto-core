# Detalle de Producto — Portal Admin

> Conocimiento detallado del Portal Admin (herramientas internas de Bind PSP para gestionar comercios, cuentas, reportería operativa y Access Management) que no es la API pública oficial de Bind PSP. Nace en la reestructuración PARA en cascada (2026-08-12) al desarmar `detalle_productos/transversal/`, que mezclaba este contenido con el de otros productos.

## Documentos de este módulo

| Archivo | Contenido |
|---|---|
| [pedidos_de_clientes_y_hallazgos_operativos.md](pedidos_de_clientes_y_hallazgos_operativos.md) | Herramientas de recuperación manual de transacciones, Access Management y AccessManagement 2.0, trazabilidad de datos, motor de reportería operativa (con el bug recurrente de filtro por Entidad), refactor de permisos, parametrización manual y fragmentada de entidades. |
| [accesos_qa_staging.md](accesos_qa_staging.md) | Credenciales de acceso de prueba al Admin en ambiente STAGING, para inspección visual en sesiones de QA/discovery — solo lectura, nunca acciones. |

## Ver también

- [detalle_productos/portal_comercio/index.md](../portal_comercio/index.md) — módulo hermano para el portal de comercios.
- [3_recursos/arquitectura_sistema/hardening_y_remediacion_de_pentests.md](../../arquitectura_sistema/index.md) — hardening de seguridad sobre Access Management.

---
*Última actualización: 2026-08-19/20 — nuevo archivo `accesos_qa_staging.md`; nueva sección de parametrización manual de entidades en `pedidos_de_clientes_y_hallazgos_operativos.md`.*
*Última actualización anterior: 2026-08-12 — Creación del módulo en la reestructuración PARA en cascada.*
