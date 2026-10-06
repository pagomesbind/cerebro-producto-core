---
id: 2026-10-02_iniciativa-inter-fechas-webhook-dolar-ccl-prd-aprobado
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Sesiones de /idea_crosscheck, /idea_risks e /idea_prd con el PM (2026-10-02) sobre PRD-259"
producto: wallet
tema: Fechas en el webhook de Dólar CCL (Inter) — revisión cruzada, riesgos y PRD aprobados
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: inter_trazabilidad_ccl
---

**PRD-259: PRD v1.0 aprobado (2026-10-02)**, junto con la revisión cruzada por área y el relevamiento de riesgos.

- **Alcance:** una sola funcionalidad MUST. Son las 8 fechas de la intención en el webhook de Dólar CCL, idénticas al GET, para todas las organizaciones y los dos modelos. Hay 6 exclusiones explícitas (momento de envío, otros datos, normalizar formato, reintentos, otros productos, alerta formal).
- **Revisión cruzada:** sin requerimientos nuevos. Hay impacto en Comercial/Impuestos (cobro del desarrollo a Inter), Soporte (nota y seguimiento manual de entregas la primera semana), IT (el éxito se mide preguntándole al cliente, porque Bind no tiene visibilidad de las APIs que consume cada uno) y clientes en producción (aviso previo y portal).
- **Riesgos:** son 6. Hay un único bloqueador de go-live: que un operador valide el esquema en forma estricta y deje de recibir los avisos. Se levanta con el aviso previo y una consulta a todas las organizaciones con Dólar CCL, que se hace con Soporte/Integraciones apenas Inter acepte el presupuesto. Se descartó el riesgo de pruebas bloqueadas en staging, porque el PM confirmó que ya está resuelto.
- **Siguiente:** sincronizar el PRD a la IDEA en Jira, bajar a historias y obtener la cotización. Construir depende de que Inter acepte el presupuesto.
