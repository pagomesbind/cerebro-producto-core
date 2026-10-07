---
id: 2026-10-07_onboarding_conocimiento_canon_desactualizado_vs_contrato_v81
pm: pablo
fecha_captura: 2026-10-07
fuente: "Pasada en limpio del proyecto Onboarding Estratégico (2026-10-07) — relectura completa del proyecto general, PRD-202/147/214/108/208/247 y del canon `3_recursos/detalle_productos/onboarding/`; síntesis en `1_proyectos/proyecto-onboarding-estrategico/artefactos/2026-10-07_estado_consolidado_vigente.md`"
producto: onboarding
tema: El canon de Onboarding en 3_recursos quedó atrasado respecto del contrato vigente (US v8.1) y de decisiones de legajo posteriores a agosto
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md (§0, §1, §4, §5.1, §5.2, §9) e integracion_worldsys_complianceone.md — ver puntos abajo"
confianza: alta
estado: en_cola
merge_commit:
---

Al releer todo el proyecto se detectó que el canon de Onboarding (solo escribible vía `/context_merge`) no refleja decisiones ya cerradas del proyecto. Cada punto cita la fuente que lo establece; el detalle completo está en el consolidado `2026-10-07_estado_consolidado_vigente.md`.

## Qué hay que actualizar en el canon

1. **Wallet y Onboarding no se hablan directo — siempre vía el KYC-wrapper.** `arquitectura_solicitud_y_flujos.md` §4, §5.1 y §5.2 dibujan Wallet→Onboarding directo. Decisión heredada #16 (2026-08-20): el KYC-wrapper, microservicio del equipo de Wallet, intermedia obligatoriamente en ambos sentidos (creación/continuación, consulta de detalle, aviso de cambio de estado y sondeo de respaldo). Además cita "decisión #1" para el `idSolicitud` donde corresponde la #9, y referencias a `proyecto.md` §4.5/§4.1/§6 que no existen con esa numeración.
2. **Modelo de palancas: `true` / `false`, no tres modos.** `true` = Onboarding corre la validación de contenido; `false` = solo verifica la evidencia de la organización y el dato crudo. El modo "No validar" fue eliminado el 2026-09-04 (`prd-202_onboarding_consolidado/decisiones.md` [2026-09-04] (2); US v8.1, US-3 AC-1/AC-2/AC-16 a AC-34). Cualquier mención canónica a *Validar / Por la orga / No validar* está superada. ARCA, UIF y Worldsys están siempre en `true` por política de PLD.
3. **Contrato de la API KYC vigente = US v8.1 (2026-09-11):** endpoints `/cuenta/kyc`, estados, `accion` ∈ {`FALTANTE`, `ALTERNATIVA`, `URL_ACCION`}, catálogo de 9 documentos que puede enviar la organización y lista de los que Onboarding genera siempre. Detalle en consolidado §1.
4. **Formato de envío a Worldsys: un ZIP por onboarding** con TXT de auditoría (decisión 2026-08-25, `prd-147_legajo_worldsys/decisiones.md`). `integracion_worldsys_complianceone.md` dice "carga siempre individual" (documento por documento): superado en ese punto. Worldsys aún debe confirmar el detalle a nivel API.
5. **Repositorio del legajo: decisión reabierta el 2026-09-08, sin resolver.** El canon no refleja ni la reapertura (Com. "A" 8471, vendor lock-in), ni el aclaratorio de Diego Scaldaferri (el mandato del banco es "legajo recuperable", no Worldsys específicamente), ni el dato de costo del 2026-09-21 (Worldsys no cobra por ticket/soporte, solo almacenamiento). §1 de `arquitectura_solicitud_y_flujos.md` deja abierto si el alta de legajo vive en la Etapa 3 de Onboarding; hoy la integración Onboarding↔Worldsys existente es solo screening (`evaluate`).
6. **Orden real de los pasos de identidad:** prueba de vida primero (Socialnet genera `SELFIE` + `EVIDENCIA_FACEMATCH` + `EVIDENCIA_LIVENESS`) y Renaper Rostro después, reutilizando la selfie. Lista 15 corre en Etapa 1.
7. **Qué guarda Onboarding cuando la organización valida por su cuenta:** según el PM (2026-10-05, item `2026-10-05_onboarding_conocimiento_alta_directa_modelo_contractual_organizaciones`, aún sin mergear) Bind **no guarda evidencia de las validaciones apagadas** — ej. si la organización hace la prueba de vida, Bind no tiene esa evidencia. La remediación es el proyecto de Onboarding estratégico (PRD-202 y relacionados).

## Reglas para el merge

- Este item **no contradice** los dos del 2026-10-05 sobre rechazadas/AES-256; los complementa. Queda pendiente verificar el alcance real del borrado al pasar a `RECHAZADA` (contradice el gap de 2026-07-20 de "sin limpieza automática").
- No elimina contenido canónico: solo corrige lo superado, citando la decisión que lo supera.
