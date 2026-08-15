---
name: sync_web
description: Sincronizador inteligente e idempotente de la documentación pública de APIs de Bind PSP. Analiza deltas en Framer y actualiza la wiki local sin duplicar archivos intactos.
when_to_use: Se activa cuando el usuario escribe de forma explícita el comando /sync_web en la terminal. Skill de fuente compartida: la corre solo el runner designado (ver `identidad.local.md`).
disable-model-invocation: true
argument-hint: ""
---

# ALGORITMO DE COMPORTAMIENTO: /sync_web (BIND PSP)

## 🔒 Paso -1 obligatorio — verificar que sos el runner

Leé `identidad.local.md` (raíz del repo). Si `runner_fuentes_compartidas` no es `true`, **abortá** con un mensaje claro: esta skill lee una fuente objetiva compartida entre los tres PM/PO. Avisale al usuario quién es el runner designado.

**Contrato de escritura (pipeline multi-PM, 2026-08-15):** `<producto>/apis_expuestas/` es espejo read-only en este install. Esta skill sigue leyendo de ahí para el Delta Check (Paso 8) y sigue calculando el contenido final igual que antes — pero **nunca escribe directo**: cada archivo con delta positivo nace como item `tipo: conocimiento` en `contexto_vivo/` (ver Paso 9).

## 📌 Contexto Técnico del Portal
- URL Base de rastreo: https://psp.bind.com.ar/developers
- URL de Seguridad Transversal: https://psp.bind.com.ar/developers/general
- Infraestructura del Portal: Framer (HTML Estático optimizado para SEO, lectura directa de DOM permitida).

## 🚨 SECCIÓN DE GOTCHAS (REGLAS DE ORO FINTECH)
Antes de escribir cualquier diff, recuerda estas verdades absolutas del producto:
1. **Falso Éxito en Staging:** El entorno de Sandbox/Staging de Bind PSP puede devolver códigos HTTP 200 OK estructurados en JSON incluso si la transacción falló internamente. Valida siempre el campo `status` o `sub_status` dentro del JSON, no te fíes solo del HTTP Status Code corporativo.
2. **Tablas Append-Only:** Las tablas de conciliación y movimientos de la API de Wallet son estrictamente de adición (*append-only*). Las filas válidas se identifican por el `version_id` más alto, jamás por el campo `created_at`.
3. **Mapeo de CUITs:** Todo endpoint de la funcionalidad de "Cuentas" requiere obligatoriamente un CUIT sanitizado (solo números, sin guiones). Si la documentación de Framer muestra guiones en los ejemplos, elimínalos al estructurar el manual local.

## 🏃‍♂️ PASOS DE EJECUCIÓN SÍNCRONA (PROHIBIDO SALTAR PASOS)

### Paso 1: Mapeo y Resolución de Enums
Antes de iniciar cualquier acción de raspado en las subpáginas, mapea las variables de entorno técnicas. Si el usuario ingresa un criterio de búsqueda de producto, conviértelo estrictamente a los Enums oficiales del portal:
- "Billetera" / "Wallet B2C" -> Mapear a la ruta técnica del portal: `wallet` o `1_wallet_services` — destino en la wiki: `detalle_productos/wallet/apis_expuestas/`
- "Cobros" / "Link de Pago" -> Mapear a la ruta técnica del portal: `soluciones_de_cobro` — destino en la wiki: `detalle_productos/agente_cobros_y_pagos/apis_expuestas/` (el slug del portal no coincide con el nombre de la carpeta de producto; no confundirlos)
- "Alta" / "Validación" -> Mapear a la ruta técnica del portal: `onboarding` — destino en la wiki: `detalle_productos/onboarding/apis_expuestas/`

**Regla general de destino:** el slug del portal Framer es solo para navegar/rastrear — el archivo se escribe siempre en `wiki/3_recursos/detalle_productos/<producto>/apis_expuestas/<funcionalidad>/`, usando el nombre de carpeta de producto que ya existe en la wiki (ver `wiki/3_recursos/detalle_productos/index.md`), no el slug literal del portal.

