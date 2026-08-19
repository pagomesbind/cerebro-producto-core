---
id: 2026-08-18_onboarding_prd202_refinamiento_wallet
pm: pablo
fecha_captura: 2026-08-18
fuente: "Ingesta manual de transcripción cruda — reunión 'Revisión Wallet - BIND' (2026-08-18), depositada en raw/ por el usuario"
producto: onboarding
tema: PRD-202 — refinamiento técnico Wallet+Onboarding, contrato de API validado de cara a las historias de usuario
tipo: iniciativa
proyecto: PRD-202
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Sesión de refinamiento técnico entre el equipo de Wallet (Juan Pablo Carubelli, Keep IT Simple) y el equipo de Onboarding (Cristian Bonafede, Tecfinanciera/Fintexa), con el PM (Pablo Gomes), explícitamente orientada a dar claridad de cómo bajar PRD-202 a historias de usuario. Se repasó endpoint por endpoint y caso por caso el contrato de API ya diseñado en `flujos_consolidado_tecnico.md`.

**Confirmado con ambos equipos técnicos:**
- Contrato de 4 endpoints de cara al cliente: crear solicitud + `GET` estado liviano (los prioritarios), `PATCH` de actualización de solicitud abierta y `GET` completo de pasamanos a Onboarding (ambos no prioritarios para el camino de creación en una sola vez).
- `externalRefId`/`codigo` de la organización pasa a ser **obligatorio**, con control de unicidad exclusivo de Wallet (no se permite una solicitud nueva con el mismo código mientras haya una viva o aprobada; se libera en `RECHAZADA`/`VENCIDA`).
- Caso DNI ilegible resuelto: en vez de rechazar y crear una solicitud nueva (comportamiento actual), la solicitud pasa a `EN_ESPERA` pidiendo de nuevo las imágenes, y se retoma con el mismo `codigo` — evita duplicar solicitudes cuando falla la lectura del documento.
- Reafirmado con ejemplos concretos: Wallet valida solo estructura/formato de dato, nunca reglas de negocio de qué es obligatorio según el flujo de la entidad (eso es exclusivo de Onboarding).
- Wallet confirmado que no debe persistir información personal del titular — solo lo necesario para gestionar el estado de la solicitud.

**2 tensiones de diseño quedaron sin cerrar entre el PM y Cristian Bonafede** (no bloquean el arranque del alcance genérico, pendientes de sesión aparte): (1) orden de validación de evidencia — paso a paso (propuesta del PM, necesaria para el caso "por partes") vs. anticipada al principio (propuesta de Onboarding, más eficiente en costo, apoyada también por Martin Hovanyecz); (2) cómo resolver el caso de onboarding fraccionado de Arcos Dorados — mecanismo genérico `EN_ESPERA`/`CAMPO_FALTANTE` reutilizado (PM) vs. endpoint dedicado (Onboarding).

**Cierre:** Wallet ya tiene lo necesario (firma de API) para avanzar en la capa de comunicación cliente↔Wallet; el microservicio KYC-wrapper hacia Onboarding arranca cuando Cristian tenga concreta su firma del lado de Onboarding. El PM va a empezar a crear los tickets en Jira con lo ya validado.

Detalle completo en [`wiki/1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/proyecto.md`](../proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/proyecto.md) §5/§6/§7/§8, `gaps.md` y `decisiones.md` del mismo PRD (ya actualizados directo, por ser trabajo de proyecto).
