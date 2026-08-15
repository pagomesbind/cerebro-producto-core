# Roadmap y Objetivos Estratégicos — Bind PSP

> Fuente: `raw/Actualidad.docx`, `raw/oportunity tree wallet.png`, `raw/oportunity tree cobro.png` (ingesta 2026-07-07). Complementa el contexto narrativo de [empresa.md](../overview_empresa/overview_empresa_general.md#contexto-actual-2026) y el registro de decisiones en [decisiones.md](decisiones.md).

## North Star Metrics vigentes (última indicación del CEO, 2026-07-17)

El usuario confirmó el 2026-07-17, transmitiendo indicación directa del CEO, que la empresa opera hoy con **dos North Star Metrics**:

1. **Ser el PSP top 2 en volumen operado en Banco Industrial (uso de API BANK).**
2. **Ser al menos top 6 adquirentes en volumen operado con el gateway Payway (tarjeta presente o no presente).** Nota de nomenclatura confirmada por el usuario: **Decidir, Payway y Prisma son el mismo gateway** — nombres distintos para la misma cosa, no tres destinos separados.

Estas dos métricas son exactamente los "objetivos fijados por el CEO a fines de 2025" documentados más abajo, sin cambios en la meta cuantitativa — el usuario confirmó el 2026-07-17 que el objetivo #1 sigue siendo "top 2", no un liderazgo absoluto (la formulación "el que más opera" del mismo día fue una forma coloquial de decir "top 2", no un endurecimiento de la meta). Quedan registradas también en [decisiones.md](decisiones.md) (entrada 2026-07-17).

> **Cómo se ejecuta la estrategia:** el 2026-07-17 el equipo de Producto se dividió en 3 focos estratégicos con OKR propio a fin de año (Onboarding/Pablo, Pagos FX/Luciana, Ardid/Nicolás), siempre mirando estas NSM. Ver [estrategia/index.md](estrategia/index.md).

## Estado de los OKR

Bind PSP **no tiene OKR formalmente definidos** a la fecha (2026-07-07). Lo que existe son dos objetivos de volumen que el CEO fijó a fines de 2025 como meta para el cierre de 2026 (detallados abajo). El 2026-07-07 se los había marcado como **inalcanzables** tras el incidente de fraude de marzo 2026 (ver [postmortem_transferencias_pull_marzo_2026.md](../../4_archivos/postmortem_transferencias_pull_marzo_2026.md)) y la pérdida de Astropay como cliente (ver [empresa.md](../overview_empresa/overview_empresa_general.md#contexto-actual-2026)) — pero la indicación del CEO del 2026-07-17 (ver sección anterior) los reafirma como North Star Metrics activas de la empresa, no reemplazadas.

## Objetivos fijados por el CEO (fin 2025, meta cierre 2026)

### 1. Ser el PSP cliente top 2 en volumen operado por API BANK (Banco Industrial)

Implicaba crecer aproximadamente **30%** en volumen operado mensualmente por API BANK.

**Oportunity tree — palancas identificadas para mover este número** (`raw/oportunity tree wallet.png`, archivado en `wiki/4_archivos/historial_raw/2026-07-07_ingesta_actualidad_rca_oportunity/`):

- **Ser top 2 volumen API BANK** se mueve directamente por:
  - **+ volumen OUT**, que a su vez se mueve directamente por:
    - + volumen transferencias salientes
    - + volumen pagos QR
  - **+ volumen IN**, que a su vez se mueve directamente por:
    - + volumen transferencias entrantes
    - + volumen DEBIN recurrente
    - + volumen transferencias pull

> ⚠️ **Precisión sobre las transferencias pull (usuario, 2026-07-21):** el diagrama original las agrupa enteras bajo IN, pero **Transferencia Pull Débito es OUT** (debita la cuenta de la wallet) y solo **Pull Crédito es IN**. La medición de [`/sync_metrics`](../../3_recursos/datos/metricas_semanales.md) implementa este split; el árbol de arriba se conserva tal como estaba en el diagrama de origen, con esta corrección al margen.
>
> **Scope operativo de la NSM #1** (confirmado por el usuario, 2026-07-21): las operaciones que efectivamente se cursan contra la API del banco son los tipos **1 Transferencia Saliente · 2 Transferencia Entrante · 3 Pago con QR · 6 Pull Crédito · 8 Pull Débito · 14 Debin Recurrente Crédito**, en estado Aprobada. Dólar CCL, cripto, Pago FX, QR Pix, cash-in con tarjeta, transferencias internas y Viaje QR **no suman** — son las palancas indirectas del árbol (para comprar dólares alguien primero tuvo que transferirse el saldo).
- Volumen OUT y volumen IN **se impactan indirectamente entre sí** (flecha punteada bidireccional en el diagrama original).
- **+ volumen IN** además recibe impacto **indirecto** de tres palancas adicionales:
  - + volumen dólar
  - + volumen PIX
  - + volumen FX

### 2. Ser al menos top 6 adquirentes en volumen operado con el gateway Payway (Decidir/Prisma — mismo gateway, ver nota de nomenclatura arriba), tarjeta presente o no presente

A la fecha de fijar el objetivo, la empresa **no tenía una métrica conocida** para entender cuánto le faltaba para alcanzarlo — un gap de medición, no solo de ejecución.

**Oportunity tree — palancas identificadas** (`raw/oportunity tree cobro.png`, misma carpeta de archivo):

- **Ser top 6 volumen Payway** se mueve directamente por:
  - + volumen BS (Botón Simple)
  - + volumen POS

> ⚠️ **Scope operativo de la NSM #2** (confirmado por el usuario, 2026-07-21): hoy lo que pasa por Payway es **cobro no presente con tarjeta** — tipos **6 Botón Simple** y **7 Botón 2.0**, con formas de pago 80 Crédito, 90 Débito, 60 Prepaga y 10 Crédito Cuotas, en estado ACREDITADO. **El POS presente (MPOS) todavía NO pasa por Payway**: ese proyecto no se shippeó. Se reporta como contexto en [`metricas_semanales.md`](../../3_recursos/datos/metricas_semanales.md) y hay que sumarlo a la NSM el día que se shippee (al 202629 aportaría ~+15%).
- **Volumen BS y volumen POS se impactan indirectamente entre sí** (flecha punteada bidireccional).
- **+ comercios** impacta **indirectamente** tanto a volumen BS como a volumen POS (palanca común aguas arriba de ambos).

## Por qué se consideran inalcanzables hoy

Tras el incidente de fraude de Transferencias Pull (marzo 2026, ~$11.500 millones) y la salida de Astropay como cliente, el foco de la empresa se movió a remediar compliance y auditoría exigidos por Grupo BIND: comités internos de decisión, auditorías internas reforzadas, regularización de riesgos abiertos y mejora de procesos (ver [empresa.md](../overview_empresa/overview_empresa_general.md#contexto-actual-2026) y el detalle de medidas correctivas en el [postmortem](../../4_archivos/postmortem_transferencias_pull_marzo_2026.md#6-medidas-de-mitigación-y-prevención)). A la fecha de esta ingesta no se identificó un nuevo set de objetivos que reemplace a estos dos ni un proceso formal de OKR.

## Pipeline comercial en curso

Pese al contexto, hay negociaciones avanzadas con clientes grandes que la empresa espera activar durante 2026 para empezar a captar su volumen, algunos ya en etapa de integración técnica con las APIs:

- COTO
- Arcos Dorados
- Hipódromo de Palermo

---
*Última actualización: 2026-07-17 — Confirmado por el usuario: la NSM #1 sigue siendo "top 2" en volumen API BANK (no cambió a liderazgo absoluto). Cierra el gap abierto en la actualización anterior.*
*Última actualización anterior: 2026-07-17 — Nueva sección "North Star Metrics vigentes": el usuario confirmó indicación directa del CEO reafirmando las dos NSM de la empresa (API BANK + Payway), resolviendo la nomenclatura Decidir=Payway=Prisma (mismo gateway).*
*Última actualización anterior: 2026-07-07 — Creación del archivo a partir de la ingesta de `Actualidad.docx` y los dos oportunity trees (wallet y cobro).*
