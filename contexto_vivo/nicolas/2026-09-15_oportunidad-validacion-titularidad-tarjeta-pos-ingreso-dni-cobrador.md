---
id: 2026-09-15_oportunidad-validacion-titularidad-tarjeta-pos-ingreso-dni-cobrador
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Charla directa con el PM, cierre del discovery de titularidad_tarjeta (2026-09-15)"
producto: Adquirencia (POS)
tema: Extender la validación de titularidad de tarjeta (MODO VaTa) al canal POS, con el cobrador ingresando el DNI del pagador por teclado
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: crear
contradice: "no"
confianza: media
estado: en_cola
---

Al cerrar el discovery de [`titularidad_tarjeta`](../titularidad_tarjeta/proyecto.md) (validación de titularidad de tarjeta en Botón Simple vía MODO VaTa, después de Ardid), el PM planteó que el mismo servicio debería estar disponible a futuro para otros canales — puntualmente **POS**, donde el cobrador ingresaría por teclado el DNI del pagador para validar la titularidad de la tarjeta presente y prevenir fraude, del mismo modo que ya se hace en Botón Simple.

No es un pedido de cliente ni tiene IDEA de Jira propia todavía — surge como extensión natural del proyecto en curso, no como discovery independiente. El proyecto `titularidad_tarjeta` ya incorpora un requerimiento no funcional para no bloquear esta extensión (el cliente de la API VaTa se diseña como componente reutilizable, no acoplado a Botón Simple — ver `decisiones.md` [2026-09-15] de ese proyecto), pero el desarrollo específico de POS (UI de ingreso de DNI en el dispositivo, flujo del cobrador, definición de fail-open/fail-closed en ese canal) queda completamente sin discovery propio.

Confianza media: la necesidad de negocio (POS también sufre el mismo tipo de fraude de tarjeta no propia) es plausible por analogía directa con Botón Simple, pero no está cuantificada ni confirmada con un caso concreto de cliente/contracargo de POS.