### Paso 2: Análisis de la Base General
Navega a https://psp.bind.com.ar/developers/general. Extrae los esquemas de autenticación actuales. Compara el texto contra los 3 archivos locales que hoy cubren ese contenido en `wiki/3_recursos/arquitectura_sistema/` (URLs base + OAuth2 + TLS + errores globales en `entornos_y_autenticacion_oauth2.md`; mTLS de APIs/webhooks en `mtls_apis_y_webhooks.md`; política de reintentos de webhook en `politica_de_reintentos_de_webhook.md`). Si hay cambios, actualizá el archivo temático que corresponda al delta detectado — no crees un archivo nuevo tipo `general_info.md` (regla anti-cajón de `CLAUDE.md`). Si es idéntico, detén la escritura de este paso.

### Paso 3: Rastreo de Menú Lateral Derecho (Crawl Profundo)
Accede recursivamente a cada producto y funcionalidad. Al abrir una página de funcionalidad (ej: `/guia-cuentas`), es obligatorio inspeccionar el contenedor del menú lateral derecho (Secciones "Guías" y "API Reference"). Extrae la lista de todas las sub-URLs de endpoints individuales y agrégalas a tu cola de procesamiento actual. **NO pases al Paso 4 hasta haber consolidado la lista total de sub-URLs del módulo.**

**Regla crítica — Slug Discovery (Anti-404):** Los slugs del portal Framer NO siguen un patrón predecible a partir del nombre del endpoint. **Está prohibido construir slugs por inferencia o naming convention** (ej. `qr-crearordenventa`). El procedimiento obligatorio es:
1. Obtener una página del módulo que responda HTTP 200 (la guía padre o cualquier endpoint conocido).
2. Extraer del HTML de esa página todos los `href` del menú lateral antes de intentar cualquier otra sub-URL.
3. Si la página obtenida no tiene sidebar con links, subir al nivel del producto padre y extraer los links desde ahí.
4. Solo intentar fetchear URLs que hayan sido extraídas del HTML — nunca URLs construidas por hipótesis.

**Regla crítica — URL Encoding (Anti-404 por acentos):** Framer encodifica caracteres especiales en slugs (tildes, ñ, acentos). Si una URL da 404, antes de declarar que el recurso no existe, **reintentar automáticamente con la versión URL-encoded** del segmento con caracteres especiales (ej. `qrест%C3%A1tico` en lugar de `qrestatico`). Solo declarar 404 definitivo si ambas variantes fallan.

### Paso 4: Extracción Obligatoria del Bloque "curl request" (Anti-Inferencia)
Cada página de API Reference del portal contiene un codeblock visible bajo el rótulo **"curl request"**, ubicado junto a la tabla de parámetros del Request. Este bloque contiene la **URL real del endpoint** (con su path completo, ej. `/bindentidad-qr-v2/v2/api/v1.201/generacion-qr-estatico`), el verbo HTTP, los query params reales y los headers usados en la llamada de ejemplo.

- **Es obligatorio extraer el contenido textual completo de ese codeblock**, no solo inferir la URL desde el breadcrumb o el título de la página.
- El bloque es seleccionable como texto plano en el DOM (no es una imagen): debe leerse directamente del HTML/snapshot de la página, igual que se lee cualquier otro texto visible. El ícono de "copy" en la esquina del bloque es solo un atajo de UI para el usuario humano — Claude Code no lo necesita, ya que puede leer el contenido del `<pre>`/`<code>` directamente.
- Si la página tiene más de un bloque de código (ej. `curl request` y un bloque de `response` aparte), captura ambos por separado y etiquétalos según su rótulo visible en la UI.
- **Prohibido alucinar o completar la URL real a partir del nombre del endpoint.** Si el codeblock "curl request" no es legible en el snapshot (por bloqueo de red o renderizado incompleto), aplica la fila correspondiente de la Tabla de Mitigación de Errores — no se debe inventar un path de URL.
- Con la URL real extraída del curl, reemplaza cualquier placeholder o ruta inferida que existiera en el archivo Markdown local de ese endpoint.

### Paso 5: Precisión Obligatoria en Descripciones y Alertas Toast (Anti-Resumen)
La descripción funcional de cada endpoint y las alertas tipo *toast* (los recuadros de advertencia/info, como el ícono ⓘ visible bajo el título "Si se modifica algún atributo del comercio..." en las páginas de API Reference) son contexto funcional crítico para el Segundo Cerebro. Es estrictamente obligatorio:

