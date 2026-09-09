---
id: 2026-09-08_iniciativa-cola-verificacion-manual-nuevo-proyecto
pm: nicolas
fecha_captura: 2026-09-08
fuente: "Discovery /idea_start sobre OB-246 (2026-09-08)"
producto: onboarding
tema: Nuevo proyecto de Nicolás Colón — reproceso masivo de solicitudes en Verificación Manual
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 4b0d3d1e684ff33256a33a29f86746dfd5c7cc9a
proyecto: cola_verificacion_manual
---

Nace el proyecto `cola_verificacion_manual` (Nicolás Colón), a partir de [OB-246](https://bindpsp.atlassian.net/browse/OB-246) (pedido de Integraciones por el cliente Inter). Pide poder reprocesar en bloque las solicitudes de Onboarding en estado "Verificación Manual", igual que ya existe hoy para "Error en alta" — un solo botón ("Reprocesar"), sin lógica de negocio nueva, que replica en bucle la acción que ya existe por solicitud individual.

Discovery cerrado en Gate 3 (2026-09-08): evaluado como BAU (no mueve NSM ni los KR de Onboarding, foco de Pablo Gomes), con demanda ya señalada de forma independiente en el canon (`detalle_productos/onboarding/hallazgos_operativos_historicos.md`, pain point documentado desde julio: "no se pueden aprobar varias solicitudes de Onboarding juntas") y alta probabilidad de generalización a otros clientes de alto volumen de Onboarding (TINPAY, Coppel). El objetivo acordado con el PM es producir una estimación de esfuerzo para presentar a Emma Vignoles (COO) y a clientes — no se decide construcción en este discovery.

Quedan dos condicionantes abiertos antes de cotizar en firme (ver `gaps.md` del proyecto): confirmar con Fintexa (dueño del producto Onboarding) el costo real, y verificar que no choque con la iniciativa "Onboarding unificado" del Comité de Arquitectura de Fintexa (en curso desde agosto 2026).

> Nota: dado que Onboarding es el foco estratégico de Pablo Gomes, si él ya tiene contexto propio sobre este pedido o sobre "Onboarding unificado" pisando este alcance, el merge puede requerir su confirmación antes de consolidar en `direccion/iniciativas.md`.
