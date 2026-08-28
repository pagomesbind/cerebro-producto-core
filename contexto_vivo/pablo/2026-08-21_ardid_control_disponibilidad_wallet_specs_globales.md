---
id: 2026-08-21_ardid_control_disponibilidad_wallet_specs_globales
pm: pablo
fecha_captura: 2026-08-24
fuente: "Grabación 'Revisión Wallet - BIND', 2026-08-21 (transcripta manualmente en sesión libre, no vía /sync_meetings) — minutos ~32 a 57, participantes Nicolás Colón, Juan Pablo Carubelli y Martín Hovanyecz (Keep IT Simple)"
producto: ardid
tema: Control de disponibilidad de Ardid en Wallet — especificación global, rechazo por caída, y cola de reintento (state monitor)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

> **Estado: diseño en discovery — nada de esto está construido ni desplegado todavía.** Es la revisión técnica de un diseño que Nicolás Colón todavía va a ajustar antes de pasarlo a desarrollo (ver cierre de la reunión, al final de este documento). Al mergear: filar como subsección delimitada y explícitamente marcada como discovery (mismo patrón que el §13 ya existente en el destino), nunca mezclado con la prosa que describe la integración ya vigente en producción — el banner `Estado: en producción` del archivo destino describe el estado general del documento, no valida automáticamente el contenido de esta sección.

Continuación técnica del discovery de robustez de Ardid presentado por Nicolás Colón el 2026-08-11 (ver `integracion_con_productos_bind.md` §13) — en esa sesión se había alcanzado consenso de que el sistema debe ser "100% rígido por defecto" (nunca dejar pasar una operación sin pasar por Ardid), con una palanca de apagado explícita y auditada como única excepción, pendiente de aprobación formal de Emma Vignoles. Esta reunión ("Revisión Wallet - BIND", 2026-08-21) es donde Nicolás Colón trajo el diseño técnico concreto de esa palanca para revisión de Juan Pablo Carubelli y Martín Hovanyecz (Wallet, Keep IT Simple), antes de pasarlo a desarrollo. Tres piezas — dos ya definidas, una tercera (la más extensa) en revisión en esta misma reunión.

## 1. Especificación de habilitación de análisis: global + por operación

Hoy existe una especificación por tipo de operación (transferencias internas/externas, pago QR, transferencia pool, pago de teléfono, etc.) que decide si esa operación puntual pasa por Ardid. Se agrega una nueva especificación **global**, con más peso que las de por operación: "la desconexión puede ser por operación, pero si la global está también activa, no tiene que pasar absolutamente nada [la desactivación] y pueden convivir" — es decir, para que una operación vaya a Ardid, **las dos especificaciones (global Y por operación) tienen que estar en `true`**; si cualquiera de las dos falta o está en `false`, esa operación no pasa por Ardid.

**Decisión de diseño acordada con Juan Pablo Carubelli:** el comportamiento por defecto se invierte respecto al patrón histórico. Hoy, para que una operación pase por Ardid, hace falta que exista y esté en `true` la especificación (patrón "por la positiva" — sin especificación, no se analiza). El nuevo default es "por la negativa": **todo pasa por Ardid salvo que exista una especificación explícita en `false` para desactivarlo** — "el default es que todo pase por arriba [Ardid]... si quiero desactivar por algún motivo, cargo la especificación para indicar que lo quiero desactivar." Aplica también a futuro: cuando la operatoria de Cobro pase por Ardid (hoy solo Wallet), debería seguir el mismo criterio.

**Por qué importa el cambio de default — antecedente real de falla operativa:** el "botón rojo" (kill switch) ya existe hoy, pero de forma poco confiable — es un script que ejecuta Infra para poner en `false` todas las especificaciones por tipo de operación. Cuando Wallet fue agregando operaciones nuevas (Pago FX, BIM recurrente, etc.), **el script nunca se actualizó** — la última vez que se intentó apagar todo, quedaron 2-3 operaciones activas sin que nadie lo supiera, precisamente porque el script no las conocía. La especificación global resuelve esto de raíz: un solo booleano, no un script a mantener por cada operación nueva.

## 2. Rechazar toda operación cuando Ardid está caído o responde error (deja de ser laxo)

Hoy, ante ciertas respuestas de error o falta de respuesta de Ardid, Wallet **deja pasar la operación igual** ("fue la definición que hubo en su momento de no cortarlo obligatorio... que pase, después veremos"). Nueva regla: **cualquier respuesta de Ardid que no sea `200` rechaza la operación** — con una excepción ya mapeada de antes que sigue funcionando igual: los rechazos de negocio propios de Ardid (`409`, ej. una regla/scoring que bloquea la operación) siguen su circuito normal de rechazo ya conocido.

**Matiz importante sobre el `409` de "cliente no encontrado":** hoy ese caso concreto (cliente no sincronizado en Ardid) también debería empezar a rechazar bajo la nueva regla, pero Nicolás Colón advirtió que primero hay que hacer un **saneamiento de cuentas** — reconoció que ya había hecho ese saneamiento antes "por los problemas que hemos tenido", pero quedaron cuentas que nunca se dieron de alta correctamente en Ardid y hoy siguen respondiendo `409`. Sin ese saneamiento previo, activar el rechazo por esta causa específica bloquearía operaciones de cuentas legítimas. Acción pendiente antes de habilitar esta parte de la regla.

