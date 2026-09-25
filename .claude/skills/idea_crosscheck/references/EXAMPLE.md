---
artifact: crosscheck
version: "1.1"
created: 2026-07-20
estado: Aprobado por PM (2026-07-22)
basado_en: {start: "1.0", solution: "1.0"}
context: Ejemplo ilustrativo — cifras ficticias, no son datos reales de Bind PSP. Continúa el caso de ejemplo del preview de documentación KYB en el alta de comercios de Adquirencia.
---

# Revisión cruzada por área: Preview de documentación KYB en el alta de comercios

## Resumen de impactos

**Áreas con impacto**

| Área | Impacto | Qué proponemos | Estado |
| --- | --- | --- | --- |
| Soporte / Operaciones | La pantalla nueva puede generar consultas al principio, de comercios que no entienden por qué se les muestra algo antes de la carga. | Tarea previa al go-live: avisar a Soporte y actualizar el manual de ayuda con la pantalla nueva. | Contemplado pero no validado |
| Soporte / Operaciones | Hoy nadie ve el abandono en el paso de KYB salvo en el informe mensual: si el preview empeora la conversión, Soporte no se entera. | Requerimiento nuevo al alcance: evento de abandono por paso del alta, visible en el tablero de funnel que ya usa Operaciones. | Contemplado y validado |
| IT | Depende de que el proveedor de onboarding confirme si expone la lista de documentos requeridos por tipo de entidad. | Tarea previa al go-live: confirmarlo antes de cerrar el diseño; si no la expone, la lista se resuelve del lado de Bind (ya contemplado en el alcance). | Pendiente |
| Cumplimiento / PLD | La lista de documentos que se muestra tiene que coincidir exactamente con la que exige la política de debida diligencia vigente. | Tarea previa al go-live: validar la lista final con PLD. | Pendiente |

**Áreas evaluadas sin impacto**
* Comercial — evaluada, sin impacto: el cambio es sobre el alta self-service, no sobre el alta asistida ni el pricing.
* Administración y recaudaciones — evaluada, sin impacto: no genera movimientos de dinero ni toca liquidaciones.
* Impuestos y contabilidad — evaluada, sin impacto: no cambia la operatoria facturada ni la información al fisco.
* Fraude — evaluada, sin impacto: no cambia qué se valida ni cuándo, solo cuándo se le informa al comercio.
* Legales — evaluada, sin impacto: no cambian contratos ni términos.
* Clientes externos en producción — evaluada, sin impacto: solo afecta altas nuevas, no a comercios activos ni a integraciones.

**Requerimientos nuevos al alcance surgidos de esta revisión**
* Evento de abandono por paso del alta — sin él, no hay forma de saber a tiempo si el preview empeora el problema que viene a resolver — Aprobado por el PM (2026-07-22). No necesita diseño funcional adicional: es un evento más sobre el tablero existente.

## Detalle por área

### 1. Comercial

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| C1 | ¿Cambia el pricing, el packaging o lo que se le puede prometer a un cliente? | No — la oferta y el precio del alta no cambian. | — | Contemplado y validado | — |
| C2 | ¿Hace falta material de preventa o actualizar el perfil del cliente? | No — el preview es autoexplicativo y no cambia lo que se le presenta al comercio en preventa. | — | Contemplado y validado | — |
| C3 | ¿Hay clientes en pipeline cuya integración cambia por esto? | No aplica — el alta self-service no tiene integración del lado del comercio. | — | Contemplado y validado | — |

### 2. Soporte / Operaciones e Integraciones

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| S1 | ¿Cambia lo que Soporte tiene que responder o diagnosticar? | Sí — aparecen consultas sobre la pantalla nueva, sobre todo en las primeras semanas. | Tarea previa al go-live: avisar a Soporte y actualizar el manual de ayuda. | Contemplado pero no validado | T-201 |
| S2 | ¿Aparecen errores o estados nuevos que Soporte hoy no sabe interpretar? | No — el fallback a la lista genérica no se muestra como error. | — | Contemplado y validado | — |
| S3 | ¿Requiere credenciales, configuración o habilitación nueva? | No — la pantalla aplica a todas las altas self-service sin configuración. | — | Contemplado y validado | — |
| S4 | ¿Soporte puede ver, de forma agregada, que esto no funciona con normalidad? | Sí — hoy el abandono por paso solo aparece en el informe mensual; si el preview empeora la conversión, nadie lo ve a tiempo. | 🆕 Requerimiento nuevo: evento de abandono por paso del alta en el tablero de funnel. | Contemplado y validado | — |
| S5 | ¿Por qué canales pueden llegar reclamos? | No — no cambia: los reclamos del alta siguen entrando por Soporte. | — | Contemplado y validado | — |
| S6 | ¿Queda registro suficiente para responder un reclamo ante BCRA o Defensa del Consumidor? | No aplica — la pantalla es informativa, no genera una operación ni una decisión sobre el comercio. | — | Contemplado y validado | — |

