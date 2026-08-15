# Pedidos de Clientes y Hallazgos Operativos Históricos — Portal Comercio

> Estado: mezcla de en producción y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde 3 archivos-cola de `detalle_productos/transversal/` (`pedidos_puntuales_de_clientes.md`, `dolores_soporte_y_administracion.md`, `reporteria_operativa.md`) que mezclaban pedidos de varios productos y del Portal Admin en un solo archivo — ver [`portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md`](../portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md) para lo específico del Admin.

## Pedidos puntuales por cliente

- **CITYGAS**: mejora de visualización del totalizador y agregar datos del pagador en el portal Comercio del canal QR (Pendiente).

## Bugs sin cliente específico

- Bug en el botón para devolver una transacción desde el Portal Comercio.
- **SUR FINANZAS: la sección Usuarios no traía información** — el listado de usuarios del portal quedaba vacío para un administrador real (confirmado en QA antes de producción). Ver ficha del cliente en [`ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md`](../ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md).

## Extracto de movimientos HTML (desarrollo en 7 partes)

Extracto de movimientos con formato HTML (no solo CSV) para Portal Comercio:
1. Modelo de extracto (back).
2. Configuración del reporte (back) — incluye logo, comentarios y domicilio de la organización como datos personalizables del extracto.
3. Portal Comercio (front).
4. Generación mensual automática del reporte.
5-6. Procesamiento de archivos grandes en pequeños pasos (batch) — mismo problema de volumen que motivó la generación asíncrona de reportes CSV del Admin.
7. No mostrar reportes expirados en Admin ni en Portal (los reportes generados tienen una vida útil/expiración).

**Pendiente sin cerrar**: "Procesar archivos grandes en pequeños pasos (batch)" para Wallet (ticket separado del de Extracto HTML) quedó en "Refinar".

## Ver también
- [portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md](../portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md) — motor de reportería CSV del Admin (bug recurrente de filtro por Entidad).
- [ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md](../ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md) — grilla de movimientos y particularidades de portal de SUR FINANZAS.

---
*Fuente: Epics Notion "Dolores de clientes", "Dolores de Soporte y administración" y "Reporting" — ingesta 2026-07-06.*
*Última actualización: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Portal Comercio de 3 archivos-cola de `detalle_productos/transversal/`.*
