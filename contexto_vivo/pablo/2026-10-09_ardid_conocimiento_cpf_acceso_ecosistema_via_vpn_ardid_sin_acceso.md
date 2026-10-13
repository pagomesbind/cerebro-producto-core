---
id: 2026-10-09_ardid_conocimiento_cpf_acceso_ecosistema_via_vpn_ardid_sin_acceso
pm: pablo
fecha_captura: 2026-10-09
fuente: "/idea_start — aclaración del PM en la sesión de discovery de PRD-278 \"CPF en onboarding\""
producto: ardid
tema: Acceso a la CPF de Coelsa — el ecosistema Bind ya lo tiene (vía VPN de Coelsa, obligatoria en pruebas y producción); Ardid todavía no
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/ardid/index.md
tipo_destino: actualizar
contradice: "wiki/3_recursos/detalle_productos/ardid/index.md — \"Gaps operativos abiertos\" punto 1 (entrega de credenciales de acceso a CPF, pendiente desde junio): no es una contradicción, precisa a quién se refiere ese pendiente"
confianza: alta
estado: en_cola
merge_commit:
---

Aclaración del PM (2026-10-09) sobre el estado del acceso a la Central de Prevención de Fraude (CPF) de Coelsa:

- **El ecosistema Bind (Wallet, Onboarding y el resto de los sistemas de Bind PSP) ya tiene acceso a la CPF**, en pruebas y en producción.
- **Ardid no tiene acceso.** El pendiente "entrega de credenciales de acceso a CPF desde junio" (reunión "Producto" del 2026-09-21) se refiere a Ardid y sigue abierto para Ardid, no para el resto del ecosistema.
- **Por qué hoy solo el ecosistema Bind llega a Coelsa:** Coelsa exige consumir sus servicios (ambiente de pruebas y de producción) a través de una VPN, y esa VPN solo está disponible hoy para el ecosistema Bind (no para Ardid, que es un proveedor externo — Fintexa/Akurtech).
- **Implicancia:** una integración de Ardid con la CPF (por ejemplo, para el screening del stock) depende de resolver su acceso a la VPN y las credenciales, o de que el ecosistema Bind exponga un servicio propio que Ardid consuma (esto último es una decisión de diseño, sin definir).
- El resto de la CPF (qué devuelve la consulta, estados, obligación de la Com. B 13117) está en los items `2026-10-09_cumplimiento_conocimiento_cpf_consulta_general_estructura_respuesta` y `2026-10-09_cumplimiento_conocimiento_com_b_13117_cpf_obligatoriedad`.

> Fuente: Pablo Gomes, sesión `/idea_start` PRD-278, 2026-10-09. Contrastado con el item archivado `2026-09-21_ardid_gap_credenciales_cpf_pendientes_desde_junio`.
