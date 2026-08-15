# Conteo de Pegadas a API Bank (Facturación con el Proveedor)

> Estado: en producción. Fuente: Epic Notion "[EPIC] Conteo de pegadas a API Bank" (Tipo Sanidad, 4 tickets, 16 SP). Reubicado desde `detalle_productos/transversal/seguridad_y_webhooks.md §4` en la reestructuración PARA en cascada (2026-08-12).

Bind PSP necesitaba poder reportar internamente el volumen de invocaciones a la **API Bank** (la API core del banco que da soporte a CVUs/cuentas) discriminado por aplicación consumidora y por entidad/organización, para negociar comercialmente el costo con el proveedor.

**Solución:** se agregó un header nuevo, `x-internalclientid`, que todo microservicio que invoca a la API Bank debe propagar hacia el egress con el formato `[Sistema]-[Id]`:
- `Wallet-14` (Organización de Wallet)
- `Aceptador-A029` (Entidad de Adquirencia)
- `CvuCollect-8` (Collector del Agente de Cobros y Pagos)

Se implementó por separado en cada uno de los 4 sistemas consumidores (Cobro genérico, Wallet, CvuCollect en 2 partes) porque cada uno arma el header con su propia clave de dominio (`Organizacion.Id`, `Entidades.Codigo`, `Collectors.Id`).

## Ver también

- [mtls_apis_y_webhooks.md](mtls_apis_y_webhooks.md) — otro header transversal de infraestructura (`X-Client-mTLS`).

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/seguridad_y_webhooks.md §4` (reestructuración PARA en cascada). Contenido sin cambios.*
