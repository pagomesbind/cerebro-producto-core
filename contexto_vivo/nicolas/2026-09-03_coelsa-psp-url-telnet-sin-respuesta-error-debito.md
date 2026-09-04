---
id: 2026-09-03_coelsa-psp-url-telnet-sin-respuesta-error-debito
pm: nicolas
fecha_captura: 2026-09-03
fuente: "Mail \"Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación\" — hilo con Coelsa (icm@coelsa.com.ar), mensajes del 2026-09-03"
producto: wallet
tema: Ticket Coelsa #456632 — Coelsa confirma que el telnet a la URL/IP del PSP registrada no responde; Bind reporta ERROR DEBITO en pruebas
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/transferencias_pull.md (§6 — circuito de reactivación en Homologación con Coelsa, ticket #456632)
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Continúa el circuito de reactivación de Transferencias Pull en Homologación con Coelsa (ticket #456632, ya documentado en §6 de `transferencias_pull.md` — última actualización mergeada citaba el hallazgo del 2026-08-27/28 sobre que un `PUT /apiCVU/PSP/ModificacionPSP/{cuit}` exitoso no se reflejaba en la consulta posterior).

- **2026-09-03 19:26** — Nicolás Colón (Bind) pregunta a Coelsa si desde su lado ya visualizan la URL (IP) del PSP bien configurada (el REQ/RESP ya se lo había pasado Ignacio Ghillini antes). Agrega un dato nuevo: en pruebas propias de Bind están recibiendo **ERROR DEBITO**, y lo atribuye tentativamente a esta falta de "comunicación" con el comprador (Coelsa).
- **2026-09-03 19:57** — Coelsa (Niurka Yamarte) responde con el dato concreto: la URL configurada en su base de datos es `https://172.30.8.62/`. Al hacer telnet a esa IP **no obtienen respuesta**. Piden a Bind que valide de su lado.

**Aprendizaje operativo (extiende el hallazgo previo):** el problema ya no se limita a que la escritura (`PUT ModificacionPSP`) no se reflejara en la lectura (`GET consultaPSP`) — ahora Coelsa aporta evidencia de que la propia conectividad de red hacia la URL registrada del PSP (`172.30.8.62`, IP privada) falla a nivel telnet desde su lado. Esto es compatible con (aunque no confirma) que el circuito completo dependa de una conexión dedicada/VPN entre Bind y Coelsa que hoy no está respondiendo en homologación, lo cual explicaría tanto la falta de tráfico en el webhook `AvisoDebinPendienteCVU` (ya reportada el 2026-08-28) como el `ERROR DEBITO` que ve Bind en sus propias pruebas.

**Estado a cierre de este barrido (2026-09-03):** sin resolver — queda pendiente que Bind valide la conectividad de red hacia `172.30.8.62` desde el ambiente de Coelsa (ver T-011 en `tareas.md`, actualizada).

> Fuente: Mail "Nueva respuesta en tu ticket 456632 - Reactivación de Transferencias Pull - Homologación" — ncolon@bind.com.ar / icm@coelsa.com.ar (2026-09-03).
