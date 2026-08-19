---
artifact: problem-statement
version: "1.0"
created: 2026-07-20
status: complete
context: Ejemplo ilustrativo — cifras ficticias, no son datos reales de Bind PSP. Sirve solo para mostrar el formato esperado.
---

# Problem Statement: Abandono en el alta de comercios de Adquirencia

## Enunciado del problema

> **Comercios PyME (1 a 10 puntos de venta) que inician el alta de Adquirencia por el flujo self-service** necesitan **completar la carga de documentación KYB sin perder el progreso ni adivinar qué les falta** porque **hoy no saben de antemano qué documentos societarios les van a pedir, el flujo no acepta fotos sacadas con el celular, y un corte de sesión los obliga a empezar de cero**.

Esto retrasa — o directamente frena — la activación de cuentas que ya mostraron intención de adherirse.

*Job story: Cuando [Ejemplo] llega al paso de subir documentación societaria sin saber de antemano qué le van a pedir, quiere completarlo en una sola sesión sin sorpresas ni reintentos, para poder activar su cuenta y empezar a cobrar sin depender de un ejecutivo comercial.*

## Afectado

Comercios PyME (1 a 10 puntos de venta) que inician el alta de Adquirencia por el flujo self-service, sin acompañamiento de un ejecutivo comercial. Representan la mayoría de las altas nuevas del canal digital.

*Alternativa actual: [Ejemplo] cuando abandonan el self-service, gran parte re-intenta semanas después por canal asistido con un ejecutivo comercial — no dejan de querer adherirse, cambian de canal a uno más caro para Bind.*

## Medida del problema

- [Ejemplo] ~1.200 comercios por mes inician el flujo de alta digital
- [Ejemplo] 58% abandona antes de completar la carga de KYB (vs. 22% de abandono en el resto del flujo)
- [Ejemplo] ~700 altas potenciales por mes que quedan truncas en ese paso

## Impacto del problema

- [Ejemplo] Cada punto de abandono recuperado en este paso representa activaciones adicionales de comercios que ya mostraron intención — no es adquisición nueva, es conversión de demanda existente
- [Ejemplo] Costo de oportunidad: los comercios que abandonan acá suelen re-intentar por canal asistido (con ejecutivo), lo que sube el costo de adquisición de esa cohorte
- Conecta directo con el foco de Onboarding del período: bajar la fricción de alta es condición para escalar volumen de Adquirencia sin sumar carga proporcional al equipo comercial — es, además, la etapa del funnel con mayor caída de todo el proceso de alta digital

*Fuerzas del cambio: [Ejemplo] push — ya decidieron adherirse antes de llegar a este paso, no es un comercio dudando; pull — activar la cuenta y empezar a cobrar; frena — la ansiedad de no saber si el documento que suben va a ser rechazado, y el hábito de resolver trámites de este tipo por teléfono con alguien, no solo, en una pantalla.*

## Meta / criterio de éxito

| Métrica | Baseline actual | Target | Plazo |
|---------|-----------------|--------|-------|
| Abandono en paso de carga KYB | [Ejemplo] 58% | [Ejemplo] 35% | [Ejemplo] fin de trimestre |
| Altas completadas sin intervención comercial | [Ejemplo] 42% | [Ejemplo] 60% | [Ejemplo] fin de trimestre |

## Restricciones y preguntas abiertas

- Los requisitos documentales de KYB no se pueden relajar — vienen de cumplimiento normativo (BCRA/UIF); lo que se puede mejorar es la experiencia de carga, no el requisito en sí
- Cualquier cambio en el flujo de carga de documentos depende de disponibilidad del proveedor de onboarding (validar con arquitectura de Fintexa si el cambio requiere su intervención)
- El flujo comparte componentes con el alta de Wallet — un cambio acá puede impactar ese producto

**Abierto:**
- [ ] ¿En qué paso puntual de la carga de KYB se concentra la mayor caída?
- [ ] ¿Cuánto de ese abandono se recupera después por canal asistido, y a qué costo?
- [ ] ¿El rechazo de documentos es la causa principal o es la fricción de UX de carga en sí?
- [ ] ¿Hay diferencia de abandono por tipo de comercio (unipersonal vs. sociedad)?
