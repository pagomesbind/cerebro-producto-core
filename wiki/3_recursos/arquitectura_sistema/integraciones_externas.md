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

## Coelsa — documentación pública (ingesta objetivo)

> Nota de registro/trazabilidad, no de contenido técnico. Sirve de baseline para futuras ingestas incrementales de la documentación pública de Coelsa (`documentacion.coelsa.com.ar`).

Se realizó una primera ingesta completa (2026-09-11) de 5 de los 9 productos que expone el sitio: **DEBIN** (incluye Pago QR/PCT, Interchange, CVU-Comercios embebido), **Comercio** (ABM unificado CBU+CVU), **CVU**, **Prevent** y **CPF**. El contenido técnico de esa ingesta ya está distribuido en los archivos correspondientes de `detalle_productos/wallet/`, `detalle_productos/adquirencia/` y `cumplimiento_normativo/`. Quedaron **excluidos a pedido explícito del usuario**: ECHEQ, FCEM, CEDIP y Alias CBU — pendientes de una ronda futura si Bind los llega a necesitar.

**Cómo detectar cambios sin releer todo:** el sitio DEBIN es el único con página de "Novedades" propia (`/debin/#novedades`, changelog cronológico) — último ítem conocido a esta ingesta: **2026-Septiembre** (actualización del Manual de Servicio Procesamiento CCT y agregado del impuesto SIRTAC al Manual de Pagos con Transferencia PCT). Comercio, CVU, Prevent y CPF no tienen changelog propio — para esos 4, detectar cambios requiere comparar el sitio completo contra lo ya documentado acá (cada uno son sitios chicos, 20K-40K caracteres).

Confirmación cruzada de esta ingesta: el reparto de Interchange (25/50/75 según tamaño de comercio) y el tramo gratuito ya documentados en `detalle_productos/adquirencia/mecanica_qr_coelsa.md` (Parte 4) coinciden exactamente con la especificación pública de Coelsa, sin contradicciones.

## Coelsa — Homologación de nueva versión de ABM de CBU (Totalizador de cuentas)

> Fuente: mail "Homologación ABM de CBU" (Coelsa, `icm@coelsa.com.ar`), 2026-09-17, dirigido a Banco Industrial con Pablo Gomes en copia.

Coelsa habilitó el ambiente de Homologación de una nueva versión del servicio **ABM de CBU vinculado al Totalizador de cuentas**: incorpora el registro de **fecha de alta y fecha de baja** de las cuentas bancarias, en línea con requerimientos normativos vigentes (comunicación puntual no especificada en el mail). Ventana de homologación: **24/08/2026 al 01/10/2026** inclusive. Salida a producción: **02/10/2026**. Documentación técnica en el portal de Coelsa — API nueva (`documentacion.coelsa.com.ar/aliascbu/#api-cbu-nuevo`) y Batch nuevo (`documentacion.coelsa.com.ar/aliascbu/#batch-cbu-nuevo`). Contacto de soporte: `icm@coelsa.com.ar`. Sin evidencia en el mail de que Bind PSP/Banco Industrial haya iniciado las pruebas de homologación todavía — a confirmar en un próximo barrido si se coordinó la ejecución antes del cierre de la ventana (01/10).

## Atenas + Worsis — integración de datos históricos PCP con Banco Industrial

> Fuente: reunión "Relevamiento WH PSP" (2026-09-04, 09:30), minuta y transcripción Gemini. Banco Industrial (María Victoria Simonetti, Alfredo Rey, DBA), Bind PSP (Hernan Clarich, Gonzalo Rivera, Giuliana Batista).

Banco Industrial requiere acceso a datos históricos de transacciones de Bind PSP (mínimo 1 año de auditoría) para alertas de cumplimiento (PLD/ROS), vía dos sistemas interconectados propios del banco:

- **Atenas** (núcleo de alertas) — sistema interno en premisas de Banco Industrial, recibe datos históricos de Bind PSP vía consultas SQL directas (sin ETL, Atenas es proveedor de datos a Worsis, no transformador), procesa alertas mensualmente (no real-time), no almacena transacciones (restricción del banco por volumen).
- **Worsis** — sistema de monitoreo del banco en SAS, acumula alertas por cliente a través de múltiples entidades y genera reportes consolidados. *(No confundir con "Worsis"/Worldsys, el conector externo de Onboarding/Ardid para PEP/Sujeto Obligado/Terrorista — mismo nombre fonético, sistemas distintos de proveedores distintos.)*

**PCP con dos verticales de negocio:** (1) Comercios — QR, botones de pago; (2) Wallet — Bind provee tecnología CVU corta a entidades (Cencosud, Carrefour, BCF, Astropay); un cliente final puede tener presencia en múltiples entidades dentro del mismo PCP y consolidarse en una sola alerta (ej. un mismo usuario en Carrefour + Astropay + Cencosud).

**Integración técnica:** consultas SQL desde Atenas hacia el nodo de historificación de Bind PSP, frecuencia a confirmar con el DBA (pendiente — ver gap en [`2_areas/gaps_y_preguntas.md`](../../2_areas/gaps_y_preguntas.md)); VPN existente limitada a APIBank, requiere refinamiento para habilitar tráfico al nodo SQL histórico, con credenciales de backend para Atenas; entornos Desa/CUA/Producción del banco conectados a Staging/Producción de Bind PSP.

## Ver también
- [mtls_apis_y_webhooks.md](mtls_apis_y_webhooks.md) — mTLS usado en la integración con Coelsa y PIX.

---
*Última actualización: 2026-09-21 — `/context_merge`: nueva sección "Coelsa — Homologación de nueva versión de ABM de CBU" (ventana 24/08-01/10, PROD 02/10) y nueva sección "Atenas + Worsis" (integración de datos históricos PCP con Banco Industrial).*
*Última actualización anterior: 2026-09-11 — `/context_merge`: nueva sección "Coelsa — documentación pública (ingesta objetivo)", registro de la primera ingesta completa del sitio público de Coelsa (5/9 productos).*
*Última actualización anterior: 2026-08-12 — Reubicado desde `arquitectura_sistema/index.md §9` (reestructuración PARA en cascada). Contenido sin cambios salvo la nota de contradicción agregada.*
