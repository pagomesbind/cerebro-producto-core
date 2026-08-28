---
id: 2026-08-26_gap_terra_blockchain_sucredito_cuarta_semana
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_metrics — análisis semanal, semana 202634"
producto: wallet
tema: Terra Blockchain — cuarta semana consecutiva de caída sostenida en Wallet; Sucredito reaparece en Payway
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Actualización al gap abierto **"[2026-08-04] — /sync_metrics: caídas de cliente sin explicación en la wiki
— Terra Blockchain (Wallet, -75,7%) y Sucredito (NSM#2, -70,9%)"** en `2_areas/gaps_y_preguntas.md`
(última actualización: 2026-08-18, tercera semana consecutiva).

**Nueva actualización (2026-08-26) — Terra Blockchain, cuarta semana consecutiva.** En la semana 202634,
Terra Blockchain cayó −83,6% vs. su promedio de 4 semanas ($4.003 M → $655 M) — el volumen semanal
individual más bajo de todo el histórico ingerido para este cliente. Progresión completa: −75,7% (semana
del 4/8) → −79,5% (11/8) → −87,9% (18/8) → **−83,6% (24/8)**. Cuatro semanas seguidas de caída sostenida
(con una leve mejora esta semana respecto al mínimo relativo de la semana anterior, pero todavía muy por
debajo de cualquier nivel normal del cliente).

**Verificación cruzada (2026-08-26, mismo día):** el usuario cuestionó el −83,6% comparando contra un
dashboard mensual propio de Comercial. Se recalculó Terra Blockchain con una segunda metodología
(acumulado de las últimas 4 semanas cerradas vs. las 4 previas, la misma que usa la sección de "Tendencia"
de las NSM) para descartar que la caída semanal fuera ruido de una sola semana floja: últimas 4 semanas
(202631→202634) $6.756,6 M vs. 4 semanas previas (202627→202630) $51.414,1 M — **Tendencia −86,9%**, incluso
peor que el −83,6% original. Las dos metodologías coinciden: la caída es real y sostenida en cualquier
ventana de medición, no hay diluación posible.

**Por qué importa:** cuatro semanas consecutivas de caída acelerándose en Terra Blockchain ya no admite
lectura de ruido semanal — el patrón es comparable al caso histórico de Octagon (hallazgo 6 del reporte
202629), que mostró la misma progresión antes de confirmarse la salida del cliente.

**Acción tomada esta corrida:** se creó la tarea personal **T-036** en `1_proyectos/tareas.md` (urgencia
🔴) para escalar formalmente a Soporte/Comercial el estado de Terra Blockchain — el umbral de "esperar una
semana más" ya se superó.

**Pregunta para el usuario (repetida, ahora en su cuarta semana):** ¿Terra Blockchain sigue operativo con
normalidad? Si no hay explicación de negocio conocida, corresponde confirmar el estado real con
Soporte/Comercial antes de que sea un hecho consumado.

**Estado:** Pendiente (severidad: se mantiene Media, pero con escalación formal iniciada vía T-036).

---

## Sucredito — CERRADO como falso positivo (2026-08-26, mismo día del reporte)

La mitad de este gap referida a **Tarjeta Sucredito** (NSM#2/Payway) queda **resuelta, no pendiente**. El
usuario cruzó el −60,7% reportado esta semana contra un dashboard mensual propio de Comercial (filtrado a
"Botón Simple", entidad TARJETA SUCREDITO) y no cerraba con una caída de esa magnitud. La revisión encontró
la causa: el −60,7% comparaba la última semana ($69,4 M) contra el promedio de las 4 semanas previas
($176,4 M) — una métrica que sobreestima el ruido en un cliente con alta volatilidad semanal (osciló entre
$55,4 M y $295,6 M en 5 semanas, sin tendencia direccional clara). Recalculando con la metodología de
tendencia de 4 semanas acumuladas vs. 4 previas: últimas 4 semanas (202631→202634) $688,7 M vs. 4 semanas
previas (202627→202630) $762,6 M — **Tendencia real: −9,7%**, consistente con el ~−13% que muestra el
dashboard mensual de Comercial (jul→ago, con agosto todavía sin cerrar).

**No hay caída sostenida de Sucredito.** Se retira de la escalación T-036 y del reporte de esta semana se
corrigió el hallazgo correspondiente (wiki y email) para reflejar esto. El gap original del 2026-08-04
sobre Sucredito queda cerrado — no ameritaba la alarma original.

**Insight metodológico que motiva esta corrección:** ver el item `tipo: decision`
`2026-08-26_decision_metodologia_caida_cliente_ventana_movil` — el usuario propuso (y se valida con este
mismo caso) migrar el detector de "caída de cliente" del pipeline de "semana vs. promedio de 4 semanas
previas" a "acumulado de últimas 4 semanas vs. 4 previas", igual que ya se usa para las NSM y las palancas.
Esto requiere un cambio de código en `_detectar_palancas`/`detectar()` de `pipeline.py`, fuera del alcance
de esta sesión (script espejado desde `CEREBRO_CORE`).