**Manejo de error de cara al cliente:** los rechazos por caída/error de Ardid deben distinguirse de un rechazo de negocio real — Nicolás propuso un código de error específico (tentativo: `99`) con mensaje "el sistema de monitoreo no se encuentra disponible", distinto del código ya usado para un rechazo real por regla de Ardid — para que soporte pueda diagnosticar por dónde viene un reclamo sin ambigüedad. Aplica a las mismas 5 operaciones que hoy se analizan: transferencias internas, externas de Bind, pago UR, transferencia pool y pago de teléfono.

## 3. State monitor — qué pasa con las peticiones que no llegaron a destino mientras Ardid está caído (la pieza más extensa, en revisión)

Nicolás ya tiene esto construido pero lo trajo a revisar antes de pasarlo, para no tener que modificarlo después. La regla se parte según el tipo de operación:

- **Alta de cuentas (siempre, sin importar la especificación global):** debe llegar a Ardid sí o sí. Si falla por intermitencia/timeout (no por estar la especificación apagada), se **encola** para reprocesar — específicamente el alta del `ClientType` (el alta del CUIT para una organización) y el `ClientProduct` (la asociación de ese cliente con un CVU).
- **Operaciones entrantes (transferencias entrantes):** mismo criterio — si falla por intermitencia/timeout, se guarda para procesar después vía el state monitor, sin importar la especificación (siempre se quiere que termine llegando a análisis).
- **Operaciones salientes (transferencia, pago QR, débito, etc.):** acá el comportamiento depende de la especificación (global/por operación) — si Ardid no responde o da timeout estando la conexión "activa" (se supone que debería analizarse), se **rechaza directamente la operación**, no se encola — coherente con la regla del punto 2 (nunca dejar pasar una saliente sin análisis).

**Distinción clave que Nicolás remarcó:** alta de cuentas y entrantes se encolan porque "siempre" tienen que terminar entrando al sistema tarde o temprano; las salientes se rechazan en el momento porque dejar pasar una salida de dinero sin haber podido analizarla es exactamente el riesgo que todo este trabajo busca evitar.

## Punto sin resolver — relación entre el feature flag y el "botón rojo"

Juan Pablo Carubelli planteó una tensión de diseño sin cerrar en la reunión: si el feature flag de "no puedo conectar → dejar pasar/rechazar" convive con el botón rojo (especificación global manual), **hay una zona gris de cuándo se activa cada uno** — "che, la toma de decisión de es el feature flag o es el botón rojo, tenemos que tener claro cuándo sí, cuándo el otro." Nicolás lo ve como un salvavidas adicional ("no debería ser necesario, pero es como un salvavidas por las dudas"), pero Juan Pablo advierte que sin claridad de cuándo usar cada mecanismo se repite el mismo problema de confusión operativa que motivó todo este trabajo (hoy soporte recibe reclamos y "no sabemos para qué son" las especificaciones existentes). Queda para seguir discutiéndolo — no bloqueante para avanzar con el desarrollo de las 2 piezas ya definidas (especificación global, rechazo por caída).

**Estado al cierre de la reunión:** Martín Hovanyecz ya está analizando el rechazo-por-caída aplicado al circuito de marketplace, sin dudas hasta el momento. Nicolás va a ajustar el diseño del state monitor con lo discutido y pasarlo. Juan Pablo cerró pidiendo visibilidad de conjunto: si estas 3 piezas (más otras 2 que Wallet ya tiene en análisis, una ya desarrollada) tienen que salir todas en la misma versión — preocupación de capacidad de equipo (análisis + desarrollo + QA) mencionada junto con otros frentes compitiendo por la misma versión (FCI, Mastercard) — sin resolver en esta reunión, a discutir en la planificación de versión.

> Fuente: grabación "Revisión Wallet - BIND - 20260821_121503-Grabación de la reunión", 21 de agosto de 2026, 3:10pm — reunión conjunta desde una sala compartida ("7D, Plaza San Martín 7"), con Pablo Gomes, Nicolás Colón, Cristian Bonafede, Juan Pablo Carubelli, Martín Hovanyecz y Analía Dobrodzejunas. La transcripción diariza todo lo dicho desde esa sala bajo una única etiqueta de orador ("7D (Plaza San Martin, 7)"), sin distinguir entre Pablo Gomes y Nicolás Colón — el tramo de este item (minutos ~32 a 57, temática Ardid) se atribuye a Nicolás Colón por ser el dueño de este frente, a diferencia de la primera mitad (minutos 0-32, Worldsys/SharedKYC, atribuida a Pablo Gomes) ya procesada aparte en `proyecto-onboarding-estrategico/artefactos/2026-08-20_alternativas_shared_kyc_vs_onboarding.md`.
