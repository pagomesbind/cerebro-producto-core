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

## Debate abierto — colas diferenciadas por cliente

Melisa Belpassi (Fintexa) planteó que separar las colas de procesamiento para clientes urgentes (ej. DPay) de la de Provincia Net sería más económico que seguir escalando recursos de infraestructura para absorber las ráfagas de este último. Tras debatir si la decisión compete a arquitectura o a negocio, se acordó retomar el análisis directamente con el equipo de arquitectura (Hernán) — sin resolución todavía.

## Ver también
- [index.md](index.md) — módulo Agente de Cobros y Pagos.

---
*Última actualización: 2026-09-11 — `/context_merge`: archivo nuevo, item de `contexto_vivo/` (reunión "Análisis COBRO", 2026-09-10).*
