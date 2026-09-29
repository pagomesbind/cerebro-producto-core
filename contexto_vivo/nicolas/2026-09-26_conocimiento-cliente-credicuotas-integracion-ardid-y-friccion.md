---
id: 2026-09-26_conocimiento-cliente-credicuotas-integracion-ardid-y-friccion
pm: nicolas
fecha_captura: 2026-09-26
fuente: "Hilo de mail 'Consultas integración' — Credicuotas / Pentass / Poincenot / Bind, 2026-08-05 → 2026-09-25"
producto: ardid
tema: Credicuotas — integración directa con Ardid/Akurtech en curso (ticket BP-52914) y fricción del cliente por demoras en credenciales
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no — nota para el merge: la cronología de la ficha (entrada 2026-08-19) menciona a 'Rodrigo Revelli'; por el dominio de mail y el resto del hilo, la persona de Bind es Rocío Revelli (rrevelli@bind.com.ar). Verificar y corregir si corresponde."
confianza: media
estado: ingestado
---

Para sumar a `Particularidades / cronología` de la ficha **CREDICUOTAS** (el cliente ya existe en `log_clientes.md`):

- **2026-08 (mesas de trabajo con Pentass, 05/08–13/08):** Credicuotas empezó una integración **directa** con Ardid/Akurtech para monitorear el fraude de su propia operatoria: onboarding, login, pagos con TD, préstamos y pagos QR. El desarrollo del cliente lo hace Poincenot (Facundo Aguirre). Se definió que toda operación originada desde el CUIT de Credicuotas es un préstamo y se habló de un scope de Préstamos con límites propios. Detalle técnico en el item `2026-09-26_conocimiento-ardid-credicuotas-consumo-apis-externas-via-apim`.
- **2026-09-15:** Poincenot avisa que está listo para integrar y pide credenciales. Pentass las deriva a Bind, porque Ardid corre sobre la infraestructura de Bind PSP.
- **2026-09-17 → 09-25:** Bind (Rocío Revelli → Hernán Clarich) arma un producto en APIM para exponer en STG las APIs de Login, Pagos (Transaction/NotRealized) y Préstamos. Onboarding sigue sin endpoint identificado. Credicuotas carga el **ticket BP-52914** (25/09).
- **Señal de relación:** Gonzalo Santos (Head de Producto) mostró **fricción** por los tiempos de Bind ("no podemos estar una semana para recién ahora levantar que hay que crear ticket") y aceptó el proceso después de la aclaración de Rocío. Se suma a otro pedido del mismo cliente que ya figura en la ficha: la fecha del análisis de 2FA en Wallet, pendiente desde el 18/08.
- **2026-09-28 (agendado):** reunión "Credicuotas-Rechazos Ardid-Base" (Rocío Revelli + Nicolás Colón).

> Fuente: Hilo de mail "Consultas integración" (2026-08-05 → 2026-09-25).
