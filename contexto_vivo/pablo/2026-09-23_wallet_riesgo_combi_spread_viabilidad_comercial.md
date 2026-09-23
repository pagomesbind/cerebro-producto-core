---
id: 2026-09-23_wallet_riesgo_combi_spread_viabilidad_comercial
pm: pablo
fecha_captura: 2026-09-23
fuente: "/sync_mails — hilo 'Re: 🔥Nuevas credenciales API Broker para Organización MOVE (Bind PSP)' (threadId 19fa8e27dd0af03d), Luciana Rudaz / Gastón Degiovanni (Bind Inversiones), 2026-09-22"
producto: wallet
tema: El spread del producto Dólar COMBI (pagos crossborder vía IVSA/Mastercard Move) puede hacerlo comercialmente inviable — validado con instrucción manual transitoria mientras se ajusta la plataforma MOVE
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

**Contexto — este hilo pertenece al proyecto Mastercard Move / PagosFX de Luciana Rudaz, Pablo Gomes solo está en copia.** Se captura acá porque el riesgo (viabilidad comercial del producto) es transversal y todavía no tiene item propio en el canon; el PM dueño real es Luciana Rudaz.

**22/09/2026 — Gastón Degiovanni (Bind Inversiones) confirma** que empiezan una prueba controlada del circuito COMBI junto con "Cristian", con un esquema **transitorio de instrucción manual** (envío de detalle de operaciones, ejecución en mercado, transferencias y conciliación a mano), mientras la plataforma MOVE recibe las mejoras necesarias para producción (comprometidas "para el próximo sprint", sin ETA confirmado).

**Luciana Rudaz acepta avanzar así "para no frenar la salida del producto"**, pero levanta dos objeciones de fondo:
1. **Pide documentar el modo de operar manual** hasta que se automatice, para no dejar lugar a dudas — dado que la mayoría de las operaciones van a ser montos altos (pagos de importaciones de bienes/servicios).
2. **Cuestiona el spread/pricing.** Consultó el BuyPrice de PROD (`1615.78000000`) contra la cotización de mercado visible ese mismo momento — poco más de 17 puntos por encima —, y advierte que si no se mejora el spread **no es viable vender el producto**. Ejemplo adicional del día siguiente en la misma cadena: el índice CCL de BYMA cerró en 1.595,84 el día anterior, mientras que el precio de compra devuelto para ese día fue 1.613,31 (~17,5 puntos de diferencia).

**Respuesta de Gastón:** el BuyPrice ya incluye la comisión cargada — la referencia de "dólar hoy" que usa el mercado (AL30/AL30C) no es comparable directamente porque no incluye ese spread; confirmó que el precio informado = precio variable + spread, y preguntó qué necesitan para empezar las pruebas. **Última respuesta de Luciana en la cadena (22/09 21:08): "que nos bajen el spread"** — sin resolución del punto al cierre de la ventana de esta corrida.

**Impacto:** riesgo de negocio (no solo técnico) — si el spread no se ajusta, el producto COMBI puede terminar sin poder venderse a los clientes que dependen de pagos crossborder en USD (ej. el flujo de INTER "Powered by Bind", que según menciones previas en el mismo hilo ya depende de esta funcionalidad).
