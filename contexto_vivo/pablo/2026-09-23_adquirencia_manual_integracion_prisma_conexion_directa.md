---
id: 2026-09-23_adquirencia_manual_integracion_prisma_conexion_directa
pm: pablo
fecha_captura: 2026-09-23
fuente: "sesión de manual de configuración PRD-70 (POS con Prisma) — PDF oficial de Prisma subido por el PM a raw/, `Manual_Integracin_CD_v1.14_(1).pdf`, 'Manual de Usuario Integraciones Conexión Directa de Sistemas Propios' (v1, autores M. Rodriguez Alemany / J.M. Petrino, nov-2021, 83 páginas)"
producto: adquirencia
tema: manual técnico ISO 8583 de integración directa con Prisma (el mismo procesador que el Admin de Bind PSP muestra como "Payway" y que en Transacciones aparece como "PlusPagos")
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/integracion_prisma_conexion_directa.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

## Qué es este documento

Es el manual oficial de Prisma para integrarse por **Conexión Directa** (mensajería ISO 8583 punto a punto, TCP/IP) desde un sistema propio — en este caso, el POS de Bind PSP. Es el mismo procesador que en el Admin de Bind PSP aparece bajo el nombre "Payway" (ID interno "Prisma", 2003) y que en la grilla de Transacciones se ve como "PlusPagos" — ver `pos_multiadquirencia.md` para esa nomenclatura de 3 nombres. El PM lo subió a `raw/` el 2026-09-23 al analizar rechazos reales de un comercio de prueba (MCC 6051, ver `1_proyectos/prd-70_pos_prisma_finalizar/`) y pidió incorporarlo al Cerebro como referencia técnica, más allá de ese caso puntual.

**Alcance de esta primera pasada:** se cargó la estructura general del documento y la tabla completa de códigos de respuesta (la pieza más accionable para diagnosticar rechazos desde Soporte/Producto). **No se cargaron todavía** los ejemplos literales de mensaje 200/210 por cada operación (compra, devolución, anulación, preautorización, cierre de lote) — quedan en el PDF original, archivado en `4_archivos/historial_raw/`. Ver tarea T-120 en `1_proyectos/tareas.md` para retomar esa profundización cuando haga falta.

## Estructura del documento (índice)

1. Objetivos del documento
2. Operaciones y funcionalidades: Echo test, Compra, Devolución, Anulación de Compra o Devolución, Reverso, Advice Compra/Devolución/Anulación, Cierre de lote, Compra + Cash Back, PreAutorización y Captura, Pago Recurrente con/sin CVV, Agregador/Softdescriptor, Modos de captación/lectura de datos, Modalidades de pago no presentes
3. Procedimiento de autorización de una operación
4. Flujos de integración de mensajería: compra/devolución/anulación online exitosa; reverso de compra/devolución/anulación online; advice por rechazo en 1ª y 2ª instancia de una tarjeta EMV; preautorización y captura
5. Descripción de la mensajería: ISO 8583, longitud del mensaje, TPDU, tipos de mensajes, mapa de bits, nomenclatura de campos, y el detalle de cada tipo de mensaje (Echo Test, Compra Online, Anulación, Devolución, Cierre de Lote, Advice de Compra/Anulación/Devolución, Pre-autorización online y su anulación, Compra/Anulación/Devolución **offline** — solo manual y banda)
6. Descripción de campos (ISO 2 al ISO 63) — ver detalle de los más relevantes abajo
7. Acceso a aplicaciones en conexión TCP/IP: descripción de la conexión, requerimientos, arquitectura transaccional, establecimiento/liberación de conexión, intercambio de datos, encriptación
8. Anexos: I (TAGs EMV + configuración interna del dispositivo), y otros no relevados en esta pasada (Productos Mandatorios, Fórmula de cálculo de PAN, etc.)

## Campos ISO 8583 más relevantes para diagnóstico (Sección 6)

- **Campo ISO 2:** Número de tarjeta (PAN), formato LLVAR.
- **Campo ISO 3:** Código de procesamiento.
- **Campo ISO 4:** Importe de la transacción.
- **Campo ISO 34:** Número de cuenta extendido (PAN), formato LLVAR (NS..28).
- **Campo ISO 35:** Track 2 — formato `;PAN=AAMM|Dat.Disc.|?` (`;`=inicio, `=`=separador, AAMM=vencimiento, `?`=fin).
- **Campo ISO 37:** Número de referencia (RRN), identificador único de cada operación, formato `an12`.
- **Campo ISO 38:** Código de autorización de una transacción aprobada, formato `an6`.
- **Campo ISO 39: Código de Respuesta — la tabla completa está abajo, es la más útil para Soporte.**
- **Campo ISO 41:** Identificación de terminal, `ans8`.
- **Campo ISO 42:** Código de identificación de Comercio (Establecimiento), `ans15`.
- **Campo ISO 45:** Track 1 — mismo esquema que Track 2 pero con nombre del titular incluido.
- **Campo ISO 49:** Código de moneda — Pesos Argentinos = `032`.
- **Campo ISO 52:** PIN block (PIN encriptado).
- **Campo ISO 60:** Versión de software del sistema propio, formato `ans...999` (LLLVAR).
- **Campo ISO 62:** Número de ticket — numérico de 4 posiciones, arranca en `0001`, incrementa 1 a 1 por cada operación aprobada (compra/anulación/devolución), reinicia a `0001` después de `9999`. **No** se incrementa por operaciones rechazadas ni por el cierre de lote en sí (el cierre consume un número de *trace*, no de *ticket*).
- **Campo ISO 63:** Mensaje a mostrar/imprimir en el ticket — si el primer carácter es `.` se muestra/imprime (máx. 40 caracteres); si es `,` no se muestra (máx. 200 caracteres); `|` = fin de línea, `^` = fin de mensaje.

