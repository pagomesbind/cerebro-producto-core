# 🔀 Patrones Transversales — Cartera de Clientes Bind PSP

> Síntesis viva construida sobre los ~200 brochures de `casos_de_uso_clientes.md`. Responde: ¿qué versatilidad demuestran nuestros productos en la práctica?, ¿qué rangos de pricing se repiten?, ¿qué arquetipos de caso de negocio existen? Se regenera/ajusta cada vez que `/sync_customers` detecta un patrón nuevo o rompe uno existente.
>
> **Base:** 200 clientes (102 En producción, 6 En producción+Evolutivo, 16 En integración, 10 En negociación, 24 Frenado, 33 Cliente no cerrado, 1 Sin Iniciar [fila basura], 8 Dado de baja).

## 1. Versatilidad de cada producto canónico por rubro

### Adquirencia (QRI, Botón de Pago, POS, RxT)
El producto más transversal de la cartera — aparece en prácticamente todos los rubros:
- **Retail/supermercados grandes** (COTO, Carrefour/BSF, Cencosud, La Anónima, Diarco): QR Aceptador con N comercios bajo un mismo CUIT liquidando a una única CVU; foco en escala (proyecciones de cientos de miles de comercios/clientes).
- **Agrupadores de pagos** (Málaga/MoPago, Crowder, Cobro Express, Benajal/Jony, PMI): "modelo Spena/Gallo/Kellerhoff" de sub-agregación — un CUIT agrupador recibe todo el flujo y reliquida a subcomercios vía CVU propia, con front desarrollado por ellos mismos.
- **Turismo/viajes y transporte** (Best Bus, Crucero del Norte, Travel Rock): RxT como canal preferido para cobros de pasajes/paquetes de alto ticket.
- **Impuestos y servicios / cobradores de terceros** (Waya, RIPSA/Grupo DESA, E-Cobro): arancel reducido (MCC 9311) para actividad de cobro de servicios públicos/impuestos.
- **Eventos** (Ticket QR): RxT en caja única, sin relación 1:1 CVU-evento.
- **Expensas cross-border** (Binco/Plexo): RxT+QRI como origen de un flujo de expatriación Argentina→Uruguay.
- **Gambling/Juego** (Grupo Slots-Jugadón, Monnet, Directa/ERON): RxT para fondeo de saldo de juego + Agente de Pagos para acreditación de premios; alto escrutinio PLD.

