---
artifact: prd
version: "2.0"
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

Agregar una pantalla de preview, antes de arrancar la carga, que le muestre al comercio la lista completa de documentos societarios requeridos según su tipo de entidad (unipersonal / sociedad), con un ejemplo visual de cada documento.

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

## Funcionalidades y roadmap

Priorizado con MoSCoW, sobre el roadmap ya acordado con Ingeniería para este trimestre:

### 🔴 Must have — MVP, imprescindible para bajar el abandono este trimestre
* Pantalla de preview de documentación requerida, mostrada antes del formulario de carga de KYB.
* Lógica de armado de la lista según el tipo de entidad declarado por el comercio (unipersonal / sociedad).
* Comportamiento de fallback: si el tipo de entidad no está declarado o falla la resolución de la lista, mostrar la lista genérica más amplia sin bloquear el alta.

### 🟠 Should have — mejora la calidad del preview, no bloquea el lanzamiento
* Imágenes de ejemplo por tipo de documento requerido.

### 🟡 Could have — deseable, sin driver de negocio que lo adelante todavía
* Aceptar fotos sacadas con el celular además de PDF — depende de cambios del proveedor de onboarding.

### ⚫ Won't have (por ahora) — fuera de foco de este ciclo
* Traducción de la lista de documentos a otros idiomas, si en el futuro hay comercios de fuera de Argentina.

## Flujos clave y referencias clave

* Flujo actual de alta de comercios (paso de carga de KYB) — [pendiente: link a diagrama/Figma existente].
* Mockup de la nueva pantalla de preview — [pendiente de Diseño].
* Problem statement de origen — `wiki/1_proyectos/.../artefactos/problem_statement_kyb.md`.
* Hipótesis validada — `wiki/1_proyectos/.../artefactos/hipotesis_preview_kyb.md`.

## Análisis de impacto en las distintas áreas

Solo se incluyen las áreas con impacto real — Administración y Legales no tienen impacto identificado en este cambio (no cambia requisitos regulatorios ni procesos administrativos) y se excluyen de la tabla.

| **Área** | **Impacto** | **Cómo la afecta el proyecto** | **¿Ya tiene lo que necesita para actuar?** |
| --- | --- | --- | --- |
| Comercial | Medio | Menos altas truncas que hoy terminan re-intentando por canal asistido; libera capacidad del equipo comercial en el corto plazo. | Sí — no requiere ninguna acción de su parte, es una liberación de carga pasiva. |
| Soporte e integraciones | Bajo | La pantalla nueva puede generar consultas puntuales al principio del lanzamiento. | No del todo — falta coordinar un aviso previo al lanzamiento con el manual de ayuda actualizado; contingencia simple, no requiere alcance nuevo. |
| Fraude | Bajo | No cambia el criterio de validación de documentos, solo cuándo se le informa al comercio qué va a necesitar. | Sí — no hay acción de su parte. |
| Clientes externos ya en producción | Nulo | Solo afecta el flujo de alta de comercios nuevos, no a comercios ya activos. | — (sin impacto, no aplica). |

## **Riesgos**

| Riesgo | Probabilidad | Impacto | Mitigación |
| --- | --- | --- | --- |
| El preview alarga la percepción de esfuerzo y empeora el abandono en vez de mejorarlo | Media | Alto | Validar primero con un A/B test antes de lanzar a 100% del tráfico. |
| Fintexa no expone la metadata de documentos requeridos por tipo de entidad | Media | Medio | Definir la lógica de lista por tipo de entidad del lado de Bind como plan B. |
| El cambio impacta componentes de UI compartidos con el alta de Wallet sin coordinación previa | Baja | Medio | Confirmar con el equipo de Wallet antes de tocar componentes compartidos. |
| Soporte no llega a tener el aviso/manual de ayuda listo para el lanzamiento (gap detectado en el análisis de impacto) | Media | Bajo | Coordinar con Soporte la fecha del aviso antes de fijar la fecha de lanzamiento. |
