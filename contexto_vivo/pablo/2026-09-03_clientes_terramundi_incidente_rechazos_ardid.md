---
id: 2026-09-03_clientes_terramundi_incidente_rechazos_ardid
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_meetings — reunión 'Join Soporte Clientes' 2026-09-02 10:01 (docId 1eBqiPncYkZgzw693JLN5rmLGwtIZST14zx6LKb3Pn_g), minuta Gemini"
producto: ardid
tema: Terramundi — aumento de rechazos de tarjetas por corrección reciente de reglas de Ardid
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Cliente:** Peak Travel (Terramundi S.A.) — ficha existente en `log_clientes.md` (Adquirencia: Botón de Pago, QRI, RxT — Viajes y Turismo, Mediano, riesgo Bajo).

**Incidente reportado (2026-09-02):** Diego Weledniger (Comercial) reportó un aumento significativo en los rechazos de tarjetas de débito y crédito para Terramundi. Causa identificada por Adriana Endzeliz: una **corrección reciente aplicada a las reglas de Ardid** ahora está impactando correctamente sobre los medios de pago — es decir, empezó a rechazar transacciones que antes, por el bug ya corregido, no se filtraban. El aumento de rechazos es consecuencia esperada de la corrección, no un nuevo bug — pero eleva la fricción real que percibe el cliente.

**Reglas de validación involucradas (mencionadas en la misma reunión, aplican de forma transversal, no exclusivas de Terramundi):** límites de **$300.000 por transacción** y **$2.000.000 mensuales**. Rocío Revelli (junto con Gonzalo Rivera) está analizando el impacto de estas reglas y ajustando parámetros para reducir la fricción de experiencia de usuario sin resignar seguridad — ver detalle de la limitación de tooling en `2026-09-03_ardid_reglas_limites_transaccion_trazabilidad`.

**Estado:** en análisis, sin resolución confirmada en la reunión. Rocío Revelli queda con 3 próximos pasos: corregir el error técnico causante del alto índice de rechazos, repasar todas las reglas de entidad vigentes, y evaluar configuraciones de reglas por entidad.

> Fuente: reunión "Join Soporte Clientes" (2026-09-02 10:01), minuta Gemini. Participantes: Mauro Suppan, Luciana Rudaz, Emma Vignoles, Diego Weledniger, Adriana Endzeliz, Gustavo Lazzaro, Gonzalo Rivera, Alberto Murad, Matías Alzogaray, Nicolás Colón, Pablo Gomes.
