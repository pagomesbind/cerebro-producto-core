# Glosario Fintech Interno

> Términos, siglas y errores de nomenclatura recurrentes de Bind PSP. Existía como promesa rota en `wiki/index.md` desde la Fase 1 de ingesta — este archivo la cierra. Sembrado con lo ya resuelto en el Cerebro (decisiones, gaps cerrados, memoria del Bibliotecario); se amplía a demanda.

## Cuidado con la transcripción (errores recurrentes de ASR de Gemini)

- **"PCP" no existe — es PSP** (Proveedor de Servicios de Pago). Error de reconocimiento de voz recurrente en las minutas de Gemini. Cuidado especial con siglas compuestas que sí son reales y no deben "corregirse": **PSPCP** (Proveedor de Servicios de Pago que ofrece Cuentas de Pago, categoría regulatoria del BCRA) y nombres propios como **BFF.PCP** o **Portal PCP** si aparecen en fuente técnica — podrían ser términos/nombres reales, no la confusión de ASR.
- **"CBU corta" no existe — es CVU** (Clave Virtual Uniforme). Mismo tipo de error de transcripción.

## Nomenclatura de negocio

- **Decidir = Payway = Prisma** — el mismo gateway de tarjetas, tres nombres distintos usados indistintamente según el interlocutor. No son tres destinos separados (confirmado por el usuario, 2026-07-17, ver [north_star.md](direccion/north_star.md)).
- **"Solución de Cobros"** — nombre histórico conjunto de **Adquirencia + Agente de Cobros y Pagos** (mismo equipo de desarrollo detrás de ambos), no un producto separado.
- **BS / Botón Simple** — producto de cobro por link de pago de Adquirencia. "BS 2.0" es su versión con soporte de POS.
- **API BANK** — la integración de Bind PSP con Banco Industrial; unidad de medida de la NSM #1.
- **AGCyP** — Agente de Cobros y Pagos (capa multi-collector sobre API BANK, ex-CVUCollect).
- **Ardid = Akurtech** — mismo producto de monitoreo transaccional/antifraude, rebrandeado desde la v1.18 (mayo 2026). El proveedor es Pentass.
- **SISCRI** — motor de cálculo de impuestos, compartido por Adquirencia y Wallet (cada uno con su propia instancia).
- **Legajo Digital vs. Worldsys/ComplianceOne** — dos repositorios de legajo en disputa arquitectónica abierta para el foco Onboarding: Legajo Digital es el desarrollo propio de Fintexa; Worldsys/ComplianceOne es el sistema de PLD del banco. Ver el riesgo abierto en `gaps_y_preguntas.md` y el detalle en [estrategia/foco_onboarding.md](direccion/estrategia/foco_onboarding.md).
- **PLD** — Prevención de Lavado de Dinero, el área de Compliance del banco/grupo que exige el mandato de KYC/KYB del foco Onboarding.
- **KYC / KYB** — Know Your Customer / Know Your Business — validación de identidad de persona física / persona jurídica.

## Estados y flujos internos

- **`FINALIZADO`** — único estado terminal real de un ticket de desarrollo en el flujo `BACKLOG → ASIGNADO → LISTO PARA DESARROLLO → EN CURSO → EN QA → CON DEFECTO → FINALIZADO`. "`HECHO`" (usado en algún documento viejo) es el mismo estado con nomenclatura desactualizada — no es un estado distinto.
- **IDEA** — unidad de trabajo del espacio Jira `PRD` (Product Discovery), el nivel donde vive un PRD/discovery de Producto. Distinto de Epic (nivel de desarrollo, en los espacios AD/WS/OB/ARD/SER) e Historia/Error (nivel de ticket).

---
*Creado: 2026-07-20 — quinto archivo de la capa de Dirección. Se amplía a demanda cuando aparece un término nuevo con ambigüedad real (no cualquier sigla del dominio fintech genérico).*
