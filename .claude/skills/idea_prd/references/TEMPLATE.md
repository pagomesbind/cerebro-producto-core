---
artifact: prd
version: "1.0"
created: <YYYY-MM-DD>
estado: Propuesta  # → "Aprobado por PM (YYYY-MM-DD)" con el OK literal del PM
basado_en: {start: "<versión>", solution: "<versión>", crosscheck: "<versión>", risks: "<versión>"}
---

# PRD: [Nombre de la feature/iniciativa]

## Problema
_// Describir el problema que debemos solucionar u oportunidad que debemos aprovechar._
Texto.

## Contexto
_// Contexto general. Por qué lo atacaríamos ahora? De dónde surgió el tema? Es urgente? Se trata de un proyecto aún más grande estratégicamente?_
Texto.

## Resumen de la solución planteada
_// Qué se construye y cómo funciona, de cara al negocio. Nombrala por lo que efectivamente se construye (ej. "nuevas funcionalidades por API para..."), no por una abstracción ambigua que suene a un proceso o servicio ya existente._
_// No alcanza con describir qué es: explicá quiénes participan, en qué orden ocurren las cosas, y qué pasa cuando algo falla — a nivel de consecuencia de negocio, no de manejo técnico del error. Es el destilado del análisis de solución si existe, no su detalle: sin contrato de endpoints, sin tablas de reintentos/backoff, sin mapa de procedencia campo por campo._
_// Si el lector no puede explicar con sus palabras cómo se resuelve el problema después de leer esta sección, quedó incompleta._
Texto.

## Objetivos
_// Cuáles son los objetivos que esperamos cumplir con este proyecto? Pensar en objetivos y beneficios para el negocio y/o operativos. Deben pensarse SMART y deben poder medirse en el futuro para validar el éxito o no de esta idea implementada._
* Texto.

## Caso de negocio
_// Describir el caso de negocio (o adjuntar archivo) para justificar el beneficio monetizado esperado. Tener en cuenta considerar el costo de construir la solución_
Texto.

## Definiciones, suposiciones y límites
_// Alguna decisión, limitante, restricción, riesgo o situación que condiciona y concluyó en preferir cierto camino para solucionar el problema._
_// Va también acá todo concepto o taxonomía que el lector necesite tener claro para entender el resto del documento (ej. tipos de cliente, modalidades de integración, estados de una operación): definilo una vez acá, no lo repartas por el documento._
* Texto.

## Alineación de la solución
_// ✅ Dibujá el perímetro.  🚫 No obligues al lector a deducir dónde termina el alcance._
_// Esta sección marca los bordes de la solución, no llena el interior: el equipo decide cómo construir dentro de ese perímetro. Si te encontrás explicando cómo se implementa algo, te pasaste del borde hacia adentro._

### Funcionalidades clave
_// Plan de registro: las funcionalidades que le dan forma a la solución, en orden de prioridad. Cada una lleva su etiqueta MoSCoW — el corte de los 🔴 MUST define el MVP._
_// Desafiá el tamaño: si un componente puede salir solo, antes que el resto, decilo acá._

**Dentro del alcance**
* 🔴 MUST — Texto.
* 🟠 SHOULD — Texto.
* 🟡 COULD — Texto.

**Fuera del alcance**
* ⚫ WON'T — Texto, con la razón por la que queda afuera.

**Consideraciones futuras**
_// Opcional. Lo que se guarda para más adelante pero condiciona cómo construimos hoy._
* Texto.

### Flujos clave
_// La experiencia end-to-end para el cliente: prosa, diagrama de flujo, capturas o exploraciones de diseño — varía según el proyecto y el equipo. No se arma en aislamiento: se trabaja con diseño e ingeniería._
_// Es natural que se vuelva más específico con el tiempo (arranca como unas capturas anotadas y puede terminar en requisitos detallados). Cuando cambie, registralo en el historial de revisiones al pie y avisá a los involucrados._
* Texto.

### Lógica clave
_// Reglas que guían el diseño y el desarrollo: escenarios comunes y casos borde. Suele ser más fácil escribirlas acá que pedirle a diseño que dibuje cada permutación._
_// No es el contrato de endpoints ni el manejo técnico del error — es la regla de negocio que decide qué pasa en cada caso._
* Texto.

## Impactos por área
_// CONSOLIDACIÓN, no análisis: se transcribe el "Resumen de impactos" de la revisión cruzada aprobada. Nunca se agrega, quita ni reinterpreta una fila._
_// Se revisaron nueve áreas: Comercial · Soporte / Operaciones e Integraciones · Administración y recaudaciones · Impuestos y contabilidad · Fraude · Legales · Cumplimiento / PLD · IT · Clientes externos en producción._
_// Las áreas con impacto van en la tabla; cada área sin impacto, en una línea con su motivo. Sin IDs de pregunta ni códigos de tarea._
_// QUÉ PROPONEMOS — Funcionalidad en el alcance (nombrada como en Funcionalidades clave) · Tarea previa al go-live · Contingencia operativa (cómo y quién lo absorbe)._

| **Área** | **Impacto** | **Qué proponemos** | **Estado** |
| --- | --- | --- | --- |
|  |  |  |  |

**Áreas evaluadas sin impacto**
* <Área> — <motivo en una frase>.

## Riesgos
_// CONSOLIDACIÓN: se transcribe el "Resumen para el PRD" del relevamiento de riesgos aprobado. Dos familias: Entrega (lo que puede impedir construirlo bien y a tiempo) y Producto (lo que puede salir mal una vez en producción)._

| Riesgo | Familia | Probabilidad | Impacto | Mitigación |
| --- | --- | --- | --- | --- |
|  | Entrega/Producto | Baja/Media/Alta | Bajo/Medio/Alto |  |

## Historial de revisiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | YYYY-MM-DD | Versión inicial del PRD |
