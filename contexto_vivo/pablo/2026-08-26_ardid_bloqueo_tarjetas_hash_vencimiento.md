---
id: 2026-08-26_ardid_bloqueo_tarjetas_hash_vencimiento
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_meetings — reunión 'Previa demo mayoristas' (2026-08-26 09:31), minuta Gemini, docId 1Vc8ksoClbXqLAtRxlw-kBB6R5HS-kkwSd1BF_e8Me_g"
producto: ardid
tema: Bloqueo permanente de tarjetas por hash de vencimiento heredado + mejora de auditoría de rechazos
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

**Contexto de la fuente:** ensayo interno ("previa"/dry-run) de la demo a la cámara de supermercados mayoristas, con Pablo Gomes, Luciana Rudaz, Gonzalo Rivera, Nicolás Colón, Adriana Endzeliz y Rocio Revelli (bancoindustrial.com.ar, presenta el módulo de reglas de fraude de Ardid en la demo). Durante el ensayo de pagos con enlace/QR surgió un problema real de plataforma, no simulado.

## Hallazgo: bloqueo permanente de tarjeta por hash ligado al primer vencimiento cargado

Si en el **primer pago** con una tarjeta se ingresa una fecha de vencimiento incorrecta, el sistema genera un hash que asocia el número de tarjeta a esos datos erróneos **de forma permanente** — la tarjeta queda bloqueada para siempre con ese error, sin mecanismo de autocorrección.

- Nicolás Colón aclaró que el hash se compone **exclusivamente de los 16 dígitos de la tarjeta**, pero una vez generado queda atado al primer vencimiento con el que se registró — si ese dato estaba mal, no hay forma de que el sistema lo corrija solo.
- Gonzalo Rivera explicó que este comportamiento es un **diseño histórico heredado de Billetera Santa Fe**, pensado originalmente como control antifraude (evitar que se reintenten combinaciones de tarjeta+vencimiento).
- Pablo Gomes cuestionó la vigencia de ese diseño para el caso de una tarjeta **renovada legalmente** (mismo número, nuevo vencimiento) — con la regla actual, esa renovación legítima también quedaría bloqueada.
- **Workaround manual ya conocido por Soporte/Rivera** (mostrado en vivo por Rocio Revelli): cambiar el estado de la tarjeta de "hash bloqueado" a "inválido" permite que el sistema genere un hash nuevo y el cliente pueda reintentar la operación. Tras aplicar el cambio, la transacción pasa a estado pendiente (confirmado por Adriana Endzeliz).

No quedó registrado en la reunión si existe hoy un ticket o pedido formal para automatizar este workaround o revisar la vigencia de la regla heredada — es un hallazgo de mecánica de producto, no una decisión de rediseño.

## Mejora pedida: incluir el ID de regla de Ardid en los códigos de rechazo de la base de transacciones (TRX)

Gonzalo Rivera propuso que, cuando una transacción se rechaza por Ardid (ej. código 1001), la base de TRX incluya además, entre paréntesis, el **ID de la regla específica** que causó el rechazo — hoy para saber qué regla exacta rechazó hace falta consultar manualmente la plataforma Ardid. El equipo lo acordó como requerimiento de auditoría técnica; Gonzalo Rivera queda a cargo de cargar el pedido de mejora al sistema correspondiente (no es una tarea de Producto/PM, la carga él mismo).

## Otros hallazgos operativos de la misma sesión (menores, mismo hilo)

- El **token/código de verificación** de pagos por enlace tuvo un comportamiento inconsistente durante las pruebas — el equipo decidió omitirlo o mencionarlo solo brevemente en la demo real para no exponerlo en vivo.
- Se decidió **acotar el alcance de la demo en vivo** a los componentes estables (onboarding, portal, POS, wallet, backoffice/portal de administración, reglas Ardid), excluyendo explícitamente detalle de movimientos, generación de archivos por lotes y carga de créditos con tarjeta — por riesgo de falla en vivo, no por limitación funcional real de la plataforma.
