# Datos — Índice

> Fusión de lo que antes eran `2_areas/control/` (stores acumulados de las skills de sync) y `2_areas/datasets/` (fichas de datasets ad-hoc). Consulta puntual — no es contexto de overview, por eso vive en `3_recursos/` y no en `2_areas/`. **Canon compartido: solo lo escribe `/context_merge`.** Excepción de mecánica: los stores de esta carpeta se aplican por **copia byte a byte** desde items `tipo: dato` de `contexto_vivo/`, sin criterio editorial — ver `CLAUDE.md`.
>
> Responsabilidad continua: mantener un registro de extracciones de datos crudos (CSV/exports de base) que un PM deja en `raw/` para análisis puntual, pero que vale la pena conservar para reutilizar en futuras ideas de producto — no solo la que motivó la extracción original.

## ⚠️ Regla dura: los archivos crudos NUNCA se suben a GitHub

Los datasets crudos que se registran acá con frecuencia contienen **PII real de clientes** (nombre, apellido, email, CUIT/CUIL, DNI, fecha de nacimiento, IPs) sin cifrar o parcialmente cifrado — subir eso a un repositorio remoto es una exposición de datos inaceptable.

**Protocolo:**
1. Los archivos crudos (`.csv`, `.xlsx`, exports de base) viven en `datasets_locales/` (raíz del repo), declarado en `.gitignore` — nunca se commitean, nunca se pushean.
2. Lo que SÍ se guarda acá (y se sube a GitHub vía el core compartido) son los **hallazgos agregados**: conteos, porcentajes, distribuciones, patrones — nunca filas individuales, nunca PII, nunca IPs ni identificadores de clientes puntuales.
3. Cada dataset registrado abajo tiene una ficha con su ubicación local, rango de fechas, columnas relevantes (sin datos reales) y qué tan sensibles son sus campos.

## Stores acumulados de las skills de sync

Nunca se releen los CSV/Excel históricos — cada skill mergea contra su store y lo deja actualizado. Alimentados por las skills de fuente compartida (correlas solo el runner designado; salida vía `contexto_vivo/` como item `tipo: dato`, aplicado por copia en el merge — ver `CLAUDE.md`).

| Store | Alimentado por | Contenido | Archivo |
|---|---|---|---|
| Store de métricas semanales (CSV) | `/sync_metrics` | Los 5 datasets de hechos (operaciones, transacciones, cuentas, comercios, transferencias del Agente de Cobros y Pagos) + dimensiones + control de semanas. Agregados puros, sin una sola fila de PII. | [`datos_metricas_semanales/`](datos_metricas_semanales/index.md) |
| Auditoría de corridas de métricas | `/sync_metrics` | Una fila por corrida: archivos, semanas, filas ingeridas. | [`log_metricas_semanales.md`](log_metricas_semanales.md) |
| Performance de desarrollo | `/dashboard_delivery` | Tabla año × mes × espacio × tipo × epic (tickets/SP publicados). | [`log_performance_desarrollo.md`](log_performance_desarrollo.md) |
| Costos de desarrollo | `/dashboard_delivery` | Tabla año × mes × espacio (horas/USD) + tarifas por perfil con origen. | [`log_costos_desarrollo.md`](log_costos_desarrollo.md) |
| SLA de tickets Highest | `/dashboard_delivery` | Tiempo de resolución de urgencias. | [`log_sla_highest.md`](log_sla_highest.md) |
| Performance de QA | `/dashboard_qa` | Una fila por ticket (upsert por Clave): tiempo por estado del workflow. | [`log_performance_qa.md`](log_performance_qa.md) |
| Versiones publicadas | `/sync_releases` | Una fila por versión: Espacio, releaseDate, tickets ingestados. | [`log_versiones_publicadas.md`](log_versiones_publicadas.md) |
| Changelog de releases | `/sync_releases` | Una entrada por versión, redactada como PM. | [`changelog_releases.md`](changelog_releases.md) |
| Calibración de iniciativas | `/context_merge`, al cerrar una IDEA | SP estimado vs. real por IDEA finalizada + trazabilidad a dónde quedó su conocimiento. Distinto de la cartera viva en `2_areas/direccion/iniciativas.md`. | [`log_iniciativas_producto.md`](log_iniciativas_producto.md) |

