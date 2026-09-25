---
artifact: crosscheck
version: "1.0"
created: <YYYY-MM-DD>
estado: Propuesta  # → "Aprobado por PM (YYYY-MM-DD)" con el OK literal del PM
basado_en: {start: "<versión>", solution: "<versión>"}  # versiones de los artefactos de arriba usadas en esta revisión
---

<!--
Artefacto de /idea_crosscheck. AUTOCONTENIDO: sin links a la wiki, sin nombres de archivo o de skill,
sin jerga de proceso interno. Los T-NNN van solo en la columna "Tarea" — /idea_prd no la transcribe.
Se recorren las 9 áreas y todas las preguntas del catálogo, sin podar. Una pregunta que no aplica
se responde "No aplica" con el motivo — nunca se borra la fila.
-->

# Revisión cruzada por área: [Nombre de la iniciativa]

## Resumen de impactos

_// Es lo que consolida el PRD. Filas con Sí o Pendiente, completas. Una línea por cada área sin ningún impacto._

**Áreas con impacto**

| Área | Impacto | Qué proponemos | Estado |
| --- | --- | --- | --- |
|  |  |  |  |

**Áreas evaluadas sin impacto**
* <Área> — evaluada, sin impacto: <motivo en una frase>.

**Requerimientos nuevos al alcance surgidos de esta revisión**
* <Nombre> — <por qué lo pide el área> — <Aprobado por el PM (YYYY-MM-DD) / Descartado — motivo / Pendiente de decisión>.
_// Si no hubo ninguno, decirlo: "Ninguno — todos los impactos se cubren con el alcance vigente o con tareas previas al go-live."_

## Detalle por área

_// RESPUESTA — Sí / No / No aplica, siempre con el porqué en una oración que el área reconozca como propia._
_// El Sí/No contesta "¿hay algo que esta área tenga que atender?", no la pregunta textual: en "¿Soporte puede ver…?" o "¿se puede testear…?", si la capacidad falta es Sí; si ya existe es No._
_// QUÉ PROPONEMOS — si fue Sí: Requerimiento en el alcance (nombrar la funcionalidad; 🆕 si es nuevo) · Tarea previa al go-live · Contingencia operativa (cómo y quién lo absorbe). Si fue No o No aplica: "—"._
_// ESTADO — Pendiente · Contemplado pero no validado · Contemplado y validado (validado = el área lo confirmó)._

### 1. Comercial

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| C1 | ¿Cambia el pricing, el packaging o lo que se le puede prometer a un cliente? |  |  |  |  |
| C2 | ¿Hace falta material de preventa o actualizar el perfil del cliente? |  |  |  |  |
| C3 | ¿Hay clientes en pipeline cuya integración cambia por esto? |  |  |  |  |

### 2. Soporte / Operaciones e Integraciones

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| S1 | ¿Cambia lo que Soporte tiene que responder o diagnosticar? ¿Hay que actualizar guías o capacitar? |  |  |  |  |
| S2 | ¿Aparecen errores o estados nuevos que Soporte hoy no sabe interpretar? |  |  |  |  |
| S3 | ¿Requiere credenciales, configuración o habilitación nueva por cliente o ambiente? |  |  |  |  |
| S4 | ¿Soporte puede ver, de forma agregada, que esto no está funcionando con normalidad? |  |  |  |  |
| S5 | ¿Por qué canales pueden llegar reclamos, y todos saben a dónde derivarlos? |  |  |  |  |
| S6 | ¿Queda registro suficiente para responder un reclamo ante BCRA o Defensa del Consumidor? |  |  |  |  |

### 3. Administración y recaudaciones

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| A1 | ¿Genera movimientos de dinero, comprobantes o tipos de operación nuevos? |  |  |  |  |
| A2 | ¿Conciliación puede identificarlos y cuadrarlos desde el día 1, o hay que parametrizar antes? |  |  |  |  |
| A3 | ¿Impacta la liquidación a comercios? |  |  |  |  |
| A4 | ¿Crea o modifica saldos? ¿El control queda en un sistema interno de Bind? |  |  |  |  |

### 4. Impuestos y contabilidad

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| I1 | ¿Cambia el cálculo o la imputación de impuestos sobre la operatoria? |  |  |  |  |
| I2 | ¿Cambia la facturación, el costo que se le cobra al cliente o cómo se le cobra? |  |  |  |  |
| I3 | ¿Cambia la registración contable o la información que se reporta al fisco? |  |  |  |  |

### 5. Fraude

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| F1 | ¿Abre un vector de riesgo nuevo o cambia el perfil transaccional que se monitorea? |  |  |  |  |
| F2 | ¿Hacen falta reglas, parámetros o límites nuevos en el motor antifraude? |  |  |  |  |
| F3 | ¿Necesita un esquema de monitoreo operativo nuevo (tablero, alerta de anomalía)? |  |  |  |  |
| F4 | ¿Cambia la información disponible para responder un reclamo de fraude de otra entidad? |  |  |  |  |

### 6. Legales

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| L1 | ¿Requiere cambio contractual, anexo o consentimiento nuevo? |  |  |  |  |
| L2 | ¿Cambian los términos y condiciones, o quién responde si la operación falla? |  |  |  |  |

### 7. Cumplimiento / PLD

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| P1 | ¿Tiene implicancias regulatorias BCRA? |  |  |  |  |
| P2 | ¿Toca UIF/PLD: debida diligencia, monitoreo de operaciones, límites o reportes? |  |  |  |  |
| P3 | ¿Toca datos personales o datos de tarjeta (PCI DSS)? |  |  |  |  |
| P4 | ¿Genera o cambia una obligación de reportería regulatoria? |  |  |  |  |

### 8. IT

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| T1 | ¿Qué volumen adicional se espera y el sistema está dimensionado? |  |  |  |  |
| T2 | ¿Requiere accesos, secretos o cambios en la superficie expuesta? |  |  |  |  |
| T3 | ¿Toca el modelo de datos, requiere migración o retención nueva? |  |  |  |  |
| T4 | ¿Hay tracking/logging suficiente para medir el criterio de éxito? |  |  |  |  |
| T5 | ¿Se puede testear en staging con datos representativos, incluidas las fallas del proveedor? |  |  |  |  |
| T6 | ¿Depende de un desarrollo de un proveedor externo, y con qué lead time? |  |  |  |  |
| T7 | ¿Depende de credenciales o APIs que administra solo el proveedor de tecnología, sin visibilidad de Bind? |  |  |  |  |

### 9. Clientes externos en producción

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| E1 | ¿Es un breaking change para alguien ya integrado? |  |  |  |  |
| E2 | ¿Hace falta preaviso, plan de comunicación y ventana de migración? |  |  |  |  |
| E3 | ¿Hay que actualizar la documentación pública? |  |  |  |  |

### Preguntas adicionales específicas de este proyecto

_// Opcional. Ampliar el catálogo está bien; podarlo, nunca. ID con prefijo del área + "x" (ej. Fx1)._

## Historial de revisiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | YYYY-MM-DD | Versión inicial de la revisión cruzada |
