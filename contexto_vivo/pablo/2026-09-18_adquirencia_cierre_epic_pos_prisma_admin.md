---
id: 2026-09-18_adquirencia_cierre_epic_pos_prisma_admin
pm: pablo
fecha_captura: 2026-09-18
fuente: "/idea_prd (PRD-70, POS con PRISMA) — barrido directo de los 15 tickets de la Epic AD-430 en Jira (bindpsp.atlassian.net), incluidos fixVersions y comentarios de cierre de cada historia"
producto: adquirencia
tema: cierre del Epic "POS con PRISMA: Admin" (AD-430) — estado final, bugs y deuda técnica
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/pos_multiadquirencia.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: f460705
---

## Cierre del Epic "POS con PRISMA: Admin" (AD-430)

El documento `pos_multiadquirencia.md` (§1.1-§1.4) venía documentando esta Epic como "en desarrollo/bloqueada". Un barrido directo en Jira (2026-09-18, con ocasión de rehacer el PRD-70) confirma que, de los 15 tickets que componen la Epic, la gran mayoría ya está en Producción, con 2 defectos abiertos y una pieza de deuda técnica todavía sin iniciar.

### Qué se confirmó como entregado (verificado por `fixVersion` publicada, no solo por el estado de Jira)

- **Configuración por defecto a nivel Entidad y habilitación a nivel Comercio** (los dos tickets que motivaban la nota "bloqueada" en el documento existente): en Producción desde el 2026-06-24 (versión AD 70.1). El estado "Bloqueado" que siguen mostrando en Jira es la aprobación QA de Bind PSP, un paso interno posterior al despliegue real — no evidencia de que el código no esté en producción. Mismo criterio para el flujo de cobro adaptado a tomar los valores parametrizados (misma versión).
- **Jerarquía de reglas de pago y promociones entre Comercio y Entidad**: en Producción desde el 2026-08-03 (versión AD 71). Resuelve el caso donde un comercio tenía reglas propias de promociones pero ninguna de procesador, y el pago fallaba en vez de escalar a buscar el procesador en la Entidad padre. La resolución es independiente por tipo de regla: `ReglasFinales.Procesador = Comercio.Procesador ?? Entidad.Procesador`, igual para promociones — un comercio puede heredar una regla y tener la otra propia al mismo tiempo.
- **Devolución con el mismo procesador que hizo el cobro original**: en Producción desde el 2026-08-31 (versión AD 72). Quedó bloqueada varias semanas en Jira porque no se podía probar en Staging (Staging sigue sin permitir pagos/devoluciones de POS con Prisma) hasta que se pudo validar directo en Producción. Regla de negocio implementada: una devolución del mismo día en que se cobró se trata como anulación; una devolución de un cobro de un día anterior se trata como devolución propiamente dicha — misma distinción que ya regía para GP. **Deuda técnica reconocida por el propio desarrollo:** las devoluciones con Prisma envían el tipo de lectura de tarjeta como "MANUAL" fijo, sin distinguir CHIP/BAND/CONTACTLESS como sí hace el proceso de pago — ya existe el enumerador necesario para esa distinción, falta aplicarlo también acá.
- **Habilitar un comercio para operar exclusivamente con Prisma ("solo Prisma"), sin convivencia obligatoria con GP**: esta capacidad estaba documentada en el registro anterior como diferida a una "Etapa 2" sin ticket ni fecha. **Terminó construyéndose y entregándose** dentro del mismo período (Producción desde el 2026-08-31, cierre formal del ticket el 2026-09-08). Durante el desarrollo se descubrió una dependencia no prevista: el mecanismo que asigna el número de serie de un POS a una caja en su primer login también filtraba exclusivamente por el procesador GP (código de procesador 2000) — sin corregir eso, un comercio configurado "solo Prisma" no podría ni siquiera vincular su primer dispositivo POS. El equipo de Producto (Pablo Gomes) decidió ampliar el alcance de la misma historia para incluir esa corrección, en vez de diferirla a un ticket nuevo. Sin deuda técnica asociada según el propio desarrollo.
- **Dos bugs de producción ya corregidos**, no documentados hasta ahora: (1) el alta de un canal POS con Prisma no creaba correctamente las reglas de negocio del comercio en el motor de reglas (`cardbusinessrules`) porque cruzaba mal las columnas de valor y código de comercio al insertar la especificación — corregido, en Producción desde el 2026-08-03; (2) cambiar el orden de prioridad entre GP y Prisma en un comercio ya habilitado dejaba el canal POS en estado de error ("GP: Error al dar de alta el subcomercio") en vez de aplicar el cambio — corregido, en Producción desde el 2026-08-31, con una advertencia del propio desarrollo de que "el código que maneja altas y modificaciones para GP sigue estando lejos de lo ideal".

