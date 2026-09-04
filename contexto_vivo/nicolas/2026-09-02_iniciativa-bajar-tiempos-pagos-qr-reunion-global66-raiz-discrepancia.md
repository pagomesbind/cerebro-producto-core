---
id: 2026-09-02_iniciativa-bajar-tiempos-pagos-qr-reunion-global66-raiz-discrepancia
pm: nicolas
fecha_captura: 2026-09-02
fuente: "Reunión \"Bind Global66, proximos pasos\" (2026-09-02)"
producto: wallet
tema: Novedad de la iniciativa PRD-199 — reunión conjunta con Global66 acota la causa de la discrepancia de medición de latencia QR al lado del cliente; nuevo hallazgo de transferencias no acreditadas; seguimiento agendado
tipo: iniciativa
proyecto: bajar-tiempos-pagos-qr
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Novedad de la iniciativa "Bajar tiempos de pagos QR" (PRD-199): en la reunión conjunta Bind/Global66 del 2026-09-02, se acotó la causa de la discrepancia de medición que Global66 venía reportando (7s del lado Bind vs. 15-20s reportados por Global66) — el cliente reconoció que su medición arranca desde que el usuario presiona el MFA, no desde que la petición llega a Bind, por lo que la latencia adicional probablemente está en su propio flujo, previo al servidor de Bind. Global66 se compromete a revisarlo internamente. En paralelo surgió un hallazgo nuevo (no relacionado a la latencia): casos de transferencias entrantes que no se acreditan del lado de Global66 pese a que Bind confirma haber enviado el webhook correcto — a investigar por Global66 la próxima semana. Se agendó reunión de seguimiento para la semana del 2026-09-08. Detalle completo en `1_proyectos/bajar-tiempos-pagos-qr/proyecto.md` (actualizado directo con esta reunión, sección "Notas de sesiones") y en el item de conocimiento de cliente del mismo barrido.

> Fuente: Reunión "Bind Global66, proximos pasos" (2026-09-02), minuta Gemini.
