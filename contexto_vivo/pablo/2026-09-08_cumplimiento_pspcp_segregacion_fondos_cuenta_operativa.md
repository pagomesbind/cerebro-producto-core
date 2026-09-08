---
id: 2026-09-08_cumplimiento_pspcp_segregacion_fondos_cuenta_operativa
pm: pablo
fecha_captura: 2026-09-08
fuente: "Texto ordenado BCRA 'Proveedores de Servicios de Pago', Sección 4 (PSPCP), incorporado vía Comunicación 'A' 7825 del 24/08/2023 — aportado por el usuario en `raw/A7825.pdf` durante una auditoría de cumplimiento normativo del proyecto Onboarding Estratégico."
producto: transversal
tema: Obligaciones normativas de administración de fondos y transparencia para PSPCP — segregación de fondos de clientes, cuenta operativa propia separada, traslado de retribución de saldos, leyendas obligatorias
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no — no hay archivo de canon existente que documente esta obligación específica. Complementario a 3_recursos/cumplimiento_normativo/ (que hoy cubre reportería PLD/UIF y límites operativos, no administración de fondos)."
confianza: alta
estado: en_cola
merge_commit:
---

## Qué exige la norma (Sección 4 de "Proveedores de Servicios de Pago", vigente desde Com. "A" 7825)

Para los PSPCP (proveedores de servicios de pago que ofrecen cuentas de pago — la categoría exacta de Bind PSP), el texto ordenado del BCRA exige:

1. **Disponibilidad inmediata (4.1.1.):** los fondos de los clientes acreditados en cuentas de pago deben estar, en todo momento, disponibles con carácter inmediato ante su requerimiento, por un monto al menos equivalente al acreditado. El PSPCP debe poder **identificar e individualizar los fondos de cada cliente** (no un pool indiferenciado).
2. **100% en cuentas a la vista en pesos en entidades financieras del país (4.1.2.):** todo el dinero de los clientes debe estar depositado, en todo momento, en cuentas a la vista en pesos en bancos locales. **La retribución (interés) que el PSPCP perciba por esos saldos debe trasladarse totalmente a los clientes** — el PSPCP no puede quedarse con el rendimiento de la plata de terceros. Excepción: si el cliente lo pide expresamente, el saldo puede aplicarse a "fondos comunes de dinero" en el país, informados de forma separada del resto.
3. **Cuenta operativa propia, distinta de la de los clientes (4.1.3.):** para transacciones por cuenta propia del PSPCP (pago de proveedores, sueldos, etc.) debe usarse una cuenta a la vista "operativa" (de libre disponibilidad) **distinta** de la cuenta donde están depositados los fondos de los clientes — segregación patrimonial explícita.
4. **Transparencia obligatoria (4.2.):** toda publicidad y documentación emitida por el PSPCP debe incluir mención clara y expresa de que (a) se limita a ofrecer servicios de pago y no está autorizado a operar como entidad financiera por el BCRA, y (b) los fondos en cuentas de pago no constituyen depósitos bancarios ni gozan de las garantías de depósito.
5. **Cumplimiento de normas de transferencias (4.3.):** remite a las obligaciones de "Sistema Nacional de Pagos – Transferencias" y sus normas complementarias.

## Por qué se captura como riesgo de contexto fijo, no como gap de un proyecto puntual

Esto es una obligación estructural de administración de fondos y transparencia — no es del dominio de Onboarding (que valida identidad), sino de Wallet/Ledger/Tesorería/Legal. Se captura como riesgo porque **el Cerebro no tiene ningún archivo que documente si Bind PSP cumple hoy con estos 4 puntos** (segregación de fondos por cliente, 100% en cuenta a la vista en banco local, cuenta operativa separada, leyendas de transparencia en la app/comunicaciones). Puede que ya se cumpla de facto (es una obligación de larga data, con la cuenta madre en Banco Industrial ya conocida por otros proyectos del Cerebro — ver `arquitectura_sistema/modelo_acoplado_vs_desacoplado.md`), pero no hay una verificación explícita documentada, y el punto 4.2 (leyendas de transparencia obligatorias en toda publicidad/documentación) es el tipo de requisito fácil de pasar por alto en pantallas de producto o piezas de marketing.

## Avance (2026-09-08) — respuesta parcial del PM, sigue sin cerrar del todo

Al preguntarle al PM si esto tiene que ver puntualmente con las altas de cuentas, aclaró que **hoy ya segregan fondos por cliente**, porque a cada organización integrada se le asigna una **cuenta recaudadora distinta** en el banco. Esto cubre, en principio, el punto 1 (individualización de fondos) — pero con una precisión importante sin confirmar todavía: la norma exige individualizar los fondos **de cada cliente** (persona física/jurídica titular de la cuenta de pago), y la segregación descripta es **por organización integrada** (ej. una cuenta recaudadora para Cencosud, otra para Credicuotas, etc.) — no queda claro si eso significa que también existe un sub-ledger que trackea el saldo de cada usuario final *dentro* de la cuenta recaudadora de su organización, o si el granular por-cliente termina resolviéndose en otro nivel (ej. en el ledger de Wallet, no en la cuenta bancaria en sí). Es una distinción con peso normativo: la cuenta recaudadora por organización resuelve la segregación entre organizaciones, pero la exigencia de individualizar "los fondos de cada cliente" probablemente apunta al usuario final, no al integrador.

## Qué falta para cerrar esto (sigue abierto)

Confirmar con el equipo de Wallet/Ledger: (1) si dentro de cada cuenta recaudadora de organización existe trazabilidad/sub-ledger del saldo de cada usuario final individual (no solo el total de la organización); (2) si el 100% de esos fondos está siempre en cuenta a la vista en pesos en el banco, en todo momento (sin excepciones operativas); (3) si existe una cuenta operativa propia de Bind PSP, distinta de las cuentas recaudadoras de clientes, para pagar proveedores/sueldos propios; (4) si la retribución (interés) de esas cuentas se traslada a los clientes o la retiene Bind PSP; (5) si las leyendas obligatorias de transparencia (4.2.1/4.2.2 — "no somos entidad financiera", "sin garantía de depósito") están presentes en la app y en materiales de marketing/comerciales.
