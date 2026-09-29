---
id: 2026-09-28_gap_altas_cuentas_wallet_caida_sostenida
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_metrics — análisis semana 202639 (fact_cuentas 202626–202639)"
producto: wallet
tema: Altas de cuentas Wallet caen cuatro semanas seguidas (leading indicator de NSM#1), pareja en los clientes grandes, sin explicación
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: crear
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## [2026-09-28] — Altas de cuentas Wallet: cuarta semana consecutiva de caída, nivel más bajo desde fines de junio

- **Severidad:** Media
- **Descripción:** las altas semanales de cuentas de Wallet (leading indicator de NSM#1) bajan cuatro semanas
  seguidas: 202636 28.658 → 202637 25.291 → 202638 22.770 → 202639 20.469. Es el nivel más bajo desde 202626
  (22.432), −19% contra la semana equivalente del mes anterior (202635, 25.254), z-score −2,44 contra las 8
  semanas previas (media 26.738) y tendencia de ventana móvil −9,3%. La caída es pareja entre los clientes
  grandes, no concentrada en uno:

  | Organización | 202636 | 202637 | 202638 | 202639 |
  |---|---|---|---|---|
  | BSF | 11.287 | 9.154 | 8.533 | 7.372 |
  | CENCOSUD | 6.535 | 5.088 | 5.230 | 4.448 |
  | Global 66 (Argpagos psp) | 3.736 | 5.026 | 3.179 | 3.030 |
  | Credicuotas | 4.122 | 3.107 | 2.516 | 2.425 |
  | Coppel | 888 | 913 | 1.164 | 1.208 |

  Parte puede ser el mismo ciclo intra-mes del volumen (ver item `2026-09-28_gap_actualizacion_caida_202638_ciclo_intra_mes`),
  pero en agosto las altas no mostraron ese ciclo (202632 30.652 → 202635 25.254, caída más suave). No hay
  proyecto, cambio de onboarding ni estacionalidad documentada que lo explique. Posible relación a descartar:
  la actualización masiva de domicilios en cuentas Wallet del 15/9 o cambios de validación de onboarding
  recientes.
- **Pregunta para el usuario:** ¿Onboarding/Comercial tienen contexto sobre una baja de altas en BSF, CENCOSUD
  y Credicuotas desde principios de septiembre (campañas que terminaron, cambios de validación, rechazos de
  onboarding en alza)?
- **Estado:** Pendiente.
