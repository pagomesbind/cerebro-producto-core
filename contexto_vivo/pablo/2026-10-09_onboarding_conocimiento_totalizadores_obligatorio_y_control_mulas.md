---
id: 2026-10-09_onboarding_conocimiento_totalizadores_obligatorio_y_control_mulas
pm: pablo
fecha_captura: 2026-10-09
fuente: "/sync_mails — hilo de Prevención de Fraudes (Emma Vignoles, Mariana Fiedotin — Líder de Prevención de Fraudes BIND Banco, Rocío Revelli), threadId 1a11dbf384b7d1e9, 2026-10-08, escalado por un caso puntual de bloqueo de fondos"
producto: onboarding
tema: Consumo obligatorio de API Totalizadores en toda alta de CVU + desarrollo en curso para detectar cuentas mula por inactividad post-alta
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/controles_antifraude_alta_cuenta.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Capturado de un intercambio entre Prevención de Fraudes de BIND Banco (Mariana Fiedotin, Emma Vignoles) y Riesgos/BSF (Rocío Revelli) escalado a partir de un caso puntual de bloqueo de fondos — se omiten los datos identificatorios del caso (cliente, CUIT, cuenta) por tratarse de información personal; el valor del hilo es la mecánica de control que describe, no el caso en sí.

**Totalizadores — consumo obligatorio (confirmado por Emma Vignoles, corrigiendo un comentario previo de Rocío Revelli):**
- La API Totalizadores se consume de forma automática y obligatoria para **todas** las altas de CVU de todos los clientes, sea onboarding propio de Bind PSP o de la entidad (cada entidad con OB propio).
- No se permiten altas a CUITs que ya tengan más de 30 cuentas — tanto para clientes de Bind como para los de las entidades.
- Las entidades también tienen la posibilidad de consumir la API Totalizadores en un momento distinto al OB (de manera manual); hoy no está atada a las transacciones del lado de Bind.
- En agosto 2026 se hizo un barrido de los CUITs con más de 30 cuentas y se envió a las entidades con más cantidad de cuentas activas (Cenco y BSF mencionadas como ejemplo).

**Desarrollo en curso — detección de cuentas mula por inactividad (Emma Vignoles, estimado fin de mes — ~octubre/noviembre 2026):**
- Al detectar inactividad en una cuenta por un plazo X luego de su creación, se la inhabilita automáticamente.
- Precedente ya ejecutado manualmente con Inter: barrido cambiando de segmento 7.500 cuentas con fecha de alta superior a 30 días sin actividad.
- Control manual actual (1 vez al mes): cruce de contribuyentes no confiables de ARCA contra Totalizadores, con baja/notificación a las entidades cuando corresponde.
- Propuesta en discusión (sin definir, "para discutir"): screening periódico de cuentas dadas de alta después de agosto 2026 que, pese a no haber superado el umbral de 30 cuentas en Bind, sí lo superan sumando cuentas en otras entidades — pensado como control posterior (y baja), no como bloqueo en el alta.

**Pedido explícito de Prevención de Fraudes del Banco (Mariana Fiedotin) a Producto/Riesgos de BSF:**
- Sugiere hacer mandatorio el consumo de Totalizadores también en lo transaccional (no solo en el alta/OB), al menos jugando con umbrales — hoy es mandatorio en OB, transaccional y barrido de stock del lado del Banco, pero no está claro que así sea del lado de todas las entidades/BSF.
- Ofrece ayuda para definir/setear controles contra la CPF (Central de Prevención de Fraude de Coelsa — documentación oficial; corregido el 2026-10-09, el mail no desarrolla la sigla), citando una comunicación B de 2026 que aclara su uso obligatorio también en OB, control de stock y transaccional — sugiere, para no afectar la experiencia de usuario, un principio restrictivo inicial solo para CUITs con casos confirmados de fraude.
- Se agenda una reunión para la semana del 12/10 para seguir definiendo controles conjuntos contra cuentas mula.

**Relevancia para Producto:** esta mecánica (Totalizadores obligatorio + futuro control de inactividad) es la base de control antifraude en la apertura de CVU — relevante tanto para `onboarding` como para el proyecto `gestion_riesgo_fraude/` (PRD-238) y para `cumplimiento_normativo/` (UIF/BCRA, cuentas mula). No se identificó un propietario único de Producto para la reunión de la semana del 12/10 — a seguir en la próxima corrida de `/sync_mails`/`/sync_meetings` si se agenda invite.

> Fuente: hilo "Re: urgente bloqueo fondos..." (threadId `1a11dbf384b7d1e9`), Emma Vignoles / Mariana Fiedotin (Líder de Prevención de Fraudes BIND Banco) / Rocío Revelli, 2026-10-08 (datos identificatorios del caso omitidos por privacidad).
