---
id: 2026-09-26_oportunidad-ardid-scope-prestamos-limites-linea-credito
pm: nicolas
fecha_captura: 2026-09-26
fuente: "Hilo de mail 'Consultas integración' — minuta de Pentass (Lorena Macedo) de la reunión del 2026-08-11 con Credicuotas"
producto: ardid
tema: Scope específico de Préstamos en Ardid — identificar como préstamo las operaciones originadas desde el CUIT de un prestamista (caso Credicuotas), informarlas por el endpoint /Loans y controlarlas con límites propios
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
---

**Oportunidad:** que Bind PSP identifique como **préstamo** toda operación originada desde el CUIT de un cliente prestamista (definido para Credicuotas: "toda operación originada desde el CUIT de Credicuotas corresponde a un préstamo") y la **informe a Ardid por el endpoint de Préstamos** (`/Loans`, ver `ardid/apis_externas.md` §16). Sumado a eso, crear en Ardid un **scope específico de Préstamos** para controlar esa operatoria por separado, por ejemplo con **límites propios para las operaciones que usan la línea de crédito**, sin tocar los límites de las otras operaciones del usuario.

- **Producto:** Ardid (con impacto en Wallet, que es donde se origina la acreditación del préstamo).
- **Origen:** mail "Consultas integración", minuta de Pentass del 2026-08-11. En esa minuta quedó "a evaluar por el equipo de PSP".
- **Señal de demanda:** Credicuotas (Gonzalo Santos, Head de Producto) lo marcó como lo que "más nos urge por temas de atención al cliente y incoming" (13/08). Se conecta con T-008 (diferenciación de créditos para nuevos límites en Wallet, pendiente desde el 18/08) y con OP-017, que también cita a Credicuotas.
- **Foco estratégico:** Ardid/antifraude. Candidato a patrón reutilizable para otros clientes con lending sobre Wallet. Relacionado conceptualmente con `ardid_limites_pj` (segmentación por tipo de cliente con reglas de montos propias).
- **Próximo paso sugerido:** evaluarlo en la reunión "Credicuotas-Rechazos Ardid-Base" del 2026-09-28 y decidir si se abre IDEA. Nunca se crea el ticket automáticamente.

> Fuente: Hilo de mail "Consultas integración" — minuta de Pentass del 2026-08-11 y mail de Gonzalo Santos del 2026-08-13.
