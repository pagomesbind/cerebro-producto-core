---
id: 2026-10-08_conocimiento-cliente-credicuotas-consultas-blacklist-akurtech-y-cvu-propia-fondeo-q4
pm: nicolas
fecha_captura: 2026-10-08
fuente: "Mail 'Consultas: integración con Akurtech (Ardid) y circuito de fondeo de wallet' — Rodrigo Novas (Credicuotas) 2026-10-07; Gonzalo Santos (Credicuotas) 2026-10-08"
producto: ardid
tema: Credicuotas — dudas sobre blacklists y reglas de Onboarding de Ardid (Akurtech) frente a su proyecto "Lista 15", y plan Q4 de una CVU propia en la PSP para separar el fondeo de la wallet
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Complementa la sección `## CREDICUOTAS` de `casos_de_uso_clientes.md` ("Particularidades / cronología"). Sigue a los items `2026-10-02_conocimiento-cliente-credicuotas-producto-apim-credenciales-stg-y-pedido-endpoint-segmento` y `2026-10-06_conocimiento-cliente-credicuotas-pedido-publicacion-apim-stg-y-minuta-consumo-datos`.

- **2026-10-07. Consultas de Credicuotas sobre la integración directa con Ardid (Akurtech)**, enviadas por Rodrigo Novas a Bind (Emma Vignoles, Nicolás Colón, Rocío Revelli), Pentass y Poincenot. Piden respuesta rápida, sobre todo de login y onboarding. Lo que muestran las preguntas:
  - **No tienen claro cómo se relacionan la blacklist de Akurtech y las de BIND.** Preguntan si se cruzan, si Akurtech tiene reglas propias que alimentan su blacklist o si la tienen que cargar ellos, si pueden usar las blacklists del grupo BIND dentro de Akurtech y si Akurtech les puede compartir blacklists de sus otros clientes.
  - **Tienen un proyecto propio, "Lista 15"**, para consumir la blacklist de BIND y bloquear desde su propio producto. Preguntan qué agrega la blacklist de Akurtech frente a eso y si con Lista 15 ya cubren la necesidad sin Ardid. Es una señal de que Credicuotas evalúa si necesita las reglas de blacklist de Ardid.
  - **Entienden que las reglas de Onboarding de Ardid son solo de blacklist.** Preguntan si aplican solo en el alta o en cualquier momento (ingresos, salidas, pagos QR, login) y, si es lo segundo, en qué se diferencian de las reglas reputacionales, que también consultan blacklists.
  - **Preguntan si Akurtech permite reglas en modo testing** antes de activarlas, y si eso es el ambiente de staging.
- **2026-10-07. Iniciativa Q4 de Credicuotas: reestructurar el circuito de fondeo de la wallet.** Evalúan abrir una **CVU dentro de la PSP a nombre de Credicuotas** que concentre la cobranza de recurrencia y los consumos con línea de crédito, separada de los movimientos hacia terceros (Tapi/Gire). Preguntan qué restricciones hay para movimientos internos entre cuentas (montos máximos, cantidad diaria) y si el **límite diario de transferencias hacia Tapi** que ya conocen aplica también a los movimientos internos hacia esa CVU o solo a las salidas externas.
- **2026-10-08.** Gonzalo Santos (Head de Producto de Credicuotas) insistió y le preguntó a "Lore" (Lorena Macedo, Pentass) si las vio. Sin respuesta de Bind a la fecha de esta captura. Tarea del PM: T-117 en `1_proyectos/tareas.md`.

**Lectura:** es el tercer frente abierto con Credicuotas en una semana (credenciales STG del APIM, endpoint de segmento, y ahora blacklists y fondeo). El plan de CVU propia cambia cómo usan Wallet: pasan de mover fondos solo hacia terceros a tener una cuenta concentradora interna.

> Fuente: Mail "Consultas: integración con Akurtech (Ardid) y circuito de fondeo de wallet" — Rodrigo Novas (2026-10-07), Gonzalo Santos (2026-10-08).
