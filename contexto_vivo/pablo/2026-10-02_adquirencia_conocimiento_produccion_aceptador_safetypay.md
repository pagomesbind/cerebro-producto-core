---
id: 2026-10-02_adquirencia_conocimiento_produccion_aceptador_safetypay
pm: pablo
fecha_captura: 2026-10-02
fuente: "/sync_mails — hilo \"PRODUCCION: Aceptador Safetypay (Newpay) – Billetera BIND PSP (COELSA)\" (threadId 1a0f88a4a284598e), Rocío Rodríguez (Newpay), 2026-10-01"
producto: adquirencia
tema: Nuevo aceptador QR interoperable habilitado en producción — Safetypay, vía proxy Newpay
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ecosistema_wallet_adquirencia/aceptadores_homologados.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

El aceptador **Safetypay** (Paysafe Group) quedó habilitado para operar en producción dentro del ecosistema QR interoperable, vía el mismo proxy Newpay que ya usan otros aceptadores homologados con Billetera BIND PSP (patrón ya documentado para WAYA, ver `mecanica_qr_coelsa.md`).

**Datos de configuración (producción):**
- Denominación: Safetypay · Razón social: Safetypay Argentina S.A. · CUIT: 30717813185.
- Reverse Domain: `com.safetypay`.
- URL IEP producción (Proxy Newpay): `https://wallet.newpay.com.ar/external/resolve?access_token={Access_token}&data={QR_RAW}` — mismo mecanismo estándar `access_token` en query param que usa el resto del ecosistema (no OAuth2 como Getnet).
- Access Token producción: reutiliza el ya configurado para el "Proxy Newpay" en Billetera BIND PSP.
- Datos del Administrador (Aceptador): NEWPAY S.A.U., CUIT 30-71786245-3.

**Prueba productiva realizada el mismo día (2026-10-01):** pago de prueba con QR real ejecutado con éxito — `operacionIdExterno: LOEJWV9JXWM5755RNQMD0G`, `estadoExterno: ACREDITADO`. Alta de configuración confirmada por Alan Martínez (BIND PSP, Área Técnica).

> Fuente: hilo de mail "PRODUCCION: Aceptador Safetypay (Newpay) – Billetera BIND PSP (COELSA)" — Rocío Rodríguez (Newpay) / Adriana Huerta (Paysafe) / Alan Martínez (BIND PSP), 2026-10-01, threadId `1a0f88a4a284598e`.
