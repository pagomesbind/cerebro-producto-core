---
id: 2026-09-22_iniciativa-titularidad-tarjeta-solucion-cerrada
pm: nicolas
fecha_captura: 2026-09-22
fuente: "Skill /idea_solution sobre titularidad_tarjeta (PRD-25), sesión 2026-09-17 a 2026-09-22"
producto: Adquirencia (Botón Simple)
tema: Análisis técnico-funcional de titularidad_tarjeta cerrado con OK del PM
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
proyecto: titularidad_tarjeta
---

Se cerró el análisis técnico-funcional (`/idea_solution`) del proyecto de validación de titularidad de tarjeta (PRD-25). Puntos centrales del diseño: el llamado al motor antifraude interno es síncrono (confirmado por el PM), lo que permite retener en memoria — sin persistencia nueva ni superficie PCI adicional — los datos de tarjeta que hoy se descartan apenas se calcula el hash para el motor antifraude, hasta después de la consulta a MODO. Se detectó y resolvió un hallazgo relevante: la determinación de marca/tipo de tarjeta para el request a MODO depende de la misma lógica interna de identificación de BIN que otro proyecto en curso (PM Pablo Gomes) ya documentó con problemas de datos conocidos — riesgo compartido de bajo impacto, se resuelve solo cuando ese otro proyecto corrija su tabla.

Se diseñó además un componente opcional (explícitamente enmarcado por el PM como "a evaluar si se construye", no comprometido para esta iteración): una caché interna de validaciones de titularidad, independiente de Bóveda (que se descartó como base porque solo retiene datos durante la transacción en curso). El diseño final: hash sobre BIN + Marca + fecha de vencimiento + últimos 4 dígitos + Tipo + DNI del pagador (el DNI es imprescindible en el hash — sin él, una tarjeta ajena ya validada por su titular real podría colarse sin re-chequearse); solo se cachean los resultados positivos de MODO, nunca los rechazos (un rechazo puede dejar de ser válido con el tiempo, ej. una tarjeta reactivada por el emisor).

Sin gaps bloqueantes. Quedan pedidos de material a MODO (rate limit, motivo específico del 409) y confirmaciones menores con Ingeniería, ninguno bloqueante. Próximo paso sugerido: actualizar el PRD ya escrito (v1.0) con los hallazgos de este análisis, ya que se armó después del PRD en vez de antes (orden invertido respecto al proceso habitual).
