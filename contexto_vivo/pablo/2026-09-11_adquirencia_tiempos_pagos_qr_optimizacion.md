---
id: 2026-09-11_adquirencia_tiempos_pagos_qr_optimizacion
pm: pablo
fecha_captura: 2026-09-11
fuente: Mail "Emisión - Tiempos de PagosQR" — Juan Pablo Carubelli (Keep It Simple) — 2026-09-11 12:04
producto: adquirencia
tema: Performance de PagosQR — Optimización post-despliegue con doble consulta Coelsa
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: no
confianza: Alta
estado: ingestado
merge_commit: <pendiente>
---

# Tiempos de PagosQR — Análisis de Optimización Post-Despliegue (Sept 2026)

**Contexto:** Tras despliegue en PROD del esquema de doble consulta a Coelsa para resolver PagosQR, Juan Pablo Carubelli (Keep It Simple, arquitecto técnico) generó nuevo análisis de tiempos de respuesta con foco en optimización continua.

**Hallazgos principales:**
- Mejora observable en tiempos de respuesta de QR tras configuración de doble consulta Coelsa (validación fallida → consulta remota sin latencia excesiva)
- Análisis detallado con gráficos (informe HTML + visualización) en archivos adjuntos

**Adjuntos:**
- `Informe Tiempos PagosQR.html` (análisis completo)
- Imagen con gráficos resumen

**Para destino:** Complementar o actualizar la descripción de la mecánica de doble consulta a Coelsa en `mecanica_qr_coelsa.md`, sección de tiempos/performance. El informe HTML contiene datos de la corrida (timestamps, distribuciones de latencia, benchmarks) — resumen técnico solo, la decisión de qué incluir en el wiki la toma el merge.

**Destinatarios en el mail:** Emma Vignoles, Gonzalo Rivera, Pablo Gomes (este usuario), CC a Nicolás Colón, Nicolás Pomponio, Mariano (KIS), Agustín Grau (TecFinanciera), Mariana Nadalin, Hernán Clarich, Gastón Agustí.
