---
id: 2026-09-18_arquitectura_split_coelsa_no_funciona_homologacion
pm: pablo
fecha_captura: 2026-09-18
fuente: "/sync_meetings — reunión 'Error de SPLIT en HOMO' (2026-09-11), minuta Gemini, con Banco Industrial (Damian Villa, Alvaro Aguirreburualde, Patricio Banegas, Claudio Grillo)"
producto: adquirencia
tema: mecánica de división de pagos (split) QR con Coelsa/Banco Industrial y falla reproducida en homologación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/index.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Mecánica de la división de pagos (split) en QR con cuenta recaudadora

Cuando un comercio tiene el split activo en un canal QR, el flujo de fondos es: el comprador paga vía Devin QR y el 100% neto de comisiones se acredita primero en la **cuenta recaudadora** del modelo PCP (ej. la cuenta `2530` para el PCP 164 en producción, subcuenta `77`). Inmediatamente después, Coelsa detecta que el canal tiene split activo y dispara **un débito automático en esa misma cuenta recaudadora por el monto neto acreditado**, con un crédito equivalente hacia la cuenta (interna al Banco Industrial, por decisión de negocio — así los fondos "duermen" en el banco) que corresponde al comercio configurado para recibir el split — dejando la recaudadora en cero. El ID de la operación de split que dispara Coelsa **es distinto** del ID del pago QR original; ambos quedan relacionados recién en el archivo de conciliación posterior que provee Coelsa, no en el momento de la transacción.

## Falla reproducida en el ambiente de Homologación

Gonzalo Rivera (Bind PSP) probó el split en Homologación para los modelos PCP 532 y PCP 531 (este último funcionaba antes) y en ninguno de los dos se ejecuta el débito/crédito del split — la operación QR original se acredita bien en la recaudadora, pero el segundo movimiento nunca llega. Al revisar un caso real de Producción (PCP 164) sí aparece el flujo completo (aviso de débito + crédito), confirmando que el mecanismo funciona en Producción pero no en Homo para los modelos nuevos.

Del lado de Banco Industrial (Alvaro Aguirreburualde) se descarta que sea un problema de Bantotal — la corrección que se había hecho ahí (permitir débito y crédito con el mismo ID de operación, que antes generaba falso duplicado) ya estaba resuelta. Tampoco hay evidencia de que el banco haya configurado algo específico de split del lado de Bantotal — Aguirreburualde entiende que la habilitación del split es responsabilidad de Bind PSP contra Coelsa. Pablo Gomes confirmó que, según lo validado con el desarrollador (Marco Pablo) al dar de alta el comercio/entidad del PCP 532, el canal QR con split había quedado habilitado correctamente del lado de Bind — pero no hay evidencia de que Coelsa haya efectivamente disparado el aviso.

**Conclusión de la reunión:** la hipótesis más fuerte es que Coelsa no está enviando el aviso de split para estos canales en Homologación (no un problema de configuración de Bantotal ni de Bind). Gonzalo Rivera va a escalar un ticket directo a Coelsa adjuntando la evidencia, con copia a Ignacio Ghillini y Claudio Grillo (Aguirreburualde está de vacaciones la semana del 14 al 21/09). Si la respuesta de Coelsa indica que el problema está del lado del desarrollo del banco, se retoma con una nueva reunión a partir del 21/09.
