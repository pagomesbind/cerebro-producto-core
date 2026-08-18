---
artifact: acceptance-criteria
version: "1.0"
created: <YYYY-MM-DD>
status: draft
---

# Criterios de aceptación: [Título de la feature o historia]

## Contexto de la historia

<!-- Recapitulá brevemente la historia, slice de feature, o sección de PRD que sustentan estos criterios. -->

[Describí la necesidad del usuario, el límite de alcance, y cualquier supuesto relevante para testing.]

## Happy path

<!-- Capturá primero el flujo principal de éxito. Cada criterio debe ser testeable de forma independiente. -->

### AC-1: [Título del happy path]

**Dado** [contexto inicial o precondición]

**Cuando** [acción o disparador del usuario]

**Entonces** [resultado observable esperado]

### AC-2: [Título del happy path]

**Dado** [contexto inicial o precondición]

**Cuando** [acción o disparador del usuario]

**Entonces** [resultado observable esperado]

## Casos borde

<!-- Documentá condiciones límite e inputs alternativos que igual deberían comportarse correctamente. -->

### AC-3: [Título del caso borde]

**Dado** [condición límite o estado alternativo]

**Cuando** [acción o disparador del usuario]

**Entonces** [resultado observable esperado]

## Estados de error

<!-- Describí fallas, problemas de validación y problemas de dependencias, con comportamiento de recuperación. -->

### AC-4: [Título del estado de error]

**Dado** [condición de falla]

**Cuando** [acción o disparador del usuario]

**Entonces** [resultado observable esperado y camino de recuperación]

## Criterios no funcionales

<!-- Capturá requisitos de performance, accesibilidad, seguridad, confiabilidad o auditoría. -->

### AC-5: [Título no funcional]

**Dado** [contexto de sistema o usuario relevante]

**Cuando** [medición o acción]

**Entonces** [restricción o garantía medible esperada]

## Notas

- [Supuesto o dependencia]
- [Pregunta abierta si la historia origen está incompleta]