- **No resumir, no parafrasear, no comprimir** la descripción textual de cada endpoint. Debe transcribirse completa y literal tal como aparece en el portal, párrafo por párrafo.
- **Capturar todo componente toast/alert visible en la página** (cajas de advertencia, nota, tip o warning con ícono), sin omitir ninguna, y transcribirlas textualmente en una sección dedicada `## ⚠️ Notas y Advertencias del Portal` dentro del archivo Markdown del endpoint. Cada alerta debe quedar diferenciada como bloque de cita (`>`) para preservar su carácter de aviso especial.
- Si una alerta toast contiene una regla de negocio (ej. "deberá volverse a regenerar el QR estático... debido a que la composición del mismo pudo haber cambiado"), esa regla **no se reformula ni se simplifica** — se preserva la redacción original del portal porque es la fuente de verdad funcional.
- Prohibido fusionar la descripción del endpoint con la descripción de la guía padre. Son dos textos distintos y deben quedar separados en el archivo.

### Paso 6: Captura Literal y Completa de Páginas de Guía (`guia_*.md`)
Las páginas de tipo "Guías" (no API Reference) son el contexto funcional principal del Segundo Cerebro y tienen un estándar de fidelidad más estricto que los endpoints:

- **Es obligatorio guardar el contenido textual de la página de guía de forma explícita y literal**, tal cual está redactado en el portal — sin resumir, sin reordenar párrafos, sin reescribir con otras palabras. El objetivo es preservar el texto fuente, no producir una versión editorializada.
- Esto incluye: introducción, conceptos clave, listas, tablas, diagramas de flujo descritos en texto, casos de uso, precondiciones y **cualquier alerta toast presente en la guía**, capturada también bajo `## ⚠️ Notas y Advertencias del Portal` con cita en bloque (`>`).
- Solo está permitido el recorte de ruido puramente visual de Framer (nav bars, footers, botones "Anterior/Siguiente", breadcrumbs repetidos) — nunca el recorte de contenido textual sustantivo.
- Si una guía ya existe localmente, el Delta Check del Paso 7 debe comparar el texto **palabra por palabra** contra la versión viva del portal, no solo a nivel temático/semántico, antes de decidir si hay delta.

### Paso 7: Descripción Textual de Flujos y Diagramas en Guías
Las páginas de tipo "Guías" frecuentemente incluyen imágenes de diagramas de flujo o secuencia que documentan lógica de negocio que **no está repetida en el texto**. Es obligatorio reconstruirlas como texto, no capturarlas como imagen.

**Limitación confirmada de Framer SPA:** todas las imágenes del portal tienen los atributos `alt` y `title` vacíos (sin metadatos). Las URLs de imagen son de `framerusercontent.com` y pueden no ser accesibles directamente. Por lo tanto, **la visión directa de la imagen no es el método primario** — se debe trabajar con lo que `get_page_text` sí devuelve.

**Procedimiento obligatorio:**

1. **Extraer los títulos de diagrama** desde el texto de la página (visible en `get_page_text` como líneas del estilo "Flujo de transferencia entrante aprobada", "Flujo de cobro exitoso con QR", etc.). Cada título de diagrama en el portal corresponde a un flujo que hay que documentar.

2. **Intentar obtener las URLs de imagen** mediante `javascript_tool` con:
   ```js
   Array.from(document.querySelectorAll('img')).map(i => i.src)
   ```
   Si alguna imagen es accesible visualmente (con herramienta de visión), interpretarla directamente. Si no es accesible, continuar con el paso siguiente.

3. **Reconstruir el flujo textualmente** combinando:
   - El título del diagrama (informa el escenario: aprobado, rechazado, en proceso, etc.)
   - La descripción funcional del texto de la página (Paso 6)
   - El comportamiento de los endpoints del módulo (Paso 4 y 5)
   - El conocimiento de dominio del sistema (estados, actores, condicionales conocidos)

