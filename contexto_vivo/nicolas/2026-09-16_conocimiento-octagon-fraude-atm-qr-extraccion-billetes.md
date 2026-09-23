---
id: 2026-09-16_conocimiento-octagon-fraude-atm-qr-extraccion-billetes
pm: nicolas
fecha_captura: 2026-09-16
fuente: "Mail 'Octagon - incidente fraudulento' — Emma Vignoles, 2026-09-15"
producto: wallet
tema: Fraude confirmado en la extracción de efectivo por QR en cajeros vía Octagon — bug de reconciliación cuando el cliente no retira todos los billetes
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md (ficha OCTAGON, particularidades/cronología)
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

**Incidente:** Octagon (cliente con ficha en `log_clientes.md` / `casos_de_uso_clientes.md`, agente de cobros y pagos que ya opera transacciones en cajeros vía QR) detectó un bug de fraude en su función de extracción de efectivo por QR en ATM.

**Mecánica del bug:** al fallar la extracción (por ejemplo, monto superado por el límite mensual del cliente o error físico al retirar los billetes), Octagon genera automáticamente una DCT (devolución) por el **total** de la operación hacia la billetera iniciadora. El bug: cuando el cliente retiraba el efectivo pero dejaba **1 solo billete dentro del cajero** (retiro incompleto, no falla total), el sistema igual interpretaba la operación como fallida y devolvía el 100% del monto a la wallet — el cliente terminaba quedándose con casi todos los billetes retirados físicamente **y además** recuperando el saldo completo en la billetera.

**Impacto cuantificado:**
- 556 transacciones — $239.466.000 ARS
- Billetera iniciadora: **MELI, 100%** de los casos
- Ventana de explotación: 08/09/2026 → 14/09/2026 (Octagon apagó el servicio el 14/09 al detectarlo)
- 84 clientes/CUITs iniciadores, 44 ATMs involucrados

**Acciones ya en curso (repartidas por entidad, según el mail de Emma Vignoles):**
- Octagon: frenó la operación el 14/09 y está armando la denuncia penal.
- Bind PSP: hará la denuncia a la CPF (Central de Prevención de Fraude de Coelsa — ver `3_recursos/cumplimiento_normativo/coelsa_cpf_central_prevencion_fraude.md`), a cargo de Nicolás Colón; se dará aviso a MELI para bloquear a los clientes involucrados (Rocío Revelli); los 84 CUITs se enviarán a black list (Rocío Revelli).
- Destinatarios del mail: Diego Scaldaferri (Compliance BIND), Gustavo Batista y Pablo Montenero (Banco Industrial), Rocío Revelli y Gonzalo Rivera (BIND), Nicolás Colón.

**Nota:** la acción de "denuncia a CPF" es una gestión operativa de Compliance/Fraude a cargo de Nicolás, no un ítem de backlog de Producto — no se registra en `tareas.md` personal (regla dura del Cerebro sobre tareas operativas), pero se deja documentado acá por su severidad y porque conecta directamente con la mecánica de CPF ya documentada en el canon.

> Fuente: mail "Octagon - incidente fraudulento" (evignoles@bind.com.ar → dscaldaferri, gbatista@bancoindustrial.com.ar, rrevelli, grivera, ncolon; cc: mnadalin, dweledniger, pmontenero@bancoindustrial.com.ar — 2026-09-15). Adjunto `Casos_con_Diferencia_de_Billetes_QR.xlsx` no descargado.
