---
id: 2026-10-06_conocimiento-devoluciones-mas-30-dias-ad-1948-config-bd-y-pase-ad-73-1
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Reunión \"RxT - Devolución de transacciones + 30 dias\" (2026-10-05), solo resumen del mail de Gemini (Drive invalidado, sin minuta completa)"
producto: agente_cobros_y_pagos
tema: Devoluciones de más de 30 días entran como AD-1948 en la versión 73.1 (pase 05/10, 21hs), con plazos configurados hoy a mano en base de datos; endpoints de configuración pendientes
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

**Qué completa.** Este item completa el item `2026-10-02_conocimiento-devoluciones-hasta-6-meses-por-entidad-ministerio-justicia` (ya en `en_cola`). Ese item dejaba abierto cómo se configuraba la especificación por entidad. La reunión del 2026-10-05 responde parte de eso.

**Cómo entra a producción:**
- La habilitación de devoluciones de transferencias de más de 30 días viaja como el ticket **AD-1948**, dentro de la **versión 73.1** de Adquirencia/Agente de Cobros y Pagos.
- AD-1948 habilita esas devoluciones **por configuración en base de datos**. Los plazos de cada entidad se cargan con una intervención manual en la BD, no desde el portal ni por API.
- El pase de la 73.1 quedó programado para el **lunes 2026-10-05 a las 21hs**, con **impacto en la pasarela de pagos**. Se iba a redactar un comunicado a clientes sobre los posibles impactos.
- La definición final del pase quedó **sujeta a la verificación de APIBank**. En el entorno de pruebas aparecieron **errores en transferencias salientes** que había que resolver antes del pase. Mariela Marin coordina su resolución (grupo de chat y reunión).
- Marcos Sanchez valida que las fechas queden bien configuradas en la base después del pase.

**Lo que sigue (deuda explícita):** Nicolás Colón queda a cargo de una solución con **endpoints de configuración** para cambiar los plazos de devolución sin tocar la base a mano. Hasta que exista, cada entidad nueva que pida el plazo extendido (Rifsa, otros ministerios) necesita una intervención manual en la BD.

**Lo que la minuta no dice:** si el pase se hizo finalmente el 05/10 (dependía de APIBank y de los errores de salientes), el nombre de la especificación y si alcanza también a QR.

> Fuente: Reunión "RxT - Devolución de transacciones + 30 dias" (2026-10-05), resumen del mail de Gemini.
