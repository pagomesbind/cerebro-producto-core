---
id: 2026-09-21_adquirencia_checkout_payment_methods_json_vs_issuer_identification
pm: pablo
fecha_captura: 2026-09-21
fuente: "Mail de Melisa Belpassi (Fintexa), hilo del ticket AD-978 — proyecto rechazos_bines_payway (PRD-251)"
producto: adquirencia
tema: Checkout de tarjeta no presente — dos sistemas independientes resuelven el tipo de tarjeta (frontend `payment_methods.json` + backend `IssuerIdentification`), con chequeo de consistencia que rechaza con 400 si discrepan
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/validacion_bines_tarjetas.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/adquirencia/validacion_bines_tarjetas.md §3.5 y el análisis técnico-funcional de rechazos_bines_payway (artefactos/rechazos_bines_payway-solution.md §6.3) — ambos daban por Supuesto/no confirmado que el backend del checkout de tarjeta no presente 'recibe el tipo ya resuelto, no vuelve a consultar la base'. Este hallazgo confirma que SÍ la consulta, como parte de un chequeo de consistencia contra el frontend, no como fuente primaria."
confianza: alta
estado: ingestado
merge_commit:
---

## Mecanismo confirmado — por qué cargar datos reales en `IssuerIdentification` puede rechazar tarjetas que hoy funcionan

Hasta ahora no estaba identificado qué componente resuelve marca/tipo de tarjeta en el checkout de tarjeta no presente (Botón Simple) antes de que el pago llegue al backend — era un gap abierto del proyecto `rechazos_bines_payway` (PRD-251). Fintexa (Melisa Belpassi) lo confirmó al explicar por qué el ticket de carga masiva de BINs (AD-978, ~89.717 altas) no se puede aplicar todavía en producción.

**Hay dos sistemas independientes que intentan identificar el tipo de tarjeta (Crédito/Débito/Prepaga) a partir del BIN, en dos momentos distintos del mismo pago:**

1. **Frontend — al tipear el número de tarjeta:** la pantalla de pago usa un archivo de configuración estático, `payment_methods.json`. Si no tiene esa tarjeta identificada puntualmente, aplica una regla general de respaldo: "empieza con 4 → Visa Crédito; empieza con 5 → Mastercard Crédito".
2. **Backend — al confirmar el pago:** el servidor vuelve a resolver el tipo de tarjeta, esta vez consultando la base real `IssuerIdentification`. Si tampoco la tiene identificada puntualmente, aplica la **misma** regla general de respaldo.

**Chequeo de consistencia:** al confirmar el pago, el backend compara lo que dijo el frontend contra lo que dice `IssuerIdentification`. Si no coinciden, lo trata como una inconsistencia sospechosa y corta la operación con `400` ("tarjeta no habilitada") — el pago nunca se termina de procesar.

**Por qué hoy funciona (por casualidad, no por estar bien identificado):** para una tarjeta que ninguno de los dos sistemas tiene identificada puntualmente, ambos caen en la misma regla de respaldo genérica, ambos dicen lo mismo, coinciden, y el pago se aprueba — aunque la clasificación sea incorrecta de fondo (el problema real que motiva PRD-251).

**Por qué el INSERT de BINs reales genera rechazos nuevos:** el script de carga de PRD-251 actualiza `IssuerIdentification` con la clasificación real y específica de cada tarjeta (para el 40% de las ~89.717 tarjetas del ticket AD-978, la clasificación real es Débito o Prepaga, no Crédito). El archivo `payment_methods.json` del frontend **no se toca** con ese script — sigue con la regla genérica vieja. Resultado: para toda tarjeta que pasa de "sin identificar, los dos coinciden por regla genérica" a "identificada con precisión solo en el backend", aparece una discrepancia entre frontend y backend, y el chequeo de consistencia la rechaza con 400 — aunque sea una tarjeta perfectamente válida.

**Ejemplo real (BIN `480459`, Visa):**
- Hoy: frontend dice "Crédito" (regla genérica) · backend dice "Crédito" (regla genérica) → coinciden → pago aprobado.
- Después del INSERT: frontend sigue diciendo "Crédito" (no se tocó) · backend dice "Prepaga" (dato real cargado) → no coinciden → pago rechazado.

**Alcance del problema, según Fintexa:** no es un error del script — el script carga el dato correcto. El problema es que la misma información vive en dos lugares (`payment_methods.json` en el frontend, `IssuerIdentification` en el backend) y solo uno de los dos se actualiza con este proyecto. Mientras no se sincronicen, cada tarjeta que pasa de clasificación genérica a específica corre riesgo de quedar bloqueada.

**Alternativa de fondo que Fintexa ya descartó como inmediata:** cambiar la lógica del frontend para que `payment_methods.json` se use solo de forma visual (mostrar el logo/nombre de la marca) y deje de participar en ninguna validación — pero aplicar ese cambio ahora dejaría de funcionar a ~35.000 tarjetas que hoy sí están identificadas puntualmente en el json y dependen de esa identificación específica (detalle sin desarrollar más por Fintexa en este intercambio, a confirmar en el seguimiento del proyecto).

**Dos preguntas que el PM (Pablo Gomes) mandó de vuelta a Fintexa, sin responder todavía:**
1. ¿Se puede actualizar `payment_methods.json` con la misma información, en el mismo momento en que se actualiza `IssuerIdentification`?
2. ¿No convendría migrar para que el checkout valide únicamente contra `IssuerIdentification` (vía consulta a la API), en vez de mantener una copia estática en el frontend? ¿Es una decisión ya evaluada, o hay una restricción técnica/de seguridad que impide que el checkout consulte la API de `IssuerIdentification` directamente desde el frontend?

> Fuente: proyecto `rechazos_bines_payway/proyecto.md` §7 (seguimiento PM), gap actualizado en `rechazos_bines_payway/gaps.md` (2026-09-21).
