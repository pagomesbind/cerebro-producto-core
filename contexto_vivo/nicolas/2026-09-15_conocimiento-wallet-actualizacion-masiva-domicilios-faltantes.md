---
id: 2026-09-15_conocimiento-wallet-actualizacion-masiva-domicilios-faltantes
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Mail 'Análisis de riesgo - Obtencion de domicilios Wallet' — Matías Alzogaray (2026-09-14)"
producto: wallet
tema: Actualización masiva en base de datos para regularizar domicilios faltantes en cuentas Wallet
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md
tipo_destino: actualizar
contradice: "no — es avance/resolución sobre el gap normativo ya documentado en organizaciones_y_configuracion.md §0 (CPA no se completa en el 72% de cuentas con domicilio)"
confianza: alta
estado: en_cola
---

Matías Alzogaray (PM, Bind) compartió la minuta de un "Análisis de riesgo" sobre una actualización masiva planificada en la base de datos de Wallet para cargar domicilios faltantes en cuentas — directamente relacionado al gap normativo ya documentado en `organizaciones_y_configuracion.md §0` (CPA no se completa en el 72% de cuentas con domicilio).

**Alcance:**
- Objetivo: actualización y carga de domicilios faltantes en cuentas de Wallet.
- Volumen afectado: 491.495 cuentas.

**Controles operativos y mitigación de impacto:**
- Ejecución controlada por lotes (batches) de 10.000 registros, con delay de seguridad de 2 a 5 segundos entre cada envío.
- Impacto acotado a la base de datos de Cuentas (WalletCuentaDB), que hoy tiene holgura de recursos — se descartan riesgos de rendimiento durante la ventana.
- Ejecución y autorización técnica documentadas bajo un ticket de soporte (trazabilidad/auditoría).

**Datos de despliegue:**
- Ambiente: Producción. Prioridad/Impacto: Media. Urgencia: Media. Vertical: Emisión (Wallet Service).
- Hora: 07:00 hs. Duración estimada: 40-60 minutos.
- APIs/MS afectados: Wallet Service (WalletCuentaDB).
- Plan de rollback: Point-in-Time Restore (PITR) de Azure SQL Database + scripts de inserción idempotentes y reanudables (patrón staging).
- Alcance real del impacto: cualquier API/MS que lea las tablas Cuentas y CuentasDomicilios podría sufrir intermitencias — el RCSI evita bloqueos clásicos lector/escritor pero hay competencia por I/O y por el version store de tempdb; el crecimiento del log de transacciones generará eventos de autogrow de 16MB (pausas breves del motor de base de datos).

Sin pregunta directa a Nicolás Colón en el mail — se captura como conocimiento de contexto/mitigación de riesgo del despliegue, sin tarea de Producto asociada.
