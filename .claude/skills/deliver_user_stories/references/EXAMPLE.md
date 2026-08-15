---
artifact: user-story
version: "1.0"
created: 2026-07-20
status: complete
context: Ejemplo ilustrativo — continúa el caso de ejemplo del preview de documentación KYB (ver /deliver_prd).
---

# Historias de usuario: Preview de documentación KYB

## US-1: Ver documentos requeridos antes de cargar

| Campo | Valor |
|-------|-------|
| ID | US-1 |
| Título | Preview de documentos requeridos |
| Persona | Comercio dando de alta su cuenta de Adquirencia |
| Prioridad | P0 |
| Epic/Feature | Preview de documentación KYB |
| Estimación | [Ejemplo] 5 puntos |

### Enunciado

**Como** comercio dando de alta mi cuenta,

**quiero** ver qué documentos me van a pedir antes de empezar a cargarlos,

**para** poder juntarlos con anticipación y no abandonar el trámite a mitad de camino.

### Contexto y antecedentes

Ver PRD de ejemplo — el 58% de abandono en el paso de KYB se atribuye en parte a que el comercio no sabe qué le van a pedir hasta que ya está en el formulario de carga.

### Criterios de aceptación

#### AC-1: Se muestra la pantalla de preview antes del formulario

**Dado** que el comercio completó el paso anterior del alta y declaró su tipo de entidad

**Cuando** avanza al paso de documentación KYB

**Entonces** el sistema muestra primero la pantalla de preview con la lista completa de documentos requeridos, antes de mostrar el formulario de carga

#### AC-2: El comercio puede avanzar desde el preview al formulario

**Dado** que el comercio está viendo la pantalla de preview

**Cuando** confirma que revisó la lista

**Entonces** el sistema lo lleva al formulario de carga de documentos

### Notas de diseño

- Pendiente: mockup de la pantalla de preview (Diseño)

### Notas técnicas

- Confirmar con Arquitectura si la lista de documentos por tipo de entidad se resuelve del lado de Bind o vía metadata de Fintexa (ver PRD, dependencia abierta)

### Dependencias

| Dependencia | Tipo | Estado |
|-------------|------|--------|
| Confirmación de metadata de Fintexa | API | [Ejemplo] Bloqueada |

### Fuera de alcance

- Cambios al formato de archivo aceptado en la carga (sigue siendo PDF)

### Preguntas abiertas

- [ ] ¿Qué pasa si el comercio cambia su tipo de entidad después de ver el preview?

---

## US-2: Lista ajustada según tipo de entidad

| Campo | Valor |
|-------|-------|
| ID | US-2 |
| Título | Lista de documentos según tipo de entidad |
| Persona | Comercio con estructura societaria |
| Prioridad | P0 |
| Epic/Feature | Preview de documentación KYB |
| Estimación | [Ejemplo] 3 puntos |

### Enunciado

**Como** comercio con estructura societaria (no unipersonal),

**quiero** que la lista de documentos se ajuste a mi tipo de entidad,

**para** no ver requisitos que no me aplican y confundirme sobre qué necesito.

### Contexto y antecedentes

El tipo de entidad (unipersonal vs. sociedad) ya se declara en un paso anterior del alta; esta historia usa ese dato para filtrar la lista.

### Criterios de aceptación

#### AC-1: Lista filtrada para unipersonal

**Dado** que el comercio declaró ser unipersonal

**Cuando** ve la pantalla de preview

**Entonces** la lista muestra solo los documentos requeridos para ese tipo de entidad

#### AC-2: Lista filtrada para sociedad

**Dado** que el comercio declaró ser una sociedad

**Cuando** ve la pantalla de preview

**Entonces** la lista incluye los documentos societarios adicionales requeridos (ej. estatuto, acta de designación de autoridades)

### Notas de diseño

- Reutiliza el mismo componente de lista que US-1, con lógica de filtrado condicional

### Notas técnicas

- Depende de la misma resolución de metadata que US-1

### Dependencias

| Dependencia | Tipo | Estado |
|-------------|------|--------|
| US-1 (pantalla de preview base) | Historia | [Ejemplo] En curso |

### Fuera de alcance

- Tipos de entidad fuera de unipersonal/sociedad (si existieran, quedan para una iteración futura)

### Preguntas abiertas

Ninguna abierta al momento de escribir esta historia.
