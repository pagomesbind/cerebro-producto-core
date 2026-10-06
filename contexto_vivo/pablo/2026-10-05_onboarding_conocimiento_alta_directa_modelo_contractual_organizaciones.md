---
id: 2026-10-05_onboarding_conocimiento_alta_directa_modelo_contractual_organizaciones
pm: pablo
fecha_captura: 2026-10-05
fuente: "sesión de trabajo del proyecto bcra_anexo_b — definiciones del PM para P-03 (Procedimiento de Alta de Cuentas con Onboarding realizado por la Organización) y PDF `REQUISITOS ALTA DE CUENTAS CONFORME LA RESOLUCIÓN UNIFORME 200-24 (2).pdf`"
producto: onboarding
tema: Modelo vigente de alta de cuentas por organizaciones con onboarding propio: qué hace y qué no guarda Bind PSP, responsabilidad contractual de la organización y derecho de Bind a exigir los legajos
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "no — la aparente contradicción con `wallet/validacion_totalizadores_cbu_cvu.md` quedó resuelta por el PM el 2026-10-05: el control de cantidad máxima de CVU, CBU o CBU y CVU por titular sí se aplica por defecto en todas las altas de cuentas de personas humanas (no aplica a personas jurídicas)."
confianza: media
estado: en_cola
merge_commit:
---

Definiciones del PM (2026-10-05) sobre cómo opera hoy el alta de cuentas cuando la validación de identidad la hace una organización cliente.

## Lo que ocurre hoy (no incluye el rediseño de Onboarding estratégico)

- **Alta completamente directa (la mayoría del volumen):** Bind PSP no controla nada sobre la identificación de la persona y no guarda legajo ni evidencia. Solo registra y persiste la información en bruto necesaria para crear la cuenta en Wallet.
- **Alta por el Onboarding de Bind con validaciones apagadas:** Bind ejecuta las validaciones que quedan activas, que son controles mínimos, y guarda información parcial en el legajo digital. **No guarda evidencia de las validaciones apagadas**, porque las hace el cliente. Ejemplo: si una organización hace la prueba de vida por su cuenta, Bind no tiene evidencia de esa prueba para esa persona en su sistema.
- La remediación (que Bind valide y guarde en todas las altas) es el proyecto de Onboarding estratégico (PRD-202 y relacionados). Como todavía no es realidad, **no se incluye en los procedimientos del Anexo B**.

## Modelo contractual vigente

- La organización es responsable de las validaciones que hace. El acuerdo con la organización debe estipular que ella cubre todas las validaciones, y que registra y conserva el legajo con la información mínima que Bind PSP exige para sus cuentas (la lista de la Resolución Uniforme UIF 200/24, para personas humanas y jurídicas, con la documentación por tipo de sociedad).
- **Bind PSP puede exigir esos legajos en cualquier momento y la organización está obligada a ponerlos a su disposición.** El PM lo marcó como la definición más importante de P-03.
- **Por verificar:** el texto de los convenios y contratos con cada organización (tarea T-170). El Cerebro no tenía esa cláusula documentada.

## Validación mínima que sí se aplica (aclarado por el PM, 2026-10-05)

Por defecto, en las altas de cuentas de **personas humanas** Bind PSP valida la cantidad máxima de CVU, CBU o CBU y CVU que puede tener el titular (totalizadores de Coelsa, en producción desde 2026-08-19). Es la validación mínima que se cubre hoy en todas las altas de persona humana, incluida el alta directa. No aplica a personas jurídicas. Se incorporó a P-01 y P-03. La mención del alta en Ardid que figura en la wiki no se incluyó en P-03.

## Validación de edad en el Onboarding de persona humana (aclarado por el PM, 2026-10-05)

En el Onboarding de Bind (P-01), la validación de edad forma parte de la consulta a RENAPER. Por defecto se rechazan las solicitudes de personas **menores de edad** (el PM escribió "mayores"; se interpretó como un error de tipeo, confirmar). En el alta directa esta validación no se hace y P-03 no la menciona.
