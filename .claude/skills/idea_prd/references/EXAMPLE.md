---
artifact: prd
version: "3.0"
created: 2026-07-20
status: complete
context: Ejemplo ilustrativo — cifras ficticias, no son datos reales de Bind PSP. Continúa el caso de ejemplo de abandono en el alta de comercios de Adquirencia.
---

# PRD: Preview de documentación KYB en el alta de comercios

## Problema

58% de los comercios que llegan al paso de carga de documentación KYB en el alta digital self-service de Adquirencia lo abandonan sin completarlo. El feedback de soporte apunta a que el comercio no sabe de antemano qué documentos societarios le van a pedir, y descubre el requisito recién cuando ya está en el formulario de carga.

## Contexto

Es la etapa del funnel de alta digital con mayor caída de todo el proceso, y conecta directo con el foco de Onboarding del período, que prioriza justamente cobertura y fricción de alta. No es un problema nuevo — aparece de forma recurrente en tickets de soporte y en feedback de comercial —, pero se vuelve urgente ahora porque escalar volumen de Adquirencia sin bajar esta fricción implica sumar carga proporcional al equipo comercial para sostener el alta asistida de los comercios que abandonan el flujo self-service.

## Resumen de la solución planteada

Se agrega una pantalla de preview, antes de arrancar la carga de KYB, que le muestra al comercio la lista completa de documentos societarios requeridos según su tipo de entidad (unipersonal / sociedad), con un ejemplo visual de cada documento.

El flujo queda así: el comercio ya declaró su tipo de entidad en un paso anterior del alta; con ese dato, el sistema arma la lista de documentos correspondiente y se la muestra antes de llevarlo al formulario de carga. El comercio revisa la lista, entiende qué va a necesitar, y recién ahí decide si continúa. Si el tipo de entidad no está declarado o la resolución de la lista falla por cualquier motivo, el sistema no bloquea el alta: muestra una lista genérica más amplia (la unión de todos los documentos posibles) para no dejar al comercio sin poder avanzar. La carga de KYB en sí no cambia — lo único nuevo es que el comercio sabe de antemano qué le van a pedir.

## Objetivos

* Bajar el abandono en el paso de carga de KYB de [Ejemplo] 58% a [Ejemplo] 45% para fin de trimestre.
* Bajar el tiempo promedio hasta activación de la cuenta de [Ejemplo] 6 a [Ejemplo] 4 días para fin de trimestre.
* Aumentar la proporción de altas completadas sin intervención de un ejecutivo comercial de [Ejemplo] 42% a [Ejemplo] 60% para fin de trimestre.

## Caso de negocio

[Ejemplo] Cada punto de abandono recuperado en este paso representa activaciones adicionales de comercios que ya mostraron intención de adherirse — es conversión de demanda existente, no adquisición nueva. Hoy, buena parte de esos comercios que abandonan re-intentan por canal asistido (con ejecutivo comercial), lo que sube el costo de adquisición de esa cohorte. El costo de construir la solución es bajo (una pantalla adicional + lógica de filtrado por tipo de entidad); el mayor riesgo de costo está en la dependencia de la metadata de documentos por tipo de entidad (ver sección de definiciones y límites).

## Definiciones, suposiciones y límites

* Los requisitos documentales de KYB no se pueden relajar — vienen de cumplimiento normativo (BCRA/UIF). Lo que se mejora es la experiencia de carga, no el requisito en sí.
* Se prioriza confirmar primero si la metadata de "documentos requeridos por tipo de entidad" está disponible del lado del proveedor de onboarding (Fintexa) antes de definir si esa lógica se resuelve ahí o del lado de Bind.
* El flujo de carga comparte componentes de UI con el alta de Wallet — cualquier cambio compartido se coordina con ese equipo antes de tocarlo.
* No se contempla en esta iteración cambiar el formato de archivo aceptado (sigue siendo solo PDF).
* **Tipos de entidad**, para referencia del resto del documento: *unipersonal* (persona humana con CUIT de monotributo o autónomo) y *sociedad* (persona jurídica, cualquier forma societaria) — son los dos únicos valores que hoy declara el comercio en el alta, y determinan qué lista de documentos se le muestra.

## Alineación de la solución

### Funcionalidades clave

Priorizado con MoSCoW, sobre el roadmap ya acordado con Ingeniería para este trimestre:

**Dentro del alcance**
* 🔴 MUST — Pantalla de preview de documentación requerida, mostrada antes del formulario de carga de KYB.
* 🔴 MUST — Lógica de armado de la lista según el tipo de entidad declarado por el comercio (unipersonal / sociedad).
* 🔴 MUST — Comportamiento de fallback: si el tipo de entidad no está declarado o falla la resolución de la lista, mostrar la lista genérica más amplia sin bloquear el alta.
* 🟠 SHOULD — Imágenes de ejemplo por tipo de documento requerido. No bloquea el lanzamiento si no llega a tiempo.
* 🟡 COULD — Aceptar fotos sacadas con el celular además de PDF. Depende de cambios del proveedor de onboarding — deseable, sin driver de negocio que lo adelante todavía.

