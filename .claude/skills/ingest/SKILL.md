---
name: ingest
description: Motor universal e inteligente de ingesta por lotes para el Cerebro Bind PSP. Procesa la carpeta raw/, aplica PARA, rota archivos y sincroniza con GitHub de forma automatizada.
when_to_use: Se activa inmediatamente cuando el usuario ejecuta el comando de barra /ingest en la terminal de Claude Code.
disable-model-invocation: true
argument-hint: "[escribe el contexto o descripción del lote aquí]"
---

# ⚙️ SÚPER-ALGORITMO DE INGESTA GENERAL: /ingest

## 📥 Contexto de Entrada Recibido
El usuario solicita procesar el lote de archivos en bruto que residen en la carpeta `raw/`. El contexto específico del lote proporcionado por el usuario en sus argumentos es: **$ARGUMENTS**

## 🏃‍♂️ PASOS DE EJECUCIÓN SECUENCIAL (PROHIBIDO SALTAR PASOS)

### Paso 1: Conversión y Extracción Local
- Inspecciona la raíz de la carpeta `raw/`. Detecta todos los archivos binarios (`.pdf`, `.docx`, `.txt`, `.csv`) presentes.
- Utiliza las herramientas CLI de la consola (`pandoc`, `pdftotext`, etc.) para volcar de forma limpia el texto plano de los archivos. Si un archivo es un `.docx`, prioriza `pandoc` para conservar tablas y sangrías de payloads JSON.

### Paso 2: Análisis de Deltas e Idempotencia (Delta Check)
- Contrasta la información extraída con el estado actual de la carpeta `wiki/` **y** con `wiki/1_proyectos/contexto_vivo/index.md` (items `capturado`/`en_cola`, todavía sin mergear). Esta skill la puede correr cualquier PM/PO sobre su propio `raw/`, así que un aporte ya capturado por otra sesión — propia o de otro PM — y pendiente de `/context_merge` cuenta como duplicado igual que si ya estuviera en el canon.
- **Ley de Hierro:** Si el conocimiento, endpoints o parámetros extraídos coinciden al 100% con los documentos ya curados en tu base local, o con un item ya capturado en `contexto_vivo/` en_cola, detén el proceso de sobreescritura/recaptura de esos elementos específicos para proteger la integridad de los metadatos y optimizar tokens.

