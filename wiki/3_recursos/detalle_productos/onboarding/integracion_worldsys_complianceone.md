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

## Requisitos de evidencia documental del legajo cuando el onboarding fue delegado a un tercero

> Estado: discovery — no construido. Insumo de negocio/PLD para T-014 (definir qué documentos exigir por entidad, antes de pedirle a Worldsys que parametrice su catálogo de `document-types`, ver más arriba) — no es una especificación de API, sino el criterio de contenido que ese catálogo/legajo debe terminar reflejando. Fuente: reunión "Consulta documento evidencia para legajo" (2026-08-24), con María Victoria Simonetti (PLD, Banco Industrial).

**Contexto:** el PM (Pablo Gomes) se reunió con María Victoria Simonetti, referente de PLD (Prevención de Lavado de Dinero) de Banco Industrial, para alinear qué documentos/evidencia debe conservar Bind PSP en el legajo (destino final: Worldsys/ComplianceOne, PRD-147) cuando la validación de identidad del cliente fue delegada a un tercero — el caso concreto discutido es BCF actuando por cuenta de un comercio (ej. Carrefour), que a su vez usa proveedores externos de prueba de vida como Socialnet o FaceTech.

**Documentación obligatoria del legajo, en cualquier escenario:**
- DNI frente y DNI dorso: siempre como **imágenes JPG separadas**, nunca unificadas en un solo archivo/PDF.
- Foto selfie.
- Evidencia de las declaraciones de **PEP** (Persona Expuesta Políticamente), **FATCA** y **sujeto obligado**.
- Evidencia de la **aceptación de términos y condiciones** por parte del cliente (Simonetti tomó como referencia un ejemplo real de otro sistema de monitoreo, "Vin Uruguay", donde el contrato completo con la aceptación queda embebido en el legajo).
- Evidencia del **control de listas**: puede entregarse como archivo de texto (TXT) o imagen (JPG), y debe detallar horario del control, contra qué lista se corrió, y resultado (positivo/negativo).

**Distinción normativa entre tipos de control de listas:**
- El **control de listas contraterroristas** es un requisito normativo obligatorio a nivel regulatorio — evalúa porcentaje de similitud por nombre y apellido, no contra el número de documento.
- La **"lista 15"** (mencionada en otros proyectos internos, ver PRD-116) es una política interna del banco para alinear criterios entre equipos — no es un mandato normativo.

**Riesgo de auditoría al delegar onboarding sin revalidación propia:** Simonetti advirtió que si Bind PSP delega el onboarding en un tercero (ej. BCF) y no ejecuta ninguna validación propia sobre lo que ese tercero le pasa, queda expuesto a observaciones de auditoría — el argumento que un auditor puede usar es que la entidad "no hace ningún control cuando pasa directo". La mitigación esperada es que Bind PSP ejecute una **revalidación interna** sobre lo que el tercero envía: por ejemplo, verificar que el porcentaje de similitud de la prueba de vida dio un valor razonable, que el DNI frente/dorso son legibles, que el domicilio y los datos identificativos están completos, y volver a correr un chequeo de listas propio. El argumento de defensa ante auditoría pasa a ser: "la entidad tiene su propio onboarding, y además hacemos una convalidación adicional con nuestro propio logueo" — no delegación ciega.

**Estructura de almacenamiento para evitar duplicidad (evitar saturación en Worldsys):**
- El paquete original del tercero (DNI, selfie, prueba de vida) **no se duplica** — se sube una sola vez.
- La revalidación/relogueo que hace Bind PSP internamente (qué controles corrió, con qué resultado) se sube como **un archivo separado (TXT/log)**, distinto del paquete original — nunca repitiendo el mismo documento dos veces.
- Este criterio de "un documento resumen de validación propia + el paquete original sin duplicar" es preferido por Simonetti para no generar una cantidad excesiva de archivos por legajo (mencionó el riesgo de Worldsys rechazando por volumen: "no me mandes 40 archivos por una persona").

**Caso específico de proveedores de prueba de vida sin evidencia rica (Socialnet, FaceTech):** cuando el proveedor de prueba de vida usado por el tercero delegado (ej. Socialnet, usado por Bind PSP mismo con algunos clientes; o FaceTech, usado por Carrefour) no entrega video ni resumen completo — solo un ID/código de consulta que permite ir a consultar el resultado en la plataforma del proveedor — la evidencia mínima aceptable es un documento que demuestre que el proveedor ejecutó la prueba, en qué horario, y qué resultado dio (aunque no incluya el video).

**Verificación de Renaper y listas antiterroristas cuando el tercero valida vigencia de DNI:** si el tercero delegado (ej. BCF) ya valida contra Renaper que el DNI está vigente, Bind PSP igual debe solicitar y conservar esa evidencia — el respaldo documental demuestra que la entidad tiene un control adicional y no procesa altas de forma directa sin revisión.

**Aplicación práctica pendiente (PRD-147):** este criterio es el insumo de fondo para T-014 — ver `1_proyectos/proyecto-onboarding-estrategico/prd-147_legajo_worldsys/decisiones.md` (2026-08-24) y `tareas.md` (T-030) del Cerebro de Pablo Gomes. La propuesta de documentos por solicitud de persona física está en preparación por el PM, a validar con Diego y Simonetti; la persona jurídica queda para un segundo pase por mayor complejidad de legajo.

> Fuente: Reunión "Consulta documento evidencia para legajo" (2026-08-24), minuta Gemini, con María Victoria Simonetti (PLD, Banco Industrial) y Pablo Gomes.

## Fuente y limitaciones de esta captura

Swagger v1.0.0, capturado 2026-07-20 — puede haber cambiado desde entonces (a confirmar antes de dar por definitivo cualquier dato de este resumen en una integración nueva). El hilo de mail no aporta ningún dato de auth/rate-limit/environments que complemente lo que falta en el Swagger — esos 3 huecos siguen abiertos también del lado del proveedor, no solo de la documentación.
