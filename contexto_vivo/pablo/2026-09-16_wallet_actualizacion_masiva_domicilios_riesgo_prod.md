---
id: 2026-09-16_wallet_actualizacion_masiva_domicilios_riesgo_prod
pm: pablo
fecha_captura: 2026-09-16
fuente: "Minuta Matias Alzogaray (15/09) — Análisis de riesgo Obtención domicilios Wallet"
producto: wallet
tema: despliegue producción, riesgos de datos, actualización masiva domicilios
tipo: decision
destino_propuesto: wiki/2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

# Actualización Masiva DB Domicilios Wallet — 15/09 Análisis de Riesgo

**Tipo de operación:** Actualización masiva de base de datos en producción para regularizar domicilios faltantes

## Objetivo

Carga de domicilios faltantes en cuentas Wallet + actualización masiva de 491.495 registros

## Despliegue operativo

- **Ambiente:** Producción
- **Prioridad/Impacto:** Media
- **Hora:** 07:00 AM
- **Duración estimada:** 40-60 minutos
- **API/MS afectada:** Wallet Service (DB: `WalletCuentaDB`)

## Mitigación de impacto — ejecución controlada

- **Batching:** Lotes de 10.000 registros máximo
- **Delays de seguridad:** 2-5 segundos entre cada envío para evitar saturación
- **Disponibilidad:** Impacto limitado a DB Cuentas (con holgura de recursos)

## ⚠️ Riesgos identificados

### I/O y recursos de BD

- **Competencia por recursos I/O:** Otras APIs/MS que lean tablas Cuentas/CuentasDomicilios pueden experimentar intermitencias
- **RCSI mitigation:** Versionado de filas evita bloqueos clásicos, pero hay competencia por resources + version store en tempdb
- **Autogrow log:** Múltiples eventos de autogrow (16 MB) → pausas breves en motor BD

### Control y trazabilidad

- Ejecución + autorización técnica documentadas en ticket de soporte
- Scripts idempotentes y reanudables

## Plan de rollback

1. **Point-in-Time Restore (PITR)** disponible en Azure SQL Database
2. **Scripts staging idempotentes** para reintentos sin duplicados

---

**Estado:** Despliegue aprobado con controles mitigantes.  
**Owner:** Matias Alzogaray (BIND PM), equipo infraestructura Fintexa
