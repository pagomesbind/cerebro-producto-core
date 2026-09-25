---
artifact: risks
version: "1.0"
created: <YYYY-MM-DD>
estado: Propuesta  # → "Aprobado por PM (YYYY-MM-DD)" con el OK literal del PM
basado_en: {solution: "<versión>", crosscheck: "<versión>"}
---

<!--
Artefacto de /idea_risks. AUTOCONTENIDO: sin links a la wiki, sin nombres de archivo o de skill.
El origen de cada riesgo se describe por su naturaleza ("surgió de la revisión con Fraude",
"falla conocida del proveedor"), nunca por el nombre de un artefacto.
Probabilidad: Baja / Media / Alta · Impacto: Bajo / Medio / Alto · Estado: Abierto / Mitigado / Aceptado (con motivo).
🚧 = bloqueador de go-live (todo riesgo de familia B con probabilidad o impacto Alto, salvo decisión explícita del PM).
-->

# Riesgos: [Nombre de la iniciativa]

## Resumen para el PRD

_// Es lo que consolida el PRD: los riesgos que un lector externo necesita conocer, de las dos familias._

| Riesgo | Familia | Probabilidad | Impacto | Mitigación |
| --- | --- | --- | --- | --- |
|  | Entrega / Producto |  |  |  |

## A — Riesgos de entrega del proyecto

_// Lo que puede impedir que se construya bien, a tiempo o con el alcance acordado: proveedores, dependencias, alcance, capacidad._

| # | Riesgo | Origen | Probabilidad | Impacto | Mitigación | Dueño | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 |  |  |  |  |  |  | Abierto |

## B — Riesgos del producto en producción

_// Lo que puede salir mal una vez andando, aunque se haya construido perfecto. Catálogo mínimo: B1 Fraude · B2 Operativo · B3 Financiero · B4 Regulatorio · B5 Reclamos y reputación · B6 Dependencia de tercero._

| # | Riesgo | Pregunta | Probabilidad | Impacto | Mitigación | Dueño | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 |  | Fraude |  |  |  |  | Abierto |

### Preguntas del catálogo B sin riesgo identificado

_// Las seis se responden siempre. Una línea por cada pregunta que no generó riesgo, con el motivo._
* B<n> — <área de la pregunta> — sin riesgo / no aplica: <motivo>.

## Historial de revisiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | YYYY-MM-DD | Versión inicial del relevamiento de riesgos |
