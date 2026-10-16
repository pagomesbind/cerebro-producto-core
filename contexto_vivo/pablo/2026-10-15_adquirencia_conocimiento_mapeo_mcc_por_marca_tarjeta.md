---
id: 2026-10-15_adquirencia_conocimiento_mapeo_mcc_por_marca_tarjeta
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-10-15, 12:01)"
producto: adquirencia
tema: Cada marca de tarjeta exige su propio código MCC para un mismo site ID de Payway — el sistema hoy solo guarda uno
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/gestion_convenios_comisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Hallazgo

Daniela Collia (Fintexa) detectó, al analizar la planilla de habilitación de Payway, que múltiples comercios con QR habilitado tienen **códigos MCC (código de categoría de comerciante) distintos según la marca de la tarjeta dentro de un mismo `site ID`**. Ejemplo concreto discutido: para un mismo site ID, **Visa usa 4829** (red de cobranza), **Mastercard usa 6051**, y **Cabal/American Express usan 9311**.

## Problema

Hoy el sistema solo maneja **una única especificación/MCC general por comercio** al crearlo (junto con el rubro), sin distinguir por marca de tarjeta. Esto no es compatible con el requisito real de Payway/las marcas.

## Solución acordada

Adaptar las **tablas internas para asociar el MCC específico que cada marca de tarjeta exige**, sin intentar unificar los rubros en un solo valor. Se necesita:
- Una **columna nueva** en la tabla para diferenciar el MCC del comercio del MCC del procesador.
- El dato de origen sale de la tabla con los datos de Payway.
- Al procesar un pago, usar el MCC del comercio asociado a la marca de la tarjeta correspondiente.
- **Reutilizar y adaptar el endpoint existente de Prisma** en vez de crear uno nuevo desde cero.

## Puntos abiertos de la misma planilla de Payway (pendientes de validar directamente con Payway, a cargo de Nicolás Colón)

- Si los `site ID` de 5-6 dígitos (ej. 50210) requieren ceros a la izquierda o un largo fijo.
- El rubro de recargas (código **4813**) está programado para **darse de baja el 13 y 15 de enero de 2026** (sic — fecha tal cual surge de la minuta; podría tratarse de 2027 dado el contexto de octubre 2026, no confirmado en la fuente).
- Resolución de inconsistencias en la planilla de IDs enviada a Payway para destrabar el proceso de habilitación.

> Fuente: reunión "Análisis COBRO", 2026-10-15 12:01hs (Daniela Collia, Nicolás Colón, Pablo Gomes).
