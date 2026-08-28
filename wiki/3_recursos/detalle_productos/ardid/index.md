# Ardid/Akurtech — Detalle de Producto (Manual Técnico y Catálogo de APIs)

> Módulo de conocimiento detallado del producto Ardid/Akurtech (monitoreo transaccional/antifraude, proveedor Pentass). Contiene todo el conocimiento técnico-operativo del proveedor que **no** es la API pública oficial de Bind PSP.
> Contenido migrado y reorganizado el 2026-07-03 desde `wiki/3_recursos/ardid_manual_tecnico/` hacia esta nueva ubicación (`wiki/3_recursos/detalle_productos/ardid/`), preservando el contenido íntegro de los 9 archivos temáticos + 1 archivo histórico.

## ⚠️ Nota Ardid = Akurtech

El proveedor del producto **rebrandeó el software de "Ardid" a "Akurtech" a partir de la versión 1.18 (mayo 2026)**, confirmado explícitamente por el usuario (2026-07-02) y corroborado por evidencia técnica directa: el token JWT de autenticación de las APIs externas sigue usando `"aud": "Ardid"` como audiencia interna, incluso en la documentación de API más reciente titulada "Documento de Integración de Akurtech" (ver [apis_externas.md](apis_externas.md#6-mecanismo-de-autenticación)). Es el **mismo producto y el mismo proveedor** (Pentass) bajo dos nombres comerciales en distintos momentos — no dos sistemas distintos. Ver la línea de tiempo completa del rebranding en [historico/historial_versiones.md](historico/historial_versiones.md).

En este módulo se usan ambos nombres indistintamente según el nombre que use cada documento fuente específico.

## Documentos de este módulo

| Archivo | Contenido | Fuente original |
|---|---|---|
| [modelo_conceptual.md](modelo_conceptual.md) | Modelo jerárquico de datos (Entidad→Cliente→Reglas), taxonomía de las 5 familias de reglas, glosario de acrónimos (PLAFT, PEP, SO, Error Tipo I/II) | `Manual de Ardid 1.13.pdf` (285 pág., enero 2025 — versión legada pre-rebranding) |
| [configuracion_inicial.md](configuracion_inicial.md) | Login/2FA, Dashboard, Parametrías Generales (16 sub-parámetros), Parametrías de Entidad, Gestión de Usuarios y Perfiles, Parametrías de Seguridad, Dashboards personalizados de Monitoreo | `Akurtech 1 - Parámetros iniciales.pdf` (98 pág.) |
| [modulo_login.md](modulo_login.md) | Reglas Estándar, Reputacionales y Comportamentales aplicadas a intentos de login de clientes finales | `Akurtech 4 - Login.pdf` (31 pág.) |
| [modulo_pagos.md](modulo_pagos.md) | Dashboard de pagos con tarjeta, las 5 familias de reglas (con 4 sub-tipos de Reglas Estándar: cliente/tarjeta/comercio/frecuencia) | `Akurtech 3 - Pagos.pdf` (81 pág.) |
| [modulo_transferencias.md](modulo_transferencias.md) | Dashboard, listado, carga masiva, las 5 familias de reglas (Estándar/IA/Reputacionales/ML/Comportamentales), Acciones Anteriores, Simulaciones, Reglas Interentidades | `Akurtech 2 - Transferencias.pdf` (120 pág.) |
| [scoring.md](scoring.md) | Sistema de puntuación (scoring) compartido entre Transferencias, Pagos y Login — umbrales, acciones por defecto | `Akurtech 7 - Transferencias/Pagos/Login con Scoring.pdf` (12 pág.) |
| [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md) | 9 categorías de Blacklist/Whitelist, carga masiva, Novedades (Worldsys), Ráfagas (Transferencias/Login/Pagos) | `Akurtech 6 - Blacklist - Ráfagas.pdf` (36 pág.) |
| [reporteria_alertas.md](reporteria_alertas.md) | Reportes Operativos (Clientes, Tarjetas, Custom, Comercio), Reporte de Auditoría, Alertas Operativas/PLAFT | `Akurtech 5 - Reportería - Alertas.pdf` (71 pág.) |
| [apis_externas.md](apis_externas.md) | Catálogo completo de 23 grupos de APIs REST (Entity, Product, ClientType, Transfer, Blacklist, Transaction, Authentication, etc.) con requests/responses/códigos de error — catálogo **interno del proveedor**, no la API pública de Bind | `ARDID_Documentacion_ApisExternas_V1.18.1.pdf` (170 pág.) |
| [historico/historial_versiones.md](historico/historial_versiones.md) | Línea de tiempo completa de versiones (1.8 a 1.18.2, junio 2024 a mayo 2026), con evidencia documental del rebranding | 9 informes de cambios/entregas del proveedor |
| [integracion_con_productos_bind.md](integracion_con_productos_bind.md) | **Lado Bind PSP de la integración** (no el manual del proveedor): cómo Wallet/Botón Simple/Centralizador/SurFin consumen Ardid — transferencias salientes/entrantes con 2FA, patrón de fallback "esquivar Ardid" ante error 500 o cliente inexistente, bug crítico de reglas restrictivas bypaseadas, sincronización de alta de cuentas/segmentos, integración de Bóveda, gap de producto abierto (datos de localización/dispositivo pedidos desde 2024, nunca desarrollados ni para Wallet ni para Botón Simple), y extensión del control antifraude al canal de **Pago QR** de Wallet (§7, IDEA Jira PRD-115, Finalizada 2026-04). Ingesta de 6 Epics históricas de Notion + 1 IDEA de Jira. | Notion histórico + Jira `bindpsp.atlassian.net` (PRD-115) |

## Relación con otros documentos de la wiki

- **[wiki/0_direccion/producto/ardid_overview.md](../../../2_areas/overview_productos/overview_ardid.md)** — overview funcional/de negocio de Ardid, mantenido directamente por el usuario. Este módulo lo profundiza a nivel de manual técnico operativo y catálogo completo de APIs. *(Solo lectura desde este módulo — no se edita acá.)*
- **API pública oficial de Bind PSP** (`<producto>/apis_expuestas/` de cada producto, portal `psp.bind.com.ar/developers`) — Ardid/Akurtech **no tiene API pública propia en ese portal**: su integración es directa proveedor↔entidad (Pentass↔Bind PSP u otra entidad integradora), documentada acá en [apis_externas.md](apis_externas.md). Ambos módulos son independientes y no deben mezclarse.
- [producto/adquirencia_overview.md](../../../2_areas/overview_productos/overview_adquirencia.md) y [producto/wallet_overview.md](../../../2_areas/overview_productos/overview_wallet.md) — ambos productos están integrados con Ardid para el análisis antifraude de transacciones.
- [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md) — preguntas abiertas y contradicciones detectadas en las fuentes de este módulo (umbrales de scoring inconsistentes entre Login y Transferencias/Pagos, "Modo de creación de cuenta" sin detallar, atribución de MongoDB, etc.).

## Cobertura y método de extracción

Los 19 PDFs fuente suman ~930 páginas. La extracción de texto (vía `pypdf`) y la estructuración de cada documento grande se delegó a agentes de investigación en paralelo (2026-07-02), cada uno con instrucciones explícitas de **no inventar información ausente** y marcar como `[fragmento poco claro en la fuente]` cualquier contenido ambiguo o cortado por ruido de extracción de PDF. Los 9 changelogs/informes de versión (cortos) se leyeron directamente.

---
*Última actualización: 2026-08-27 — `/context_merge`: `integracion_con_productos_bind.md` suma §6.1 (tarea abierta de mapeo de motivos de rechazo hacia Onboarding, reunión "Producto" 2026-08-18) y §14 (discovery de robustez, continuación de §13: especificación global de habilitación, rechazo por caída de Ardid, y diseño de state monitor — reunión "Revisión Wallet - BIND", 2026-08-21, marcado explícitamente como no construido). `modulo_pagos.md` suma §14 (identificación real de tarjetas por hash de 16 dígitos completos, reunión "ARDID" 2026-08-24; bloqueo permanente de tarjeta por hash ligado al primer vencimiento cargado y mejora pedida de auditoría en TRX, reunión "Previa demo mayoristas" 2026-08-26).*
*Última actualización anterior: 2026-08-05 — `/sync_meetings`: `integracion_con_productos_bind.md` suma §12 (bug de alta de organización — API Product no registra tipo/categoría/producto, postergado a v72, workaround manual coordinado con el grupo de integraciones). Ver reunión "Análisis de riesgos - W 71.6" del 2026-08-05 en `wiki/5_control/log_reuniones.md`.*
*Última actualización anterior: 2026-07-30 — `/sync_meetings`: `integracion_con_productos_bind.md` suma §2.1 (intención de extender el monitoreo transaccional de Ardid al canal Post/POS, hoy limitado a Botón Simple). Ver reunión "Análisis COBRO" del 2026-07-30 en `wiki/5_control/log_reuniones.md`.*
*Última actualización anterior: 2026-07-17 — `/sync_meetings`: `integracion_con_productos_bind.md` ampliado con §11 (incidente de reinicio de límites diarios 2-3 julio, hotfix de reintentos de Pentass, causa raíz de performance aún abierta).*
*Última actualización anterior: 2026-07-13 — `/sync_releases` backfill vía XML: espacio ARD COMPLETO (4 tickets, 3 versiones). `integracion_con_productos_bind.md` ampliado con §8 (incidente 403 de disponibilidad), §9 (hotfix reglas transferencias entrantes) y §10 (línea de tiempo de versiones Jira).*
