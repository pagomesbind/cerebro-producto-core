---
id: 2026-09-03_ardid_reglas_limites_transaccion_trazabilidad
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_meetings — reunión 'Join Soporte Clientes' 2026-09-02 10:01 (docId 1eBqiPncYkZgzw693JLN5rmLGwtIZST14zx6LKb3Pn_g), minuta Gemini"
producto: ardid
tema: Límites de reglas de validación por transacción/mensual, y limitación de tooling para identificar qué regla causó cada rechazo
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/modulo_transferencias.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

**Reglas de validación confirmadas (vigentes, transversales a entidades):** límite de **$300.000 por transacción** y **$2.000.000 mensuales** — motivadas por el aumento de rechazos analizado en el incidente de Terramundi (ver `2026-09-03_clientes_terramundi_incidente_rechazos_ardid`), pero las reglas en sí no son específicas de ese cliente.

**Limitación de tooling identificada en la reunión:** hoy es difícil identificar, para un rechazo puntual, **qué regla específica** de Ardid lo causó — las herramientas de consulta actuales no permiten aislarlo con precisión por rechazo individual. Gonzalo Rivera compartió una consulta de base de datos (no detallada en la minuta) para facilitar el monitoreo de rechazos por entidad y marca, como paliativo mientras no exista una vía directa de trazabilidad regla→rechazo.

**Plan acordado:** Rocío Revelli y Gonzalo Rivera van a **ajustar los parámetros de las reglas** para reducir la fricción de experiencia de usuario, manteniendo el nivel de seguridad — sin un valor numérico nuevo confirmado todavía, ni fecha de implementación. Próximos pasos explícitos: (1) corregir el error técnico causante del alto índice de rechazos, (2) repasar todas las reglas de entidad vigentes, (3) evaluar configuraciones de reglas en cada entidad, (4) actualizar la consulta para incluir el nombre de la regla mediante su ID (mejora de trazabilidad, a cargo de Gonzalo Rivera).

> Fuente: reunión "Join Soporte Clientes" (2026-09-02 10:01), minuta Gemini. Participantes: Mauro Suppan, Luciana Rudaz, Emma Vignoles, Diego Weledniger, Adriana Endzeliz, Gustavo Lazzaro, Gonzalo Rivera, Alberto Murad, Matías Alzogaray, Nicolás Colón, Pablo Gomes.
