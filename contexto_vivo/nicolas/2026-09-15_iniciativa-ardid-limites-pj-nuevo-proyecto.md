---
id: 2026-09-15_iniciativa-ardid-limites-pj-nuevo-proyecto
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Discovery propio /idea_start (2026-09-11 al 15)"
producto: ardid
tema: Proyecto nuevo — segmentación de personas jurídicas en Ardid (reglas de montos), discovery cerrado
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: ardid_limites_pj
---

Proyecto nuevo (sin IDEA de Jira todavía) — discovery cerrado en Gate 3 vía `/idea_start`: el negocio le trasladó a Producto que las cuentas de Wallet de organizaciones cuyos usuarios finales son mayoritariamente personas jurídicas quedan sujetas a las mismas reglas de montos de Ardid que las personas físicas, sin ningún mecanismo automático hoy para tratarlas distinto.

**Solución adoptada:** identificación automática de PJ por validación algorítmica del CUIT (server-side, prefijos 30/33/34) en el alta de cuenta de Wallet, con asignación automática a un segmento distinto en Ardid vía `ClientBankType` — mismo mecanismo técnico ya construido en PRD-17 (segmentación de menores de edad). Alcance acotado a reglas Estándar/`ClientBankType` (fuera scoring/Reputacionales) y sin migrar las 3.740 cuentas PJ ya existentes (queda a mano, fuera de este desarrollo).

**Deslinde relevante:** el discovery detectó y descartó una posible superposición con la directiva del directorio sobre límites operativos bajos para cuentas de PJ sin documentación (T-041/T-042, frente de Pablo Gomes, iniciativa `onboarding_shared_kyc_worsis`) — el PM confirmó que aplican a poblaciones distintas (Organizaciones sin onboarding completo vs. cuentas PJ ya dadas de alta vía Onboarding con documentación), sin conflicto de política.

**Estado:** Gates 1-3 cerrados, sin gaps bloqueantes. Los 2 gaps técnicos iniciales se resolvieron por criterio del PM (mismo día): identificación de PJ/PF por primer dígito del CUIT ("2"→PF, "3"→PJ, con excepción a revisión manual fuera de esos dígitos — más robusto que enumerar prefijos de 2 dígitos) y el mecanismo `ClientBankType` de PRD-17 dado por reutilizable tal cual. Próximo paso: aprobación de Emma Vignoles, después confirmación técnica puntual (no de diseño) con Ingeniería/Fintexa. Compite por capacidad con las otras 3 iniciativas vivas del foco Ardid del mismo PM (`ardid_desconocimientos`, `titularidad_tarjeta`, PRD-191).

> Fuente: `wiki/1_proyectos/ardid_limites_pj/proyecto.md`, discovery `/idea_start` 2026-09-11 al 15.
