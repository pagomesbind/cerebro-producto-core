---
id: 2026-09-25_ardid_conocimiento_despliegue_v1190_nuevas_reglas_fraude
pm: pablo
fecha_captura: 2026-09-25
fuente: "/sync_meetings — reunión \"Análisis de riesgo - Ardid V 1.19.0\" (2026-09-25 16:01, compartida por malzogaray), minuta Gemini"
producto: ardid
tema: Cronograma de despliegue en staging de Ardid v1.19.0 (no v1.19.1) + nuevas reglas de fraude incorporadas + confirmación de compatibilidad de integraciones
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/despliegues_y_operacion.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/ardid/historico/historial_versiones.md — el roadmap documentado el 2026-09-21 decía 1.19 (sin fix UTC 0) → 1.19.1 (fix UTC 0, sin fecha) → 1.20; esta reunión confirma que el despliegue de staging es sobre 1.19.0 puntual, no 1.19.1 ('Se estuvo hablando de 1191, pero al final no. Solamente nos vamos a estar dedicando a la 1190'). No se aclaró si 1.19.1 se salteó definitivamente o queda pendiente para después — no hay dato suficiente para resolverlo, solo para anotar la confirmación de qué versión se despliega ahora."
confianza: alta
estado: ingestado
merge_commit: 9fbee64
---

**Contexto:** reunión de análisis de riesgo pre-despliegue de Fintexa/Pentass (Matías Alzogaray como moderador; participan Daniel Zalazar, Osmel Mata, Luis y Santiago Fernandez por Pentass/Fintexa, y por Bind PSP Andrea Orsini, Pablo Serra, Gonzalo Rivera, Mariana Nadalin, Nicolás Colón, Pablo Gomes). Formato estándar: se revisa documentación + ticket de infraestructura y se define fecha/horario/nivel de riesgo antes de autorizar el pase.

**Decisiones de cronograma (staging, no producción):**
- **Wallet:** lunes 28/09, 9:00–11:00 hs.
- **Ardid v1.19.0:** martes 29/09, 8:00–10:00 hs (separado del de Wallet a pedido de Andrea Orsini, para no pisar las regresiones y no bloquear en paralelo la ventana de pruebas de Nico Pomponio sobre Wallet).
- Ambos se comunican a clientes como posible intermitencia en el ambiente de staging (no hay impacto de cliente real, es ambiente de pruebas).
- **Aparte, de forma tangencial:** un hotfix de producción (sin identificar cuál, no ligado explícitamente a ningún PRD en la minuta) se reprograma de hoy (25/09) al **lunes 28/09 a la mañana**, para reducir el impacto en horario de alta transaccionalidad — mencionado por Daniel Zalazar al arranque de la reunión, confirmado por Hernán Clarich/Mariana Nadalin al cierre.

**Alcance técnico de la v1.19.0:**
- APIs/microservicios afectados: Transfer API Gateway, SQL Server, MongoDB.
- Se crean 4 índices nuevos en las colecciones `transaction` y `transfer` de MongoDB — posible intermitencia/lentitud temporal en pantallas principales, dashboard, pagos y transferencias mientras se actualizan imágenes Docker y corre el actualizador de base de datos.
- El componente Transfer Service se reinicia por la inyección de una nueva variable de entorno.
- **Nuevas reglas de fraude incorporadas en esta versión:** ráfagas de pago, IP, geolocalización y dominios reputacionales — con posibles comportamientos anómalos o rechazos temporales mientras entran en vigencia (no se detalló más mecánica que esta mención; posible input para ampliar `blacklist_whitelist_rafagas.md` cuando haya documentación del proveedor).
- **Plan de rollback:** scripts de reversión en carpeta `rollbacks`, restauración de copias de respaldo previas de archivos y Docker Compose, y comandos `Drops Index` para deshacer los índices nuevos si hay falla de rendimiento.
- **Lección aprendida citada por Osmel Mata:** en el despliegue anterior de la 1.18.2 en producción, la recreación de índices de MongoDB tardó "varias horas", a diferencia de staging — a tener en cuenta para el futuro pase a producción de la 1.19.0.
- Se realizan backups de SQL y MongoDB al momento del despliegue; monitoreo a cargo del equipo de Fintech + DBA (Juan).

**Compatibilidad de integraciones confirmada:** Pablo Serra preguntó explícitamente si había cambios de firma o de endpoints usados por las integraciones de Botón Simple y Wallet. Luis (Pentass) confirmó, tras consultar con la líder de desarrollo (Lorena), que **no hubo cambios en los endpoints consumidos por Ardid** en este ciclo — dato que sostiene la clasificación de riesgo.

**Riesgo asignado:** **amarillo** — por el impacto potencial en el transaccionamiento (no por cambios de integración, que se descartaron).

**Precedente citado (no nuevo, pero relevante para `despliegues_y_operacion.md`):** para producción, el impacto se mitiga solicitando la desconexión de Coto durante su ventana de mantenimiento (22:00–08:00) — mismo patrón ya documentado en el caso AD-1374.

> Fuente: minuta Gemini de la reunión "Análisis de riesgo - Ardid V 1.19.0" (2026-09-25, 16:01), compartida por malzogaray@bind.com.ar.
