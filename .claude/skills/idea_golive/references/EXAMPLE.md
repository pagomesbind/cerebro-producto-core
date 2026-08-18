---
artifact: launch-checklist
version: "1.0"
created: 2026-07-20
status: complete
context: Ejemplo ilustrativo — cifras y nombres ficticios. Continúa el caso del preview de documentación KYB.
---

# Checklist de lanzamiento: Preview de documentación KYB

## Overview del lanzamiento

| Campo | Valor |
|-------|-------|
| Qué | Pantalla de preview de documentos requeridos antes de la carga de KYB en Adquirencia |
| Fecha de lanzamiento | [Ejemplo] 2026-08-15 |
| Tipo de lanzamiento | Feature menor (A/B test primero, luego rollout completo) |
| Responsable del lanzamiento | [Ejemplo] PM de Onboarding |
| Quién decide go/no-go | [Ejemplo] Product Lead |

### Stakeholders clave

| Rol | Nombre | Contacto |
|-----|--------|----------|
| Producto | [Ejemplo] N/N | — |
| Ingeniería | [Ejemplo] N/N | — |
| Diseño | [Ejemplo] N/N | — |
| Soporte | [Ejemplo] N/N | — |
| Cumplimiento | [Ejemplo] N/N | — |

## Ingeniería

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Código completo y mergeado | Ing. | [Ejemplo] T-5 días | Pendiente | |
| [ ] Feature flag configurado para A/B 50/50 | Ing. | [Ejemplo] T-5 días | Pendiente | |
| [ ] Resolución de metadata de Fintexa confirmada | Ing./Arquitectura | [Ejemplo] T-10 días | Bloqueador | Ver PRD de ejemplo, dependencia abierta |

## QA y testing

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Test funcional de ambas variantes (con/sin preview) | QA | [Ejemplo] T-3 días | Pendiente | |
| [ ] Testing mobile del flujo de alta | QA | [Ejemplo] T-3 días | Pendiente | |

## Diseño y UX

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Mockup de pantalla de preview aprobado | Diseño | [Ejemplo] T-8 días | Pendiente | |
| [ ] Imágenes de ejemplo por tipo de documento | Diseño | [Ejemplo] T-6 días | Pendiente | |

## Comunicación

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] N/A — cambio interno del flujo, sin comunicación externa | — | — | N/A | El A/B test no requiere anuncio |

## Soporte

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Aviso al equipo de soporte sobre la nueva pantalla | Soporte | [Ejemplo] T-2 días | Pendiente | Para que sepan explicarla si un comercio pregunta |

## Legal y cumplimiento

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Confirmar que la pantalla no modifica los requisitos de KYB en sí (solo los muestra antes) | Cumplimiento | [Ejemplo] T-4 días | Pendiente | |

## Operaciones e infraestructura

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] N/A — sin cambios de infraestructura | — | — | N/A | |

## Analítica y monitoreo

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Instrumentación de evento "vio preview" y "abandonó en preview" | Ing./Data | [Ejemplo] T-5 días | Pendiente | Necesario para medir la hipótesis de ejemplo |
| [ ] Dashboard de abandono por variante | Data | [Ejemplo] T-3 días | Pendiente | |

## Criterios de go/no-go

### Imprescindibles (bloqueadores)

- [ ] Metadata de Fintexa resuelta (o plan B del lado de Bind implementado)
- [ ] Instrumentación de analítica funcionando (sin esto no se puede medir la hipótesis)

### Deseables

- [ ] Imágenes de ejemplo para los 2 tipos de entidad completas (unipersonal puede lanzar sin sociedad si hace falta priorizar)

### Nice to have

- [ ] Copy revisado por un segundo PM

## Plan de rollback

### Condiciones que lo disparan

- El feature flag muestra un error de renderizado en la pantalla de preview para más del 1% de sesiones
- La variante con preview empeora el abandono en vez de mejorarlo (señal temprana, antes de fin de test)

### Pasos de rollback

1. Apagar el feature flag (rollback inmediato, sin deploy)
2. Confirmar que el flujo vuelve al comportamiento anterior para el 100% del tráfico
3. Avisar a soporte que la pantalla de preview ya no está activa

### Responsable del rollback

[Ejemplo] PM de Onboarding — vía feature flag, sin necesidad de ingeniería en el momento

### Tiempo estimado de rollback

Minutos (es un feature flag, no un deploy)

## Cronograma de check-ins

| Checkpoint | Fecha | Participantes |
|------------|-------|----------------|
| Revisión T-7 días | [Ejemplo] | PM, Ing., Diseño |
| Go/no-go T-2 días | [Ejemplo] | PM, Product Lead |
| Sync día del lanzamiento | [Ejemplo] | PM, Ing. |

## Issues abiertos

| Issue | Responsable | Estado | Impacto |
|-------|-------------|--------|---------|
| Metadata de Fintexa sin confirmar | Arquitectura | En curso | Bloqueador |