## Reporte de métricas (agregado, sin PII)

| Qué | Descripción | Archivo |
|---|---|---|
| **Reporte semanal de las NSM** | Estado de las dos North Star Metrics semana a semana + hallazgos + anexo de soporte. Incremental: la semana nueva se antepone, el histórico se conserva. Lo genera [`/sync_metrics`](../../../.claude/skills/sync_metrics/SKILL.md). | [`metricas_semanales.md`](metricas_semanales.md) |

## Datasets ad-hoc disponibles

| Dataset | Ubicación local (git-ignored) | Rango de fechas | Sensibilidad | Ficha / hallazgos |
|---|---|---|---|---|
| Solicitudes de Onboarding | `datasets_locales/solicitudes desde mayo.csv` (38.152 filas, ~123 columnas) | Desde 2026-05-01 (inclusive) | Media — campos de identidad cifrados en origen; `Ip`, `IdOrganizacion`, `Estado`, `TipoSolicitud`, `ExternalRefid` en texto plano | [`ficha_solicitudes_onboarding.md`](ficha_solicitudes_onboarding.md) |
| Cuentas de Wallet | `datasets_locales/cuentas wallet desde mayo.csv` (304.356 filas, 25 columnas) | Desde 2026-05-01 (inclusive) | **Alta — PII real sin cifrar**: Nombre, Apellido, Email, CuitCuil, DNI, FechaNacimiento, Celular en texto plano | [`ficha_cuentas_wallet.md`](ficha_cuentas_wallet.md) |

## Referencias (metadata de negocio, no PII)

| Referencia | Descripción | Archivo |
|---|---|---|
| Organizaciones de Wallet | Tabla Id → Nombre de las organizaciones activas/históricas de Wallet | [`organizaciones_wallet.md`](organizaciones_wallet.md) |
| Estados de solicitud de Onboarding | Legend de los 8 códigos numéricos del campo `Estado` | ver [`ficha_solicitudes_onboarding.md`](ficha_solicitudes_onboarding.md) |
| Motivos de rechazo de Onboarding | Legend de los 33 códigos del campo `MotivoRechazo` | [`motivos_rechazo_onboarding.md`](motivos_rechazo_onboarding.md) |

## Hallazgos derivados (análisis puntuales, reutilizables entre proyectos)

| Fecha | Hallazgo | Motivado por | Archivo |
|---|---|---|---|
| 2026-07-16 | Cruce Onboarding × Wallet (cobertura real, dominancia de organizaciones, segmentación persona física/jurídica y edad, calidad de datos) | [PRD-202](../../1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/proyecto.md) | [`hallazgos_2026-07-16_onboarding_vs_wallet.md`](hallazgos_2026-07-16_onboarding_vs_wallet.md) |
| 2026-07-20 | Volumen de La Virginia sobre el total de cuentas (0,07%) y sobre su propio total (98,2% PF, ~97% con Onboarding aprobado) | [riesgos_y_decisiones_onboarding.md §6](../../1_proyectos/proyecto-onboarding-estrategico/artefactos/riesgos_y_decisiones_onboarding.md#6-front-ob-de-la-virginia--tc-de-cuenta-comitente) | [`hallazgos_2026-07-20_volumen_la_virginia.md`](hallazgos_2026-07-20_volumen_la_virginia.md) |
| 2026-08-06 | Volumen operado por La Virginia en Wallet (crecimiento ~30x en 1 año, ~$460M/semana) y en Cobro/Adquirencia (~$9,1M/semana) + interpolación de referencia para el stock de 2.000 PJ pendientes | [proyecto-la-virginia-ob-pj](../../1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md) | [`hallazgos_2026-08-06_volumen_operado_la_virginia.md`](hallazgos_2026-08-06_volumen_operado_la_virginia.md) |

---
*Última actualización: 2026-08-15 — Fusión de `2_areas/control/` (9 stores/logs) y `2_areas/datasets/` en esta carpeta, dentro del pipeline de sincronización multi-PM.*
