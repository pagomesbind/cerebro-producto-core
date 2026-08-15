# Integraciones Externas

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`. Reubicado desde `arquitectura_sistema/index.md §9` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md).

| Sistema | Protocolo | Dirección | Propósito |
|---|---|---|---|
| Coelsa / Bind | REST + mTLS | Bidireccional | Red de pagos CVU, transferencias interbancarias, clearing |
| AFIP | SOAP/XML | Saliente | Validaciones CUIT/CUIL, padrones |
| BCRA | SFTP | Saliente | Reportes regulatorios, información prudencial |
| RENAPER | REST | Saliente | Validación de identidad, biometría facial |
| Visa / Mastercard | ISO 8583 / REST | Bidireccional | Autorización, clearing y settlement con tarjeta |
| Lirium | REST + Webhook | Bidireccional | Trading de criptomonedas, cotizaciones en tiempo real |
| Poincenot | REST | Saliente | Mercado de capitales: FCI, dólar MEP/CCL |
| PIX / PagBrasil | REST + mTLS | Bidireccional | Pagos transfronterizos Argentina-Brasil |
| **Ardid** | REST | Bidireccional | Sistema core bancario integrado |
| **Siscri** | Database | Saliente | Scoring crediticio integrado |

> Nota de correlación: `Ardid` y `Siscri` ya estaban documentados como producto/componente propio (ver [2_areas/overview_productos/overview_ardid.md](../../2_areas/overview_productos/overview_ardid.md) y [detalle_productos/siscri/index.md](../detalle_productos/siscri/index.md)). Este documento confirma su rol técnico como integraciones externas del núcleo Wallet.
>
> ⚠️ Nota: la fila "Siscri — Database" contradice la descripción de Siscri como motor con **API/Swagger propio** documentada en `detalle_productos/siscri/configuracion_entidades.md` — puede tratarse de que Wallet consulta Siscri directo a base de datos para lecturas de bajo nivel mientras usa la API para altas/configuración, o de una simplificación del documento fuente. No confirmado.

## Ver también
- [mtls_apis_y_webhooks.md](mtls_apis_y_webhooks.md) — mTLS usado en la integración con Coelsa y PIX.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/index.md §9` (reestructuración PARA en cascada). Contenido sin cambios salvo la nota de contradicción agregada.*
