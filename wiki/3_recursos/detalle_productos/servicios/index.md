# Detalle de Producto — Servicios

> Conocimiento detallado de producto: mecánica interna, historia de build y mantenimiento del producto **Servicios**. Nace en Jira como espacio propio (`SER`) el 2026-06-04, con **Pago Fácil** como único cliente/caso de uso a la fecha de esta ingesta (2026-07-13).

## ⚠️ Nota — dónde vive cada pieza de conocimiento de Pago Fácil

Pago Fácil tiene su conocimiento repartido en 2 lugares por decisión deliberada (evitar duplicar contenido ya bien ubicado):

- **PRD-57** — historia de build del Epic MVP (SER-1, 31 tickets). Es la fuente de verdad de qué se construyó y por qué; proyecto de Nicolás Colón, vive en su propio Cerebro desde 2026-08-13 (ya no en `1_proyectos/` de esta instancia).
- **[`pago_facil.md`](pago_facil.md)** (este módulo) — documentación técnica del API cliente-facing (contratos, request/response) + **[`pago_facil_mantenimiento.md`](pago_facil_mantenimiento.md)** — todo lo que la otra fuente no cubre: el Epic **ETAPA 2** (evolución post-MVP) y ajustes finos del MVP (cargo de servicio, reintentos de confirmación/devolución, homologación con BPG, reCaptcha).

## Archivos de este módulo

| Archivo | Contenido |
|---|---|
| [pago_facil.md](pago_facil.md) | API cliente-facing completa (contratos, request/response, flujos), configuración de entes, ambiente de prueba, y el cliente adicional Grupo DESA (RIPSA) sobre el mismo motor. Reubicado desde `detalle_productos/transversal/pago_facil.md` (reestructuración PARA en cascada, 2026-08-12). |
| [pago_facil_mantenimiento.md](pago_facil_mantenimiento.md) | Epic "ETAPA 2" (expirar link, monto no exacto transferido, mejoras de pantalla de vencimiento) y ajustes finos del MVP no cubiertos en PRD-57 (cargo de servicio, forma de pago, reintentos de confirmación/devolución en BPG, webhook `PAGO_SERVICIOS`, correcciones post-homologación, reCaptcha en producción). Backfill vía `/sync_releases`, versión SER 1 (2026-06-04). |

## Ver también

- PRD-57 — proyecto vivo/historia de build del MVP (Cerebro de Nicolás Colón).
- [wiki/3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md §6-7](../adquirencia/boton_simple_2_0.md) — objeto Deuda y BPG reutilizados como motor de cobro.
- [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md) — falta el overview de negocio del producto Servicios, pendiente de que lo aporte el usuario.

---
*Última actualización: 2026-08-12 — `pago_facil.md` reubicado a este módulo desde `detalle_productos/transversal/` (reestructuración PARA en cascada); ya no queda ningún archivo de Servicios fuera de esta carpeta.*
*Última actualización anterior: 2026-07-13 — Creación del módulo, backfill `/sync_releases` vía XML (espacio SER COMPLETO: 39 tickets, versión SER 1, única publicada a la fecha).*
