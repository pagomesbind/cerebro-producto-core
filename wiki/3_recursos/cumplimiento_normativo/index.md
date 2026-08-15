# Cumplimiento Normativo

> Obligaciones normativas que Bind PSP debe cumplir independientemente del producto (Wallet o Adquirencia): reportería antilavado al banco/BCRA, certificación PCI DSS, y límites operativos de gestión de riesgo UIF/ROS. Nace en la reestructuración PARA en cascada (2026-08-12) al desarmar `detalle_productos/transversal/cumplimiento_normativo.md`, que mezclaba estos 3 temas normativos en un solo archivo.

## Documentos de este módulo

| Archivo | Contenido |
|---|---|
| [reporteria_worldsys_bcra.md](reporteria_worldsys_bcra.md) | Los 5 tipos de archivo diario que Bind PSP informa al banco/BCRA vía Worldsys (Wallet + Adquirencia), enriquecimiento de datos para Matriz de Riesgo, y el conflicto de diseño sin resolver sobre comprobantes vs. movimientos. |
| [pci_dss_recertificacion.md](pci_dss_recertificacion.md) | Mantenimiento de la certificación PCI DSS propia de Bind PSP: alta disponibilidad de pago presente, reducción de alcance PCI (TTL en Bóveda). |
| [limites_operativos_uif_ros.md](limites_operativos_uif_ros.md) | Topes operativos mensuales por segmento de cliente para decidir cuándo pedir documentación adicional, evitando ROS innecesarios ante la UIF. |

## Ver también

- [3_recursos/arquitectura_sistema/index.md](../arquitectura_sistema/index.md) — infraestructura y seguridad que sostiene estas obligaciones (mTLS, PCI a nivel de red).
- [3_recursos/detalle_productos/index.md](../detalle_productos/index.md) — mecánica de producto de Wallet/Adquirencia sobre la que corren estos reportes.
- [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md) — gap abierto sobre PCI DSS del proveedor Fintexa (distinto de la recertificación propia documentada acá).

---
*Última actualización: 2026-08-12 — Creación del módulo en la reestructuración PARA en cascada, desarmando `detalle_productos/transversal/cumplimiento_normativo.md` en 3 archivos temáticos.*
