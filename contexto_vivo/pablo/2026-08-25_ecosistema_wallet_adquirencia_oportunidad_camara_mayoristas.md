---
id: 2026-08-25_ecosistema_wallet_adquirencia_oportunidad_camara_mayoristas
pm: pablo
fecha_captura: 2026-08-25
fuente: "/idea_start — discovery de comercios_mayoristas, retomando un discovery externo (Notion, dic-2025 a mar-2026) del propio PM"
producto: ecosistema_wallet_adquirencia
tema: Ecosistema financiero cerrado para comerciantes de la cámara de supermercados mayoristas
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## Qué es la oportunidad

Una cámara de supermercados mayoristas (agrupa a Diarco, Yaguar, Maxiconsumo y otros — cliente contractual único, no cada mayorista por separado) contactó a Bind PSP en 2026-03 buscando construir su propio ecosistema financiero cerrado (cobro + wallet) para los comerciantes que le compran mercadería (almacenes, autoservicios, supermercados chinos — ~50% de los compradores de estos mayoristas). Hoy esos comerciantes cobran con plataformas externas (PVS, Código Pago) que no le dan ninguna participación al mayorista, pese a que es él quien financia las promociones que esos comerciantes aprovechan. El contacto se enfrió y **volvió a manifestar interés activo** — hay una demo pautada con la cámara para 2026-08-26 mostrando las capacidades actuales de Bind aplicables a este journey.

## Dimensión de mercado (sin verificar externamente)

+6.500 comercios, +14M transacciones/mes, +$337.000 M de volumen/mes agregados — cifra de un discovery previo del propio PM (2026-03), confirmada como "vigente" pero sin ningún mail/acta de la cámara que la respalde todavía. Equivaldría a ~61% del NSM#1 actual (volumen API BANK, $548.736M en jun-2026) si se materializa.

## Señal de demanda

- La cámara reactivó el interés después de ~6 meses de silencio (fuente: PM, vía sector comercial, sin mail/acta propia).
- **Maxiconsumo**, uno de los mayoristas nombrados, ya es cliente directo de Bind PSP — inició integración a Wallet y Onboarding y la pausó cuando surgió este proyecto de cámara más grande (entendimiento del PM, no confirmado formalmente con el account de Maxiconsumo).
- Coincide con el patrón que Bind ya usa en la práctica para priorizar ("driver comercial concreto": cliente/prospecto real presionando — mismo patrón que Arcos Dorados, Coppel, La Virginia).

## Por qué es una oportunidad y no solo una IDEA más

Gran parte de la base técnica necesaria ya existe en producción: el patrón de entidades (mayorista→comercios, cada uno con cuenta+CVU propia) se apoya en piezas ya construidas de **Agrupador Mayorista** (ABM de canales de cobro, ABM de roles/AccessManagement 2.0) y **SUR FINANZAS** (plataforma multi-comercio white-label Wallet+Adquirencia). No es un producto desde cero.

## Estado y condición de reactivación

El discovery completo (`1_proyectos/comercios_mayoristas/proyecto.md`) se cerró el 2026-08-25 en **Gate 2: 🟡 Diferido** — no se justifica gastar esfuerzo de desarrollo sin un acuerdo comercial cerrado con la cámara (choca con la restricción de capacidad del equipo, ~1 IDEA cada 3 meses, y no encaja en ningún foco 2026 vigente). Decisión textual del PM: *"al ser un proyecto tan grande, de tal envergadura, y profit y transacciones, se convierte en un proyecto estratégico... si eso sale, será prioridad número 1."* **Condición de reactivación: cierre de acuerdo comercial entre Bind y la cámara.** Si eso ocurre, el proyecto pasa a ser prioridad #1, por encima del foco Onboarding vigente (liderado por el mismo PM).

## Fuente completa

`1_proyectos/comercios_mayoristas/proyecto.md`, `decisiones.md` y `gaps.md` — discovery completo con tabla de evidencia Gate 2, 7 referencias del discovery externo original, y el registro de las 2 rondas de preguntas al PM.
