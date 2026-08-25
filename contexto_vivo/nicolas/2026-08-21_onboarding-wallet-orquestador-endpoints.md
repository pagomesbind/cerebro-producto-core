---
id: 2026-08-21_onboarding-wallet-orquestador-endpoints
pm: nicolas
fecha_captura: 2026-08-21
fuente: "Reunión \"Producto\" (2026-08-18), minuta Gemini"
producto: onboarding
tema: Wallet como orquestador de Onboarding — prioridad de casos y endpoints propuestos
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

En la reunión "Producto" (Luciana Rudaz, Pablo Gomes, Emma Vignoles, Nicolás Colón — 2026-08-18) se precisó la arquitectura objetivo de la integración Onboarding↔Wallet:

- **División de responsabilidades**: Onboarding valida la información (personas y documentos); Wallet mantiene la responsabilidad de crear la cuenta y actúa como orquestador que invoca a Onboarding para acciones específicas — pensado para escalar a productos futuros (ej. cuentas comitentes).
- **Prioridad de casos de uso**: personas físicas primero, luego personas jurídicas, y por último menores. El manejo de comercios queda para una etapa posterior, priorizando una base robusta del alta de cuentas antes de expandir alcance.
- **Casos existentes/legados** (ej. Tin y ciertos comercios bajo el modelo antiguo) se mantienen operando como están — el desarrollo nuevo no busca migrarlos, para poder concentrarse en los procesos nuevos.
- **Tres escenarios operativos**: sin onboarding, con onboarding propio, y configuraciones combinadas donde el sistema debe poder identificar datos faltantes (ej. una selfie) y permitir al usuario completar el proceso en etapas.
- **Endpoints propuestos**: cuatro endpoints para gestionar creación y actualización de solicitudes de onboarding. Pablo Gomes buscaba convencer a Cristian (proveedor) de permitir que procesos en espera se completen vía PATCH en lugar de requerir reinicios completos del flujo.
- **Riesgo de arquitectura señalado en la propia reunión**: preocupación por terminar con una arquitectura difícil de mantener ("Frankenstein") al tener servicios separados para clientes que usan el onboarding interno vs. los que usan uno propio. Se reconoce la dificultad pero se decide avanzar igual con esta implementación como punto de partida.

> Fuente: Reunión "Producto" (2026-08-18), minuta Gemini.
