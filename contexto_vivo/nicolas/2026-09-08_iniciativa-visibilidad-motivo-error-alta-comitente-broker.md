---
id: 2026-09-08_iniciativa-visibilidad-motivo-error-alta-comitente-broker
pm: nicolas
fecha_captura: 2026-09-08
fuente: "Discovery /idea_start sobre OB-247 (Jira), pedido de Integraciones por el cliente Inter"
producto: onboarding
tema: Nuevo proyecto — visibilidad del motivo de error de broker en alta de cuenta comitente
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 4b0d3d1e684ff33256a33a29f86746dfd5c7cc9a
proyecto: visibilidad_error_alta
---

Proyecto nuevo en el Cerebro de Nicolás Colón: [`1_proyectos/visibilidad_error_alta/`](../visibilidad_error_alta/proyecto.md), a partir de [OB-247](https://bindpsp.atlassian.net/browse/OB-247) (Historia de Jira, reporter malzogaray/Integraciones, por pedido del cliente Inter).

**Problema:** Inter (banco/broker brasilero, integra Wallet + Dólar CCL vía el broker IVSA-Poincenot) no puede ver el motivo de error de una alta de cuenta comitente fallida en la grilla general de solicitudes del portal de Onboarding — solo entrando al detalle de cada solicitud una por una. Con Inter masificando su volumen de altas, ese proceso manual dejó de escalar.

**Discovery cerrado el mismo día (Gates 1-3 confirmados):** evaluado como Bau (no mueve NSM ni los KR del foco Onboarding, que es de Pablo Gomes) pero generaliza a cualquier cliente con alta de cuenta comitente (La Virginia, Coppel, Octagon). Solución adoptada tal cual la trajo el PM: columna con el motivo de error (dato ya existente, visible hoy en el detalle de la solicitud — no requiere integración nueva con IVSA) + export a CSV, acotado al estado "Error en Alta". El objetivo acordado es conseguir de Fintexa (dueño del producto Onboarding) una cotización real de esfuerzo, no decidir construcción todavía.

**Nota de proceso:** mismo cliente (Inter), mismo portal y mismo día que [OB-246](https://bindpsp.atlassian.net/browse/OB-246)/`cola_verificacion_manual` (otro proyecto nuevo de este Cerebro) — se sugirió cotizar ambos cambios juntos con Fintexa, pendiente de que el PM lo decida.

**Gap abierto:** el tamaño real del problema no es medible con el dataset histórico de Onboarding (el estado "Error en Alta" es transitorio — Inter corrige y reprocesa, lo que lo saca del corte estático) — se necesita un dato directo de Integraciones o Fintexa.
