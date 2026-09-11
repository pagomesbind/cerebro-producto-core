---
id: 2026-09-10_conocimiento-masividad-generacion-qr-provincia-net-arquitectura-secuencial
pm: nicolas
fecha_captura: 2026-09-10
fuente: "Reunión \"Análisis COBRO\" (2026-09-10), minuta Gemini"
producto: agente_cobros_y_pagos
tema: Arquitectura de generación masiva de QR — proceso secuencial por archivo/caja, tiempos medidos y decisión de pruebas reales con Provincia Net
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/masividad_generacion_qr.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
---

En "Análisis COBRO" (2026-09-10) se profundizó en la limitación arquitectónica que motiva el ticket AD-935 (masividad de Provincia Net satura la cola general de QR, ver [T-030](../tareas.md)):

**Mecánica actual:** el sistema utiliza un grupo ("pool") de códigos QR pregenerados que se asignan a las deudas al recibir el archivo del cliente. Esto agiliza la asociación, pero la generación de lotes **opera de manera estrictamente secuencial por archivo y por caja** — no hay paralelización entre cajas ni entre archivos. Habilitar procesamiento en paralelo requeriría modificaciones arquitectónicas sustanciales (Daniela Collia, Fintexa, se comprometió a llevar la consulta al área de arquitectura).

**Tiempos medidos en staging:** procesar 1.000.000 de códigos QR toma aproximadamente 3 horas y 25 minutos, por los "jobs" programados con intervalos de 15 minutos entre corridas. Provincia Net maneja picos diarios más chicos (lotes de ~5.000 registros) y prefiere la **API** (tarda 2 minutos) frente al protocolo **SFTP** (tarda 1 hora) para esos volúmenes menores — aunque su plan a futuro, al incorporar clientes grandes (ej. La Matanza, 700.000-1.000.000 de códigos QR), es migrar a SFTP.

**Decisión de siguiente paso:** en vez de asumir que acortar los intervalos de consulta resuelve el problema (podría generar costos operativos innecesarios o solapamiento de archivos, según Daniela Collia), se acordó que **Provincia Net debe ejecutar pruebas reales en staging** enviando lotes de 5.000 registros para medir tiempos de respuesta con volúmenes menores — Pablo Gomes revisará en paralelo la viabilidad de ajustar los tiempos de espera del proceso masivo vía SFTP.

**Dato adicional — volumen de QR no cobrados:** Pablo Gomes advirtió que aproximadamente el **97% de los códigos QR creados vencen sin ser abonados**, generando acumulación de deudas inútiles en las tablas del sistema. Quedó pendiente confirmar con el equipo de infraestructura si esas tablas se purgan periódicamente.

**Debate abierto — colas diferenciadas:** Melisa Belpassi (Fintexa) planteó que separar las colas de procesamiento para clientes urgentes (ej. DPay) de la de Provincia Net sería más económico que seguir escalando recursos de infraestructura para absorber las ráfagas de este último. Tras debatir si la decisión compete a arquitectura o a negocio, se acordó retomar el análisis directamente con el equipo de arquitectura (Hernán) — sin resolución todavía.

> Fuente: Reunión "Análisis COBRO" (2026-09-10), minuta Gemini.