### Qué sigue sin resolver a la fecha de esta ingesta (2026-09-18)

- **2 defectos abiertos, detectados después del último release (AD 72) y todavía sin ningún comentario de seguimiento del proveedor tecnológico:**
  1. Cambiar la prioridad de los procesadores de un comercio ya configurado (de GP a Prisma, mostrado en el Admin como "Payway") no aplica el cambio — el comercio queda con GP como principal pese a guardar la edición.
  2. Un comercio que hereda el canal POS con Prisma como principal desde la configuración de su Entidad falla su alta porque no se genera el CVU correspondiente.
  Ambos son el mismo tipo de fricción operativa que esta Epic buscaba eliminar (configuración manual/con errores) — mientras sigan abiertos, no se puede decir que la configuración self-service esté completamente resuelta.
- **Deuda técnica de fondo sobre el motor de reglas de pago, ya diagnosticada pero sin desarrollo iniciado:** el motor no trata el **Canal** de cobro (presencial, Botón Simple, QR, etc.) como una dimensión propia de las reglas del mismo modo en que sí distingue entre reglas de procesador y reglas de descuento. Hoy, para el procesador, el canal es solo un filtro puntual — si el comercio tiene una regla de procesador en un canal distinto al que se está evaluando, se descarta entera en vez de convivir con la regla de la Entidad en el canal correcto. Para los descuentos, el canal ni siquiera se mira en el mismo punto del código. Resultado: no existe hoy una forma de que un comercio acumule, por ejemplo, una regla de procesador propia del canal presente con una regla de descuento heredada de otro canal — se pisan o se descartan en vez de convivir. La solución propuesta (todavía sin construir) es cambiar la llave de resolución de "tipo de regla" a "tipo de regla + canal". Antes de tocar código hace falta confirmar contra la base real qué valores tiene cargado el campo Canal de cada regla — la migración que restringe los valores válidos de ese campo (`PRESENTE`, `BOTON_SIMPLE`, `QR`, `QR_TARJETA`) corrió solo en el ambiente interno del proveedor, nunca en Staging ni en Producción, y nunca se confirmó si hay valores mal cargados (typos, mayúsculas, sinónimos) que quedarían huérfanos con la nueva lógica.
- Se mantienen sin desarrollo iniciado, consistente con lo ya documentado: la orquestación/failover automático entre procesadores (decisión explícita de no priorizarlo), la gestión de la tabla de parámetros de Prisma por rubro desde el Admin, y el alta en Prisma con un identificador de adquirente distinto al de Bind PSP.

### Nota de nomenclatura

En las pantallas del Admin, el segundo procesador (Prisma) se muestra con el nombre "Payway" — varios de los defectos y bugs de esta Epic (incluidos los 2 todavía abiertos) están redactados por QA usando ese nombre visible en pantalla, no "Prisma". Cualquier guía de soporte o capacitación sobre esta configuración debería usar el mismo nombre que ve el usuario, para evitar que un caso se busque por el nombre técnico y no aparezca.
