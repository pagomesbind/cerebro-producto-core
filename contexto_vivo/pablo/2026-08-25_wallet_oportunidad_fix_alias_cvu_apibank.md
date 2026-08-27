---
id: 2026-08-25_wallet_oportunidad_fix_alias_cvu_apibank
pm: pablo
fecha_captura: 2026-08-25
fuente: "/idea_start — discovery de `asignacion_alias_cvu` (ticket MDA-292391, Banco Industrial), 2026-08-25"
producto: wallet
tema: "Fix de resiliencia: reintento ante falla de asignación de alias post-CVU (apibank/Coelsa)"
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Candidata a IDEA: fix de reintento en la asignación de alias tras creación de CVU

**Origen:** ticket de soporte MDA-292391 (Banco Industrial/apibank) — +1500 casos de `422 VW006` en los primeros 4 días desde el 06/08/2026. Escalado por Gonzalo Rivera (BAU/Soporte) el 2026-08-24, discovery completo en `1_proyectos/asignacion_alias_cvu/`.

**Señal de demanda:** transversal, no de un cliente puntual — afecta a toda organización sobre PSP=184 que crea CVU (>30 clientes de Wallet-as-a-Service). El banco ya cerró su ticket sin ofrecer solución de su lado; el fix queda enteramente del lado de Bind.

**Foco estratégico que alimentaría:** ninguno de los 3 focos vigentes (Onboarding/Pagos FX/Ardid) — es BAU técnico, no iniciativa de foco. Discovery completo justificó igual atacarlo ahora (Gate 2: ✅ vale la pena) por bajo costo de implementación estimado (reutiliza el mecanismo de resiliencia Polly ya productivo) y alto impacto transversal.

**Solución ya definida (Gate 3 + análisis técnico-funcional completo):** ante el error de "CVU no existe" en la asignación de alias contra el banco, esperar 700ms y reintentar una vez — con el requisito funcional de cubrir tanto el flujo automático de creación de CVU como el endpoint de asignación directa de alias (misma causa raíz en ambos), sin corregir nada más allá del propio request/response de quien llama. Sin PRD formal — listo para ticket de Ingeniería directo, con análisis técnico completo (contrato, diagramas, máquina de estados) como base (ver `1_proyectos/tareas.md` T-032/T-033).

> Fuente: discovery `/idea_start` completo, 2026-08-25. Ver `1_proyectos/asignacion_alias_cvu/proyecto.md` y `decisiones.md` para el detalle de los 3 gates.
