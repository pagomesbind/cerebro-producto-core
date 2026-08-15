---
artifact: launch-checklist
version: "1.0"
created: <YYYY-MM-DD>
status: draft
---

# Checklist de lanzamiento: [Nombre del lanzamiento]

## Overview del lanzamiento

| Campo | Valor |
|-------|-------|
| Qué | [Feature/producto que se lanza] |
| Fecha de lanzamiento | [Fecha objetivo] |
| Tipo de lanzamiento | [Release mayor / Feature menor / Experimento / Hotfix] |
| Responsable del lanzamiento | [Nombre] |
| Quién decide go/no-go | [Nombre] |

### Stakeholders clave

| Rol | Nombre | Contacto |
|-----|--------|----------|
| Producto | [Nombre] | [Email/Slack] |
| Ingeniería | [Nombre] | [Email/Slack] |
| Diseño | [Nombre] | [Email/Slack] |
| Soporte | [Nombre] | [Email/Slack] |
| Cumplimiento | [Nombre] | [Email/Slack] |

## Ingeniería

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Código completo y mergeado | [Nombre] | [Fecha] | | |
| [ ] Code review aprobado | [Nombre] | [Fecha] | | |
| [ ] Feature flags configurados | [Nombre] | [Fecha] | | |
| [ ] Migraciones de base de datos listas | [Nombre] | [Fecha] | | |
| [ ] Documentación de API actualizada | [Nombre] | [Fecha] | | |

## QA y testing

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Plan de test ejecutado | [Nombre] | [Fecha] | | |
| [ ] Tests de regresión pasan | [Nombre] | [Fecha] | | |
| [ ] UAT completo | [Nombre] | [Fecha] | | |
| [ ] Testing mobile | [Nombre] | [Fecha] | | |
| [ ] Test de carga completo | [Nombre] | [Fecha] | | |
| [ ] Revisión de seguridad completa | [Nombre] | [Fecha] | | |

## Diseño y UX

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Diseños finales aprobados | [Nombre] | [Fecha] | | |
| [ ] QA de diseño completo | [Nombre] | [Fecha] | | |
| [ ] Copy/contenido finalizado | [Nombre] | [Fecha] | | |
| [ ] Estados de error diseñados | [Nombre] | [Fecha] | | |
| [ ] Estados vacíos diseñados | [Nombre] | [Fecha] | | |

## Comunicación

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Anuncio de lanzamiento redactado | [Nombre] | [Fecha] | | |
| [ ] Comunicación a comercios/clientes preparada | [Nombre] | [Fecha] | | |
| [ ] Material actualizado en portal de developers (si aplica) | [Nombre] | [Fecha] | | |

## Soporte

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Documentación de soporte actualizada | [Nombre] | [Fecha] | | |
| [ ] FAQ creada/actualizada | [Nombre] | [Fecha] | | |
| [ ] Equipo de soporte capacitado | [Nombre] | [Fecha] | | |
| [ ] Respuestas predefinidas preparadas | [Nombre] | [Fecha] | | |
| [ ] Camino de escalamiento definido | [Nombre] | [Fecha] | | |

## Legal y cumplimiento

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Impacto regulatorio revisado (BCRA/UIF) | [Nombre] | [Fecha] | | |
| [ ] Cumplimiento PCI DSS verificado (si aplica) | [Nombre] | [Fecha] | | |
| [ ] Términos y condiciones revisados | [Nombre] | [Fecha] | | |
| [ ] Política de privacidad actualizada (si aplica) | [Nombre] | [Fecha] | | |

## Operaciones e infraestructura

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Infraestructura escalada | [Nombre] | [Fecha] | | |
| [ ] Sistemas de backup verificados | [Nombre] | [Fecha] | | |
| [ ] Plan de respuesta a incidentes listo | [Nombre] | [Fecha] | | |
| [ ] Guardia (on-call) confirmada | [Nombre] | [Fecha] | | |

## Analítica y monitoreo

| Item | Responsable | Fecha | Estado | Notas |
|------|-------------|-------|--------|-------|
| [ ] Instrumentación de analítica | [Nombre] | [Fecha] | | |
| [ ] Dashboards creados | [Nombre] | [Fecha] | | |
| [ ] Alertas configuradas | [Nombre] | [Fecha] | | |
| [ ] Métricas de éxito con baseline | [Nombre] | [Fecha] | | |

## Criterios de go/no-go

### Imprescindibles (bloqueadores)
<!-- Items que TIENEN que estar completos para lanzar -->

- [ ] [Bloqueador 1]
- [ ] [Bloqueador 2]

### Deseables
<!-- Items que preferimos fuertemente pero se puede lanzar sin ellos -->

- [ ] [Deseable 1]

### Nice to have
<!-- Items que gustaría tener pero no retrasan el lanzamiento -->

- [ ] [Nice-to-have 1]

## Plan de rollback

### Condiciones que lo disparan
<!-- ¿Cuándo haríamos rollback? -->

- [Condición 1]
- [Condición 2]

### Pasos de rollback

1. [Paso 1]
2. [Paso 2]

### Responsable del rollback

[Nombre] - [Contacto]

### Tiempo estimado de rollback

[Duración]

## Cronograma de check-ins

| Checkpoint | Fecha | Participantes |
|------------|-------|----------------|
| Revisión T-7 días | [Fecha] | [Nombres] |
| Go/no-go T-2 días | [Fecha] | [Nombres] |
| Sync día del lanzamiento | [Fecha/Hora] | [Nombres] |
| Revisión T+1 día | [Fecha] | [Nombres] |

## Issues abiertos

<!-- Items sin resolver que podrían afectar el lanzamiento -->

| Issue | Responsable | Estado | Impacto |
|-------|-------------|--------|---------|
| [Issue 1] | [Nombre] | [Estado] | [Bloqueador/Riesgo] |
