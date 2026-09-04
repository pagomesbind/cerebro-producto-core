---
id: 2026-09-02_cliente-terramundi-incidente-rechazos-por-correccion-reglas-ardid
pm: nicolas
fecha_captura: 2026-09-02
fuente: "Reunión \"Join Soporte Clientes\" (2026-09-02)"
producto: ardid
tema: Incidente de aumento de rechazos de tarjetas débito/crédito en Terramundi, causado por la corrección del bug de grupo BIN de Ardid (efecto colateral esperable, no una regresión nueva)
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

En la reunión "Join Soporte Clientes" (2026-09-02), Diego Gaston Weledniger reportó un aumento significativo de rechazos de tarjetas de débito y crédito para el cliente **Peak Travel (Terramundi S.A.)** (ficha en `clientes/casos_de_uso_clientes.md`). Causa identificada por Adriana Endzeliz: no es una regresión nueva, sino el efecto esperado de la corrección del bug de grupo BIN mal configurado en Ardid (ver item de conocimiento de producto relacionado, mismo barrido) — las reglas de validación de pago de Terramundi ahora impactan correctamente por primera vez, rechazando transacciones que antes pasaban sin control. Equipo (Rocio Revelli) trabajando en ajustar los parámetros de esas reglas para reducir la fricción sin resignar seguridad — sin fecha de resolución confirmada en la reunión.

> Fuente: Reunión "Join Soporte Clientes" (2026-09-02), minuta Gemini. Ver item de producto relacionado: `2026-09-02_ardid-reglas-pago-corregidas-generan-rechazos-legitimos-terramundi`.
