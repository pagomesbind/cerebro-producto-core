# Cuotas y Campañas (CFT) — Adquirencia

> Estado: en producción.

> Fuente: Notion histórico, Epic **"Cuotas CFT cliente: POS"** (⭐ Epics, tipo Negocio, lanzada ~fines de 2024\*). Mecánica del pago en cuotas con tarjeta de crédito y del módulo de Campañas que traslada el costo financiero total (CFT) al cliente final.

## 1. Qué resuelve

Permitir que un comercio ofrezca pago en cuotas con tarjeta de crédito (MVP: canal POS, extendible a Botón Simple) **sin absorber el costo financiero**: el cliente final paga un recargo sobre el importe original, y con ese recargo Bind PSP paga el CFT al procesador.

## 2. Modelo de Campañas

La pieza central es el módulo de **Campañas** (+ una **API Promociones** propia):

- **Fórmula**: `CFTcliente (monto) = índiceCFTcliente × importe`. El cliente paga `importeBruto = importeOriginal + CFTcliente`.
  - Ejemplo: campaña de 3 cuotas con índice 1.1 → transacción de $1000 en 3 cuotas → el cliente paga $1100.
- **Dimensiones de una campaña** (diseñado genérico para poder reutilizarlo a futuro en descuentos o reintegros):
  - Cuotas (3, 6, 12, 30…), con prioridad y `codigoCuotasProcesador`.
  - Índices separados por actor: `cftcliente`, `cftcomercio`, `cftEntidad` (cada uno con su descripción).
  - Canal: uno, varios o todos (MVP: POS y/o Botón Simple).
  - Medio de pago: uno, varios o todos (MVP: tarjeta de crédito).
  - BIN de tarjeta: uno, varios o todos (MVP: todos).
  - Vigencia: fecha de inicio y fin; opcionalmente días específicos (MVP: todos los días).
- **Herencia**: la campaña puede definirse a nivel **Entidad** (la heredan sus comercios) o ser **específica de un comercio**.
- **Fallback**: si el comercio/entidad no tiene campaña para la combinación dada, se cobra normal (1 cuota, sin recargo).
- **Trazabilidad**: la transacción guarda el **id de campaña aplicada**, para saber qué campaña afectó cada cobro.

## 3. Impacto contable y en liquidaciones

- **Forma de pago separada**: crédito en 1 cuota = forma de pago 80; crédito en cuotas = forma de pago propia — la razón de negocio es poder asignar **comisiones y plazos de liquidación distintos** al cobro en cuotas.
- En la **liquidación** del comercio: el total de CFTcliente aparece sumarizado en el resumen, y el detalle de transacciones muestra una columna adicional con el CFT que pagó el cliente. El dato de CFT también se actualizó en el **PDF de liquidaciones**.
- Pregunta que quedó abierta en la definición original: **sobre qué importe se calculan los impuestos al comercio** (original vs bruto) — verificar cómo quedó implementado.

## 4. Superficies tocadas

- **API Promociones** (nueva).
- **SDK** de cobro adaptado para cuotas.
- **APK POS**: pantallas nuevas de selección de cuotas.
- **Detalle de transacción** con info de cuotas en las tres vistas: Admin, Portal comercio y POS.
- **Devolución de un cobro en cuotas** (flujo de devolución adaptado).

## 5. Estado al freeze del Notion

Todo en producción salvo el ticket principal **"Campaña CFT a cargo del cliente (inserción de transacción) (POS)"** (XL), que quedó **En Staging** — verificar en Jira/producción si el cálculo de recargo por campaña llegó a producción o si el esquema vigente es otro.
