---
id: 2026-09-02_wallet_mastercard_xbs_pvt_alcance
pm: pablo
fecha_captura: 2026-09-02
fuente: "/sync_mails — mail \"Re: Fw: Implementation plan CIS-2026-13184 PVT XBS\" (threadId 1a05e59f178140ee), Luciana Rudaz / Omar Vladimir Gomez (Mastercard), 2026-09-01"
producto: wallet
tema: Mastercard Cross-Border (XBS) — Implementation Plan v3.0 aprobado, alcance de corredores confirmado, deadline de pruebas productivas movido a 16/09
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_fx.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Fuente:** hilo "Implementation plan CIS-2026-13184 PVT XBS" con Mastercard (Omar Vladimir Gomez, Federico Darnond, Juan Puig Moreno, Juan Carlos Lozano Cortes, Olga Perdomo del lado Mastercard; Luciana Rudaz del lado Bind PSP), 2026-08-26/2026-09-01. Proyecto CIS-2026-13184 = **Production Validation Testing (PVT)** de Mastercard Move / Cross-Border Services (XBS), previo/paralelo al alcance ya documentado en `dolar_fx.md §2` (que cubre hasta W70/PRD-10).

**Hito 2026-09-01:** Luciana Rudaz aprobó el **Implementation Plan v3.0** ("Genial, estamos OK con ese documento"). El plazo del proyecto se actualizó a 22 días — **las pruebas productivas de este scope deben completarse a más tardar el 16/09/2026** (el deadline anterior mencionado por Mastercard en el hilo era el 15/09, corregido por su equipo a 16/09).

**Alcance de corredores (scope) confirmado:**
- Cubiertos: Brasil, Canadá, Colombia, República Dominicana, México, Estados Unidos, Reino Unido, Suiza, SEPA.
- **China excluido** del scope — deseable pero no bloqueante para no atrasar el inicio del proyecto (decisión de Federico Darnond/Mastercard, ya acordada desde el 28/08).
- **México con limitación**: Mastercard solo proveyó una cuenta de prueba "Bank Account - Personal" para México (no "Business"/B2B) — el tipo de corredor B2B que menciona el Implementation Plan **no se puede cubrir** con la cuenta disponible. Casos de prueba cubribles para México: *Bank Account MXN P2P* y *Bank Account MXN B2P* únicamente.
- Mastercard pidió explícitamente que, si Bind quiere habilitar en Producción algún corredor sin completar su PVT correspondiente, se identifique el riesgo asociado a esa falta de validación de forma explícita y documentada.

> Pablo Gomes está solo en copia (cc) de este hilo como PM de Wallet — la iniciativa la lidera Luciana Rudaz (foco Pagos FX/Mastercard Move). Mismo criterio de atribución que `2026-08-14_wallet_pagosfx_primer_pago_prod` (ya mergeado en `dolar_fx.md`).
