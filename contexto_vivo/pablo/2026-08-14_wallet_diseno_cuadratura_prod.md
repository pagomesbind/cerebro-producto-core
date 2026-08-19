---
id: 2026-08-14_wallet_diseno_cuadratura_prod
pm: pablo
fecha_captura: 2026-08-17
fuente: "/sync_mails — mail \"Diseño de Cuadratura en prod - Wallet\" (threadId 1a001dfe2bf40326), Mariana Nadalín/mvila@bind.com.ar, 2026-08-14"
producto: wallet
tema: Diseño técnico de los archivos de cuadratura (resumen de saldos y comprobantes) para publicar en la Web
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/conciliacion_y_totalizadores.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Fuente:** mail enviado a Pablo Gomes y Nicolás Colón con el diseño formal de los archivos de cuadratura, para publicar en la Web (mismo criterio que los archivos de movimientos/saldos ya documentados en `conciliacion_y_totalizadores.md`).

**Dos archivos nuevos:**
- `CUADRATURA-RESUMENSALDOS-{{codigoOrganizacion}}-AAAAMMDD`
- `CUADRATURA-RESUMENCOMP-{{codigoOrganizacion}}-AAAAMMDD`

**Formato:** delimitado por punto y coma (`;`). Se genera un archivo diario, agrupado y zipeado por fecha de proceso, con la misma lógica de generación que los archivos de movimientos ya existentes — **solo se generan en días hábiles**.

**`CUADRATURA-RESUMENSALDOS` — campos:** Fecha, Saldo CVU, Saldo S/extracto, Diferencia, Consumos.
- **Saldo CVUs**: sumarización (suma/resta) de los saldos de todos los CVU de la organización al cierre del día.
- **Mov Extracto**: sumarización (suma/resta) de todos los movimientos registrados en el extracto bancario en esa fecha.
- **Saldo S/Extracto**: saldo al cierre del día — se toma el valor del último movimiento del día en el extracto.
- **Diferencia**: cálculo entre Saldo CVUs y Saldo S/Extracto. **Si es negativo, es observado por el BCRA** — los saldos de las CVU deben ser iguales o menores a los saldos de la cuenta recaudadora (CBU).
- **Consumos**: sumarización (considerando el signo) de los comprobantes de la organización.
- Ejemplo de fila: `11/12/2024;22302808.70;19051866.42;22369580.41;66771.71;19060113.41`

**`CUADRATURA-RESUMENCOMP`:** contiene el consumo del saldo del día, desagregado por tipo de comprobante.
