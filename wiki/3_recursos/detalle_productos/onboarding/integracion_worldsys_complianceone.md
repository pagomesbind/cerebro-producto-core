# Integración con Worldsys — API ComplianceOne

> Estado: discovery — no construido (documentación de la API pública del proveedor; la integración de Bind PSP con estos endpoints está en diseño vía PRD-147, no en producción). Fuente: Swagger público de ComplianceOne v1.0.0 (servidor único `https://api.complianceone.worldsys.io/BIND_PSP`, 518 endpoints, capturado 2026-07-20 — reporte HTML estático, no especificación interactiva) + hilo de mail con Worldsys (Pablo Stach, Gonzalo Quintana, Matias Quimey Larumbe, 2026-04-15 a 2026-08-14).

Conocimiento técnico reusable sobre la API pública de Worldsys (producto **ComplianceOne**), el sistema de control documental/legajo que Bind PSP integra por mandato de Compliance (ver PRD-147, Legajo Worldsys, KR2 de Onboarding Estratégico).

## Autenticación

OAuth 2.1 vía `POST /auth/token`. Soporta `client_credentials` (server-to-server, el relevante para integraciones backend), `password` (ROPC) y `authorization_code` con PKCE. El token viaja como `Authorization: Bearer {access_token}`. Existen además flujos de MFA (`/auth/mfa/*`), SSO/SAML y gestión de API keys de aplicación (`/application/register`, `/application/keys`) — no relevantes para integraciones servidor-a-servidor simples.

**No hay ambiente de sandbox/staging declarado** — el Swagger solo lista el servidor de producción. Tampoco hay ningún rate limit, cuota o límite de throughput documentado en el Swagger, ni Worldsys llegó a confirmar un número concreto pese haberse preguntado explícitamente por mail (27/07/2026).

## Endpoints relevantes para gestión de personas/clientes

- `POST /profile/customers` — crea persona + registro de cliente en una transacción. **El body no está expandido en el Swagger** (tipo `object` genérico) — es el hueco de documentación más importante encontrado. Devuelve `201` o `409` ("ya existe un cliente con esa identificación", sin body en la respuesta de error — no trae el `personId` existente).
- `PATCH /profile/customers/{id}` — sí documentado completo: ~35 campos, todos opcionales, incluyendo `identification`, `name`, `birthDate`, `email1`/`phone1`, campos PEP (`isPep`, `pepCharacterId`, etc.), `personType` (`NATURAL_PERSON`|`LEGAL_PERSON`), y `customFields` (objeto libre).
- `GET /profile/by-identification/{identification}` — devuelve `personId`+`customerId` de la persona que coincide con esa identificación (según la descripción textual; el objeto `data` de la respuesta no está expandido en el schema). `404` si no existe.

## Gestión de documentos

- `POST /file/upload` (multipart) — sube el archivo, devuelve `reference` (hash MD5) y `version` (mencionados solo en prosa, no en el schema tipado). Query param `encrypt` (acepta valores en texto libre tipo `si`/`no`/`true`/`false`) — **si se omite, cifra por default**. Campo `renameTo` permite fijar el nombre del archivo.
- `POST /profile/{id}/documents` (`id` = `personId`) — asocia un archivo ya subido a la persona: `{documentTypeId, description, validFrom, validUntil, fileReference}`.
- `GET /profile/{id}/documents/{documentId}` — **confirmado que es metadata-only, no devuelve bytes/contenido**: `{id, description, fileReference, validFrom, validUntil, documentType}`.
- **No existe ningún endpoint de descarga de contenido/bytes de un documento de perfil** en todo el Swagger — pese a que la categoría "File" se autodescribe como "subida, descarga y metadatos", solo el endpoint de subida está documentado. Worldsys confirmó verbalmente (reunión 2026-08-07) que la descarga es viable, pero no había entregado documentación formal a la fecha de captura del Swagger (20/07) ni al cierre del hilo de mail (14/08).

## Catálogo de tipos de documento — hallazgo importante para el diseño

`GET /people/document-types` — **es de solo lectura, sin ningún endpoint de creación en todo el Swagger.** El catálogo de tipos de documento está configurado del lado de Worldsys a nivel de todo el tenant/suscriptor (Bind PSP como entidad única), no es autoservicio por API. Cualquier diseño que dependa de "un tipo de documento distinto por unidad de negocio/entidad" requiere que Worldsys lo parametrice manualmente cada vez — una dependencia operativa a tener en cuenta antes de elegir ese patrón. La alternativa (usar un tipo genérico por categoría de documento y calificar la entidad en el campo `description`, de texto libre) evita esa dependencia.

Worldsys mismo (mail de Matias Quimey Larumbe, Service Delivery Manager, 2026-08-14) planteó esta disyuntiva sin resolverla de su lado, dando como ejemplo de convención de nombre: `DNI_QUIMEY_ASTROPAY` / `DNI_QUIMEY_CREDICUOTAS`.

## Importación masiva — solo para personas, no para documentos

Categoría "Import" (23 endpoints) con 3 modalidades, todas basadas en un `templateId`:
- `POST /import/entity` — importación online, una entidad.
- `POST /import/bulk` — importación batch, array de entidades del mismo tipo.
- `POST /import/interfaces` — procesamiento asíncrono por cola (con seguimiento vía `GET /import/process/{processId}/status` y `/errors`).

**Los tipos de entidad soportados son `PeopleCustomer`/`PeopleSupplier`** — es decir, este mecanismo de importación masiva nativo de Worldsys sirve para crear/actualizar personas en lote, pero **no cubre documentos/archivos** — la carga de archivos siempre es individual vía `/file/upload` + `/profile/{id}/documents`, sin variante bulk documentada. Relevante para cualquier proyecto de carga masiva de legajo de stock (ver PRD-214 en el Cerebro de Pablo Gomes).

## Inconsistencias propias de la API, a tener en cuenta al integrar

- El envelope de respuesta varía entre endpoints: algunos devuelven `{success, data}`, otros solo `{data}`, otros campos sueltos sin envolver — no asumir un formato único.
- El nombre del campo raíz de error de validación (`400`) varía entre `errorCode` y `code` según el endpoint.

## Fuente y limitaciones de esta captura

Swagger v1.0.0, capturado 2026-07-20 — puede haber cambiado desde entonces (a confirmar antes de dar por definitivo cualquier dato de este resumen en una integración nueva). El hilo de mail no aporta ningún dato de auth/rate-limit/environments que complemente lo que falta en el Swagger — esos 3 huecos siguen abiertos también del lado del proveedor, no solo de la documentación.
