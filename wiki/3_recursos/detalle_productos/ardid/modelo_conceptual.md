# Ardid/Akurtech — Modelo Conceptual y Glosario

> Estado: en producción.

> Fuente: `Manual de Ardid 1.13.pdf` (285 páginas, enero 2025), sección de síntesis conceptual. Extracción y estructuración vía agente de investigación (2026-07-02). Este manual es la versión previa al rebranding a "Akurtech" — ver [index.md](index.md#nota-ardid--akurtech). Se usa aquí porque aporta una síntesis del modelo de datos que las guías Akurtech 2026 (más nuevas, pero divididas por módulo) no repiten de forma unificada.

## 1. Modelo jerárquico de datos

```
ENTIDAD (banco/fintech cliente de Ardid — unidad de configuración raíz)
   │
   ├── Parametrías propias (independientes de Parametrías Generales del sistema):
   │     niveles de inferencia, aprobación de transferencias a clientes no existentes,
   │     tiempo de depuración de alertas, notificaciones (email/Telegram), Apps, Actions
   │
   ├── Segmentación de CLIENTES (formato elegido una única vez, irreversible):
   │     Tipo de Persona → Tipo de Banca → Tipo de Cliente
   │     (jerarquía configurable; cada nivel tiene ID único usado por APIs externas)
   │
   ├── CLIENTE
   │     ├── segmentado por: Tipo de Persona / Tipo de Banca / Tipo de Cliente
   │     ├── tiene: Tipo de Producto → Tipo de Subproducto (cuentas, tarjetas)
   │     ├── genera: TRANSFERENCIAS (Interna/Externa/Debin × Entrante/Saliente)
   │     └── genera: PAGOS (con Tarjeta, Canal de pago, Tipo de pago, Comercio)
   │
   └── REGLAS (aplican sobre Transferencias y/o Pagos de los clientes de la entidad)
         ├── Estándar (atómicas, sí/no, con "Acciones Anteriores" + "Acciones" resultado)
         ├── IA (aprende habitualidad → habilita reglas ML equivalentes)
         ├── Reputacionales (score 0-1000, alimentadas por Blacklist/Whitelist)
         ├── Machine Learning (score 0-1000, dependientes de Reglas IA activas)
         └── Comportamentales (score 0-1000, dependientes de Actions de una App)

BLACKLIST / WHITELIST (por entidad, 9 categorías: Identificación, Dispositivo, Cuenta,
   IP, Correo, Dominio de E-mail, Geolocalización, Tarjeta, Comercio)
   → alimenta directamente las Reglas Reputacionales

WORLDSYS (conector externo) → alimenta Blacklist automáticamente (PEP, Sujeto Obligado, Terrorista)
```

Este modelo es el resultado de cruzar el contenido de [configuracion_inicial.md](configuracion_inicial.md) (Parametrías), [modulo_transferencias.md](modulo_transferencias.md)/[modulo_pagos.md](modulo_pagos.md)/[modulo_login.md](modulo_login.md) (Reglas) y [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md) (Blacklist/Whitelist/Worldsys).

## 2. Regla general de resolución de conflictos entre reglas

Declarada explícitamente en el manual: **"La acción a realizar se contrarrestará con el resultado de los otros tipos de reglas y el sistema tomará la acción más restrictiva."**

Es decir, el motor de decisión combina los resultados de **Estándar + Reputacionales + ML + Comportamentales** sobre una misma transacción/login y aplica siempre la acción más severa entre todas las que se hayan disparado. Ver el detalle del sistema de scoring compartido en [scoring.md](scoring.md).

## 3. Taxonomía de las 5 familias de reglas

| Tipo de regla | Lógica | Scoring |
|---|---|---|
| **Estándar** | Reglas "atómicas" — condiciones booleanas explícitas (montos, tiempos, acciones anteriores) evaluadas individualmente | No acumula score; se dispara sí/no (salvo que se active el switch de Scoring — ver [scoring.md](scoring.md)) |
| **IA** | Detecta "habitualidad" de un comportamiento (aprende el patrón normal del cliente) | Habilita las reglas de Machine Learning correspondientes |
| **Reputacionales** | Basadas en pertenencia a Blacklist/Whitelist | Suma/resta puntos (0-1000) |
| **Machine Learning (ML)** | Evalúa si el comportamiento actual es habitual o no, según lo aprendido por Reglas IA | Suma/resta puntos (0-1000), misma lógica que Reputacionales |
| **Comportamentales** | Evalúa secuencias de "Actions" dentro de una App móvil/web de la entidad | Suma/resta puntos (0-1000) |

## 3.1. "Niveles de inferencia" — hipótesis sin confirmar

En la sección de Parametrías de Entidad, el manual define:

> "Los niveles de inferencia refieren a la categorización de riesgos y respuestas automáticas que el sistema implementa para cada transacción en función de la probabilidad de fraude. A través de la integración de reglas y modelos de aprendizaje, ARDID evalúa cada transacción para determinar su nivel de riesgo y decide la acción correspondiente, que puede ir desde una aprobación automática hasta el bloqueo de la cuenta del cliente."

El texto fuente no cruza explícitamente esta definición con el modelo de scoring de 4 umbrales (Aceptado/Bajo/Medio/Alto → Aprobar/2FA/Rechazar/Bloqueo) documentado en [scoring.md](scoring.md). Sin embargo, la coincidencia exacta de las 4 categorías de riesgo en ambos lugares del manual sugiere fuertemente que son el mismo concepto.

> ⚠️ **Esto es una inferencia razonada del agente que procesó el manual, no una afirmación literal del texto fuente.** Pendiente de confirmación con el equipo/proveedor — ver gap en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md).

