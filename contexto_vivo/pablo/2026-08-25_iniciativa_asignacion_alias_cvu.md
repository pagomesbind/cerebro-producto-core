---
id: 2026-08-25_iniciativa_asignacion_alias_cvu
pm: pablo
fecha_captura: 2026-08-25
fuente: "/idea_start — discovery de `asignacion_alias_cvu`, 2026-08-25"
producto: wallet
tema: "Nuevo proyecto asignacion_alias_cvu — discovery cerrado de punta a punta en una sesión"
tipo: iniciativa
proyecto: asignacion_alias_cvu
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

Nuevo proyecto de Pablo Gomes: `asignacion_alias_cvu/` — fix de resiliencia para la asignación automática de alias tras creación de CVU (apibank/Coelsa), a partir del ticket de soporte MDA-292391 (Banco Industrial). Discovery completo en una sola sesión (2026-08-25): los 3 gates de `/idea_start` confirmados por el PM. ✅ Vale la pena ahora (BAU técnico, transversal a toda la cartera de Wallet-as-a-Service, banco ya cerró su ticket sin ofrecer alternativa). Solución acotada al mínimo esfuerzo: detectar el error `422 VW006` y reintentar una vez tras 700ms, reusando el mecanismo de resiliencia Polly ya productivo — sin tocar las altas donde la organización gestiona su propio alias por API. Listo para ticket de Ingeniería/Fintexa (sin PRD formal).

> Fuente: `1_proyectos/asignacion_alias_cvu/proyecto.md` y `decisiones.md`.
