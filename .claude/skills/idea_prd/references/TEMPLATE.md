---
artifact: prd
version: "3.0"
created: <YYYY-MM-DD>
status: draft
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

## Checklist operativo por área
_// Recorré las 7 áreas completas, sin saltear ninguna, con una fila por pregunta. El valor está en dejar constancia de que se evaluaron todas, incluidas las que no tienen impacto._
_// RESPUESTA — nunca un Sí/No pelado: siempre Sí o No **más la explicación de por qué**, en una oración que alguien de esa área pueda leer y reconocer como su propio problema (ej. "Sí, porque se agrega un estado nuevo de la operación que el cliente tiene que contemplar en su conciliación diaria"). Un No también se explica._
_// QUÉ PROPONEMOS — una de tres salidas, siempre explícita; si la respuesta fue No, va "—":_
_//   · **Funcionalidad en el alcance** — y cuál, nombrada como aparece en Funcionalidades clave._
_//   · **Tarea previa al go-live** — algo a hacer antes de salir a producción que no es desarrollo (capacitar a un área, actualizar la documentación pública, comunicar a clientes integrados, cargar una configuración, validar un cálculo con el área). Muchas filas caen acá: el área tiene un impacto real y no hay nada que construir, hay algo que hacer._
_//   · **Contingencia operativa** — se convive con el impacto; decir cómo y quién lo absorbe._
_// ESTADO — Pendiente | Contemplado pero no validado | Contemplado y validado. "Validado" significa que el área lo confirmó, no que se asumió por cuenta propia._

| **Área** | **Pregunta clave** | **Respuesta (Sí/No + por qué)** | **Qué proponemos** | **Estado** |
| --- | --- | --- | --- | --- |
| Comercial |  |  |  | Pendiente |
| Soporte e Integraciones |  |  |  | Pendiente |
| Recaudaciones/Conciliación |  |  |  | Pendiente |
| Fraude |  |  |  | Pendiente |
| Legales |  |  |  | Pendiente |
| IT |  |  |  | Pendiente |
| Clientes externos en producción |  |  |  | Pendiente |

## **Riesgos**
_// Clasificar riesgos identificados con este proyecto — incluí los gaps de capacidad detectados en el checklist operativo que todavía no tengan resolución._

| Riesgo | Probabilidad | Impacto | Mitigación |
| --- | --- | --- | --- |
|  | Baja/Media/Alta | Bajo/Medio/Alto |  |
