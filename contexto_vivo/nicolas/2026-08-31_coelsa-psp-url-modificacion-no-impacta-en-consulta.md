---
id: 2026-08-31_coelsa-psp-url-modificacion-no-impacta-en-consulta
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Mail \"Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación\" — hilo con Coelsa (icm@coelsa.com.ar), mensajes del 2026-08-27 y 2026-08-28"
producto: wallet
tema: Ticket Coelsa #456632 — modificar la URL del PSP vía PUT no impacta en la consulta posterior, bloqueando la reactivación de Transferencias Pull en Homologación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/transferencias_pull.md (§6 — circuito de reactivación en Homologación con Coelsa, ticket #456632)
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 7fd6e3f
---

Continuación del circuito de reactivación de Transferencias Pull en Homologación con Coelsa (ticket #456632, ya documentado en §6 de `transferencias_pull.md`). Coelsa había indicado (2026-08-24) que debía registrarse la URL del PSP con `PUT /apiCVU/PSP/ModificacionPSP/{cuit}` para poder arrancar las pruebas de estado.

- **2026-08-27** — Nicolás Colón (Bind) confirma a Coelsa que modificaron el PSP con la URL correspondiente y que la API respondió exitosamente, pero que **al consultar después, el cambio no aparece reflejado**. Suma a Ignacio Ghillini (Bind, Analista Canales Digitales) como quien hizo el alta inicial (ya con la URL correcta) y la modificación reciente.
- **2026-08-28 18:03** — Coelsa (Niurka Yamarte) responde que están enviando una TRX pero no llega al endpoint `https://172.30.8.62/AvisoDebinPendienteCVU` — piden que Bind verifique de su lado.
- **2026-08-28 18:39** — Ignacio Ghillini valida en Homologación consultando `GET /PSP/consultaPSP/5071/30714979732` y **sigue devolviendo sin datos** (prueba efectuada 2026-08-28 15:27:26).
- **2026-08-28 20:27** — Coelsa pide que se les envíe el REQUEST/RESPONSE de esa consulta para poder investigar.

**Aprendizaje operativo:** en el circuito de alta/actualización de PSP de Coelsa, un `PUT /apiCVU/PSP/ModificacionPSP/{cuit}` exitoso (HTTP 200) **no garantiza que el cambio se refleje** en la consulta posterior (`GET /PSP/consultaPSP/{id}/{cuit}`) — hay una discrepancia entre escritura y lectura del lado de Coelsa (o una demora de propagación no documentada) que sigue sin resolverse a la fecha de este mail. El endpoint `AvisoDebinPendienteCVU` (webhook de aviso de Débin pendiente por CVU) tampoco está recibiendo tráfico de Coelsa en este ambiente.

**Estado a cierre de este barrido (2026-08-31):** sin resolver — Bind quedó a la espera de enviar el REQUEST/RESPONSE pedido por Coelsa (ver tarea T-011 en `tareas.md`, actualizada).

> Fuente: Mail "Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación" — icm@coelsa.com.ar / ighillini@bind.com.ar / ncolon@bind.com.ar (2026-08-27 y 2026-08-28).
