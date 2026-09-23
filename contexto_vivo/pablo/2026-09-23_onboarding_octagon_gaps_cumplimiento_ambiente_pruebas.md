---
id: 2026-09-23_onboarding_octagon_gaps_cumplimiento_ambiente_pruebas
pm: pablo
fecha_captura: 2026-09-23
fuente: "/sync_mails — hilo 'Re: Integración On Boarding' (threadId 1a0623520bc8519e), Ana Laura Irrazabal (PLA/FT/FP, BIND), 2026-09-22"
producto: onboarding
tema: PLD detecta datos y DDJJ mínimos faltantes en el ambiente de pruebas del sistema de onboarding de desarrollo propio (integración Octagon) — insumo para T-057
tipo: gap
destino_propuesto: 3_recursos/detalle_productos/onboarding/
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

**Fuente:** Ana Laura Irrazabal (Analista de PLA/FT, Gerencia de Prevención de LA/FT/FP y Cumplimiento de BIND) revisó el entorno de pruebas (testing) del "sistema de onboarding de desarrollo propio" que el equipo está por implementar — este es el sistema al que se integraría Octagon (ver `2026-09-03_onboarding_octagon_paquete_datos_integracion`, en cola, y la tarea T-057 de Pablo Gomes).

**Hallazgo — datos mínimos exigidos por normativa que el sistema omite** para la correcta identificación de las personas humanas vinculadas (integrantes del órgano de administración o equivalente, representantes legales, apoderados y Beneficiarios Finales):
- Número de teléfono.
- Dirección de correo electrónico.
- Estado civil.
- Actividad principal.
- Declaraciones Juradas (DDJJ) de **PEP, FATCA, OFAC y Sujeto Obligado**.

**Pedido de PLD:** incorporar los datos y DDJJ faltantes para asegurar un proceso de debida diligencia alineado a la normativa vigente de PLA/FT y optimizar la gestión documental.

**Sugerencias adicionales de mejora de UX/gestión documental sobre las actas de designación:**
- Visualizar claramente identidad, cargos otorgados y duración de los mismos.
- Mostrar la lista completa de autoridades y representantes autorizados para operar la cuenta.
- Habilitar la descarga del legajo completo en formato PDF.

**Preguntas abiertas de PLD, sin responder todavía (candidatas a reunión, según propone la propia Ana Laura):**
1. Si el motor de búsqueda no encuentra una actividad económica asociada, ¿permite continuar con el alta y el análisis?
2. ¿Qué información contendrá el formulario KYC/KYB final que debe firmar el cliente potencial?
3. La matriz de riesgo cliente que se muestra: ¿es única e inicial, o hay una secundaria según la transaccionalidad del cliente? ¿Cómo se pondera?

**Relevancia:** este hallazgo es un insumo directo para la tarea T-057 (analizar el paquete de datos propuesto por Octagon para la integración de onboarding PJ) — el gap de datos detectado por PLD debería incorporarse a la especificación antes de cerrar el diseño de la integración con Octagon.
