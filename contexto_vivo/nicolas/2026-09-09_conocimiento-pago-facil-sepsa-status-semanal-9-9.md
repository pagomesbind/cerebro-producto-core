---
id: 2026-09-09_conocimiento-pago-facil-sepsa-status-semanal-9-9
pm: nicolas
fecha_captura: 2026-09-09
fuente: "Mails \"Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 2-9\" (hilo 2026-09-02 → 2026-09-09) y \"Minuta 9-9\" (2026-09-09) — Guillermo Paolucci (Western Union) y Adriana Endzeliz (Bind, Comercial)"
producto: servicios
tema: Seguimiento semanal del Piloto Productivo Bind-SEPSA (Pago Fácil/Western Union) — avance y estado de los puntos operativos abiertos en §5 de pago_facil_mantenimiento.md
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

Delta de dos minutas semanales sucesivas del seguimiento comercial Bind-SEPSA (mismo frente que §5 de este archivo, hilo 2026-08-19/25 ya documentado) sobre los puntos operativos que seguían abiertos:

**Nuevas entidades del Piloto:** UAT confirmada para **CREDITIA CORP, CREDIMAS y COMAFI** (minuta 2-9); PRD para **COOP ELECT RIO COLORADO** (minuta 2-9); próxima UAT **EL CUATRO** (minuta 9-9, reemplaza a las entidades ya mencionadas en §5 que ya habrían avanzado).

**Estado al 09/09 de los puntos abiertos (respuesta de Adriana Endzeliz, Comercial Bind, previa a la reunión del 09/09):**
- **Habilitación/inhabilitación de comercios desde el Portal ADMIN:** finalizado.
- **Tarjeta Prepaga:** con demora — Bind sigue esperando devolución del procesador para concluir las pruebas.
- **Envío de comprobante por e-mail:** propuesta refinada compartida el 01/09, a la espera de la devolución de Western Union (§5 ya documentaba una propuesta previa de 27/08; esta es una iteración posterior). La minuta 9-9 confirma que WU instruyó "avanzar con el desarrollo".
- **Alias en transferencias:** se va a mostrar el alias que **genera aleatoriamente Coelsa** (no un alias propio de Bind) — sin fecha de implementación todavía.
- **Confirmación online a entidades:** documento con el alcance corregido entregado el 09/09, con el método de seguridad definido: **Whitelist de IP**.
- **Pago QR y Transferencia (identificación de origen):** Bind ya compartió el detalle bruto de transacciones a Western Union para que su equipo de PowerBI trabaje sobre el campo **"CompradorCuenta"** — los 3 primeros dígitos de ese campo identifican la entidad de origen — junto con el listado de entidades. Resuelve el punto abierto de §5 (identificación de billetera/tarjeta de origen).
- **Botón "Flecha":** cambiar su descripción es técnicamente posible, sin estimación de fecha todavía (distinto del punto ya cerrado de §5 sobre sacarlo definitivamente, que requiere protocolo formal y traslado de costos).
- **Colores del front (MKT):** seguía pendiente de validación por Western Union al 09/09 (venía arrastrándose desde antes de §5); Guillermo Paolucci (WU) quedó nuevamente en validarlo, reclamado explícitamente en la minuta del 09/09.

> Fuente: Mails "Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 2-9" (hilo 2026-09-02 → 2026-09-09) y "Minuta 9-9" (2026-09-09).
