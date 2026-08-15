# Lending — discovery de crédito embebido en Wallet (nunca construido)

> Estado: discovery — no construido.

> Fuente: Notion histórico, Epics **"Lending - Préstamos individuales"** y **"Lending - Pagar QR con línea de crédito"** (ambas quedaron en **Discovery - Priorización**, sin desarrollo). Se documentan como discovery de producto genuino — el modelo de negocio y la arquitectura de terceros están completamente definidos aunque nunca se haya construido nada.

## 1. Modelo de negocio: BindPSP como middleware entre la wallet y un scorer externo

Ambas iniciativas comparten el mismo patrón arquitectónico: **Bind PSP no otorga crédito ni hace scoring propio** — actúa como middleware entre la billetera cliente y un proveedor de crédito externo (**Credicuotas**, mencionado explícitamente en los flujos). El crédito, el scoring y el riesgo crediticio quedan en la empresa proveedora; Bind PSP orquesta el flujo de datos y los movimientos de dinero (siempre vía CVU, siempre "as a service").

## 2. Préstamos individuales — journey completo (5 etapas)

1. **Onboarding de usuarios potenciales (análisis crediticio, batch mensual)**: la billetera comparte su base de usuarios con Bind PSP (API o batch seguro, con contrato de privacidad), Bind PSP la reenvía a Credicuotas (DNI, CUIT/CUIL, teléfono, email, CVU, movimientos), Credicuotas calcula scoring y devuelve una lista de usuarios precalificados con monto máximo, tasas y plazos. Bind PSP normaliza y expone esto vía API a la billetera. **Nota explícita**: Bind PSP no marca ni guarda en sus propias bases qué cuentas son aptas para crédito — ese dato vive del lado de Credicuotas.
2. **Simulación de oferta en tiempo real**: el usuario pide simular un monto en la app; Bind PSP consulta en vivo a Credicuotas y devuelve combinaciones de monto/tasa/plazo/cuota/CFT.
3. **Originación del préstamo**: el usuario acepta una oferta y los T&C particulares (provistos por Credicuotas); Bind PSP transmite la instrucción, Credicuotas registra el crédito y ordena el fondeo **desde su propia cuenta recaudadora en Bind PSP hacia la CVU del usuario** — la transferencia es **interna dentro de Bind PSP, sin pasar por Coelsa** (ambas cuentas recaudadoras viven en la misma plataforma).
4. **Consulta de estado de deuda**: Bind PSP consulta a demanda o recurrentemente el estado a Credicuotas (saldo, cuotas, vencimientos, mora) y lo traslada a la billetera.
5. **Cobranza de cuotas**: Credicuotas expone diariamente qué usuarios tienen cuotas vencidas; Bind PSP debita de la CVU del usuario (total o parcial según saldo disponible) e informa el resultado tanto a Credicuotas como a la billetera (que gestiona la experiencia de mora con el usuario final).

**Decisión de alcance explícita**: no hay gestión de "línea de crédito" (saldo disponible reutilizable) — cada préstamo es una originación puntual (*ad hoc*), no un crédito revolving. No incluye BNPL ni créditos recurrentes automáticos. Diseñado para escalar a otros canales de originación (QR, ecommerce, link de pago) — puente conceptual hacia la segunda Epic.

## 3. Pagar QR con línea de crédito — variante "crédito revolving" nunca resuelta

A diferencia de la anterior, esta Epic sí contempla una **línea de crédito viva** (revolving) desde la cual el usuario puede pagar QR tomando préstamos sucesivos. Alcance definido: consultar ofertas de "credicuotas" para una cuenta/CUIT, aceptar la línea, leer un QR y pagarlo con un préstamo originado de esa línea, consultar detalle/estado de la línea activa, y cobro automático de cuota debitando saldo en una fecha durante un plazo acotado.

**Quedó con preguntas de diseño abiertas y sin resolver** (evidencia de por qué nunca avanzó a desarrollo):
- Si se acredita el saldo del préstamo pero el pago QR posterior falla, ¿cómo se revierte? (sin definición).
- Si el usuario pide **N préstamos QR** con distintos montos/plazos sobre la misma línea, ¿paga **N cuotas separadas** o una cuota mensual consolidada? (sin definición — pregunta de diseño financiero no trivial, condiciona todo el modelo de cobranza).

Supuestos ya fijados: sin marca de aptitud crediticia en las BD de Wallet (igual que en préstamos individuales), y **sin cargo adicional de Bind PSP** sobre el crédito (a diferencia de otros productos financieros de Wallet como CCL o FCI, acá no hay un x/y de comisión propia contemplado en el discovery).

## Ver también

- Patrón similar de "Bind PSP como middleware sobre proveedor externo" en [cuenta_remunerada_fci.md](cuenta_remunerada_fci.md) (IVSA/Poincenot como gestor del FCI) y en [crypto.md](crypto.md) (Lirium como exchange).
