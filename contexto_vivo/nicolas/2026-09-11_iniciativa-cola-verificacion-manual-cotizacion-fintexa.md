---
id: 2026-09-11_iniciativa-cola-verificacion-manual-cotizacion-fintexa
pm: nicolas
fecha_captura: 2026-09-11
fuente: "Cotización de Fintexa recibida por el PM (2026-09-11), formalizada en Jira/wiki el 2026-09-15"
producto: onboarding
tema: Novedad del proyecto cola_verificacion_manual — cotización real de Fintexa recibida
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: cola_verificacion_manual
---

El proyecto `cola_verificacion_manual` (Nicolás Colón, PRD-242) recibió la cotización real de Fintexa: **56 horas de desarrollo (~3 SP)**, pedida por separado del proyecto hermano `visibilidad_error_alta` (OB-247, cotizado en 24 hs / ~1 SP — mismo cliente Inter y mismo portal, cerrados el mismo día de discovery pero cotizados de forma independiente, no como paquete). El costo bajo confirma la hipótesis del Gate 3: la solución reutiliza sin cambios el mecanismo de acción masiva ya construido para el estado "Error en alta".

El PRD se actualizó a v1.1 (Caso de negocio con el costo real, retirado el riesgo de "costo no confirmado") y se cargó en Jira: descripción de PRD-242 actualizada con el cuerpo completo del PRD, campo "SP estimado" = 3, y OB-246 linkeada como delivery ticket de PRD-242 ("Polaris work item link").

Queda un solo condicionante abierto antes de presentar la cotización en firme a Emma Vignoles: confirmar con Fintexa si la iniciativa "Onboarding unificado" (Comité de Arquitectura, en curso desde agosto) afecta la misma pantalla del backoffice que esta solución extiende.
