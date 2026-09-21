# Masividad de generación de QR — arquitectura secuencial y límites (caso Provincia Net)

> Estado: en producción (arquitectura y tiempos medidos), con debate abierto de infraestructura/roadmap sin resolver.
>
> Fuente: Reunión "Análisis COBRO" (2026-09-10), minuta Gemini.

## Mecánica actual

El sistema utiliza un grupo ("pool") de códigos QR pregenerados que se asignan a las deudas al recibir el archivo del cliente. Esto agiliza la asociación, pero la generación de lotes **opera de manera estrictamente secuencial por archivo y por caja** — no hay paralelización entre cajas ni entre archivos. Habilitar procesamiento en paralelo requeriría modificaciones arquitectónicas sustanciales (Daniela Collia, Fintexa, se comprometió a llevar la consulta al área de arquitectura).

Esta limitación es la que motiva el ticket **AD-935** (la masividad de Provincia Net satura la cola general de QR).

## Tiempos medidos en staging

Procesar **1.000.000 de códigos QR** toma aproximadamente **3 horas y 25 minutos**, por los "jobs" programados con intervalos de 15 minutos entre corridas.

Provincia Net maneja picos diarios más chicos (lotes de ~5.000 registros) y prefiere la **API** (tarda 2 minutos) frente al protocolo **SFTP** (tarda 1 hora) para esos volúmenes menores — aunque su plan a futuro, al incorporar clientes grandes (ej. La Matanza, 700.000-1.000.000 de códigos QR), es migrar a SFTP.

## Próximo paso acordado — pruebas reales, no solo ajustar intervalos

En vez de asumir que acortar los intervalos de consulta resuelve el problema (podría generar costos operativos innecesarios o solapamiento de archivos, según Daniela Collia), se acordó que **Provincia Net debe ejecutar pruebas reales en staging** enviando lotes de 5.000 registros para medir tiempos de respuesta con volúmenes menores. Pablo Gomes revisará en paralelo la viabilidad de ajustar los tiempos de espera del proceso masivo vía SFTP.

## Dato adicional — volumen de QR no cobrados

Pablo Gomes advirtió que aproximadamente el **97% de los códigos QR creados vencen sin ser abonados**, generando acumulación de deudas inútiles en las tablas del sistema. Queda pendiente confirmar con el equipo de infraestructura si esas tablas se purgan periódicamente.

## Colas diferenciadas por cliente — resuelto por umbral de tasa, no por cliente nombrado (2026-09-17)

> Fuente: Reunión "Análisis de riesgo: AD V 73" (2026-09-17), minuta Gemini.

El debate abierto arriba (Melisa Belpassi proponía separar colas de procesamiento para clientes urgentes como DPay de la de Provincia Net) se resolvió con una **gestión inteligente de cola implementada en AD V73**: los clientes que superen las **200 solicitudes por minuto** se despriorizan temporalmente y pasan a una **cola secundaria**, en vez de competir por los mismos recursos que el resto del tráfico. La solución final no separa por cliente nombrado sino por **umbral de tasa de peticiones** (200 req/min), que en la práctica despriorizaría a cualquier cliente que genere ráfagas de ese volumen, no solo a Provincia Net.

Contexto del disparador: en esta misma reunión se discutió una incidencia de demora superior a 35 segundos en la disponibilidad de datos de códigos QR dinámicos, atribuida a Provincia Net (ticket AD-935, ya referenciado arriba). Daniel Zalazar explicó la mecánica de despriorización descrita.

**Seguimiento operativo acordado:** el equipo de infraestructura debe monitorear el consumo de bases de datos y las colas de RabbitMQ durante el manejo de ráfagas (asignado color amarillo, no verde). Hernán Clarich queda a cargo de avisar preventivamente a Provincia Net sobre el envío de ráfagas en horarios específicos, para minimizar riesgos durante el despliegue.

## Ver también
- [index.md](index.md) — módulo Agente de Cobros y Pagos.

---
*Última actualización: 2026-09-21 — `/context_merge`: resolución del debate de colas diferenciadas (reunión "Análisis de riesgo: AD V 73", 2026-09-17).*
