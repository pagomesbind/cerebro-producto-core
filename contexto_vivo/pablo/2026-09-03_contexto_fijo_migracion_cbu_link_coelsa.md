---
id: 2026-09-03_contexto_fijo_migracion_cbu_link_coelsa
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_meetings — reunión 'Bind PSP - Próximos pasos' 2026-09-02 14:00 (docId 1UXKd5g7MgxS6Zg90IWoM0Kgy2uN-C9xeLsSetRAn7S8, con Banco Industrial), minuta Gemini"
producto: adquirencia
tema: Migración de transferencias salientes de CBU vía red Link a Coelsa, y candidatos a modelo desacoplado
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 57c0e9b
---

**Decisión acordada (2026-09-02, reunión con Banco Industrial):** avanzar con pruebas de enrutamiento de transferencias salientes de CBU larga (hoy cursadas por la red **Link**) a través de **Coelsa** en su lugar, usando cuentas específicas como piloto. Gonzalo Rivera queda a cargo de cargar un caso de prueba con una CBU larga concreta.

**Por qué:** el motivador explícito es reducir la dependencia de Link para conciliación — hoy, al salir por Link, Bind PSP no recibe una referencia utilizable para conciliar del lado propio (usa un `origin ID` interno que no se envía externamente); saliendo por Coelsa, la transferencia sí lleva un ID que permite conciliar. Alan Marchesi (Banco Industrial) aclaró que la migración no requiere homologación formal, solo una verificación técnica de garantías.

**Clientes candidatos identificados en la reunión (con volumen aproximado, sin confirmar formalmente todavía):**
- **Cucurú** — cliente Agente de Cobros y Pagos, ficha existente en `log_clientes.md` — ~100-200 transferencias/día.
- **Tienda Nube** — mencionado como candidato relevante por reclamos de latencia — ~2.000-3.000 transferencias/día, con potencial de crecer a ~10.000/día. **No tiene ficha en `log_clientes.md`** — no se puede confirmar contrato/producto/riesgo desde el Cerebro.
- Entre ambos, volumen agregado citado como referencia: "no sé, por decirte algo, 200.000 transferencias por mes" (cifra aproximada dada en la reunión, no exacta).

**Tema relacionado, discutido en la misma reunión — candidatos a migrar al "modelo desacoplado" (circuito distinto, no es lo mismo que la migración Link→Coelsa):** Alan Marchesi (Banco Industrial) preguntó qué cuentas de Bind PSP serían candidatas a migrar al esquema desacoplado — Hernán Clarich se comprometió a consultarlo con Ema/Gastón (Bind PSP) y mencionó como posibles nombres a futuro **Carrefour**, **Coto** y, más adelante, **Arcos Dorados** — sin ninguna decisión tomada todavía, solo una intención de sondeo. Los tres tienen ficha en `log_clientes.md`; Arcos Dorados además tiene proyecto vivo propio ([PRD-216](../prd-216_arcos_dorados_productos_resolve/proyecto.md)), sin relación directa con este tema hoy (se menciona "a futuro", no como parte del alcance actual de PRD-216).

**Contexto operativo adicional:** tras la salida de Personal Pay (cliente que generaba inestabilidad), Banco Industrial reporta mayor estabilidad general en los últimos 7-10 días, con tiempos de respuesta 1-2 segundos mejores en transferencias CBU — pese a 2 incidentes puntuales con Coelsa en el mismo período. Hernán Clarich se compromete a compartir estadísticas semanales de seguimiento.

> Fuente: reunión "Bind PSP - Próximos pasos" (2026-09-02 14:00), minuta Gemini. Participantes Bind PSP: Gonzalo Rivera, Mariana Nadalin, Carlos Natale, Inti Benites, Hernán Clarich. Participantes Banco Industrial: Alan Marchesi, Gisela Fernández, Ariel Matías Galano, Álvaro Aguirreburualde.

**Nota de cruce (paso de revisión hacia atrás):** el mismo día se capturó, vía `/sync_mails`, el item `2026-09-03_arquitectura_bancoindustrial_proximos_pasos` a partir de un mail de Alan Marchesi que resume esta misma reunión — ese item deja "migración CBU link a Coelsa" como pregunta abierta sin detalle ("no hay contexto previo... queda como pregunta abierta"). Este item, tomado directo de la minuta de la reunión, **responde esa pregunta**: no es un servicio de vinculación externo, es la migración de transferencias salientes de CBU larga hoy cursadas por la red Link hacia Coelsa, motivada por conciliación (ver arriba). El merge debería tratar ambos items como complementarios, no como versiones en competencia — este aporta el detalle que al otro le faltaba.
