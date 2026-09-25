---
artifact: risks
version: "1.0"
created: 2026-07-23
estado: Aprobado por PM (2026-07-23)
basado_en: {solution: "1.0", crosscheck: "1.1"}
context: Ejemplo ilustrativo — cifras ficticias, no son datos reales de Bind PSP. Continúa el caso de ejemplo del preview de documentación KYB en el alta de comercios de Adquirencia.
---

# Riesgos: Preview de documentación KYB en el alta de comercios

## Resumen para el PRD

| Riesgo | Familia | Probabilidad | Impacto | Mitigación |
| --- | --- | --- | --- | --- |
| El preview alarga la percepción de esfuerzo y empeora el abandono en vez de mejorarlo | Producto | Media | Alto | Lanzamiento gradual (A/B) medido con el evento de abandono por paso, con vuelta atrás si empeora. |
| El proveedor de onboarding no expone la lista de documentos por tipo de entidad | Entrega | Media | Medio | Resolver la lista del lado de Bind como plan B, ya dentro del alcance. |
| La lista que se muestra no coincide con la que exige la política de debida diligencia | Producto | Baja | Alto | Validación de la lista final con PLD antes de salir, y un único origen de la lista para el preview y la carga. |
| El cambio toca componentes de pantalla compartidos con el alta de Wallet sin coordinación | Entrega | Baja | Medio | Confirmar con el equipo de Wallet antes de tocar componentes compartidos. |
| Soporte no llega a tener el aviso y el manual actualizados para el lanzamiento | Entrega | Media | Bajo | Fijar la fecha del aviso con Soporte antes de fijar la fecha de lanzamiento. |

## A — Riesgos de entrega del proyecto

| # | Riesgo | Origen | Probabilidad | Impacto | Mitigación | Dueño | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | El proveedor de onboarding no expone la lista de documentos por tipo de entidad | Pregunta sin resolver de la revisión con IT | Media | Medio | Resolver la lista del lado de Bind como plan B, ya dentro del alcance. | PM (con el proveedor de onboarding) | Abierto |
| A2 | El cambio toca componentes de pantalla compartidos con el alta de Wallet sin coordinación | Decisión de diseño del análisis de solución | Baja | Medio | Confirmar con el equipo de Wallet antes de tocar componentes compartidos. | Equipo de Onboarding | Abierto |
| A3 | Soporte no llega a tener el aviso y el manual actualizados para el lanzamiento | Tarea previa al go-live de la revisión con Soporte | Media | Bajo | Fijar la fecha del aviso con Soporte antes de fijar la fecha de lanzamiento. | PM (con Soporte) | Abierto |

## B — Riesgos del producto en producción

| # | Riesgo | Pregunta | Probabilidad | Impacto | Mitigación | Dueño | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B2 | 🚧 El preview alarga la percepción de esfuerzo y empeora el abandono en vez de mejorarlo — sin medición por paso, se vería recién en el informe mensual | Operativo | Media | Alto | Lanzamiento gradual (A/B) medido con el evento de abandono por paso; vuelta atrás si el abandono sube más de [Ejemplo] 3 puntos en dos semanas. | PM (con Operaciones) | Abierto |
| B4 | 🚧 La lista que se muestra no coincide con la que exige la política de debida diligencia: el comercio se prepara para algo distinto de lo que después se le pide | Regulatorio | Baja | Alto | Validar la lista final con PLD antes de salir; el preview y la carga leen la lista del mismo origen, así no pueden divergir. | PM (con PLD) | Abierto |

### Preguntas del catálogo B sin riesgo identificado

* B1 — Fraude — sin riesgo: la lista de documentos ya es pública en la ayuda del alta; mostrarla antes no le da información nueva a un tercero.
* B3 — Financiero — no aplica: no hay movimiento de dinero ni saldo involucrado.
* B5 — Reclamos y reputación — sin riesgo adicional: el peor caso (lista equivocada) ya está cubierto en B4.
* B6 — Dependencia de tercero en producción — sin riesgo: si la consulta al proveedor falla, se muestra la lista genérica y el alta sigue.

## Historial de revisiones

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-07-23 | Versión inicial. Aprobada por el PM el 2026-07-23, que confirmó marcar B2 y B4 como bloqueadores de go-live. |
