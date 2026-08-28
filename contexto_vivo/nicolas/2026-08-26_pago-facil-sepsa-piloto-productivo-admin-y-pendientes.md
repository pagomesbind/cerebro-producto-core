---
id: 2026-08-26_pago-facil-sepsa-piloto-productivo-admin-y-pendientes
pm: nicolas
fecha_captura: 2026-08-26
fuente: "Mail \"Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 19-8\" — Guillermo Paolucci (Western Union) y Adriana Endzeliz (Bind, Comercial), hilo 2026-08-19 → 2026-08-25"
producto: servicios
tema: Pago Fácil (Western Union/SEPSA) — plataforma admin para Piloto Productivo, listado de Billers y puntos operativos abiertos del checkout
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Hilo de seguimiento comercial/operativo entre Western Union (marca **Pago Fácil**, legal **SEPSA**) y el equipo Comercial de Bind (Adriana Endzeliz) sobre el desarrollo de la "Pasarela de Pagos Bind-SEPSA" (Botón de Pago / checkout que corre sobre Botón Simple 2.0, mismo motor que documenta `pago_facil_mantenimiento.md`). No estaba documentado en el Cerebro el detalle operativo de este frente — el archivo existente cubre solo el backlog técnico Jira (espacio SER).

**Plataforma de administración nueva para el Piloto Productivo:** `https://admin.bindpagos.com.ar/`. Permite a Pago Fácil hacer monitoreo transaccional diario, descargar reportes, y — una vez recibida la capacitación — autogestionar el **bloqueo y desbloqueo de comercios** durante el Piloto Productivo. Adriana Endzeliz ofreció sesión de orientación el jueves 27/08 (11:00 o 15:00hs) y compartió las credenciales de acceso por canal separado (no por este mail).

**Listado de Billers/comercios:** se compartió un adjunto `Billers Pago Facil_Comercios en Bind PSP.xlsx` con el mapeo de cada Biller y el comercio asociado en Bind PSP — **no se descargó** (regla de la skill: adjuntos quedan pendientes, no se procesan automáticamente). Queda como pendiente de revisión manual si se necesita ese detalle.

**Estado de entidades del Piloto (al 2026-08-19):** UAT confirmada para **PRO ACTION**; próximas entidades piloto: **Colegio Ing Cba** y **Marea TV**.

**Puntos operativos abiertos de la minuta del 19/08** (sin confirmación de resolución en el mail del 25/08 — a validar en próxima corrida):
- **Tarjeta Prepaga:** se iba a configurar como Tarjeta de Crédito (TC) para que pase por ese flujo del checkout; pasaje a producción estimado semana del 17-ago, pendiente de confirmar fecha real.
- **MODO:** la operatoria entre Bind y MODO se revisaba con Coelsa; status a la fecha era "en espera de validación del administrador", sin información nueva.
- **Botón "Flecha"** en el checkout: se evaluaba sacarlo; mientras tanto queda deshabilitado (provisorio) pero visible en pantalla, con posibilidad de rebautizarlo "FINALIZAR" una vez confirmado. Sacarlo definitivamente requiere protocolo formal y traslado de costos.
- **Identificación de origen de pago:** para Pagos con QR y Transferencia se necesita informar a Pago Fácil desde qué billetera se emitió el pago; para pagos con Tarjeta, con qué tarjeta se pagó — Adriana Endzeliz quedó en coordinar reunión con Banco Industrial (BI) para resolverlo.
- **Colores del front:** Guillermo Paolucci (WU) quedó en validar con su equipo de Marketing la definición de colores para el checkout — pendiente a la fecha del mail.
- **Confirmación online a entidades:** cambios de alcance a coordinar en reunión propia, sumando al equipo del Proyecto SEPSA (no confundir con el Proyecto Servicios de Wallet, ver `[[2026-08-25_proyecto-servicios-integracion-pipeline-wallet]]` — mismo cliente Pago Fácil, frentes distintos: uno es checkout/Botón de Pago con WU/Comercial, el otro es DeudaManagement con Fintexa/Wallet).

> Fuente: Mail "Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 19-8" (hilo 2026-08-19 → 2026-08-25).
