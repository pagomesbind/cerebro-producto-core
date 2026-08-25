---
id: 2026-08-25_redlink-error-404-consulta-estado-transferencias
pm: nicolas
fecha_captura: 2026-08-25
fuente: "Mail \"Error 404, levantar guardia\" — luciano.sanjurjo-ext@bind.com.ar a alertas_HtH_Link@bancoindustrial.com.ar (2026-08-23)"
producto: transversal
tema: Errores 404 al consultar estado de transferencias contra Red Link en ambiente de integración — producto/dueño no identificado
tipo: gap
destino_propuesto: "sin determinar — a evaluar en /context_merge (posible arquitectura_sistema/ o detalle_productos/<producto que integra con Red Link>)"
tipo_destino: crear
contradice: "no"
confianza: baja
estado: en_cola
---

El 2026-08-23 se escaló al "equipo de Integración de Red Link" (mail a `alertas_HtH_Link@bancoindustrial.com.ar`) un pedido de "levantamiento de guardia" por errores bloqueantes en el ambiente de integración: al consumir el endpoint de consulta de estado de transferencias contra `bancos.integracion.redlink.com.ar` (`GET /bancos/transferencias/1/0/0/estado`), el servidor devuelve **HTTP 404 (Not Found)**. Detalle del error: fecha/hora `Ago 23 05:07:55`, W3C trace ID `cd56b9dbf5b79987ec98cb25f70a2915`.

No hay wiki actual (`3_recursos/detalle_productos/`) que documente una integración con Red Link — no se pudo determinar con confianza qué producto de Bind PSP consume este endpoint (candidatos posibles: Adquirencia o Wallet, dado que el mail llegó a la bandeja de Nicolás Colón, pero no hay contexto suficiente en el hilo para confirmarlo). Se captura como gap literal, sin inventar el destino, para que `/context_merge` (o una sesión con más contexto) decida si corresponde a un producto puntual o a `arquitectura_sistema/`.

> Fuente: mail "Error 404, levantar guardia", luciano.sanjurjo-ext@bind.com.ar → alertas_HtH_Link@bancoindustrial.com.ar (2026-08-23), un solo mensaje sin respuesta visible en la ventana analizada.
