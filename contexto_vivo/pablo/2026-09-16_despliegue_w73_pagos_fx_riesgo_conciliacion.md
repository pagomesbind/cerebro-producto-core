---
id: 2026-09-16_despliegue_w73_pagos_fx_riesgo_conciliacion
pm: pablo
fecha_captura: 2026-09-16
fuente: "Email minuta reunión Matias Alzogaray (11/09)"
producto: transversal
tema: despliegue W72.3 Pagos FX — riesgo de conciliación de transferencias
tipo: decision
destino_propuesto: wiki/2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

# Despliegue W 72.3 (Pagos FX) — 17/09/2026 7:00 AM

**Decisión:** Proceder con despliegue a producción de Pagos FX MVP 2 y actualización de proxys, **con plan de contingencias y alertas críticas documentadas**.

## Detalles técnicos

- **Ambiente:** Producción
- **Fecha/Hora:** Jueves 17/09, 7:00 AM (proxy), 8:00 AM (Wallet+Ingress)
- **Duración estimada:** 1 hora (15 min monitoreo adicional de proxy)
- **APIs afectadas:** 
  - `Wallet.CrossBorderRouting`
  - `Shared.MastercardCrossBorder`
  - `Shared.FileManager`
  - Tráfico Ingress

## Decisiones de scope

- **Calculador de costos:** Explícitamente EXCLUIDO de este pasaje a producción
- **Tickets en versión:** 11 tickets, prioridad Medium; 2 con impacto alto (DEM-891/593: cambio de comportamiento fundamental)

## ⚠️ Alerta crítica detectada en reunión

**Herramienta de conciliación de transferencias actualmente INOPERATIVA:**
- Riesgo: No registrar transferencias entrantes + no acreditar saldos si Ingress sufre intermitencias durante despliegue
- Responsable escalado: Nico Colón → MDA-298450 (conciliación Wallet PROD)
- Owner de resolución: Gonzalo Damian RIVERA (deadline 17/09)

## Plan de rollback

- **Proxys:** Revertir a versión anterior (sin cambio de lógica)
- **Wallet:** Revertir commit específico o imagen en AKS vía `kubectl set image`
- **Contingencia de Ingress:** Rollback por reinicio previo

## Action items (de minuta 11/09)

| Acción | Owner | Deadline | Prioridad |
|--------|-------|----------|-----------|
| Escalado MDA error conciliación | Maria Eugenia VILA | 11/09 | Alta |
| Resolver conciliación transferencias | Gonzalo Rivera | 17/09 | Alta |
| Bloquear comprobantes reservados (Coppel) | [DEFINIR] | 17/09 | Alta |
| Notificar clientes ventana maintenance | Gonzalo Rivera | Antes 17/09 | Media |
| Monitorear Ingress/Egress durante reinicio | Juan Pablo Carubelli / Daniel Zalazar | 17/09 | Alta |
| Reportar bloqueos onboarding testing | Equipo despliegue | 17/09 | Alta |

## Asistentes & Aprobación

Reunión: 11/09/2026, 12:00-13:00 GMT-3  
Aprobado por: Andrea ORSINI, Matias Alzogaray, Gonzalo Rivera, Pablo Gomes, Nicolás Colón (sin ausencias registradas)

---

**Impacto:** Despliegue permite avance en cross-border pero requiere seguimiento cerrado de la conciliación para evitar pérdida de transacciones.