4. **Escribir una sección por cada flujo detectado**, usando el formato:
   ```markdown
   ## Flujo — [título del diagrama tal como aparece en la página]

   ```
   [descripción en bloque de código con pasos numerados, actores → acciones, condicionales]
   ```
   ```
   Sin emojis en el encabezado. Sin referencias a URLs de imagen. Sin notas de "interpretado por Claude Code". El texto debe ser directo y legible como contexto de segundo cerebro.

5. **Idempotencia:** si la guía ya tiene secciones `## Flujo —` que cubren los mismos títulos de diagrama que muestra la página, y el contenido de la página no cambió, no reescribir. Contar como sin delta para esta sección.

6. Si una guía no tiene ningún título de diagrama en su página, omitir las secciones de flujo por completo.

7. Las secciones de flujo son **complementarias** al texto literal del Paso 6, nunca un reemplazo: ambas quedan en el archivo, separadas.

### Paso 8: Análisis de Diferencias e Idempotencia (Delta Check)
Para cada sub-URL de endpoint o guía procesada en el Paso 3, verifica si ya existe su archivo Markdown homólogo en `wiki/3_recursos/detalle_productos/<producto>/apis_expuestas/`.
- **Acción:** Compara el esquema de parámetros del Request, el bloque `curl request` extraído en el Paso 4, la descripción y alertas toast extraídas en el Paso 5, el texto literal de guía extraído en el Paso 6, el hash/URL de imágenes de diagrama del Paso 7, el JSON Payload de ejemplo y las respuestas HTTP vivas de la web contra el archivo local.
- **Condición de Bloqueo:** Si el contenido técnico coincide al 100% (incluyendo la URL real del curl, la descripción literal, las alertas toast y el hash de las imágenes de diagrama), ignora la acción de escritura. Queda estrictamente prohibido sobrescribir un archivo si no presenta deltas, para conservar los metadatos y la caché del sistema.
- **Caso especial — Archivo con URL inferida:** si el archivo local tiene una URL marcada como "pendiente de confirmación con equipo técnico" o inferida del contexto, y el Paso 4 logró extraer la URL real, esto SIEMPRE cuenta como delta positivo aunque el resto del contenido no haya cambiado.
- **Caso especial — Descripción resumida en ciclo anterior:** si el archivo local contiene una descripción condensada, parafraseada o una nota de "el portal no expone descripción completa" (heredada de un ciclo de extracción anterior menos riguroso), y esta corrida logra capturar el texto literal completo, esto SIEMPRE cuenta como delta positivo.
- **Caso especial — Guía sin flujos textuales:** si una guía local fue creada en un ciclo anterior y el portal muestra títulos de diagrama que no están documentados como secciones `## Flujo —` en el archivo local, esto SIEMPRE cuenta como delta positivo aunque el resto del contenido no haya cambiado.
- **Caso especial — Guía con flujos en formato obsoleto:** si el archivo local tiene secciones `## 🔀 Diagrama de Flujo (interpretado)` con comentarios `<!-- img-src -->` y referencias a URLs de imagen de Framer, contar como delta positivo y reescribirlas en el nuevo formato `## Flujo —` sin emojis ni referencias a imagen.

### Paso 9: Captura Selectiva como Items de `contexto_vivo/`
Solo si el endpoint o guía es completamente nuevo o presenta modificaciones en sus parámetros, URL real, descripción, alertas toast, diagramas o ejemplos (Caso de Delta Positivo), generá **un item `tipo: conocimiento` en `wiki/1_proyectos/contexto_vivo/`** por archivo (`destino_propuesto` = la ruta del archivo Markdown atómico en `apis_expuestas/`, `tipo_destino: crear` o `actualizar`). El cuerpo del item mantiene el estándar de diseño de siempre:
- **Para endpoints:** Descripción (literal), URL/Método (URL real extraída del curl, no inferida), Tabla de Parámetros, Bloque `curl request` íntegro, Request JSON, Response JSON, Errores, y sección `## ⚠️ Notas y Advertencias del Portal` con las alertas toast capturadas.
- **Para guías:** Contenido literal completo de la página (introducción, conceptos, flujos, casos de uso), sección `## ⚠️ Notas y Advertencias del Portal` con las alertas toast capturadas, y una sección `## Flujo — [nombre]` por cada diagrama o escenario detectado en la página (sin emojis, sin referencias a imágenes, como bloques de texto plano en formato código).