## 4. Glosario de acrónimos y términos

| Término | Significado |
|---|---|
| **PLAFT** | Prevención de Lavado de Activos y Financiamiento del Terrorismo — categoría de alertas paralela a las "Operativas" |
| **PEP** | Persona Expuesta Políticamente |
| **SO** | Sujeto Obligado (obligado legalmente a reportar actividad financiera) |
| **Error Tipo I** | Falso positivo — transacción/transferencia legítima incorrectamente identificada como fraudulenta |
| **Error Tipo II** | Falso negativo — transacción/transferencia fraudulenta no detectada, aprobada como legítima |
| **α (Alfa) / Nivel de Significancia** | Umbral aceptable de Error Tipo I |
| **β (Beta) / Nivel de Potencia** | Umbral aceptable de Error Tipo II |
| **BIN** | Bank Identification Number — primeros 6-8 dígitos de una tarjeta, identifican entidad emisora y producto |
| **CIMPRA / Worldsys** | *(No confundir)* — CIMPRA es la Comisión Interbancaria para Medios de Pago (normativa QR); Worldsys es el conector externo de Ardid/Akurtech para verificación de PEP/SO/Terroristas |
| **Excepción** | Habilitación temporal de una transferencia/pago previamente bloqueado, tras marcarlo manualmente como "Confiable" — retroalimenta el algoritmo de IA para reducir falsos positivos |
| **Modificaciones pendientes** | Flujo de doble control: toda alta/edición/eliminación de reglas Reputacionales/IA/ML/Comportamentales requiere aprobación de un segundo usuario con permisos antes de tomar efecto |

## 5. Nota histórica — versión del manual fuente

Este manual (versión 1.13, enero 2025) usa **exclusivamente el nombre "Ardid"** — no hay ninguna mención a "Akurtech" en todo el documento, consistente con la hipótesis (confirmada por el usuario, ver [index.md](index.md#nota-ardid--akurtech)) de que Akurtech es el nombre comercial adoptado en un rebranding posterior (documentado a partir de la versión 1.18, mayo 2026 — ver [historico/historial_versiones.md](historico/historial_versiones.md)).

---
*Ver también: [scoring.md](scoring.md) para el detalle completo del sistema de puntuación, y [index.md](index.md) para el mapa completo del módulo.*
