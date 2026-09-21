---
id: 2026-09-10_adquirencia_emision_v72_2_cashout_bloqueado
pm: pablo
fecha_captura: 2026-09-10
fuente: "Mail Re: Minuta: Análisis de Riesgo - Emisión V 72.2 (2026-09-10, 12:48), María Eugenia Vila"
producto: wallet
tema: falla del endpoint /ConciliarCoelsa con movimientos Cashout tras W 72.2 — acción bloqueante pendiente en PROD
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/conciliacion_coelsa_cashout.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: pendiente
---

# 🔴 Emisión V 72.2 — Validación Cashout falla en PROD

**Fecha:** 2026-09-10  
**Remitente:** María Eugenia VILA (mvila@bind.com.ar)  
**Fuente:** Mail RE: Minuta: Análisis de Riesgo - Emisión V 72.2

## Problema

No se puede validar que los movimientos de Cashout hayan sido incluidos en la conciliación Coelsa durante el despliegue de W 72.2 porque:
- **El endpoint `/ConciliarCoelsa` da error al correr el proceso**
- Esto fue identificado por María Vila y revisado junto con Nicolás Colón (ncolon@bind.com.ar)

## Impacto

- Despliegue del lunes 07/09 llegó a producción pero quedó con **acción bloqueante pendiente:** validar el funcionamiento correcto de la conciliación Cashout
- Las procesadas sí se generaron (4 para Cencosud, 37 para Coto)
- **Estado actual:** "Hay que revisarlo" — sin resolución confirmada

## Contexto

Este es uno de 3 semáforos amarillos de W 72.2:
1. Consultas GET (`idComprobanteRelacionado`, `MotivoRechazo`) — integración activa del cliente
2. Asignación de Alias Automático — reintento con espera corta
3. **Conciliación Coelsa — semáforo VERDE en análisis de riesgo, pero falla real en PROD**

Las transferencias Cashout se incluyeron en el filtro de `/ConciliarCoelsa` (ajuste DEM-1806/WS-1552) para unificar la conciliación de transferencias entrantes. El endpoint aparentemente no soporta el nuevo tipo.

## Acciones requeridas

- [ ] Revisar por qué el endpoint falla con CASHOUT en PROD (aparentemente no lo soporta)
- [ ] Verificar si es regresión desde STG o diferencia de ambientes
- [ ] Resolver y validar antes de dar por terminado W 72.2

## Relacionado

- PRD-200 (Validar cantidad CBU/CVU) — depende de que esta validación funcione
- Acción Matías Alzogaray 10/09: "Aguardo sus comentarios" sobre el plan de acción del despliegue

> Fuente: Mail "Re: Minuta: Analisis de Riesgo - Emisión V 72.2" (2026-09-10, 12:48)
