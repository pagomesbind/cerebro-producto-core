---
id: 2026-10-06_conocimiento-ardid-consumo-de-datos-vistas-ventana-45-dias-e-historico
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Mail 'RE: Consumo de datos | Ardid Credicuotas' — minuta de Paula Lamarca (Pentass) de la reunión del 2026-10-01, enviada el 2026-10-06"
producto: ardid
tema: Consumo de datos de Ardid — vistas por entidad en SQL/MongoDB, front limitado a 48 h, ventana de datos de 45 días y opciones para el histórico
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/reporteria_alertas.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

Lo que se habló en la reunión "Consumo de datos | Ardid Credicuotas" (01/10) con Pentass, según la minuta de Paula Lamarca. Son propuestas y opciones evaluadas, no decisiones cerradas: la propia Pentass pide otra reunión con Lorena Macedo porque "se generaron dudas al retransmitirlo".

**1. Vistas y métricas (solución rápida propuesta).** Crear **vistas en SQL y MongoDB filtradas por entidad**, con campos acotados e índices, validadas con el DBA. Las vistas cubren dos frentes:
- el pedido de datos de Credicuotas (su área de Fraudes);
- las métricas internas de Bind: tablero de métricas, controles de fraude y lavado, y alertas del banco.

**2. Ventanas de consulta e histórico.**
- El **front** de Ardid queda limitado a consultas **del día o de las últimas 48 h**. Las consultas masivas pasan por "la nueva funcionalidad" (la minuta no dice cuál es).
- La **ventana actual de datos de Ardid es de 45 días**.
- Para el histórico se evaluaron dos opciones: un **segundo MongoDB (opción preferida)** o capas de storage en **Cosmos DB / DocumentDB**.

**3. Datos para clientes.** El área de Fraudes de un cliente (caso Credicuotas) necesita analizar operaciones y rechazos. Hoy eso solo llega **por CSV**, sin acceso directo a tablas. La salida propuesta es exponerlo con **APIs del back de Ardid**. Hay un ticket abierto para identificar el endpoint.

**Por qué importa:** los 45 días de retención y el límite de 48 h del front condicionan cualquier análisis de fraude o conciliación que necesite más historia (por ejemplo, la facturación mensual de Ardid por entidad, ver `2026-10-06_conocimiento-ardid-facturacion-por-entidad-sin-id-univoco-con-wallet`).

> Fuente: Mail "RE: Consumo de datos | Ardid Credicuotas" — Paula Lamarca, Pentass (2026-10-06), minuta de la reunión del 2026-10-01.
