---
id: 2026-09-26_conocimiento-ardid-credicuotas-consumo-apis-externas-via-apim
pm: nicolas
fecha_captura: 2026-09-26
fuente: "Hilo de mail 'Consultas integración' — Lorena Macedo (Pentass), Gonzalo Santos / Juan I. Bigourdan (Credicuotas), Facundo Aguirre (Poincenot), Rocío Revelli y Hernán Clarich (Bind), mensajes del 2026-08-05 al 2026-09-25 (thread visto por primera vez en este barrido)"
producto: ardid
tema: Credicuotas integra directamente con las APIs externas de Ardid/Akurtech (Login, Transaction/NotRealized, Loans) expuestas por la infraestructura de Bind PSP vía APIM — definiciones de las mesas de trabajo de agosto y estado del pedido de credenciales en STG
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 9fbee64
---

**Qué es:** Credicuotas (cliente de Bind PSP, lending de consumo con billetera propia sobre Wallet) se está integrando **directamente contra las APIs externas de Ardid/Akurtech** (catálogo documentado en `ardid/apis_externas.md`) para sus procesos propios de onboarding, login, pagos con tarjeta de débito y préstamos, y así usar el monitoreo antifraude sobre su operatoria. El desarrollo del lado del cliente lo lleva **Poincenot** (Facundo Aguirre). Pentass (Lorena Macedo, Samira Aouada) acompaña la integración funcional. Es un patrón nuevo respecto de lo documentado: hasta ahora Ardid se integraba con los productos de Bind (Wallet, Botón Simple), no con el sistema propio de un cliente.

**Arquitectura de acceso:** según Pentass (15/09), como Ardid corre sobre la **infraestructura de Bind PSP**, las credenciales las da Bind. En la práctica, Bind publica un **producto nuevo en su APIM** para que lo consuma Credicuotas. Poincenot preguntó si le pega "a la API actual de Bind PSP o a una API nueva", y el hilo no lo contestó explícitamente.

**Endpoints identificados por Bind (Hernán Clarich, 23/09) para armar el producto APIM**, según la documentación `Akurtech_ApisExternas_`:
- Login: **12.e / Login**
- Pagos con TD: **17.a / Transaction** y **17.b / NotRealized**
- Préstamos: **16 API / Loans**, **16.a / GetLoanById**
- **Onboarding: no se encontró referencia** en la documentación de APIs externas. Hernán preguntó si "esto es de ARDID", y Pentass mandó el 24/09 un PDF adicional (`ARKUTECH_Documentacion_Ardid.APIBlacklist_CheckBlacklist.pdf`) que no se descargó. Además, hace falta confirmar con Pentass los endpoints de backend para armar bien el producto y la política de APIM.

**Pedido formal y estado:** Rocío Revelli (17/09) pidió a Hernán exponer en **STG** las APIs de Onboarding, Login y Préstamos. El 24/09 pidió a Credicuotas cargar un ticket para seguimiento. Gonzalo Santos (Head de Producto, Credicuotas) se quejó por la demora ("no podemos estar una semana para recién ahora levantar que hay que crear ticket"; lo que necesitan son las credenciales). Rocío aclaró que el pedido ya se estaba gestionando y que en adelante se pedirá ticket desde el comienzo. **Ticket BP-52914** cargado por Credicuotas el 25/09. Hernán Clarich avisa las novedades. A la fecha, **sin credenciales de STG entregadas**.

**Definiciones de las mesas de trabajo de agosto (minutas de Pentass):**
- *11/08 — Préstamos:* toda operación originada desde el **CUIT de Credicuotas** es un préstamo. El PSP debería identificarlas como préstamo e informarlas a Ardid por el endpoint de Préstamos, algo que el equipo PSP tiene que evaluar. También se va a evaluar un **scope específico de Préstamos** para controlar esa operatoria por separado (por ejemplo, límites propios para operaciones con la línea de crédito sin afectar los de otras operaciones). Se compartió un caso de ejemplo con Rocío.
- *11/08 — Controles:* se revisaron los controles actuales de Ardid, entre ellos el **intervalo de tiempo entre transferencias**. Se van a evaluar controles adicionales ligados a la operatoria del cliente y controles específicos para pagos con tarjeta.
- *11/08 — Pagos QR:* falta validar con el PSP si los pagos QR pueden informarse a Akurtech **como Pagos y no como Transferencias**, para tipificarlos bien y aplicar los controles que correspondan. Las modalidades de pago identificadas son Transferencia/QR, Tarjeta y Dinero en cuenta, y hay que revisar cómo se informa y diferencia cada una hacia Ardid.
- *11/08 — Blacklist:* se confirmó que se pueden agregar destinatarios a la Blacklist sin problemas.
- *13/08 — Onboarding y Login:* se hacen con las APIs que comparte el PSP. Quedaron pendientes: notificaciones a **Slack desde Akurtech**, que el equipo PSP confirme si hoy hay **2FA** disponible y cómo se implementa en el flujo, y si se pueden sumar **latitud/longitud** como datos para reglas.

**Próximo hito conocido:** reunión "Credicuotas-Rechazos Ardid-Base", convocada por Rocío Revelli para el lunes 28/09 de 10:00 a 10:30. El título sugiere que se van a revisar rechazos de Ardid sobre la operatoria de Credicuotas.

> Fuente: Hilo de mail "Consultas integración" (2026-08-05 → 2026-09-25) — Pentass, Credicuotas, Poincenot y Bind. Adjuntos no descargados: `ARDID_Documentacion_APIBlacklist_CheckBlacklist 1 (1).pdf` (18/08), `Akurtech_ApisExternas_.pdf` (23/09), `ARKUTECH_Documentacion_Ardid.APIBlacklist_CheckBlacklist.pdf` (24/09).
