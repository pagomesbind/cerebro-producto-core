---
id: 2026-09-08_conocimiento-portal-admin-limitacion-busqueda-parcial-referencia-csv
pm: nicolas
fecha_captura: 2026-09-09
fuente: "Reunión \"Revisemos ADMIN Pago Facil\" (2026-09-08), minuta Gemini"
producto: portal_admin
tema: Limitación de búsqueda parcial por referencia en el Admin y workaround vía export CSV (Pago Fácil)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

Reunión "Revisemos ADMIN Pago Facil" (2026-09-08, 11:02) — Adriana Endzeliz, Luisina Luca, Nicolás Colón. Preparación de una capacitación al equipo de soporte de Pago Fácil (a las 11:30 el mismo día) para que puedan verificar transacciones, operaciones, devoluciones y estados de pago directamente en el panel de administración, antes de escalar un ticket de soporte a Bind.

**Hallazgo técnico (filtros del Admin):** al filtrar transacciones por forma de pago "transferencias", se detectó que el personal externo (soporte de Pago Fácil) solo conoce la parte del identificador de referencia ubicada **antes de la barra inclinada** — y la plataforma de administración **no permite búsquedas parciales directas** en ese campo de referencia. Workaround acordado: descargar el archivo CSV del listado y hacer ahí la búsqueda parcial.

**Otros filtros disponibles relevados en la misma prueba:** identificador externo, identificador de procesador, identificador de deuda. El identificador de transacción propio de Bind se genera **antes** que el registro del emisor. Las transferencias rechazadas por montos más altos u otros motivos deben gestionarse usando el **identificador externo**.

> Fuente: Reunión "Revisemos ADMIN Pago Facil" (2026-09-08), minuta Gemini.
