---
id: 2026-08-18_onboarding_prd147_legajo_worldsys_alcance_ampliado
pm: pablo
fecha_captura: 2026-08-18
fuente: "/idea_start — discovery Modo D sobre PRD-147, material técnico nuevo (hilo mail Banco Industrial/Worldsys + PDF Ingesta de Documentos + Swagger ComplianceOne)"
producto: onboarding
tema: PRD-147 (legajo Worldsys) — alcance ampliado a creación online de persona, manejo de duplicados resuelto
tipo: iniciativa
proyecto: PRD-147
pm_destino:
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Novedad puntual (2026-08-18):** PRD-147 (guardar documentación en el legajo de Worldsys, foco Onboarding — KR2) tuvo una sesión de discovery formal con material técnico nuevo del proveedor. Tres avances:

1. **Alcance ampliado:** además de cargar documentos, Onboarding pasa a **crear/consultar la persona en Worldsys de forma online** (`POST /profile/customers` de la API ComplianceOne, con `GET /profile/by-identification/{cuit}` como fallback) — necesario porque subir un documento requiere un `personId` que hoy solo existe si la persona fue cargada por el batch diario de PLD/BCRA (proceso ya en producción, separado de este proyecto).
2. **Gap técnico resuelto:** Worldsys no es multi-entidad (Bind PSP es una única entidad de su lado) — un mismo CUIT en distintas organizaciones de Bind es la misma persona en Worldsys, y la creación online puede devolver `409` si ya existe. Se definió que Onboarding asocia el `customerId`/`personId` igual y actualiza el perfil con los datos de la nueva organización.
3. **Alcance recortado (diferido):** la consulta de Wallet a Worldsys (recuperar documentos) se separa como no prioritaria por ahora — el foco actual es solo la creación del legajo por parte de Onboarding.

Nuevo gap abierto (no bloqueante): cómo convive la creación online de persona con el batch diario existente a Worldsys SOS — pendiente de preguntarle directamente al proveedor (T-005 en `1_proyectos/tareas.md`).
