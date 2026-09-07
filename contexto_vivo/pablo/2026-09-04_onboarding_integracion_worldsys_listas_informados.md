---
id: 2026-09-04_onboarding_integracion_worldsys_listas_informados
pm: pablo
fecha_captura: 2026-09-04
fuente: "Email real de integración con Worldsys AML (Kevin Díaz/Leandro Competiello, Worldsys Group) con Banco Industrial/Bind PSP, hilo 'API WS Listas' (jul-2025 en adelante) — archivado en 4_archivos/historial_raw/2026-09_worldsys_listas_informados/. Complementado con capturas de pantalla del backoffice de Entidades de Onboarding y de la documentación pública apis.worldsys.com.ar, aportadas por el PM el 2026-09-04 en el chat."
producto: onboarding
tema: Integración real con el servicio "Listas de Informados" (LDI) de Worldsys — endpoints, autenticación, parámetro ConfigurationName, y distinción Evaluate vs. SourcesSearch
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/integracion_worldsys_listas_informados.md
tipo_destino: crear
contradice: "no — complementa 3_recursos/detalle_productos/onboarding/validacion_lista_negra_bind.md (mismo dominio: consultas a listas/blacklists durante el onboarding, pero servicio distinto — 'Lista Negra BIND' es un servicio SOAP de Banco Industrial/Bantotal, 'Listas de Informados' es un servicio REST de Worldsys, con su propio Compliance One)."
confianza: alta
estado: en_cola
merge_commit:
---

## Qué es

Bind PSP integra el servicio **"Listas de Informados" (LDI)** de Worldsys — la misma consulta que en el motor de validación de Onboarding se llama **"Consulta Worldsys"**, y que **unifica en una sola llamada las listas de PEP y de Terroristas** (antes hubiera requerido 2 consultas separadas). El resultado de esta consulta es la evidencia que se guarda en el legajo como `EVIDENCIA_WORLDSYS`.

## Endpoints reales (confirmados por Worldsys, ambiente productivo)

- **Autenticación:** `POST https://bind_psp.apicompliance.worldsysweb.com/api/TokenAuth/Authenticate`
- **Evaluate v2:** `POST https://bind_psp.apicompliance.worldsysweb.com/api/ldi/v2/Evaluate`
- **SourcesSearch v2:** `POST https://bind_psp.apicompliance.worldsysweb.com/api/ldi/v2/SourcesSearch`

En el ambiente de QA, el prefijo `bind_psp` se reemplaza por `bind_pspqa` en todos los hosts.

## `Evaluate` vs. `SourcesSearch` — no son intercambiables

Diferencia confirmada explícitamente por Worldsys (Kevin Díaz, 2026-07-03): **`Evaluate v2` deja la consulta registrada y visible en Compliance One** (sección "Listas de Informados → Evaluaciones") — es la que le da valor de auditoría/trazabilidad a la consulta desde el lado del banco. **`SourcesSearch v2` no queda registrada en Compliance One.** Para el propósito de Onboarding (dejar evidencia auditable en el legajo del titular), el método correcto es **`Evaluate`**, no `SourcesSearch`.

## Parámetro `ConfigurationName` — reemplaza al genérico "Búsqueda general"

Al arrancar la integración, el valor por defecto de `ConfigurationName` era `"Busqueda general"` (referencia a búsquedas ya guardadas en Compliance One, con criterios de similitud 90%/75% en la configuración inicial). A pedido explícito de Bind (Cristian Bonafede, 2026-07-21 — "necesitamos agrupar en un solo control las listas de PEP y Terroristas, con el fin de no realizar varias llamadas a los servicios y poder resolverlo en una sola"), Worldsys unificó ambas listas en una búsqueda nueva:

```
"ConfigurationName": "Control Terrorista y PEP"
```

Este valor es **configurable por entidad** — en el backoffice de Onboarding (pantalla "Entidades → Configuración") aparece como el campo **"Control (Worldsys)"**, junto a:
- **Factor Similitud (Worldsys)** — entero 1-100 (visto en backoffice: `80`)
- **Factor Similitud Inverso (Worldsys)** — entero 1-100 (visto en backoffice: `80`)

⚠️ **Nota de reconciliación:** la documentación pública genérica del servicio (`apis.worldsys.com.ar`, endpoint "Search", parámetros `nombre`/`documento`/`identificacionTributaria`/`control`/`factorSimilitud`/`factorSimilitudInverso`/`tipoFuente`/`fuentes`) nombra este mismo concepto como `control`, no `ConfigurationName` — puede ser el mismo campo con nombre distinto según la versión/endpoint de la API (`Search` genérico vs. `Evaluate` v2 específico de Bind), o dos cosas relacionadas pero no idénticas. A confirmar con Worldsys/Onboarding antes de fijar el nombre exacto del parámetro en cualquier contrato interno.

## Decisión de Onboarding: no se manda el campo `fuentes`

Aunque la documentación pública del servicio lo lista como parámetro opcional (un array de `string` con los nombres de las fuentes puntuales donde buscar), Onboarding **no lo envía** en la consulta — se deja que `ConfigurationName`/`control` resuelva sola qué fuentes usar, según lo configurado del lado de Worldsys.

## Response real (ejemplo de producción, aportado por el PM 2026-09-04)

```json
{
  "Worldsys": {
    "evaluationId": 47908430,
    "matchCount": 0,
    "maxScore": 0,
    "minScore": 0,
    "hasDocumentHits": false,
    "includesOwnSources": false,
    "isMarkedNegative": false,
    "systemResult": 6,
    "hits": []
  }
}
```

⚠️ **Gap sin resolver:** no hay un diccionario/leyenda de los valores posibles de `systemResult` (en este ejemplo, `6`) en ninguna fuente disponible todavía — mismo patrón de gap ya visto antes en este Cerebro con otros códigos numéricos sin leyenda (ej. `Estado`/`MotivoRechazo` del CSV histórico de solicitudes de Onboarding, PRD-202). Habría que pedírselo a Worldsys (Kevin Díaz/Leandro Competiello) antes de poder interpretar `systemResult` con confianza — hoy solo se puede inferir el resultado a partir de `matchCount == 0` (sin coincidencias).

## Relación con otros documentos

- Documento hermano en el mismo dominio (listas/blacklists), pero servicio distinto: `validacion_lista_negra_bind.md` (servicio SOAP `ConsultarListaNegra`, Banco Industrial/Bantotal — cubre específicamente la "lista 15" exigida por PLD del banco). **Ambos corren en el motor de Onboarding, en pasos distintos** — "Lista 15 del banco" (Etapa 1, justo después de Renaper Datos) y "Consulta Worldsys" (Etapa 2, incluye PEP).
- Contrato de datos de PRD-202 (`onboarding_consolidado-us.md`) y el borrador de la matriz de validaciones (`prd-202_onboarding_consolidado/artefactos/2026-09-02_borrador_matriz_validaciones_onboarding.md`) — este último ya documenta el formato propuesto del documento `EVIDENCIA_WORLDSYS` para el legajo, con estos datos reales incorporados (ronda 19).
