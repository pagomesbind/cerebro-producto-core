---
id: 2026-08-28_adquirencia_convenios_configuracion-ac_alcance_completo
pm: pablo
fecha_captura: 2026-08-28
fuente: "/idea_ac — sesión directa sobre convenios_configuracion/artefactos/convenios_configuracion-solution.md"
producto: adquirencia
tema: criterios de aceptación del proyecto de convenios/comisiones
tipo: iniciativa
proyecto: convenios_configuracion
pm_destino:
destino_propuesto: wiki/2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

`convenios_configuracion` (Adquirencia, Pablo Gomes) suma 28 criterios de aceptación Given/When/Then cubriendo el alcance completo del proyecto de mejoras en la configuración y herencia de convenios entidad↔comercio — happy path (alta sin copia, cascada de resolución, propagación automática, origen visible), casos borde (los 8 casos estado×origen×acción del Admin, diálogo de doble nivel, migración de grupos compartidos), estados de error (constraint de unicidad, validación de comisión QR, idempotencia, concurrencia) y criterios no funcionales (congelamiento del endpoint transaccional, no-borrado físico/auditoría, remediación de datos previa al Go Live).

Particularidad de proceso: se redactaron directo desde el documento de análisis técnico-funcional (`/idea_solution`, ya validado dos veces en vivo con Soporte y Fintexa), sin que existan todavía un documento de historias de usuario (`/idea_us`) ni un PRD formal (`/idea_prd`) — ambos pasos siguen pendientes en el plan del proyecto. Consultado explícitamente sobre el recorte de alcance (mecanismo central del Admin / todo el alcance completo / solo la validación de comisión QR), el PM eligió cubrir el alcance completo. El contrato de integración concreto sigue sin validar en la mesa técnica formal (T-026) — los criterios se redactaron en términos de comportamiento observable, no de endpoints específicos, para no atarse a un diseño que todavía puede cambiar.

Ver `wiki/1_proyectos/convenios_configuracion/proyecto.md §8` (Sesión 2026-08-28) y `wiki/1_proyectos/convenios_configuracion/artefactos/convenios_configuracion-ac.md`.
