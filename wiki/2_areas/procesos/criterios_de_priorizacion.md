# Criterios de Priorización

> No es un framework de scoring genérico (RICE/ICE) importado de afuera — es el criterio **que el equipo de Producto ya usa de hecho**, destilado de decisiones reales dispersas en `decisiones.md`, `estrategia/index.md` y `tareas_producto.md`. Sirve para que el Cerebro pueda ayudar a priorizar con el mismo criterio que usaría el PM, no con uno inventado. Cada punto marca si es **confirmado** (el PM lo dijo explícitamente) o **inferido** (se dedujo del patrón de decisiones, a validar).

## El orden de corte, de mayor a menor peso

### 1. Compliance/remediación primero — ✅ confirmado
Post-fraude de marzo 2026 (~$11.500M, Transferencias Pull) y auditoría reforzada de Grupo BIND: todo lo que remedia riesgo regulatorio o de fraude pasa antes que crecimiento. Es el driver que hizo que Onboarding —no una feature de producto nueva— fuera el foco del PM líder. Ver [north_star.md](../direccion/north_star.md) y [estrategia/index.md](../direccion/estrategia/index.md).

### 2. Las 2 NSM como marco permanente — ✅ confirmado
Todo lo demás se evalúa contra si mueve (directa o indirectamente) volumen de API BANK o de Payway. Ver [north_star.md](../direccion/north_star.md) — incluye los oportunity trees con las palancas concretas por NSM.

### 3. Capacidad real, no capacidad deseada — ✅ confirmado
**~1 IDEA entregada cada 3 meses, frente a ~6 IDEAs abiertas simultáneamente en Jira** (T-035, `2_areas/tareas_producto.md`). Este dato debería vetar cualquier plan que asuma que se puede avanzar en paralelo sin trade-off. Precedente directo: el 2026-07-20 el PM se negó a comprometerse a partir la capacidad de ingeniería 50/50 entre KR1 y KR2 de Onboarding, citando el riesgo de no llegar a ninguno de los dos si se fuerza la mezcla (ver [estrategia/foco_onboarding.md](../direccion/estrategia/foco_onboarding.md) §3).

### 4. Simplicidad de objetivo — ✅ confirmado
1-2 KRs máximo por foco. Decisión explícita del PM líder (2026-07-17): "el equipo viene sin dirección y un objetivo simple maximiza el foco; se irá a más cuando la primera ola esté resuelta" (ver [estrategia/index.md](../direccion/estrategia/index.md)).

### 5. La estrategia manda, pero el BAU no desaparece — ✅ confirmado
Los 3 focos estratégicos no reemplazan el flujo de IDEAs del negocio ni las urgencias de BAU — la regla es mantener foco dentro de ese ruido, no eliminarlo. Ver [estrategia/index.md](../direccion/estrategia/index.md).

### 6. Mayor apalancamiento antes que orden cronológico o inversión previa — 🟡 inferido
Patrón repetido: el PM relegó PRD-108 (legajo, con desarrollo ya avanzado) frente a PRD-202 (validación en el alta) porque "el problema de mayor apalancamiento es no tener la herramienta para forzar la validación en las altas nuevas" — pese a que empezar por PRD-108 "en retrospectiva, no fue la jugada correcta" (ver [estrategia/foco_onboarding.md](../direccion/estrategia/foco_onboarding.md) §3). Sugiere que el criterio no es "qué ya tiene inversión" sino "qué desbloquea más cosas después".

### 7. Driver comercial concreto como desempate — 🟡 inferido
Cuando dos iniciativas compiten sin diferencia clara de las reglas de arriba, el PM prioriza la que tiene un cliente/prospecto real presionando con riesgo de churn o volumen cuantificado — ej. Octagon (100-120 CVUs proyectadas, ya evaluando otro proveedor por falta de ETA) empujó la apuración del alta de cuenta comitente simplificada (T-038, decisión con Emma Vignoles 2026-07-20) por sobre otros temas del mismo roadmap. Otros ejemplos del mismo patrón: Arcos Dorados, Coppel, La Virginia.

### 8. Medición antes que ejecución — 🟡 inferido
Cuando aparece una duda técnica que condiciona el costo/arquitectura de una decisión (ej. si Worldsys puede devolver archivos), el PM pausa el research de costo hasta confirmar la duda técnica primero — no avanza en paralelo sobre un supuesto no validado (ver `../gaps_y_preguntas.md`, caso Worldsys/ComplianceOne 2026-07-20).

## Cómo usar esto

Al evaluar una IDEA o feature nueva, en este orden: (1) ¿remedia riesgo de compliance/fraude? (2) ¿mueve una NSM, directa o indirectamente? (3) ¿la capacidad real del equipo la absorbe sin canibalizar el foco activo? (4) ¿mantiene el foco simple (no suma un tercer KR)? Si sobrevive a los 4 filtros, los puntos 6-8 desempatan entre candidatas.

**Lo que este archivo NO es:** un sustituto del juicio del PM. Es contexto para que el Cerebro razone con el mismo criterio, y para que cualquier recomendación de priorización cite explícitamente contra cuál de estos puntos se está evaluando.

---
*Creado: 2026-07-20 — segundo archivo de la capa de Dirección, destilado de decisiones ya tomadas (no un framework nuevo impuesto). Revisar con el PM cuando el equipo pase a la "segunda ola" de foco (ver punto 4) — probablemente haga falta un criterio más granular en ese momento.*
