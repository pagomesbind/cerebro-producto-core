---
artifact: hypothesis
version: "1.0"
created: 2026-07-20
status: complete
context: Ejemplo ilustrativo — cifras ficticias, no son datos reales de Bind PSP. Continúa el caso del problem statement de ejemplo (abandono en alta de comercios de Adquirencia).
---

# Hipótesis: Preview de documentación requerida antes de la carga de KYB

## Enunciado de la hipótesis

**Creemos que** mostrarle al comercio, antes de arrancar la carga, la lista completa de documentos societarios que va a necesitar (con ejemplos de cada uno)

**para** comercios PyME que inician el alta digital de Adquirencia

**va a lograr** que completen la carga de KYB en la misma sesión con más frecuencia, en vez de abandonar e intentar retomar después

**medido por** tasa de abandono en el paso de carga de KYB

## Contexto y fundamento

### Contexto del problema

Ver [problem statement de ejemplo](../../idea_problem/references/EXAMPLE.md): 58% de abandono en el paso de carga de KYB, con feedback de soporte apuntando a que los comercios "no saben qué les van a pedir" antes de empezar.

### Evidencia de respaldo

[Ejemplo] En entrevistas de soporte, la queja más repetida no fue "no tengo el documento" sino "no sabía que me lo iban a pedir en este momento y tuve que ir a buscarlo".

### Hipótesis alternativas consideradas

- Que el problema sea el formato de archivo aceptado (solo PDF) — se consideró pero el volumen de tickets sobre esto es menor.
- Que el problema sea la duración total del flujo — se descartó como hipótesis primaria porque el abandono se concentra en un paso puntual, no distribuido a lo largo de todo el proceso.

## Segmento de usuario objetivo

### Definición

Comercios PyME (1-10 puntos de venta) que llegan al paso de carga de documentación KYB en el alta digital self-service de Adquirencia.

### Tamaño del segmento

[Ejemplo] ~1.200 comercios/mes llegan a este paso.

### Comportamiento actual

[Ejemplo] 58% abandona sin completar la carga; de los que abandonan, una fracción minoritaria vuelve a intentar por su cuenta días después.

## Métricas de éxito

### Métrica primaria

| Métrica | Baseline actual | Target | Efecto mínimo detectable |
|---------|-----------------|--------|---------------------------|
| Abandono en paso de carga KYB | [Ejemplo] 58% | [Ejemplo] 45% | [Ejemplo] 8 puntos porcentuales |

### Métricas secundarias

| Métrica | Baseline actual | Dirección esperada |
|---------|-----------------|---------------------|
| Tiempo hasta completar la carga | [Ejemplo] 6 días | Disminuye |
| Documentos rechazados por primera carga | [Ejemplo] 31% | Disminuye |

### Métricas guardrail

| Métrica | Valor actual | Rango aceptable |
|---------|--------------|-------------------|
| Tiempo de carga de la página de alta | [Ejemplo] 1.2s | No superar 1.8s |

## Enfoque de validación

### Método

A/B test: variante de control (flujo actual) vs. variante con preview de documentación antes de arrancar la carga.

### Tamaño de muestra y duración

- Tamaño de muestra: [Ejemplo] ~600 comercios por variante
- Duración: [Ejemplo] 3 semanas
- Asignación de tráfico: 50/50

### Criterios de pass/fail

- **Se valida si:** la variante con preview reduce el abandono en al menos 8 puntos porcentuales con significancia estadística.
- **Se invalida si:** no hay diferencia significativa entre variantes al cierre del test.
- **Es inconcluso si:** el volumen de la muestra no alcanza el mínimo detectable en el plazo previsto.

## Riesgos y supuestos

### Supuestos clave

- Se asume que el comercio llega al flujo con intención real de completarlo (no es tráfico exploratorio).
- Se asume que mostrar la lista completa no genera el efecto contrario (abrumar y frenar antes de arrancar).

### Riesgos

- Que el preview alargue la percepción de esfuerzo y empeore el abandono en vez de mejorarlo.
- Que el efecto sea real pero pequeño, y quede diluido por otras causas de abandono no atacadas por este cambio (ver preguntas abiertas del problem statement).

## Cronograma

| Fase | Fechas | Duración |
|------|--------|----------|
| Setup e instrumentación | [Ejemplo] Semana 1 | 1 semana |
| Test corriendo | [Ejemplo] Semanas 2-4 | 3 semanas |
| Análisis | [Ejemplo] Semana 5 | 3 días |
| Decisión | [Ejemplo] Semana 5 | - |
