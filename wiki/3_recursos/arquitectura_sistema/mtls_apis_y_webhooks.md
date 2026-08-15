# mTLS — APIs y Webhooks

> Estado: en producción. Contenido completo transcrito desde `wiki/3_recursos/conocimiento_interno/manual_para_configuraciones/implementacion_de_mtls_webhooks_y_apis.md`. Reubicado desde `detalle_productos/transversal/seguridad_y_webhooks.md §1` en la reestructuración PARA en cascada (2026-08-12) — es infraestructura/seguridad transversal, no conocimiento de producto.

# 🛡️ Guía Interna: Implementación de mTLS (APIs y Webhooks)

Esta documentación detalla el proceso para habilitar la Autenticación Mutua de TLS (mTLS) con clientes externos en ambientes de Staging y Producción. Utilizamos el caso de YouHodler como estándar de referencia.

## 1. Conceptos Clave y Regla de Oro

mTLS no es solo cifrado; es un apretón de manos bidireccional donde ambas partes validan su identidad. La regla de oro arquitectónica para estos despliegues es el modelo **"CA del Host"**: el dueño del servidor que recibe la petición es quien actúa como Autoridad Certificante (CA).

- **Inbound (Entrante):** El cliente llama a nuestras APIs. BIND es el Host. Nosotros validamos al cliente firmando su CSR.
- **Outbound / Egress (Saliente):** Nosotros enviamos Webhooks al cliente. El cliente es el Host. Ellos validan a BIND firmando nuestro CSR.

## 2. Escenario A: Cliente consume nuestras APIs (Inbound)

### Paso 1: Generación y Firma de CSR

