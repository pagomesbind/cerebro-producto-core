---
artifact: hypothesis
version: "1.0"
created: <YYYY-MM-DD>
status: draft
---

# Hipótesis: [Título breve]

## Enunciado de la hipótesis

**Creemos que** [acción o cambio específico]

**para** [segmento de usuario objetivo]

**va a lograr** [resultado/cambio de comportamiento esperado]

**medido por** [métrica de éxito primaria]

## Contexto y fundamento

### Contexto del problema
<!-- ¿Qué problema busca resolver esta hipótesis? Linkeá al problem statement si existe. -->

[Contexto del problema]

### Evidencia de respaldo
<!-- ¿Qué datos, research u observaciones llevaron a esta hipótesis? -->

[Evidencia que respalda esta creencia]

### Hipótesis alternativas consideradas
<!-- ¿Qué otras explicaciones o enfoques se consideraron? -->

[Enfoques alternativos]

## Segmento de usuario objetivo

### Definición
<!-- Criterios específicos que definen este segmento -->

[Definición del segmento]

### Tamaño del segmento
<!-- ¿Cuántos usuarios caen en este segmento? -->

[Conteo o porcentaje estimado]

### Comportamiento actual
<!-- ¿Cómo se comportan hoy estos usuarios? ¿Cuál es el baseline? -->

[Estado actual]

## Métricas de éxito

### Métrica primaria
<!-- La métrica principal que determina si la hipótesis se valida -->

| Métrica | Baseline actual | Target | Efecto mínimo detectable |
|---------|-----------------|--------|---------------------------|
| [Nombre de la métrica] | [Valor actual] | [Valor objetivo] | [% MDE] |

### Métricas secundarias
<!-- Métricas adicionales que dan contexto -->

| Métrica | Baseline actual | Dirección esperada |
|---------|-----------------|---------------------|
| [Métrica 1] | [Valor] | [Aumenta/Disminuye/Sin cambio] |
| [Métrica 2] | [Valor] | [Aumenta/Disminuye/Sin cambio] |

### Métricas guardrail
<!-- Métricas que NO deberían verse afectadas negativamente -->

| Métrica | Valor actual | Rango aceptable |
|---------|--------------|-------------------|
| [Métrica 1] | [Valor] | [Rango] |

## Enfoque de validación

### Método
<!-- ¿Cómo se va a testear? A/B test, prototipo, entrevistas, etc. -->

[Método de validación]

### Tamaño de muestra y duración
<!-- Requisitos estadísticos del test -->

- Tamaño de muestra: [Número por variante]
- Duración: [Período de tiempo]
- Asignación de tráfico: [Porcentaje]

### Criterios de pass/fail
<!-- ¿Qué resultados validan o invalidan la hipótesis? -->

- **Se valida si:** [Criterio específico]
- **Se invalida si:** [Criterio específico]
- **Es inconcluso si:** [Criterio específico]

## Riesgos y supuestos

### Supuestos clave
<!-- ¿Qué estás asumiendo como verdadero? -->

- [Supuesto 1]
- [Supuesto 2]

### Riesgos
<!-- ¿Qué podría salir mal? ¿Qué podría invalidar los resultados? -->

- [Riesgo 1]
- [Riesgo 2]

## Cronograma

| Fase | Fechas | Duración |
|------|--------|----------|
| Setup e instrumentación | [Fechas] | [Duración] |
| Test corriendo | [Fechas] | [Duración] |
| Análisis | [Fechas] | [Duración] |
| Decisión | [Fecha] | - |
