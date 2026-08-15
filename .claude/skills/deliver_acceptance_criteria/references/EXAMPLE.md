---
artifact: acceptance-criteria
version: "1.0"
created: 2026-07-20
status: complete
context: Ejemplo ilustrativo — continúa el caso de US-1 (preview de documentos requeridos) de /deliver_user_stories.
---

# Criterios de aceptación: Preview de documentos requeridos (US-1)

## Contexto de la historia

Antes del formulario de carga de KYB en el alta de Adquirencia, se agrega una pantalla de preview con la lista de documentos requeridos según el tipo de entidad del comercio. Ver historia US-1 en `/deliver_user_stories`.

## Happy path

### AC-1: El preview se muestra antes del formulario

**Dado** que el comercio completó el paso anterior del alta y declaró su tipo de entidad como "unipersonal"

**Cuando** avanza al paso de documentación KYB

**Entonces** el sistema muestra la pantalla de preview con la lista de documentos requeridos para entidades unipersonales, antes de mostrar el formulario de carga

### AC-2: El comercio avanza del preview al formulario

**Dado** que el comercio está viendo la pantalla de preview

**Cuando** hace clic en "Continuar"

**Entonces** el sistema lo lleva al formulario de carga de documentos, con el mismo progreso de alta que tenía antes

## Casos borde

### AC-3: Comercio sin tipo de entidad declarado

**Dado** que el comercio llega al paso de KYB sin haber declarado su tipo de entidad en el paso anterior (por ejemplo, por un alta iniciada antes de agregar ese campo)

**Cuando** el sistema intenta armar la pantalla de preview

**Entonces** muestra la lista genérica más amplia (unipersonal + sociedad) y pide al comercio confirmar su tipo antes de continuar

### AC-4: Comercio que retoma un alta abandonada

**Dado** que el comercio ya vio el preview en una sesión anterior y abandonó antes de completar la carga

**Cuando** vuelve a entrar al flujo de alta

**Entonces** el sistema no vuelve a mostrar el preview desde cero — lo lleva directo al formulario de carga, salvo que lo pida explícitamente (link "ver documentos requeridos" visible en el formulario)

## Estados de error

### AC-5: Falla la resolución de la lista de documentos

**Dado** que el sistema no puede resolver la lista de documentos requeridos (por ejemplo, falla la consulta de metadata)

**Cuando** el comercio llega al paso de KYB

**Entonces** el sistema muestra un mensaje de error genérico y permite continuar directo al formulario de carga con la lista completa por defecto (unipersonal + sociedad), sin bloquear el alta

## Criterios no funcionales

### AC-6: Tiempo de carga de la pantalla de preview

**Dado** que el comercio avanza al paso de KYB

**Cuando** se carga la pantalla de preview

**Entonces** el tiempo de carga no supera 1.8 segundos en percentil 95 (guardrail definido en la hipótesis de ejemplo)

### AC-7: Accesibilidad de la lista de documentos

**Dado** que un comercio usa un lector de pantalla

**Cuando** navega la pantalla de preview

**Entonces** cada documento de la lista se anuncia con su nombre y una descripción textual equivalente a la imagen de ejemplo (no solo la imagen)

## Notas

- Supuesto: la metadata de documentos por tipo de entidad está disponible antes del lanzamiento (ver dependencia abierta en el PRD de ejemplo).
- Pregunta abierta: ¿qué pasa si el comercio cambia su tipo de entidad declarado después de haber visto el preview? No cubierto en esta versión — flaggeado en `../../../../wiki/2_areas/gaps_y_preguntas.md` en el cierre.
