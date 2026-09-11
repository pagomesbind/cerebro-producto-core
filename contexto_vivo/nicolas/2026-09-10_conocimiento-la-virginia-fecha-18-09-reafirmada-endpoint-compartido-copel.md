---
id: 2026-09-10_conocimiento-la-virginia-fecha-18-09-reafirmada-endpoint-compartido-copel
pm: nicolas
fecha_captura: 2026-09-10
fuente: "Reunión \"Join Soporte Clientes\" (2026-09-09, 10:03), minuta Gemini"
producto: onboarding
tema: La Virginia — fecha de producción del 18/09 reafirmada por Matías Alzogaray pese a la tensión de cronograma detectada el 2026-09-09 (QA recién entrega el 21/09); el endpoint de cuenta comitente se comparte con Copel; ambiente de staging ya disponible
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "Complementa (no contradice) el item en_cola 2026-09-09_conocimiento-la-virginia-endpoint-comitente-confirmado-w73 (mismo tema, fuente mail Fintexa), que dejaba abierta la duda de si la fecha compromiso del 18/09 seguía en pie dado que QA Externo entrega recién el 21/09."
confianza: alta
estado: en_cola
---

Esta reunión (2026-09-09, mismo día que el mail de Fintexa "RE: Version W 73 Wallet Service" que generó el item `2026-09-09_conocimiento-la-virginia-endpoint-comitente-confirmado-w73`) toca el mismo tema desde el ángulo de Soporte/Integraciones y aporta 3 datos nuevos:

1. **Fecha reafirmada:** Mauro Suppan y Adriana Endzeliz repasaron la fecha de implementación en producción del nuevo flujo de onboarding para personas jurídicas de La Virginia, **fijada para el 18 de septiembre**, con una ventana estratégica de 1-2 semanas para gestionar expectativas del cliente (ver decisión general de "Estrategia de plazos para entregas a producción" de esta misma reunión). **Matías Alzogaray confirmó que la fecha se mantiene** conforme al alcance previsto — pese a esto, no se mencionó explícitamente la fecha de entrega a QA Externo (21/09) del mail de Fintexa, por lo que la tensión de cronograma detectada en ese item **sigue sin resolución explícita** (¿"se mantiene la fecha" incluye el margen para QA post-21/09, o es una confirmación anterior a conocer esa fecha de QA?).
2. **Endpoint de cuenta comitente compartido con Copel:** Mauro Suppan detalló que el endpoint en desarrollo (para que el cliente envíe el ID de cuenta por ticket y reciba la cuenta comitente vinculada) es el mismo que usarán **La Virginia y Copel**. Matías Alzogaray revisará si el desarrollo entra en la versión 73 o 74.
3. **Staging ya disponible:** ante la consulta de Mauro Suppan sobre si es posible entregar un entorno de staging al cliente antes del 18/09, Matías Alzogaray respondió inicialmente que no, pero Adriana Endzeliz y Emma Vignoles aclararon que **el entorno de pruebas ya está disponible y se opera en paralelo** — se acordó comunicar los plazos con claridad a la contraparte.

> Fuente: Reunión "Join Soporte Clientes" (2026-09-09, 10:03), minuta Gemini.