### Paso 3: Clasificación Taxonómica Estricta (Framework PARA)
Rutea el conocimiento nuevo bajo estos criterios de negocio — pero **`2_areas/` y `3_recursos/` nunca se escriben directo**: nace todo como item en `wiki/1_proyectos/contexto_vivo/` (ver plantilla ahí), con `destino_propuesto` apuntando a la ruta real. Solo `/context_merge` escribe esas dos capas.
- `wiki/1_proyectos/`: Iniciativas o integraciones vivas con fecha de finalización fija — **esto sí es escritura directa**, resolvé la carpeta real en `wiki/1_proyectos/index.md` antes de escribir, nunca asumas la ruta plana. Un gap detectado sobre un proyecto va a su `gaps.md` propio, no al canon fijo.
- `wiki/2_areas/`: Responsabilidades operativas, mapas de stakeholders o funnels continuos → item `tipo: conocimiento`. `wiki/2_areas/overview_productos/overview_<producto>.md` es el overview de negocio vivo de cada producto (Wallet, Adquirencia, Agente de Cobros y Pagos, Onboarding, Ardid) — el usuario lo actualiza directamente con contexto/noticias actuales; **nunca propongas reemplazarlo ni fusionarlo con contenido de `raw/`**, como mucho un item de agregado puntual si el lote trae una novedad de negocio genuina.
- `wiki/3_recursos/`: recurso técnico o de referencia, partido en 3 vías que **no se mezclan entre sí** — igual, cada uno como item con `destino_propuesto` correspondiente:
  - `<producto>/apis_expuestas/` — dominio exclusivo de la skill `/sync_web` (texto literal del portal público de developers). `/ingest` **nunca propone esta ruta**, aunque el lote traiga specs de API — si eso pasa, `destino_propuesto` va a `detalle_productos/<producto>/` como nota, no a esta carpeta.
  - `arquitectura_sistema/` — sistemas/IT duro **no ligado a un producto**: infraestructura cloud, seguridad de plataforma, NFR/performance, evolución de plataforma, relación técnica con el proveedor (ej. Fintexa). Si el contenido tiene un producto dueño claro, `destino_propuesto` va a `detalle_productos/<producto>/`, no acá.
  - `cumplimiento_normativo/` — obligaciones regulatorias (PLD/BCRA/Worldsys, PCI DSS, límites UIF/ROS).
  - `detalle_productos/<producto>/`: **destino por defecto de casi todo lo que ingresa por `/ingest`** cuando no pertenece a un proyecto vivo ni a `2_areas/` — mecánica interna, manuales de configuración/integración, aprendizajes de reuniones, documentación de procesadores externos, hacks operativos, y **cualquier conocimiento no técnico relevante a otras áreas de Bind PSP** (Soporte, Comercial, Integraciones, Administración), no solo Producto/Ingeniería. Subdividido primero por producto (`wallet/`, `adquirencia/`, `agente_cobros_y_pagos/`, `onboarding/`, `ardid/`, `siscri/`, `servicios/`, `portal_admin/`, `portal_comercio/`, `apk_wallet/`, `ecosistema_wallet_adquirencia/`, y los que corresponda), luego por archivos temáticos de funcionalidad dentro de cada producto (**1 tema = 1 archivo** — agrupá por tema, revisando primero el `index.md` del producto para ver si el contenido nuevo encaja en un archivo temático ya existente antes de proponer uno nuevo). **Si no se identifica el producto dueño, no lo metas por descarte en ninguno — capturalo como item `tipo: gap`** (regla anti-cajón de `CLAUDE.md`; nombres como `transversal/`, `otros/`, `varios/` están vetados).
- `wiki/4_archivos/`: Historial inactivo o post-mortems de caídas del sistema. **Nunca es destino de una ingesta nueva**, salvo el cierre de algo que efectivamente termina.

### Paso 4: Ejecución de Leyes de Control de Memoria (CLAUDE.md)
Durante el procesamiento de este lote (orientado a: $ARGUMENTS), ejecuta obligatoriamente estos tres sub-procesos de calidad:
1. **Control Activo de Gaps:** Si encuentras contradicciones o vacíos técnicos, capturalos ordenados por fecha y severidad en el destino correcto (Protocolo de Ruteo de Ingesta de `CLAUDE.md`): `gaps.md` del proyecto/IDEA si el lote es específico de uno (directo), o item `tipo: gap` en `contexto_vivo/` si es de contexto fijo. Consúltame la resolución de estas dudas en la terminal al final de tu turno.
2. **Log de Decisiones:** Si el lote revela definiciones o trade-offs estratégicos tomados por la empresa, capturalos de inmediato como item `tipo: decision` en `contexto_vivo/` — nunca directo a `wiki/2_areas/direccion/decisiones.md`.
3. **Mecanismo de Rotación Efímera:** Una vez capturado el conocimiento (en `contexto_vivo/` o directo en `1_proyectos/`), crea una carpeta en `wiki/4_archivos/historial_raw/` nombrada con el formato: `YYYY-MM-DD_ingesta_[breve_nombre_del_lote]`. Mueve físicamente todos los archivos binarios originales desde `raw/` hacia esa subcarpeta histórica usando el comando `mv`. La carpeta `raw/` debe quedar completamente vacía.

### Paso 5: Cierre
1. Regenerá `contexto_vivo/index.md` si capturaste items nuevos.
2. Actualizá los índices locales de `1_proyectos/` que hayas tocado directo. Los índices de `2_areas/`/`3_recursos/` los actualiza `/context_merge`, no esta skill.
3. **Sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día — no lo ejecutes vos.
