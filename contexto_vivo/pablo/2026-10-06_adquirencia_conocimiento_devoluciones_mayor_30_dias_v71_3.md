---
id: 2026-10-06_adquirencia_conocimiento_devoluciones_mayor_30_dias_v71_3
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_mails — mail \"Documentación Para Integraciones\" de Melisa Belpassi (Fintexa, PM), 2026-10-05, threadId 1a10dbd6c929c9d7, a malzogaray/grivera/pagomes/lrudaz/ncolon/mnadalin/pablo.serra"
producto: adquirencia
tema: Nueva funcionalidad en producción — configuración de entidades para devoluciones con plazo mayor a 30 días (v71.3)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Fintexa (Melisa Belpassi, PM) entregó el 2026-10-05 la documentación técnica para **configurar entidades que necesiten realizar devoluciones con un plazo mayor a 30 días** — funcionalidad que salió a producción ese mismo día, **05/10/2026 a las 21:15hs, en la versión 71.3 de Adquirencia**.

Detalle de la entrega:

- Adjunto: PDF `AD-Modificar entidad para que pueda devolver con plazo mayor a 30 días.-051026-182958.pdf` — documentación de configuración, no leída automáticamente por esta skill (queda pendiente lectura manual si el PM necesita el detalle de parámetros/flags exactos de la entidad).
- El mail no especifica a qué entidad puntual dispara el cambio (no hay cliente nombrado en el cuerpo) — a confirmar con Soporte/Integraciones si hay un caso de uso concreto detrás (reclamo de cliente, pedido comercial) o si es una mejora de plataforma general.
- Reacción de Mariana Nadalin (COO) al hilo con un emoji, sin agregar contexto adicional.

**Nota de ruteo:** esta es documentación de *cómo configurar* la funcionalidad (vive en `detalle_productos/adquirencia/devoluciones_y_contracargos.md`, igual que el resto de la mecánica de devoluciones/contracargos ya documentada) — distinto del changelog de versión que cubre `/sync_releases`; si `/sync_releases` ya registró el pase a producción de la v71.3 por otra vía, este item solo aporta el detalle funcional de configuración, no duplica el changelog.