**Fuera del alcance**
* ⚫ WON'T — Traducción de la lista de documentos a otros idiomas: se difiere porque hoy no hay comercios de fuera de Argentina en el flujo self-service.

**Consideraciones futuras**
* Si en el futuro se suman más tipos de entidad (ej. fideicomisos), la lógica de armado de lista tiene que poder extenderse sin rehacer la pantalla — no es parte del alcance de este PRD, pero condiciona que la lista no se hardcodee por los dos valores actuales.

### Flujos clave

1. El comercio llega al paso de KYB del alta digital, con su tipo de entidad ya declarado en un paso previo.
2. El sistema arma la lista de documentos requeridos para ese tipo de entidad y la muestra en la pantalla de preview, con un ejemplo visual de cada documento.
3. El comercio revisa la lista y confirma que quiere continuar (o sale del alta sin completarla, igual que hoy).
4. Al confirmar, el comercio pasa al formulario de carga existente — sin cambios sobre cómo se sube cada documento.
5. Si el tipo de entidad no está declarado, o la resolución de la lista falla, el paso 2 muestra la lista genérica en vez de bloquear el avance.

*(Mockup de la pantalla de preview: en definición con Diseño al momento de este PRD.)*

### Lógica clave

* La lista de documentos se resuelve una sola vez, al entrar a la pantalla de preview — si el comercio corrige su tipo de entidad después de ver el preview, se le vuelve a mostrar la lista actualizada antes de dejarlo avanzar a la carga.
* El fallback a lista genérica nunca es un error visible para el comercio: se muestra como si fuera el comportamiento normal, sin mensaje de error ni fricción adicional.
* La pantalla de preview no persiste ninguna decisión del comercio — es solo informativa; no cambia ni valida nada del lado del sistema hasta que el comercio llega al formulario de carga real.

## Checklist operativo por área

| **Área** | **Pregunta clave** | **Respuesta (Sí/No + por qué)** | **Qué proponemos** | **Estado** |
| --- | --- | --- | --- | --- |
| Comercial | ¿Hay clientes en pipeline cuya integración cambia por esto? | No — el cambio es sobre el flujo self-service, no sobre el proceso de alta asistida que usa comercial. | — | Contemplado y validado |
| Soporte e Integraciones | ¿Aparecen errores o estados nuevos que Soporte va a ver en un reclamo y hoy no sabe interpretar? | Sí — la pantalla nueva puede generar consultas puntuales al principio del lanzamiento, sobre todo de comercios que no entienden por qué ahora se les pide algo "antes" de cargar. | Tarea previa al go-live: avisar a Soporte antes del lanzamiento y actualizar el manual de ayuda con la pantalla nueva. | Pendiente |
| Administración | ¿Genera movimientos de dinero nuevos o cambia cómo se contabilizan y concilian? | No — no toca liquidaciones, impuestos ni conciliación; es un cambio de experiencia en el alta. | — | Contemplado y validado |
| Fraude | ¿Cambia el criterio de validación de documentos o el perfil de riesgo del alta? | No — no cambia qué se valida ni cuándo, solo cuándo se le informa al comercio qué va a necesitar. | — | Contemplado y validado |
| Legales | ¿Tiene implicancias regulatorias (BCRA, UIF/PLD)? | No — los requisitos documentales de KYB no cambian, solo el momento en que se comunican. | — | Contemplado y validado |
| IT | ¿Depende de un desarrollo de un proveedor externo y con qué lead time? | Sí — depende de que Fintexa confirme si expone la metadata de "documentos requeridos por tipo de entidad" o si esa lógica se resuelve del lado de Bind. Todavía no está confirmado. | Tarea previa al go-live: confirmar con Fintexa la disponibilidad de la metadata antes de cerrar el diseño técnico; si no la expone, la lógica de lista se resuelve como funcionalidad propia (ya contemplada en Funcionalidades clave). | Pendiente |
| Clientes externos en producción | ¿Es un breaking change para alguien ya integrado? | No — solo afecta el flujo de alta de comercios nuevos, no a comercios ya activos. | — | Contemplado y validado |

## **Riesgos**

| Riesgo | Probabilidad | Impacto | Mitigación |
| --- | --- | --- | --- |
| El preview alarga la percepción de esfuerzo y empeora el abandono en vez de mejorarlo | Media | Alto | Validar primero con un A/B test antes de lanzar a 100% del tráfico. |
| Fintexa no expone la metadata de documentos requeridos por tipo de entidad (gap detectado en el checklist operativo, IT) | Media | Medio | Definir la lógica de lista por tipo de entidad del lado de Bind como plan B. |
| El cambio impacta componentes de UI compartidos con el alta de Wallet sin coordinación previa | Baja | Medio | Confirmar con el equipo de Wallet antes de tocar componentes compartidos. |
| Soporte no llega a tener el aviso/manual de ayuda listo para el lanzamiento (gap detectado en el checklist operativo, Soporte) | Media | Bajo | Coordinar con Soporte la fecha del aviso antes de fijar la fecha de lanzamiento. |
