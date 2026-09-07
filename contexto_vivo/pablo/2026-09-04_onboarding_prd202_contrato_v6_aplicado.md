---
id: 2026-09-04_onboarding_prd202_contrato_v6_aplicado
pm: pablo
fecha_captura: 2026-09-04
fuente: "Sesión de diseño de la matriz de validaciones y documentos de evidencia del legajo (23 rondas, 2026-09-02 a 2026-09-04), aplicada al contrato oficial a pedido del PM — ver artefactos/2026-09-02_borrador_matriz_validaciones_onboarding.md y onboarding_consolidado-us.md v6.0"
producto: onboarding
tema: Actualización del contrato de datos de PRD-202 (Fase 1) — modelo de palancas simplificado, renombres, precisión de alcance
tipo: iniciativa
proyecto: PRD-202
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: ee14a4b68342c2020cd4dfbc817cd6bc347de70d
---

`onboarding_consolidado-us.md` (PRD-202, Fase 1 — alta wallet PF mayor de edad) pasó de v5.10 a v6.0 (2026-09-04), aplicando el diseño cerrado en una sesión previa de 23 rondas sobre la matriz de validaciones del motor de Onboarding y los documentos de evidencia del legajo para Worldsys.

**Cambios de definición del contrato:** `personaFisica.fiscal.cuit` migra a `personaFisica.personal.cuil` (deja de ser dato fiscal, lo resuelve Renaper Datos, con rescate automático vía Nosis si viene vacío/inválido); `domicilioLegal` se anida dentro de `personal`; catálogo cerrado de 5 valores para `condicionFiscal` con su lógica exacta de resolución vía ARCA; renombres de documentos (`DNI_FRENTE`→`DNIFRENTE`, `DNI_DORSO`→`DNIDORSO`, `SELFIE_FOTO`→`SELFIE`, `EVIDENCIA_CONSENTIMIENTO`→`TYC`, `EVIDENCIA_RENAPERROSTRO`→`EVIDENCIA_FACEMATCH`, `EVIDENCIA_PRUEBADEVIDA`→`EVIDENCIA_LIVENESS`, `trazabilidadCliente`→`perfilDigital`); nuevo objeto `personaFisica.validacionEmail.otp`/`validacionTelefono.otp` para la confirmación de contactabilidad vía `PATCH`.

**Cambio de flujo más significativo:** el motor de validación por paso, que modelaba 3 modos configurables (*Validar*/*Por la orga*/*No validar*), se simplifica a una palanca booleana `true`/`false` — el modo *No validar* no existe en la operación real del motor. Esto renumeró los criterios de aceptación de la historia US-3 (Endpoint de Onboarding crear/continuar).

**Cambio de alcance relevante para el roadmap:** se precisó que el motor de Etapa 2 (ARCA condición fiscal, UIF, Worldsys) y Lista 15 (Etapa 1) **ya existen y corren en producción** para otros flujos de Onboarding — PRD-202 los adapta al nuevo modelo de palancas, no los construye desde cero. El "Fuera de alcance" de US-3 quedó desactualizado en este punto (decía "construcción en IDEAs separadas" para los tres). Solo **ARCA no confiables (PRD-117) y Totalizadores Coelsa** siguen siendo construcción futura, confirmado por el PM.

Sin impacto en prioridades, SP estimados ni dependencias entre historias — es una actualización de contrato de datos y de precisión de alcance, no una resegmentación.
