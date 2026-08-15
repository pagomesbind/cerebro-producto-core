# Ardid/Akurtech — Sistema de Scoring (Transferencias, Pagos y Login)

> Estado: en producción.

> Fuente: `Akurtech 7 - Transferencias - Pagos y Login con Scoring.pdf` (12 páginas), guía funcional oficial del proveedor. Extracción y estructuración vía agente de investigación (2026-07-02). Complementado con el modelo conceptual confirmado en `Manual de Ardid 1.13.pdf` (sección "Modelo de scoring unificado"). Ver [index.md](index.md) para contexto general.

## 1. Concepto general

El scoring es un modo alternativo de operación de las **reglas estándar** (de Transferencias, Pagos y Login): en lugar de ejecutar directamente una acción fija (bloquear, rechazar, etc.), cada regla **asigna un puntaje numérico** según el riesgo detectado.

- Se activa mediante el switch **"Activar scoring"**, ubicado en **Parametrías de entidad** (ver [configuracion_inicial.md](configuracion_inicial.md#4-parametrías-de-entidad)).
- Cada regla estándar tiene un campo de puntuación (score) asociado a la acción que genera. Ejemplo: una regla de "Monto acumulado diario" con score de 300 puntos.
- Cada vez que se procesa una operación (transferencia, pago o login), el sistema evalúa qué reglas se activan y **suma los puntos** de todas las reglas activadas.

Este es el mismo modelo de puntuación que usan, de forma no configurable en su caso (siempre activo), las **Reglas Reputacionales**, **Machine Learning** y **Comportamentales** — ver detalle en [modulo_transferencias.md](modulo_transferencias.md#53-reglas-reputacionales), [modulo_pagos.md](modulo_pagos.md) y [modulo_login.md](modulo_login.md). El "scoring" documentado en este archivo es específicamente su aplicación a las **reglas estándar**.

## 2. Acciones por defecto al activar el switch

Idénticas para Transferencias, Pagos y Login (con una diferencia menor en Login, ver nota):

| Acción | Puntos (Transferencias) | Puntos (Pagos) | Puntos (Login) |
|---|---|---|---|
| 🔔 Alerta | 0 | 0 | 0 |
| 🔐 Solicitar Challenge | 1 | 10 | 1 |
| ❌ Rechazo | 100 | 100 | 100 |
| 🚫 Bloqueo de cliente | 1000 | 1000 | 1000 |

> ⚠️ **Inconsistencia detectada en la fuente:** el valor por defecto de "Solicitar Challenge" en Pagos (10 puntos) difiere del valor en Transferencias y Login (1 punto). No se aclara en el documento si es intencional. Ver gap registrado en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md).

Estos valores son configurables en la sección de acciones de las reglas.

## 3. Umbrales de score acumulado → acción final

**Transferencias y Pagos:**

| Rango de score acumulado | Acción |
|---|---|
| 0 – 1 | ✔️ Aprobado |
| 1 – 99 | 🔐 Solicita Challenge |
| 100 – 999 | ❌ Rechaza (transferencia/transacción) |
| ≥ 1000 | 🚫 Bloquea la cuenta |

**Login:**

| Rango de score acumulado | Acción |
|---|---|
| 0 – 1 | ✔️ Aprobado |
| 10 – 99 | 🔐 Solicitar Challenge |
| 100 – 999 | ❌ Rechazar |
| ≥ 1000 | 🚫 Bloquea la cuenta |

> ⚠️ **Inconsistencia detectada en la fuente:** el umbral inferior de "Solicitar Challenge" en Login está documentado como "Entre 10 y 99", a diferencia de Transferencias/Pagos donde es "Entre 1 y 99". No se aclara si es una inconsistencia de redacción del proveedor o un umbral real distinto para Login. Ver gap registrado en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md).

Estos umbrales son configurables en la parametrización.

Ejemplos de condiciones evaluadas en reglas de login con scoring: geolocalización ilógica (distancia-tiempo imposible), IP distinta a la habitual, dispositivo nuevo, multiplicidad de intentos fallidos seguidos.

## 4. Crear Regla con scoring activo

Común a Transferencias, Pagos y Login: botón **"Crear Regla"** (a la derecha del campo Buscador) abre el modal de creación tradicional, pero **el campo de acciones finales se reemplaza por un input numérico de puntaje** (score que se sumará al total del cliente/cuenta).

**Campos generales de la regla** (varían levemente según el módulo):

| Campo | Transferencias | Pagos | Login |
|---|---|---|---|
| Nombre de la restricción | Sí | Sí | Sí |
| Ámbito | Sí | — | — |
| Modo de creación de la cuenta | — | Sí | Sí |
| Segmentación (persona, banca, cliente, producto, etc.) | Sí | Sí | Sí (persona, banca, cliente) |
| Moneda y montos mínimos/máximos | Sí | Sí | — |
| Vigencia, días y horarios | Sí | Sí | Sí |
| Acción anterior (si aplica) | login fallido, cambio de dispositivo, etc. | login fallido, frecuencia de pagos en tarjetas, etc. | Distancia en km y tiempo, intervalo de tiempo entre login, etc. |
| Campo Scoring (reemplaza acción final) | Sí (ej. 200) | Sí (ej. 150) | Sí (ej. 200) |
| Botón final | "Guardar" | "Aceptar" | "Guardar" |

## 5. Desactivación del switch de scoring

Comportamiento común a los tres módulos:

1. El sistema vuelve al esquema tradicional (acciones fijas por regla, sin ponderación numérica).
2. Se muestra un **modal obligatorio** donde debe seleccionarse al menos una acción fija (bloqueo, solicitar challenge, rechazo) por cada tipo de regla, para no perder funcionalidad.
3. Esas acciones se aplican a todas las reglas estándar ya existentes.
4. El campo de scoring de cada regla queda en **null** / se limpia, desactivando la lógica de puntaje.

## 6. Modelo de scoring unificado (confirmado por el Manual de Ardid 1.13)

Las reglas basadas en puntaje (Reputacionales, Machine Learning, Comportamentales — activas siempre, no requieren el switch de este documento) comparten exactamente el mismo esquema de decisión que el scoring de reglas estándar:

1. Cada regla activa suma o resta puntos (rango 0-1000; Negativa = signo "+", Positiva = signo "−") al score de la cuenta/cliente.
2. El score total se compara contra 4 umbrales configurables que determinan la acción (Aprobar / Solicitar 2FA / Rechazar / Bloqueo de Cliente), correspondientes a 4 niveles de riesgo (Aceptado / Bajo / Medio / Alto).
3. Cada nivel admite activar o no una Alerta independientemente de la acción tomada.
4. Cuando coexisten resultados de múltiples tipos de regla (Estándar + Reputacional + ML + Comportamental) sobre una misma transacción, **el sistema aplica la acción más restrictiva de todas**.

> 💡 El Manual de Ardid 1.13 plantea la hipótesis (no confirmada explícitamente en el texto fuente, pero razonablemente inferida) de que este esquema de scoring es la implementación concreta de lo que las Parametrías de Entidad llaman **"niveles de inferencia"** — la categorización de riesgo y respuestas automáticas por transacción. Ver [modelo_conceptual.md](modelo_conceptual.md#31-niveles-de-inferencia--hipótesis-sin-confirmar).

---
*Ver también: [modulo_transferencias.md](modulo_transferencias.md), [modulo_pagos.md](modulo_pagos.md), [modulo_login.md](modulo_login.md) para el detalle de reglas estándar por módulo, y [modelo_conceptual.md](modelo_conceptual.md) para el modelo de datos unificado.*