## Tabla completa de Códigos de Respuesta (Campo ISO 39)

Esta es la tabla oficial que define qué significa cada código de rechazo/aprobación que Prisma (Payway/PlusPagos) devuelve. **Clave para diagnosticar reclamos de Soporte sin escalar a Fintexa cada vez:**

| Código | Descripción | Referencia / acción |
|---|---|---|
| 00 | Aprobada (authno) | Operación aprobada, emitir cupón (cargo o ticket) |
| 01 | Pedir Autorización | Solicitar autorización telefónica; si se aprueba, cargar el código obtenido y dejar la operación en OFFLINE |
| 02 | Pedir Autorización | Ídem código 01 |
| 03 | Comercio Inválido | Verificar parámetros del sistema, código de comercio mal cargado |
| 04 | Capturar Tarjeta | Denegada, capturar la tarjeta |
| **05** | **Denegada** | **Denegada — código genérico, sin motivo más específico en la propia tabla** |
| 07 | Retenga y Llame | Denegada, llamar al Centro de Autorizaciones |
| 11 | Aprobada | Operación aprobada, emitir cupón |
| 12 | Transacción Inválida | Verificar el sistema, transacción no reconocida |
| 13 | Monto Inválido | Verificar el sistema, error en el formato del campo importe |
| 14 | Tarjeta Inválida | Denegada, tarjeta no corresponde |
| 25 | No Existe Original | Denegada, registro no encontrado en el archivo de transacciones |
| 28 | Servicio No Disponible | Momentáneamente no disponible, reintentar en unos segundos |
| 30 | Error En Formato | Verificar el sistema, error en el formato del mensaje |
| 31 | Aplica Dcc | Devuelve al POS info de tipo de cambio y moneda extranjera |
| 38 | Excede Ingreso de PIN | Denegada, excede reintentos de PIN permitidos |
| 39 | Código de seguridad incorrecto | Solo E-Commerce |
| 43 | Retener Tarjeta | Denegada, retener tarjeta |
| 45 | Número de Opera en Cuotas | Denegada, tarjeta inhibida para operar en cuotas |
| 46 | Tarjeta no Vigente | Denegada, tarjeta no está vigente aún |
| 47 | PIN Requerido | — |
| 48 | Excede Máximo Cuotas | Denegada, excede cantidad máxima de cuotas permitida |
| 49 | Error Fecha Vencimiento | Verificar el sistema, error en formato de fecha de expiración |
| 51 | Fondos Insuficientes | Denegada, no posee fondos suficientes |
| 53 | Cuenta Inexistente | Denegada, no existe cuenta asociada |
| 54 | Tarjeta Vencida | Denegada, tarjeta expirada |
| 55 | PIN Incorrecto | Denegada, código de identificación personal incorrecto |
| 56 | Tarjeta no Habilitada | Denegada, emisor no habilitado en el sistema |
| 57 | Transacción no Permitida | Verificar el sistema, transacción no permitida a dicha tarjeta |
| 58 | Servicio Inválido | Verificar el sistema, transacción no permitida a dicha terminal |
| 61 | Excede Límite | Denegada, excede límite remanente de la tarjeta |
| 65 | Excede Límite Tarjeta | Denegada, excede límite remanente de la tarjeta |
| 76 | Llamar al Emisor | Solicitar autorización telefónica; si se aprueba, cargar el código y dejar en OFFLINE |
| 77 | Error Plan/Cuotas | Denegada, cantidad de cuotas inválida para el plan seleccionado |
| 85 | Aprobada | Operación aprobada, emitir cupón |
| 89 | Terminal Inválida | Denegada, número de terminal no habilitado por el Emisor |
| 91 | Emisor Fuera Línea | Solicitar autorización telefónica; si se aprueba, cargar el código y dejar en OFFLINE |
| 94 | Número de Secuencia Duplicada | Denegada — error en mensaje, reenviar incrementando el system trace |
| 95 | Re-Transmitiendo | Diferencias en la conciliación del cierre |
| 96 | Error en Sistema | Mal funcionamiento del sistema, solicitar autorización telefónica |
| 98 | Desincronización de Working Key | Reintentar la operación |
| xx | Rechazada (Codnum) | Denegada, cualquier otro código no contemplado en la tabla |

**Nota de aplicación directa (2026-09-23):** al analizar rechazos con motivo "05" sobre un comercio de prueba de PRD-70 (POS con Prisma), se confirmó que "05" es el código genérico "Denegada" — no distingue por sí solo un rechazo del emisor de una posible mala configuración de datos en Payway. Ver `1_proyectos/prd-70_pos_prisma_finalizar/artefactos/2026-09-22_manual_pos_prisma_payway.html` (Caso Unhappy 3) y tarea T-118.
