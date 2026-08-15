# Guía: Comercios y Transacciones (CORE) — Adquirencia

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/guia-transaccion (y https://psp.bind.com.ar/developers/apis/guia-comercio)
> Producto: Adquirencia / Soluciones de Cobro

---

## Guía: ¿Cómo integrar Transacciones?

"Con este producto la entidad puede utilizar distintos canales de cobro. Puede integrarse a uno o varios canales de cobro según sus necesidad de negocio."

"La transacción es la entidad más importante que compone el producto de adquirencia. Centraliza el resultado de cualquier canal de cobro (QR, Botón simple, Recaudación por transferencia, POS, etc)."

"Mediante el proceso de liquidación el sistema calcula automáticamente el importe neto que corresponde cobrar a un comercio por cada transacción."

"El momento de liquidación de cada transacción se realiza según el plazo de acreditación que le corresponda."

---

## Guía: ¿Qué debes saber sobre los comercios?

"La entidad puede crear los comercios desde donde operará con las cobranzas. Cada comercio tiene los datos que se utilizarán luego para calcular los impuestos (CUIT, domicilio, condiciones impositivas, etc)."

Las sucursales permiten "separación física o conceptual de los cobros a recibir."

"La caja es obligatoria para poder cursar una transacción por cualquier medio de pago."

## Flujo — Estructura y ciclo de vida de una transacción

```
ESTRUCTURA JERÁRQUICA (configurar una vez):
  Entidad
    └── Comercio (datos CUIT, domicilio, condición impositiva → usados para impuestos)
          └── Sucursal (separación física o conceptual de los cobros)
                └── Caja (obligatoria para cursar cualquier transacción)

CICLO DE VIDA DE UNA TRANSACCIÓN:
  1. Canal de cobro genera una transacción (QR, Botón simple, RXT, POS, etc.)
     → Transacción queda registrada con estado inicial

  2. Bind PSP dispara EVENT webhook → entidad es notificada en tiempo real

  3. LIQUIDACIÓN (según plazo de acreditación "convenio" por comercio + medio de pago):
     → Puede ser en línea (liquidación inmediata) o diferida (días hábiles posteriores)
     → Sistema calcula: monto bruto - impuestos - comisiones = importe neto a acreditar
     → Cálculo de impuestos SIEMPRE es asincrónico (incluso en liquidación en línea)
     → Si la entidad usa Wallet: crea comprobantes en el CVU del comercio (ver guia-cobrosenwallet)

  4. Consulta: GET /consultar-transacciones (filtros: comercio, fecha, canal, estado, etc.)
```

## Jerarquía Estructural

```
Entidad
  └── Comercio
        └── Sucursal
              └── Caja
```

Cada elemento de esta jerarquía es configurable y forma la base para las operaciones de cobro.

## Endpoints Disponibles (Slugs Reales del Portal)

| Slug Real | Método | Operación |
|-----------|--------|-----------|
| `./comercio-crearsucursal` | POST | Crear sucursal |
| `./comercio-modificarsucursal` | PUT | Modificar sucursal |
| `./comercio-crearcaja` | POST | Crear caja |
| `./comercio-modificarcaja` | PUT | Modificar caja |
| `./comercio-eliminarcaja` | DEL | Eliminar caja |
| `./consultar-transacciones` | GET | Consultar transacciones |

> Nota: Los comercios se crean/gestionan fuera del portal API (configuración manual). El portal no expone endpoints de crear/consultar/habilitar comercio directamente.
