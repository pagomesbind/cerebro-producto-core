---
id: 2026-08-27_adquirencia_iniciativa_convenios_validado_gonzalo
pm: pablo
fecha_captura: 2026-08-27
fuente: "Reunión de validación del prototipo de convenios_configuracion con Gonzalo Rivera (Integraciones/Soporte de Cobro), 2026-08-27"
producto: adquirencia
tema: convenios_configuracion — prototipo validado por el usuario real, listo para mesa técnica con Fintexa
tipo: iniciativa
proyecto: convenios_configuracion
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Novedad puntual:** el proyecto `convenios_configuracion` (rediseño del modelo de herencia de convenios entidad→comercio, en discovery desde el 2026-08-21) pasó su primera validación real de usuario. El PM le mostró un prototipo interactivo completo (Admin mockeado, navegable, con la lógica de cascada funcionando en vivo) a Gonzalo Rivera — el referente de Integraciones/Soporte de Cobro que originalmente reportó el dolor que dio origen al proyecto. Gonzalo confirmó explícitamente que el modelo resuelve el problema y dio luz verde para avanzar con el desarrollo, y validó también la decisión de reusar la infraestructura actual de convenios en vez de reconstruirla desde cero.

Quedaron 2 hallazgos menores de UX (no de modelo de datos) antes de llevar la propuesta a Fintexa/Ingeniería: el diálogo que advierte sobre desactivar un convenio propio cuando la entidad todavía define algo detrás no se entendió a la primera vista y necesita una vuelta de diseño de interacción; y falta contemplar la auto-generación del nombre/descripción del convenio a partir de los valores elegidos, siguiendo una convención que Soporte ya usa hoy manualmente.

**Estado del proyecto:** pasa de "discovery/diseño" a "validado, preparando mesa técnica" — no tiene todavía IDEA de Jira propia ni estimación técnica.
