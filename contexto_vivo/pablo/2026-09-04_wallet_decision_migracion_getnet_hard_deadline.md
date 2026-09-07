---
id: 2026-09-04_wallet_decision_migracion_getnet_hard_deadline
pm: pablo
fecha_captura: 2026-09-04
fuente: "Reunión 'Producto - Prioridades v1' (2026-09-04, minuta Gemini) — corregido el 2026-09-07 contra la documentación técnica oficial de Getnet y el discovery completo del proyecto getnet_oauth2_resolve"
producto: wallet
tema: Getnet impone migración obligatoria de su API Resolve, hard deadline fin de septiembre 2026
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Corrección (2026-09-07):** la captura original de este item (reunión "Producto - Prioridades v1", 2026-09-04) describía el problema como un cambio de **formato del código QR** de los POS de Getnet, con Wallet necesitando actualizar su parser/lector. Se confirmó con el PM que es una descripción imprecisa del mismo hecho — el problema real, ya confirmado contra la documentación técnica oficial de Getnet, es otro: Getnet cambió el **mecanismo de autenticación** de su API Resolve (de un token de acceso fijo a OAuth2 `client_credentials`), no el formato del QR en sí (que sigue el estándar EMVCo/CIMPRA común a todo el ecosistema, sin cambios). El cuerpo de este item queda corregido con el hecho real.

## Decisión acordada

Getnet (aceptador de pagos con QR del ecosistema interoperable, procesado por PagoNxt/Banco Industrial) comunicó formalmente que va a apagar el mecanismo de autenticación anterior de su API Resolve — hasta ahora, como el resto del ecosistema, un token de acceso fijo enviado en cada consulta. En su lugar, exige que la billetera pida primero un token temporal (OAuth2 `client_credentials`, válido una hora) presentando credenciales propias, y lo use en cada consulta posterior. El deadline de corte es **fin de septiembre de 2026 (30/09)** — confirmado tanto por el propio Getnet como por escalamiento interno de Integraciones (Gonzalo Rivera, Alan Martínez).

**Implicancia:** sin este cambio, Bind Wallet deja de poder leer y pagar cualquier código QR de un comercio que use a Getnet como aceptador. En agosto de 2026 se registraron 13.280 pagos con QR de comercios Getnet — ese es el volumen mensual en riesgo.

## Impacto en Bind PSP

**Solución en curso:** ya existe un proyecto de producto completo para este problema (`getnet_oauth2_resolve/`, Pablo Gomes) — discovery cerrado (⚠️ Obligatorio, no por valor/NSM), PRD formal, 2 historias de usuario confirmadas y creación completa en Jira: IDEA **PRD-237** (EN APROBACION, prioridad Highest, SP 10), Epic **WS-1599**, Historias **WS-1600** (autenticación configurable por aceptador, aplicada a Getnet) y **WS-1601** (extender el mecanismo de gestión de aceptadores para que Soporte lo use, incluyendo el nuevo mecanismo). No hace falta ningún desarrollo de "parser de QR" — el QR en sí no cambia.

## Criticidad

- **Plazo:** 30/09/2026 (⚠️ hard, impuesto unilateralmente por Getnet).
- **Prioridad:** Alta — pérdida total de la capacidad de pago QR con comercios Getnet si no se llega a tiempo.
- **Responsabilidad:** Wallet (Pablo Gomes) + equipo de desarrollo externo (Fintexa, ya con análisis/diseño propio en curso).

> Fuente original: Reunión "Producto - Prioridades v1" (2026-09-04 14:01), minuta Gemini, mail de Getnet citado en la reunión. Corrección técnica confirmada por el PM el 2026-09-07 contra la documentación oficial de Getnet ya relevada en `getnet_oauth2_resolve/referencias/`.
