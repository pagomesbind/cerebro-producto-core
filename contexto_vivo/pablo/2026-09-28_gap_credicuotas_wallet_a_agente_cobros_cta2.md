---
id: 2026-09-28_gap_credicuotas_wallet_a_agente_cobros_cta2
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_metrics — análisis semana 202639 (fact_operaciones + fact_transferencias_agente_cobro, 202630–202639)"
producto: transversal
tema: Credicuotas corre volumen de Wallet a Agente de Cobros desde 202636, en la misma semana en que Bind PSP liquidaciones cta 2 se apaga — sin confirmar si es migración de flujos
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: crear
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## [2026-09-28] — Credicuotas: volumen se corre de Wallet a Agente de Cobros, coincidente con el apagado de Bind PSP liquidaciones cta 2

- **Severidad:** Media
- **Descripción:** Dos movimientos de NSM#1 arrancan en la misma semana (202636, 31/8 → 7/9) y no tienen
  explicación documentada:
  1. **Credicuotas como collector del Agente de Cobros** salta de $1.533–5.419 M semanales (202630–202635) a
     $20.008 M (202636), $25.791 M (202637), $15.288 M (202638) y $13.628 M (202639). Ventana de 4 semanas:
     $74.715 M vs. $11.483 M previas.
  2. **Credicuotas como organización de Wallet** cae: ventana de 4 semanas $15.698 M vs. $22.205 M previas
     (−29%); 202639 $1.684 M (−62,4% vs. su promedio de 4 semanas). Las altas de cuentas de Credicuotas
     también bajan (4.122 en 202636 → 2.425 en 202639).
  3. **Bind PSP liquidaciones cta 2** (misma CUIT que Bind PSP SA) movía $11.029–21.246 M por semana
     (202630–202635); cae a $2.165 M en 202636 y queda en $0 en 202637, 202638 y 202639. Su caída ya se había
     marcado como hallazgo [ALTA] en 202636 ("posible cambio de cuenta o redistribución de flows — validar con
     Operaciones"), sin respuesta registrada. Bind PSP liquidaciones cta 8 también quedó en $0 desde 202637.
  Las dos fuentes (Wallet y Agente de Cobros) suman a NSM#1, así que el efecto neto sobre la métrica es
  positivo — pero si cta 2 no migró a Credicuotas, su salida (~$15.000 M semanales) está siendo tapada por
  el crecimiento de Credicuotas. No se puede determinar desde los agregados si es la misma plata cambiando de
  camino o dos hechos independientes.
- **Preguntas para el usuario:**
  1. ¿Credicuotas cambió su operatoria (p. ej. acreditación de préstamos o cobranza de resúmenes vía Agente
     de Cobros en vez de Wallet) a fines de agosto? ¿Comercial lo tiene registrado?
  2. ¿Qué pasó con Bind PSP liquidaciones cta 2 y cta 8 — se dieron de baja, se reemplazaron por otra
     cuenta, o sus flujos pasaron a Credicuotas? ¿Administración puede confirmarlo?
- **Estado:** Pendiente.