1. El cliente debe generar un **CSR (Certificate Signing Request)** y enviárnoslo.
2. Abrimos un ticket interno en **Seguridad Informática (Jira)** adjuntando el archivo. (https://fintexa.atlassian.net/servicedesk/customer/portal/70/group/236/create/496)
3. SegInfo nos devuelve un archivo `.crt` firmado. Se lo enviamos al cliente para que lo instale en su servidor y lo adjunte en sus peticiones

### Paso 2: Obtención del Token (JWT)

El cliente no puede usar el scope HTTPS estándar. Debe solicitar el token de OAuth2 usando el Scope específico para mTLS: `api://2356cbac-6958-45a6-b7c4-ff5b888a2fe9/.default`.

- IMPORTANTE!!! = **Acción Interna:** Se debe solicitar a fintexa la creación de un **Consumer mTLS** y enviarlo al cliente

### Paso 3: Llamada a la API

El cliente **debe** cambiar la URL base de sus peticiones. El Gateway estándar no valida certificados; solo lo hace el **Gateway de mTLS**.

- **URL Estándar (NO USAR):** `https://gw-staging-qrbind...`
- **URL mTLS (Correcta):** `https://mtls-gw-staging-qrbind.epays.services/`.
- **Requerimiento técnico:** La petición debe incluir los archivos `--cert` (el que le firmamos) y `--key` (su clave privada).

## 3. Escenario B: Webhooks de BIND hacia el Cliente (Outbound)

Aquí la lógica se invierte: nosotros somos el cliente y ellos la autoridad que nos firma.

### Paso 1: Requisitos del Cliente

Debemos solicitar al cliente:

- **Common Name (CN):** El nombre que quieren que tenga nuestro certificado (ej: `YOUHODLER-DEV`).
- **URL de Destino:** Dónde debemos disparar las notificaciones.

### Paso 2: Generación Interna de CSR

1. Abrimos ticket en **Seguridad Informática** pidiendo la **Generación de un CSR interno para Egress.** (https://fintexa.atlassian.net/servicedesk/customer/portal/70/group/236/create/496)
2. Enviamos este archivo `.csr` al cliente para que su área de DevOps/Seguridad lo firme con su propia Root CA.

### Paso 3: Configuración del Egress

1. El cliente nos devuelve el certificado firmado (`.crt`).
2. Abrimos ticket a **Infraestructura (Pablo Vargas)** para cargar ese certificado en el **Egress de Staging/Producción** apuntando a la URL del cliente. (https://fintexa.atlassian.net/servicedesk/customer/portal/70/group/236/create/496)

Este flujo es más complejo ya que involucra tres áreas distintas y una cadena de dependencias técnica.

**🔄 Cadena de Trabajo y Responsabilidades**
Para que un webhook salga con mTLS, se deben completar estos tres pasos en orden

| Ticket | Responsable | Qué hace | Dónde |
| --- | --- | --- | --- |
| SI- | Seguridad | Genera CSR interno, gestiona firma del cliente y carga secretos en **Key Vault**. | Azure Key Vault |
| INF- | Infraestructura | Configura el **proxy de egress** (Nginx/OpenResty) para enrutar el tráfico. | Proxy Egress |
| EM- | Emisión/Wallet | Configura el **destino del webhook** (URL) en la aplicación. | DB Wallet Service |

## 4. Troubleshooting: Errores Comunes

### Error: `401 Unauthorized - Missing claims: roles`

- **Causa:** El cliente está usando el token viejo de HTTPS estándar.
- **Solución:** Pedir el token con el nuevo scope de mTLS (`api://2356cbac...`).

### Error: `Audience validation failed`

- **Causa:** El cliente obtuvo el token de mTLS pero le está pegando a la URL de HTTPS (`gw-staging...`).
- **Solución:** Cambiar la URL al endpoint que empieza con `mtls-gw-staging...`.

### Error: `ASN1/wrong tag` al intentar firmar CSR

- **Causa:** El texto del CSR se corrompió al copiar/pegar (usualmente por Slack o Teams).
- **Solución:** Enviar siempre el CSR como un archivo adjunto `.txt` o `.csr` sin formato.

## 5. Arquitectura y Flujo de Datos (Deep Dive)

Para entender cómo viaja la petición y por qué fallan las validaciones si no se sigue el proceso, analizamos el siguiente flujo de infraestructura:

**1. El Punto de Entrada (Application Gateway)**
El tráfico desde la nube llega a nuestra IP pública (PIP) y pasa por la política de WAF antes de dividirse en el Application Gateway (AppGW):

- **Listener HTTPS:** Es el carril estándar para clientes que no usan certificados.
- **Listener mTLS:** Es el carril seguro. Este componente es el encargado de validar el certificado del cliente. Si la validación es exitosa, el AppGW inyecta automáticamente dos elementos críticos antes de pasar la posta al APIM: el mTLS Header (`X-Client-mTLS: SUCCESS`) y el Security Header.

**2. El Cerebro del Proceso (APIM & Policy OAuth2)**
El API Management (APIM) recibe la petición y aplica la Policy de OAuth2, la cual actúa de forma distinta según el origen:

- **Si viene del Listener mTLS:** La política verifica la presencia del header `X-Client-mTLS` y obliga al sistema a validar la Audience de mTLS.
- **Si viene del Listener HTTPS:** Se aplica la Audience Default de HTTPS.

**3. Validación de Identidad (MS Entra ID)**
Dependiendo de qué token pida el cliente, MS Entra ID emitirá un JWT con una "audiencia" específica:

- **Audience Wallet HTTPS:** Para consumidores que solo operan por el carril estándar.
- **Audience Wallet mTLS:** Para consumidores que operan exclusivamente por el carril seguro.
- **Punto de falla crítico:** Si un cliente intenta usar un token de la Audience mTLS entrando por el Listener HTTPS, el APIM rechazará la petición porque las audiencias no coinciden (*mismatch*). Por eso es vital que el cliente use la URL que apunta al Listener mTLS.

**4. Ejecución (AKS)**
Una vez que el APIM valida que el token es correcto para ese carril, la petición llega finalmente a la API Wallet corriendo en el cluster de AKS, donde se procesa la lógica de negocio.

## Ver también

- [politica_de_reintentos_de_webhook.md](politica_de_reintentos_de_webhook.md) — qué pasa si el webhook (mTLS o no) no responde HTTP 200.
- [conteo_de_pegadas_api_bank.md](conteo_de_pegadas_api_bank.md) — header transversal que propagan todos los microservicios que llaman a API Bank.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/seguridad_y_webhooks.md §1` (reestructuración PARA en cascada). Contenido sin cambios.*