### Wallet (PSP-as-a-Service / Wallet-as-a-Service)
Segundo producto más transversal, con dos sub-patrones claros:
- **Marca blanca para no-financieras** (Astropay, TCash/E-Cobro, La Anónima, Coppel, Arcos Dorados, Vecinos app, House4you): empresas de otros rubros (retail, gambling, delivery, marketplace) que quieren ofrecer cuentas/CVU a sus usuarios sin construir un PSP desde cero — Bind licencia la infraestructura.
- **Expatriación/cross-border FX** (Global 66, Inswitch, House4you, Binco/Plexo, Directa/ERON): CVU en pesos + operatoria CCL/USDT para comprar divisas y transferir al exterior, bajo la figura de Agente de Cobros y Pagos.
- **Cuentas eco-cerrado / menores de edad** (Arcos Dorados/McDonald's, GST/Hipódromo): saldo restringido a un ecosistema controlado, con reglas de edad mínima y QR de monto cerrado.
- **Revenue share vía Cuenta Remunerada/FCI** (La Virginia, Coppel, Consorcio Abierto, Diarco): retrocesión de un % de la comisión de inversión al cliente, usado como palanca comercial (paridad de TNA exigida por algunos clientes grandes).

### Agente de Cobros y Pagos
El más especializado — casi siempre acoplado a un flujo de **expatriación de fondos** o a un **agrupador con pass-through internacional**:
- Astropay, Directa/ERON, House4you, Global 66: reciben ARS localmente y liquidan en USD/exterior a través de Bind como Agente de Cobros y Pagos.
- Row Payments/Koywe: cross-border para turistas + lectura QR vía exchange cripto (Bybit).

### Onboarding
Casi siempre acompaña a Wallet o Adquirencia como habilitador de altas masivas — nunca aparece solo. Casos de referencia: COTO (proyección 100k→650k clientes), Arcos Dorados (OB mínimo por DNI + cuentas de menores), Diarco (superapp retail).

## 2. Patrones de pricing observados

> Rangos observados en fichas con datos numéricos concretos — útil como referencia para estimar casos de negocio nuevos, no como tarifario oficial (cada contrato tiene su propia negociación).

| Concepto | Rango típico observado | Notas |
|---|---|---|
| **QR Aceptador (arancel aceptador)** | 0,8% (estándar) | Prácticamente uniforme en toda la cartera — Coelsa limita comisión por rubro a nivel PSP (0,6%-0,8% para la mayoría de los rubros, ver [decisiones.md](../direccion/decisiones.md)). |
| **RxT** | 0,25%-0,6% (Frenado/Negociación), 0,35%-0,49% (Dado de baja/No cerrado) | Fee COELSA subyacente ~0,05% + margen administrativo ~0,55%. |
| **Cash in / cash out (Wallet)** | 0,20%-0,35% (mín $20, máx $350) o montos fijos ($5-$17 por operación) | Los agrupadores grandes negocian montos fijos por operación en vez de porcentaje. |
| **CVU activa mensual** | USD 0,10-0,10 (bonificado escalonado por volumen) o $10 fijos en pesos | Bonificaciones agresivas los primeros 6 meses hasta cierto umbral de CVUs activas. |
| **Onboarding (por alta/validación)** | USD 1-1,5/alta, o escalonado $15-$25/validación según volumen mensual | Escalonado inverso: a mayor volumen, menor costo unitario. |
| **Setup inicial** | USD 1.500 (chico) → USD 10.000-25.000 (agrupador mediano) → USD 45.000-70.000 (integración compleja/cross-border grande) | Frecuentemente 50% a la firma + 50% al pase a producción; bonificaciones de 10-50% negociadas. |
| **Abono mensual / licencia PSP** | USD 1.500-5.000/mes (agrupadores) → USD 10.000-50.000/mes (clientes grandes con mínimo de facturación garantizado) | |
| **Módulo Agrupador** | USD 1.500-5.000/mes | Adicional a la licencia PSP base. |
| **Tarjeta de Débito / Crédito (arancel adquirente)** | TD ~1,1-2,5% · TC ~2-3% (+ 0,3% adicional en algunos contratos) | |
| **Retrocesión/revenue share (Cuenta Remunerada FCI)** | ~30-40% de la comisión de inversión | Palanca comercial en clientes con volumen alto de saldo ocioso. |

## 3. Arquetipos de caso de negocio

1. **Agrupador de pagos / sub-agregación** ("modelo Spena/Gallo/Kellerhoff/One Pay"): un CUIT central agrupa N subcomercios, cada uno con su propia CVU, reliquidados por el agrupador. Repetido en >15 clientes de rubros muy distintos (retail, servicios, expensas, gambling).
2. **PSP/Wallet-as-a-Service para no-financieras**: empresas de retail, delivery, gambling o marketplace que licencian infraestructura de cuentas/CVU de Bind para ofrecer una billetera propia sin ser ellas mismas un PSP regulado.
3. **Recaudador de recaudadores / cripto-expatriación**: exchanges y fintechs (Inswitch→Binance, Directa/ERON, Global 66) que usan Bind como puente entre recaudación local en ARS y liquidación en USD/USDT en el exterior.
4. **Cobrador sectorial de impuestos/servicios con arancel reducido**: cooperativas eléctricas, entes de impuestos, distribuidoras (RIPSA/Grupo DESA, Waya, Cooperativa Eléctrica) que operan bajo MCC 9311.
5. **Superapp retail**: cadenas grandes (Coppel, La Virginia, Diarco, Carrefour/BSF) que combinan Wallet + Onboarding + FCI + créditos en una única app para sus clientes.
6. **Cross-border de nicho geográfico**: flujos ARS↔USD/otras monedas atados a un caso puntual (expensas Punta del Este vía Binco/Plexo, apuestas del exterior vía Directa/ERON, remesas vía Tap Tap Send).
7. **Integrador/reventa técnica (no cliente final)**: partners que revenden la tecnología de Bind a sus propios clientes bajo revenue share por producto (Cuoma/Pax Manager, Remitee "PSP para PSPs").

## 4. Motivos de baja / freno más comunes

- **Precio no competitivo** frente a la solución actual del cliente (Fiserv, otros PSP) — motivo repetido en varios "Frenado".
- **Facturación mínima no alcanzable** para el cliente (mínimos mensuales fijos vs. volumen real esperado).
- **Compliance/PLD no superado** — rechazo por no aceptar hacer onboarding a sus propios clientes finales (Directa/ERON) o por perfil de riesgo alto sin resolución (varios "Frenado" y "No cerrado").
- **Incumplimiento de piloto productivo** pactado como condición de arranque (Málaga/MoPago).
- **Inactividad post-contrato** sin uso real del servicio contratado (E-Cobro).

---

*Última actualización: 2026-07-07 — cierre de la carga inicial completa (200/200 clientes). Se debe revisar y ajustar en cada corrida de `/sync_customers` que aporte casos nuevos relevantes a alguna de estas secciones.*