### 3. Administración y recaudaciones

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| A1 | ¿Genera movimientos de dinero, comprobantes o tipos de operación nuevos? | No — es un cambio de experiencia en el alta, sin operación asociada. | — | Contemplado y validado | — |
| A2 | ¿Conciliación puede cuadrarlos desde el día 1? | No aplica — no hay nada nuevo que conciliar (A1 = No). | — | Contemplado y validado | — |
| A3 | ¿Impacta la liquidación a comercios? | No — el comercio todavía no opera en este punto del alta. | — | Contemplado y validado | — |
| A4 | ¿Crea o modifica saldos? | No — no toca saldos. | — | Contemplado y validado | — |

### 4. Impuestos y contabilidad

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| I1 | ¿Cambia el cálculo o la imputación de impuestos? | No — no hay operatoria nueva. | — | Contemplado y validado | — |
| I2 | ¿Cambia la facturación o el costo al cliente? | No — el alta no se factura distinto. | — | Contemplado y validado | — |
| I3 | ¿Cambia la registración contable o la información al fisco? | No — sin operatoria nueva, no hay registración nueva. | — | Contemplado y validado | — |

### 5. Fraude

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| F1 | ¿Abre un vector de riesgo nuevo? | No — mostrar qué documentos se piden no da información que un tercero pueda usar para suplantar al comercio; la lista ya es pública en la ayuda. | — | Contemplado y validado | — |
| F2 | ¿Hacen falta reglas o límites nuevos en el motor antifraude? | No — la validación de documentos no cambia. | — | Contemplado y validado | — |
| F3 | ¿Necesita un esquema de monitoreo operativo nuevo? | No — el monitoreo que hace falta es de conversión, no de fraude; ya está cubierto en S4. | — | Contemplado y validado | — |
| F4 | ¿Cambia la información para responder un reclamo de fraude de otra entidad? | No aplica — no hay operación sobre la que otra entidad pueda reclamar. | — | Contemplado y validado | — |

### 6. Legales

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| L1 | ¿Requiere cambio contractual o consentimiento nuevo? | No — no cambia lo que el comercio acepta en el alta. | — | Contemplado y validado | — |
| L2 | ¿Cambian los términos y condiciones? | No — la pantalla es informativa. | — | Contemplado y validado | — |

### 7. Cumplimiento / PLD

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| P1 | ¿Tiene implicancias regulatorias BCRA? | No — los requisitos del alta no cambian, solo cuándo se comunican. | — | Contemplado y validado | — |
| P2 | ¿Toca UIF/PLD? | Sí — la lista que se muestra tiene que coincidir exactamente con la que exige la política de debida diligencia; si difiere, el comercio se prepara para algo distinto de lo que después se le exige. | Tarea previa al go-live: validar la lista final por tipo de entidad con PLD. | Pendiente | T-202 |
| P3 | ¿Toca datos personales o de tarjeta? | No — la pantalla no captura datos. | — | Contemplado y validado | — |
| P4 | ¿Genera o cambia una obligación de reportería? | No — no hay operación reportable nueva. | — | Contemplado y validado | — |

### 8. IT

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| T1 | ¿Qué volumen adicional se espera? | No — una consulta extra por alta, sobre un volumen de [Ejemplo] 1.200 altas/mes. | — | Contemplado y validado | — |
| T2 | ¿Requiere accesos o cambios en la superficie expuesta? | No — la pantalla vive dentro del alta ya autenticada. | — | Contemplado y validado | — |
| T3 | ¿Toca el modelo de datos? | No — la lista se resuelve en el momento, no se persiste. | — | Contemplado y validado | — |
| T4 | ¿Hay tracking suficiente para medir el criterio de éxito? | Sí — el criterio de éxito es el abandono en el paso KYB, que hoy no se mide por paso. | Cubierto por el requerimiento nuevo de S4. | Contemplado y validado | — |
| T5 | ¿Se puede testear en staging? | No — ya se puede: el ambiente de pruebas del proveedor de onboarding tiene los dos tipos de entidad. | — | Contemplado y validado | — |
| T6 | ¿Depende de un desarrollo de un proveedor externo? | Sí — depende de que el proveedor de onboarding confirme si expone la lista de documentos por tipo de entidad. | Tarea previa al go-live: confirmarlo antes de cerrar el diseño; si no la expone, la lista se resuelve del lado de Bind (ya en el alcance). | Pendiente | T-203 |
| T7 | ¿Depende de credenciales o APIs que administra solo el proveedor de tecnología? | No — usa la misma integración que el alta ya existente. | — | Contemplado y validado | — |

### 9. Clientes externos en producción

| # | Pregunta | Respuesta | Qué proponemos | Estado | Tarea |
| --- | --- | --- | --- | --- | --- |
| E1 | ¿Es un breaking change para alguien ya integrado? | No — solo afecta altas nuevas. | — | Contemplado y validado | — |
| E2 | ¿Hace falta preaviso o ventana de migración? | No aplica — no hay nada que migrar. | — | Contemplado y validado | — |
| E3 | ¿Hay que actualizar la documentación pública? | No — la ayuda del alta ya lista los documentos; se actualiza el manual de Soporte (S1). | — | Contemplado y validado | — |

## Historial de revisiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-07-20 | Versión inicial de la revisión cruzada |
| 1.1 | 2026-07-22 | El PM aprobó sumar al alcance el evento de abandono por paso (S4/T4). Aprobada por el PM el 2026-07-22. |
