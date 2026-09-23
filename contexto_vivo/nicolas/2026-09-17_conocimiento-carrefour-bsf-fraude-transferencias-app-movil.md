---
id: 2026-09-17_conocimiento-carrefour-bsf-fraude-transferencias-app-movil
pm: nicolas
fecha_captura: 2026-09-17
fuente: "Mail 'Fwd: BSF - Reporte de incidente fraudulento 10/09' — Emma Vignoles (reenviando cadena con Carrefour/BSF), 2026-09-16"
producto: wallet
tema: Fraude confirmado en transferencias salientes no autorizadas desde la app móvil de Carrefour (BSF) — 217 clientes afectados
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md (ficha Carrefour (BSF), particularidades/cronología)
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 25b8e37
---

**Incidente:** Carrefour (BSF — Banco de Servicios Financieros Carrefour S.A.U., ficha Wallet en `log_clientes.md`/`casos_de_uso_clientes.md`) confirmó un incidente de fraude en su aplicación móvil: detección de transacciones no autorizadas que resultaron en extracción fraudulenta de fondos desde cuentas de **217 clientes** hacia cuentas de terceros.

**Cronología (según reporte de Eduardo Dezuliani, Director de Legales/Compliance/RRHH de BSF, 2026-09-16):**
- **10/09/2026, 9:14hs:** detección del incidente — servicio afectado: aplicación móvil, transferencias salientes.
- Los servicios de la app se restablecieron parcialmente desde las 15hs del mismo día (con intermitencias por cambio en el proceso de validación de logueo), y con total normalidad desde las 19:30hs.

**Acciones correctivas tomadas por BSF:**
- Reintegro de fondos a los 217 clientes afectados.
- Reducción del piso a partir del cual se exige validación biométrica en transferencias salientes a terceros: de $500.000 a **$50.000**.
- Refuerzo del proceso de logueo: agregado de validación biométrica (rostro) para recupero de usuario/contraseña.
- Notificación a los clientes afectados (incidente + restitución de fondos).
- Presentación de denuncia penal por parte de BSF.
- BSF continúa analizando la causa (vulnerabilidad puntual todavía no confirmada por escrito en el hilo — Bind PSP la pidió explícitamente y sigue sin respuesta a la fecha de este mail).

**Pedido de Bind PSP a BSF (Gonzalo Rivera, 2026-09-15):** reporte del fraude con avances, en base a lo charlado en una meet la semana previa (no cubierta por `/sync_meetings` — instancia distinta, sin minuta de Gemini).

**Acción pendiente del lado Bind (mail de Emma Vignoles, 2026-09-16, dirigido a Rocío Revelli y Nicolás Colón, cc Gonzalo Rivera):** "¿Podemos denunciar en CPF por favor?" — gestión operativa de Compliance/Fraude (denuncia a la Central de Prevención de Fraude de Coelsa, ver `3_recursos/cumplimiento_normativo/coelsa_cpf_central_prevencion_fraude.md`), mismo patrón que el incidente de Octagon del 2026-09-15/16 (`contexto_vivo/2026-09-16_conocimiento-octagon-fraude-atm-qr-extraccion-billetes.md`, ya ingerido). No se registra en `tareas.md` personal por ser tarea operativa, no de Producto — queda documentada acá por severidad y para la ficha de cliente.

**Adjunto no descargado:** `Clientes afectados 100926.xlsx` (listado de transacciones/clientes afectados, compartido por Rodrigo Golini, Carrefour).

> Fuente: mail "Fwd: BSF - Reporte de incidente fraudulento 10/09" (evignoles@bind.com.ar → rrevelli@bind.com.ar, ncolon@bind.com.ar; cc grivera@bind.com.ar — 2026-09-16), reenviando cadena con Rodrigo Golini, Eduardo Dezuliani y Rodrigo Quiñones (Carrefour/BSF) y Gonzalo Rivera (Bind PSP), 2026-09-15/16.
