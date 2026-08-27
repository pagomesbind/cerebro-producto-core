---
id: 2026-08-21_oportunidad_convenios_configuracion
pm: pablo
fecha_captura: 2026-08-21
fuente: "/idea_start — discovery completo (Gates 1-3 cerrados) sobre convenios_configuracion, 2026-08-21"
producto: adquirencia
tema: Rediseño del modelo de herencia de convenios entidad→comercio (convenio_entidad/convenio_comercio)
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

**Candidata a IDEA nueva, con discovery formal ya completo** (a diferencia de la mayoría de las filas de `oportunidades.md`, que son señales tempranas sin trabajar): ver `1_proyectos/convenios_configuracion/proyecto.md` para el detalle completo — problema, tabla de evidencia y solución ya acordados con el PM.

**Problema:** el mecanismo de herencia de convenios (comisiones/plazos/canal+forma de pago) entre entidad y comercio es rígido — no soporta que un comercio mantenga una excepción persistente en un medio de pago mientras el resto sigue heredando cambios de la entidad. Hoy se compensa con configuración 100% manual (Integraciones/Soporte de Cobro), con riesgo real de pérdida financiera (precedente análogo de $15M ARS/mes) y de que medios de pago o entidades enteras dejen de operar.

**Origen:** reunión "Mejoras en convenios" (2026-08-11, Gonzalo Rivera/Nicolás Colón/Mariana Nadalin/Pablo Gomes), formalizada como discovery el 2026-08-21. Consolida 2 escaladas previas sin resolución: T-067 (Nicolás Colón, 2026-07-27) y T-103/T-104 (Pablo Gomes, 2026-08-11) — **al mergear esta oportunidad, marcar esas 3 tareas en `2_areas/tareas.md` como absorbidas por este proyecto**, en vez de dejarlas sueltas.

**Señal de demanda:** Gonzalo Rivera (Integraciones) la señala como una de las prioridades más altas del BAU de Adquirencia. Sin cifra de incidentes/tickets todavía (gap abierto en `1_proyectos/convenios_configuracion/gaps.md`).

**Foco estratégico que alimentaría:** ninguno de los 3 focos 2026 (Onboarding/Pagos FX/Ardid) — corre como BAU/deuda técnica de Adquirencia.

**Solución ya acordada (Gate 3, re-cerrado en definitivo el 2026-08-24 — ver `1_proyectos/convenios_configuracion/decisiones.md`):** resolución en cascada por canal+forma de pago, con override explícito en cada nivel, sobre las tablas reales de `SharedComisionesDB` (`CONVENIO` catálogo compartido → `GRUPO_CONVENIO` adopción de entidad → `COMERCIO_CONV` adopción de comercio) — sin tablas nuevas. Reemplaza la referencia original a espejar `canal_entidad`/`canal_comercio` de AD-8, descartada tras confirmarse (vía el contrato real de la API y un análisis forense de la base productiva) que el mecanismo real de herencia es una copia puntual al crear el comercio, no un vínculo vivo, y que el patrón AD-8 no es un espejo confiable.

**Estado sugerido para el merge:** no "Nueva" — ya tiene discovery y análisis técnico completos (incluida validación empírica contra el contrato de API y la base de datos real), lista para crear la IDEA de Jira y arrancar estimación técnica con Ingeniería/Fintexa (pendiente de validar con ellos el costo de migración del flag de override sobre datos ya existentes).
