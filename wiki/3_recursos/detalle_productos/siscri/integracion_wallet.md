# Integración SISCRI ↔ Wallet — cálculo de impuestos por comprobante

> Estado: en producción.

> Fuente: Notion histórico, Epic **"Impuestos en Wallet"** (~97 SP, ~42 tickets — la Epic normativa más grande relevada en Wallet). Cubre la instancia de SISCRI orientada a **personas** (cuentas de Wallet), complementaria a [configuracion_entidades.md](configuracion_entidades.md) (orientado a comercios/Adquirencia). Ver también el rol general de SISCRI en [siscri/index.md](index.md).

## 1. Modelo de integración: asíncrono, no bloqueante

Decisión de diseño central de toda la Epic: **el cálculo de impuestos nunca bloquea ni condiciona la operación original**.

- Wallet envía el comprobante a SISCRI (API de Persona) para calcular impuesto; SISCRI confirma recepción y calcula de forma asíncrona.
- **Si falla el cálculo de impuesto** (error de sistema, configuración o negocio) **igual se deja crear el comprobante original**.
- **Si falla la creación del comprobante de débito por el impuesto**, igual se deja operar — el débito por impuesto se reintenta después, cuando el usuario tenga saldo (vía cola de **recycle**, mismo motor genérico de reintentos documentado en otras partes de la wiki de Wallet).
- Ejemplo explícito: si un cliente transfiere y a su cuenta le corresponde retener impuestos, **puede transferir el importe total sin restricción** — el comprobante de débito por impuesto queda pendiente de aplicar cuando tenga saldo, no bloquea la transferencia.
- Parámetros de reintento configurables por tipo de operación: distancia inicial entre reintentos (default 5 min hasta 3 intentos), distancia final entre reintentos (default 1 hora), y tiempo total activo del esquema (default: nunca vence — el cobro del impuesto puede reintentarse indefinidamente salvo que Bind PSP decida explícitamente dejar de intentarlo).

## 2. Tipos de comprobante de impuesto (nuevos, de sistema)

| Código | Significado | Se aplica a |
|---|---|---|
| `IMPD` | Impuesto al débito | Solo comprobantes originales de débito |
| `IMPC` | Impuesto al crédito | Solo comprobantes originales de crédito |
| `IMPS` | SIRCUPA | Se agrega junto a IMPD o IMPC cuando corresponde |

Cada comprobante de impuesto lleva como `idComprobanteRelacionado` el id del comprobante original que lo generó — clave para poder reversarlo o rastrearlo.

- **Alta de Cuenta como Persona en SISCRI**: ocurre al crear la cuenta+CVU (vía Onboarding o directo), guardando `FechaAltaSiscri` en la cuenta para saber si el alta fue exitosa.
- **Parametrización por Organización + Tipo de Comprobante**: no todos los tipos de comprobante de todas las organizaciones deben calcular impuesto — es configurable, explícitamente para minimizar el volumen de comprobantes enviados a SISCRI (control de costo/carga, no solo de negocio).
- **Arquitectura async por lote vs. individual**: se construyeron dos caminos de cálculo — por lote (para volumen) y cálculo individual por transacción — cada uno con su propio spike de análisis previo al desarrollo.

## 3. Reversa de impuestos (quedó "Listo para desarrollo", no confirmado si se construyó)

Problema de negocio real: si una operación termina **rechazada**, el cliente no debe pagar impuestos por ella. Diseño elegido (Opción 2, menor impacto sobre el proceso existente): ante el rechazo de una operación, según en qué etapa esté el cálculo de impuesto —

1. Si el cálculo aún está pendiente → cancelarlo.
2. Si ya se calculó y hay comprobantes de impuesto pendientes de crear → eliminarlos, nunca crearlos.
3. Si ya están en la cola de recycle esperando reintento → sacarlos de la cola.
4. Si el comprobante de impuesto **ya se creó y debitó** → generar un comprobante de **reversa** (crédito) por cada uno, con códigos dedicados (`DEV_SIRCUPA`, `DEV_SIRCUPA_TUC`, `DEV_IMPD`, `DEV_IMPC`).

## 3.1 ComprobanteId en el webhook de operaciones (Jira PRD-61)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA **PRD-61** "Impuestos wallet ajustes para integrarse" (Finalizada) → Historia **WS-37** (vínculo directo, sin Epic intermedio).

- **Problema**: cuando se aplica un impuesto en Wallet, el comprobante de débito por la retención se informaba asociado únicamente al comprobante que lo generó — la organización tenía que llamar al endpoint de consulta de operación para conocer los comprobantes relacionados, y no todas las integraciones usan ese mecanismo.
- **Solución**: se agregó `comprobanteId` a **todos los webhooks de operaciones** (no solo a los de impuestos), para que la organización tenga esa referencia sin necesidad de una consulta adicional.
- **Fuera de alcance explícito**: no se agregó el camino inverso (`idOperacion` relacionado en el webhook de comprobantes).
- **Decisión de producto**: cambios en la estructura de webhooks son sensibles porque pueden afectar a organizaciones ya integradas — quedó documentado el riesgo aunque se decidió avanzar igual, ya que agregar un campo nuevo es no-breaking.
- Documentado para integradores en `psp.bind.com.ar/developers/apis/guia-impuestos-wallet` y `.../webhook-impuesto-online`.

## 4. Retenciones Wallet — nueva base de datos y API dedicada

Desarrollo separado (2 partes: API nueva + base de datos nueva) para el cálculo/registro de retenciones — indica que el modelo de datos de impuestos de Wallet creció lo suficiente como para necesitar su propio almacenamiento dedicado en vez de vivir en las tablas genéricas de comprobantes.

## 5. Cluster de bugs operativos — padrones provinciales desactualizados

Gran parte de los ~15 bugs de esta Epic son variaciones del mismo problema raíz: **padrones/registros externos de percepción-retención por jurisdicción que no se actualizan solos** — se detectaron desactualizados IIBB Tucumán, MEMPRE, SIRTAC y SIRCUPA en distintos momentos, cada uno como un ticket de bug independiente. **Aprendizaje operativo**: los padrones provinciales de impuestos requieren un proceso de actualización recurrente monitoreado — no es un dato que se cargue una vez y quede vigente.

Otros bugs puntuales con causa raíz confirmada:
- **Alta de cuenta no impactaba en SISCRI como Persona** pese a responder OK — desincronización entre el alta en Wallet y el alta real en SISCRI.
- **Cálculo de impuesto usando un CUIT "hardcodeado"** en vez del CUIT real de la cuenta de Wallet — bug de integración donde el valor de prueba/default nunca se reemplazó por el dato dinámico correcto.
- **Alta de organización en Wallet no daba de alta automáticamente en SISCRI** — paso manual que debía ser parte del flujo de alta de organización.
- Actualización de una cuenta pisaba datos válidos existentes (bug de merge de datos).

## Ver también

- [configuracion_entidades.md](configuracion_entidades.md) — configuración de SISCRI del lado Adquirencia/comercios.
- [wallet/organizaciones_y_configuracion.md](../wallet/organizaciones_y_configuracion.md) — configuración de impuestos/SISCRI por organización de Wallet (alta inicial).