## 🛠️ TABLA DE MITIGACIÓN DE ERRORES (ANTI-ALUCINACIÓN)
Si golpeas un fallo en la red o en el DOM, ejecuta la siguiente ruta de recuperación determinista de forma inmediata:
| Error Detectado | Causa Probable | Acción de Recuperación Obligatoria (Claude Code) |
| :--- | :--- | :--- |
| WebFetch devuelve contenido vacío o solo metadatos del sitio (título "Bind PSP", sin texto de guía/endpoint) | Framer SPA requiere JavaScript para renderizar — WebFetch solo obtiene el shell HTML estático | **Escalada obligatoria al Chrome MCP:** usar `mcp__Claude_in_Chrome__navigate` para navegar a la URL, luego `mcp__Claude_in_Chrome__get_page_text` para extraer el contenido renderizado. Para imágenes de diagrama, usar `mcp__Claude_in_Chrome__javascript_tool` para obtener los `src` de los `<img>` y luego leerlas con visión. Este es el método correcto para Framer — no reintentar con WebFetch. |
| HTML DOM Vacío / Bloqueo de IP (Chrome MCP también falla) | Control de Tráfico / Cloudflare activo en Framer | Detén el raspado automático. Registra la página en la sección **PÁGINAS CON ERROR** del reporte final. Notifica al usuario: "Bloqueo de red detectado en [URL]. Por favor, realiza un copy-paste del texto visible en el browser y deposítalo en raw/api_docs_raw.txt para procesarlo de forma local". |
| Parámetros faltantes en sub-página | Renderizado incompleto del componente web | Primero intentar Chrome MCP (ver fila anterior). Si también falla, usar Bash `curl` con headers de User-Agent reales para forzar la descarga del HTML crudo y buscar bloques de código bajo etiquetas `<pre>` o `<code>`. |
| Ruta de Producto Desconocida | Cambio de estructura en el CMS de Framer | No improvises una ruta nueva. Capturá un item `tipo: gap` (`destino_propuesto: 2_areas/gaps_y_preguntas.md`) detallando la URL huérfana y solicitá la intervención del usuario. |

### 📋 Registro obligatorio de páginas con problema
Al finalizar cada módulo, el reporte de salida **debe incluir explícitamente** una sección:
```
PÁGINAS CON ERROR (requieren revisión manual):
- [URL] — Motivo: [WebFetch vacío / 404 definitivo / Chrome MCP bloqueado / contenido parcial]
```
Si no hubo páginas con error, escribir `PÁGINAS CON ERROR: ninguna`. Esta sección nunca debe omitirse — es la señal para que el usuario pueda corregir manualmente lo que la skill no pudo resolver.

## 📊 EJEMPLO DE FORMATO DE SALIDA DE LA SKILL
Al finalizar el escaneo completo, debes imprimir en la terminal un reporte consolidado idéntico a este formato:
```text
Sincronización de APIs finalizada. Estado del Segundo Cerebro:
- [NUEVO ENDPOINT] Creado de forma atómica: wiki/3_recursos/detalle_productos/wallet/apis_expuestas/cuentas/endpoint_post_crear.md
- [ACTUALIZADO] Deltas aplicados en JSON de respuesta: wiki/3_recursos/detalle_productos/wallet/apis_expuestas/transferencias/endpoint_get_id.md
- [DESCRIPCIÓN ACTUALIZADA] Texto literal capturado, reemplaza resumen previo: wiki/3_recursos/detalle_productos/adquirencia/apis_expuestas/qr_estatico/endpoint_get_generar_codigo_qr.md
- [FLUJO TEXTUAL AGREGADO] 3 escenarios documentados (aprobado/rechazado/sin orden): wiki/3_recursos/detalle_productos/adquirencia/apis_expuestas/qr_estatico/guia_qr_estatico.md
- [SIN CAMBIOS] 24 endpoints verificados e ignorados por idempotencia.
```

## Cierre

Regenerá `contexto_vivo/index.md` con los items nuevos de esta corrida. **Sin git** — el commit del repo personal lo hace el hook `SessionStart` una vez al día.
