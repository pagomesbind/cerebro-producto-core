---
id: 2026-10-15_transversal_riesgo_decision_soporte_qa_sin_stakeholders_presentes
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_mails — hilo 'Informe Estado Proyectos Emisión al 08/10/2026' (threadId 1a11cec7ef70f307), Andrea Orsini / Pablo Serra / Agustín Grau (Fintexa), 2026-10-15"
producto: transversal
tema: Decisión de suspender el soporte diario de Fintexa al QA interno de Bind, tomada en una reunión de refinamiento sin presencia de QA ni Tecnología, formalmente disputada por la Líder de Calidad
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

En el informe semanal de Wallet del 08/10/2026, Nicolás Pomponio (Fintexa) comunicó que "se definió en la reunión que el equipo de Fintexa deja de dar soporte diario y ad hoc al QA interno de Bind; las consultas se centralizan a través de Matías Alzogaray, y el QA interno debe atenerse a la definición de cada ticket". Emma Vignoles (Producto) ya había cuestionado la gestión de ese punto en el momento ("¿no poder coordinar la interdependencia... a 1 día del pase a PROD?" — ver item hermano `2026-10-09_transversal_riesgo_coordinacion_wallet_onboarding_cuenta_comitente`).

**Escalamiento formal el 2026-10-15:** Andrea Orsini (Líder de Calidad, BIND PSP) retoma el hilo una semana después y objeta la decisión de fondo, no solo la ejecución:

- La decisión se tomó en una **reunión de refinamiento de Wallet** (convocada para otros temas, no para discutir performance de QA), **sin que participaran representantes de QA ni de Tecnología** para dar su conformidad.
- Por ese motivo, Andrea considera que la decisión "no debería darse por válida ni aplicarse hasta que sea discutida y consensuada en una reunión conjunta con todas las partes involucradas".
- Señala además que aplicar un cambio así **a un día y medio de un pase a producción** implica un riesgo operativo significativo.

Pablo Serra (Delivery Manager, Fintexa) responde que Fintexa solo comunicó un problema legítimo de su propio equipo de QA, y que "Pablo" (referencia al PM de Bind) ya había respondido en la reunión original — ofrece repasar el alcance de la decisión. **Agustín Grau (CTO de Fintexa) escala directamente**, pidiéndole a Andrea que lo revise "con Pablo internamente" y proponga alternativas.

**Por qué es un riesgo transversal (no solo de este proyecto):** es la segunda vez en menos de dos semanas que una decisión que afecta a un equipo (primero Onboarding con "cuenta comitente", ahora QA) se toma en una reunión de refinamiento sin que ese equipo esté presente, y en ambos casos la fricción aparece recién días después del hecho, cerca de un pase a producción. Sugiere un patrón de gobernanza de reuniones (quién debe estar presente para decisiones que impactan a otros equipos) más que un problema puntual — ver tarea T-220 para el seguimiento concreto del PM.

> Fuente: hilo "Re: Informe Estado Proyectos Emisión al 08/10/2026" (threadId `1a11cec7ef70f307`), Andrea Orsini, Pablo Serra, Agustín Grau (Fintexa), mensajes del 2026-10-15.
