# Integración con MODO — VATA (Validación de Titularidad de Tarjetas)

> Estado: servicio externo documentado, sin integración productiva confirmada todavía — en curso de adopción por el proyecto `titularidad_tarjeta` (PRD-25, ver abajo).
>
> Nota de encasillado: VATA es un servicio externo de un tercero (MODO), del mismo tipo que Coelsa (`mecanica_qr_coelsa.md`), API Bank (`arquitectura_sistema/api_bank/`) o un API Broker — no es un módulo interno de Adquirencia. Se documenta acá porque es Adquirencia quien lo termina consumiendo (validación de titularidad de tarjeta en Botón Simple), pero el servicio en sí vive y se mantiene del lado de MODO.

## Qué es VATA

**VATA (Validación de Titularidad de Tarjetas)** es una API pública de MODO que permite confirmar si una tarjeta pertenece efectivamente a la persona que la está usando para pagar — pensada para reducir contracargos por "tarjeta no propia" (fraude de titularidad).

- Documentación pública: `https://docs.modo.com.ar/api-docs/api-vata`.
- Contrato comercial: template `PDSA - Acuerdo VATA (template).docx`, provisto por MODO.

## Origen del conocimiento — reenvío de un mail de enero 2025

Pablo Gomes reenvió el 2026-09-10 a Nicolás Colón, sin agregar comentario propio, una cadena de mails de **enero 2025**: el mail original (14/01/2025) fue de Ignacio Heidenreich (MODO, con Lucas Bacelo y Santiago Bozzo de MODO/ingeniería en copia) a Emma Vignoles, ofreciendo la API VATA; Emma Vignoles lo reenvió el 27/01/2025 a Pablo Gomes y a gente de Tec Financiera, mencionando una reunión a las 17hs ese mismo día — sin registro en el Cerebro de qué se resolvió en esa reunión ni de qué pasó con la propuesta en el año y medio que siguió. No hay evidencia de que en ese momento se haya avanzado con una integración.

## Por qué es relevante ahora — mismo servicio que adopta `titularidad_tarjeta` (PRD-25)

Casi un año y medio después de ese mail, el proyecto **`titularidad_tarjeta`** (Nicolás Colón, foco Ardid/Adquirencia, PRD-25) diseñó de forma independiente una integración con "VaTa (MODO)" para resolver exactamente el mismo problema (Bind no valida hoy la titularidad de la tarjeta en Botón Simple, generando contracargos por "tarjeta no propia") — sin que quede confirmado en ninguna fuente si el equipo retomó conscientemente esta propuesta de 2025 o llegó a la misma solución de forma independiente. Ver el diseño completo ya cerrado en [`2_areas/direccion/iniciativas.md`](../../../2_areas/direccion/iniciativas.md) (fila `titularidad_tarjeta`):

- Validación contra VATA **después** de que el motor antifraude interno (Ardid) analice la transacción, y solo si Ardid no la rechaza por motivos propios (~10% de rechazo propio) — ahorra ≈USD 73.000/año frente a validar el 100% de las transacciones.
- Resiliencia: ante timeout/caída de MODO, 2 reintentos y luego fail-open; ante un `409` de "titular inválido/tarjeta deshabilitada/expirada" se rechaza la transacción; el resto de los `409` y los `400`/`401`/`404` continúan normalmente.
- Componente de integración diseñado como servicio reutilizable, pensando en un futuro consumidor en POS (ver oportunidad OP-026).
- Estimación preliminar: 7 SP para el alcance comprometido (rango 7-15 por tocar código crítico de aprobación/rechazo de pagos) + 3 SP opcionales (rango 3-7) para un componente de caché de validaciones, no comprometido para esta iteración.
- Checklist de 7 áreas con la mayoría "Pendiente": Fraude no validó formalmente el diseño de resiliencia, Legales debe revisar el contrato con MODO (posiblemente el mismo template `PDSA - Acuerdo VATA` de 2025, a confirmar si sigue vigente o hay que renegociarlo), Soporte necesita capacitación, Comercial no definió si se factura a comercios, IT debe confirmar ambiente de pruebas.

**Pendiente de confirmar (no resuelto por este merge):** si el contrato/acuerdo comercial de 2025 sigue vigente o hace falta renegociarlo con MODO antes de avanzar con la integración técnica ya diseñada — tarea para Legales dentro del checklist de `titularidad_tarjeta`.

## Ver también
- [validacion_bines_tarjetas.md](validacion_bines_tarjetas.md) — otro mecanismo de identificación de tarjeta (BIN/tipo), problema relacionado pero distinto (clasificación crédito/prepaga, no titularidad).
- [boton_simple_2_0.md](boton_simple_2_0.md) — canal donde hoy se concentra el problema de contracargos por "tarjeta no propia" que `titularidad_tarjeta` busca resolver.
- [`ardid/modulo_pagos.md §14`](../ardid/modulo_pagos.md) — mecánica de identificación de tarjetas por hash en Ardid, motor que corre antes de la validación VATA en el diseño de `titularidad_tarjeta`.

---
*Última actualización: 2026-09-23 — `/context_merge`: archivo nuevo, a pedido explícito del usuario de encasillar la API VATA de MODO como servicio externo de Adquirencia (mismo criterio que Coelsa/API Bank), conectándola con el proyecto activo `titularidad_tarjeta` que ya la integra en su diseño.*
