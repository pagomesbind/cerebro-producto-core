---
artifact: problem-statement
version: "1.0"
created: 2026-07-20
status: complete
context: Ejemplo ilustrativo — cifras ficticias, no son datos reales de Bind PSP. Sirve solo para mostrar el formato esperado.
---

# Problem Statement: Abandono en el alta de comercios de Adquirencia

## Resumen del problema

Los comercios que inician el alta digital en Adquirencia abandonan el flujo de carga de documentación KYB antes de completarlo en una proporción alta. Llegan hasta el paso de subir la documentación societaria pero no lo terminan, lo que retrasa (o directamente frena) la activación de cuentas que ya mostraron intención de adherirse.

## Impacto en usuarios

### ¿Quién está afectado?

Comercios PyME (1 a 10 puntos de venta) que inician el alta de Adquirencia por el flujo self-service, sin acompañamiento de un ejecutivo comercial. Representan la mayoría de las altas nuevas del canal digital.

### ¿Cómo está afectado?

Reportan (vía tickets de soporte y feedback de comercial) fricción con:
- No saber de antemano qué documentos societarios van a pedirles antes de empezar
- Formularios de carga que no aceptan fotos sacadas con el celular, solo PDF escaneado
- Falta de feedback claro cuando un documento es rechazado (se enteran días después)
- Tener que retomar el flujo desde cero si se cierra la sesión a mitad de camino

### Escala del impacto

- [Ejemplo] ~1.200 comercios por mes inician el flujo de alta digital
- [Ejemplo] 58% abandona antes de completar la carga de KYB (vs. 22% de abandono en el resto del flujo)
- [Ejemplo] ~700 altas potenciales por mes que quedan truncas en ese paso

## Contexto de negocio

### Alineación estratégica

Conecta directo con el foco de Onboarding del período: bajar la fricción de alta es condición para escalar volumen de Adquirencia sin sumar carga proporcional al equipo comercial.

### Impacto de negocio

- [Ejemplo] Cada punto de abandono recuperado en este paso representa activaciones adicionales de comercios que ya mostraron intención — no es adquisición nueva, es conversión de demanda existente
- Costo de oportunidad: comercios que abandonan acá suelen re-intentar por canal asistido (con ejecutivo), lo que sube el costo de adquisición de esa cohorte

### ¿Por qué ahora?

- El foco estratégico de Onboarding del período prioriza justamente cobertura y fricción de alta
- Es la etapa del funnel con mayor caída de todo el proceso de alta digital

## Criterios de éxito

| Métrica | Baseline actual | Target | Plazo |
|---------|-----------------|--------|-------|
| Abandono en paso de carga KYB | [Ejemplo] 58% | [Ejemplo] 35% | [Ejemplo] fin de trimestre |
| Tiempo promedio hasta activación | [Ejemplo] 6 días | [Ejemplo] 3 días | [Ejemplo] fin de trimestre |
| Altas completadas sin intervención comercial | [Ejemplo] 42% | [Ejemplo] 60% | [Ejemplo] fin de trimestre |

## Restricciones y consideraciones

- Los requisitos documentales de KYB no se pueden relajar — vienen de cumplimiento normativo (BCRA/UIF), lo que se puede mejorar es la experiencia de carga, no el requisito en sí
- Cualquier cambio en el flujo de carga de documentos depende de disponibilidad del proveedor de onboarding (validar con arquitectura de Fintexa si el cambio requiere su intervención)
- El flujo comparte componentes con el alta de Wallet — un cambio acá puede impactar ese producto

## Preguntas abiertas

- [ ] ¿En qué paso puntual de la carga de KYB se concentra la mayor caída?
- [ ] ¿Cuánto de ese abandono se recupera después por canal asistido, y a qué costo?
- [ ] ¿El rechazo de documentos es la causa principal o es la fricción de UX de carga en sí?
- [ ] ¿Hay diferencia de abandono por tipo de comercio (unipersonal vs. sociedad)?
