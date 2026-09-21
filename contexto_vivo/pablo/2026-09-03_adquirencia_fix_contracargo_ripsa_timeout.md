---
id: 2026-09-03_adquirencia_fix_contracargo_ripsa_timeout
pm: pablo
fecha_captura: 2026-09-03
fuente: "Reunión Análisis de Riesgo - Fix Contracargo (2026-09-03 16:01), minutas y transcripción Gemini"
producto: adquirencia
tema: fix técnico AD1639 — timeout en contracargos por consulta con ID referencia TX voluminoso (cliente Ripsa)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/portal_cobro_contracargos.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
---

# Fix técnico: contracargo timeout — Ripsa

## Problema y solución técnica (2026-09-03)
Ticket **AD1639**: Cliente Ripsa experimenta timeout al intentar realizar contracargos desde el portal. Análisis técnico reveló que la consulta SQL realiza una búsqueda con un dato muy grande: el campo de **ID referencia TX** que almacena el stream completo del código QR (ID transacción QR + stream QR). Esta voluminosidad causa timeout.

**Solución:** Se optimizó la consulta para evitar búsquedas con ese identificador tan grande, resolviendo el problema de timeout sin afectar otros flujos.

## Decisión de deploy (2026-09-03)
**Acordado:** Desplegar el fix a producción mediante canal habitual (no hotfix improvisado). Pruebas exitosas completadas antes del 3 de septiembre en entorno de staging. Monitoreo post-deploy asignado a Andrea ORSINI.

**Debate resuelto:** Se consideró clasificar como hotfix urgente, pero se determinó que:
- El ticket finalizó el 2 de septiembre, fue probado el 3 de mañana en staging
- Impacto bajo pero frecuente (solo cliente Ripsa, pero puntual)
- Prioridad alta por cliente histórico, pero no crítica como un portal caído
- Deploy en horario laboral (antes de 17:00) sin riesgos asociados

## Detalles técnicos
- **Componente:** Deuda QR / Portal Cobro — contracargos
- **Cambio:** Consulta específica por ID referencia TX (optimizada)
- **Riesgo de colaterales:** Bajo — cambio muy específico, no toca consulta general por ID deuda
- **Clientes afectados:** Ripsa (y eventualmente otros con volumen masivo de contracargos)

## Próximos pasos
[Melisa Belpassi/Fintexa] Coordinar con infraestructura para paso a producción  
[Andrea ORSINI] Realizar pruebas de deuda en producción post-deploy + monitoreo durante pasaje

> Fuente: Reunión "Análisis de Riesgo - Fix Contracargo" (2026-09-03 16:01), minutas y transcripción Gemini
