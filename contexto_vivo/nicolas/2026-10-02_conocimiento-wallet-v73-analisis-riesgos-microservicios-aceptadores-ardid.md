---
id: 2026-10-02_conocimiento-wallet-v73-analisis-riesgos-microservicios-aceptadores-ardid
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Reunión \"W 73 - Análisis de riesgos\" (2026-10-01), solo resumen del mail de Gemini (Drive invalidado, sin minuta completa)"
producto: wallet
tema: Análisis de riesgo del pase de Wallet V73 — 11 microservicios, autenticación de aceptadores, colas quórum, OAuth2, alta previa de cuentas en Ardid, nuevo webhook de bloqueo de cuenta
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

**Contexto.** Hubo un análisis de riesgo del pase de Wallet V73 el 2026-10-01. El pase venía corrido "al 8" (probablemente 2026-10-08) según la reunión "W 73 - Impacto de temas" del 2026-09-24.

**Qué entra en V73, según el resumen:**
- **11 microservicios** que hay que coordinar en estimación y alcance técnico.
- **Autenticación de aceptadores**, con tickets operativos asociados, y **control antifraude**.
- **Migración a colas quórum** (RabbitMQ) y **soporte OAuth2**. Las dos tienen validaciones pendientes.
- **Nuevo webhook de aviso de bloqueo de cuenta.** Pablo Gomes lo documenta en el portal de developers. Cuando esté publicado, `/sync_web` lo levanta en `wallet/apis_expuestas/`. Este item no documenta el contrato del webhook.
- **Débito recurrente:** Andrea Orsini hace la regresión para confirmar que sigue pasando bien por Ardid.

**Prerequisitos operativos antes del pase:**
- Nico Pomponio avisa al grupo cuando la infraestructura esté terminada.
- Juan Pablo Carubelli carga los aceptadores nuevos cuando el microservicio esté desplegado.
- Ana prueba el flujo de lectura de QR el viernes 2026-10-02.
- Andrea Orsini abre un chat para coordinar las pruebas de habilitación de flags del viernes.
- **Nicolás Colón da de alta en Ardid todas las cuentas pendientes antes del pase.** Además arma una consulta automática que detecte las altas de cuenta fallidas en Ardid y mande una notificación diaria. Esto conecta con lo que ya documenta `organizaciones_y_configuracion.md` sobre el alta de cuenta con timeouts de Ardid, con la deuda técnica de redelivery (WS-1139) y con la especificación `OPERACIONES_ORGANIZACION_HABILITADA_ARDID` (WS-1242).
- Matías Alzogaray hace el seguimiento diario y manda por mail el plan de acción con semáforos.

**Lo que la minuta no dice:** la fecha exacta del pase, el semáforo de riesgo asignado y cuántas cuentas están pendientes de alta en Ardid. Se puede completar con el mail del plan de acción de Matías Alzogaray cuando llegue.

> Fuente: Reunión "W 73 - Análisis de riesgos" (2026-10-01), resumen del mail de Gemini.
