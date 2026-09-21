---
id: 2026-09-16_wallet_estado_epicasepocas_reformulacion_w73
pm: pablo
fecha_captura: 2026-09-16
fuente: "Email informe Nicolas Pomponio (11/09) + decisión Matias Alzogaray (3/09)"
producto: wallet
tema: roadmap, scope, épicas, reformulación W73
tipo: decision
destino_propuesto: wiki/2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: f230716c54a5ca6600a2bce4e46bf0292d56a58c
---

# Estado Wallet — Épicas y Reformulación W 73 (al 11/09)

**Fuente:** Informe semanal Nicolas Pomponio (PM Fintexa), validado por Matias Alzogaray (PM BIND)

## Hitos completados

- **W 72.2 → PROD:** 07/09/2026, 8 AM (3 fixes: Coelsa, Cta Corriente/Movimiento, Alias)
- **W 72.3 (Pagos FX MVP2):** Entregado a QA Ext. el 07/09, **Despliegue PROD confirmado para 17/09**

## Épica 1: FCI (Fondos Comunes de Inversión)

**Status:** 🟢 En curso  
**PROD MVP2 estimado:** Fines de agosto (sin cambios)

### Decisión de scope

**Removida de W 73** por baja prioridad de negocio. Se postergó QA y entrega a QA Ext.
- 2 observaciones de STG → pasan a **W 74**
- No hay problemas productivos

### Alertas/Controles

- Monitoreo diario: Coppel, La Virginia (PROD) + Hipódromo de Palermo (nuevo)

---

## Épica 2: Mastercard Move (Pagos Cross-Border)

**Status:** 🟢 En curso, MVP1 activo en PROD  
**PROD MVP2 estimado:** 17/11/2026

### PRD Statusactual

**QA Ext. en STG:**
- Todos los casos PVT funcionando bien
- 3 casos pendientes feedback Mastercard:
  - Canada Bank Account CAD P2P (bug Mastercard)
  - Switzerland IBAN CHF P2P (IBAN inválido)
  - Switzerland IBAN CHF B2P (IBAN inválido)

### Nuevos hallazgos

- **DEM-1974 detectado:** Falta ruteo de MS FileManager + CalculadorCostos para PROD
- **Futura solicitud (pospuesta):** Colombia 4 tipos pagos — solicitan teléfono del sender en endpoint guide (debe ser calculado por Wallet)

---

## Reformulación W 73 — Scope Final (Entrega QA: 21/09)

**Contexto:** Necesidad de incluir desarrollo GetNet sin correr fecha fin de mes.

### Opciones evaluadas
1. **Adoptada:** Reformular W73 cortando scope
2. **Descartada:** Estirar GetNet
3. **Descartada:** Dejar igual y patear todo

### Qué entra en W 73

- **Onboarding** (PRIORIDAD PRINCIPAL): Persistencia de ID solicitud en KYC + nuevo endpoint búsqueda por solicitud
- **Ardid:** Mapeo motivo rechazo, habilitación global operaciones, rechazo al caer Ardid, deshabilitación automática cuentas bloqueadas
- **GetNet:** Autenticación configurable aceptador (OAuth + esquema actual), resolución QR, gestión aceptadores
- **Mejoras técnicas:** Migración parcial Colas Quorum, Sentinel, GracefulShutdown, revisión exposición datos sensibles en logs

### Qué sale de W 73 → W 74

- Ardid State Monitor (bajo análisis, no bloquea resto)
- FCI (sin urgencia negocio)
- Resto Colas Quorum fuera de ventana

### ⚠️ Riesgo detectado

**Ardid sin State Monitor (si está caído, rechaza transacciones):**
- Impacto funcional: puede rechazar transacciones legítimas
- **Acción:** Avisar a Soporte con anticipación + análisis de riesgo antes de habilitar

---

## Cronograma confirmado

- **QA Ext. delivery:** 21/09 (lunes)
- **Nota:** QA probablemente en paralelo para algunos desarrollos, dada lo ajustado del cronograma

---

**Dueños:** Nicolas Pomponio (Fintexa/Dev), Matias Alzogaray (BIND/PM), Pablo Gomes (BIND/PM)
