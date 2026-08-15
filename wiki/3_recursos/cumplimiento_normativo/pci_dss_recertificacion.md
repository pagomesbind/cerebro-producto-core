# PCI DSS — Recertificación de Bind PSP

> Estado: en producción (mantenimiento continuo). Reubicado desde `detalle_productos/transversal/cumplimiento_normativo.md §3` en la reestructuración PARA en cascada (2026-08-12).

Epic de mantenimiento de la certificación **PCI DSS** de Bind PSP (obligatoria para el ecosistema Aceptador — procesamiento de tarjetas Visa/Mastercard).

> Nota de alcance: esto es la recertificación PCI **propia de Bind PSP**. La certificación PCI DSS del proveedor de infraestructura Fintexa es un tema relacionado pero distinto — ver el gap abierto sobre PCI DSS del proveedor en [`../../2_areas/gaps_y_preguntas.md`](../../2_areas/gaps_y_preguntas.md).

- **Replicar pago presente en otro cluster** (etiqueta `💳 POS`): ajuste de alta disponibilidad/resiliencia para el flujo de pago presente (POS), replicando el procesamiento en otro cluster — mitigación de punto único de falla, requisito típico de continuidad operativa en una recertificación PCI.
- **Configurar TTL en CardTemp (Bóveda)**: se configuró un índice TTL (time-to-live) en Mongo para que los registros de tarjetas temporales en **Bóveda** (guardado de credenciales de pago recurrente de Botón Simple) se eliminen automáticamente a los 60 minutos si el pago no se completó — medida directa de **reducción de alcance PCI** (no retener datos de tarjeta más tiempo del estrictamente necesario). Conecta con la instancia MongoDB `mongodb-botonsimple-prd-boveda-api` documentada en [3_recursos/arquitectura_sistema/](../arquitectura_sistema/index.md) (atribución en disputa — ver gap).
- **Reajustes Certificación PCI**: ticket contenedor de ajustes generales de recertificación, sin contenido adicional documentado en Notion más allá del título.

## Ver también

- [reporteria_worldsys_bcra.md](reporteria_worldsys_bcra.md) — otra obligación normativa de Bind PSP, dominio distinto (PLD/BCRA vs. tarjetas).
- [3_recursos/arquitectura_sistema/modelo_de_seguridad.md](../arquitectura_sistema/index.md) — controles de seguridad de infraestructura que sostienen esta certificación.

---
*Fuente: Notion histórico, Epic "PCI: Recertificación" (3 tickets) — ingesta 2026-07-06.*
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/cumplimiento_normativo.md §3` (reestructuración PARA en cascada). Contenido sin cambios.*
