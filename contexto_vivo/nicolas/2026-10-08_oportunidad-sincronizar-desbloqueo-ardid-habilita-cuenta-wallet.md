---
id: 2026-10-08_oportunidad-sincronizar-desbloqueo-ardid-habilita-cuenta-wallet
pm: nicolas
fecha_captura: 2026-10-08
fuente: "Charla directa con el PM (2026-10-08) sobre el reclamo de COTO + PRD-187, sección 'Funcionalidades a considerar a futuro'"
producto: wallet
tema: Sincronizar el desbloqueo de Ardid con Wallet — que desbloquear en el front de Ardid rehabilite la cuenta de Wallet
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

**Oportunidad:** con PRD-187 (W73), un bloqueo de Ardid deshabilita la cuenta de Wallet, pero el desbloqueo no se propaga. Para que la persona vuelva a operar, la organización tiene que desbloquear en Ardid y además llamar a `PATCH /Habilitado/Cuenta/{id}`. Si lo hace en el orden inverso, la próxima operación analizada vuelve a deshabilitar la cuenta.

**Señal de demanda:** COTO opera los bloqueos desde el front de Ardid y se queja de que integrar el endpoint de habilitación de Wallet no está en su flujo y le pone un freno (reportado por el PM el 2026-10-08). PRD-187 ya listaba "Sincronizar automáticamente el bloqueo Ardid<->Wallet" como fuera de alcance para una próxima etapa.

**Producto:** Wallet + Ardid. **Origen:** reclamo de cliente (COTO). **Fecha detectada:** 2026-10-08. **Foco estratégico:** Ardid / experiencia de integración de clientes. Estado: Nueva. Para evaluar: si Ardid (Pentass) puede emitir un evento o callback al desbloquear, o si alcanza una alternativa en Wallet (por ejemplo, revalidar con Ardid al habilitar).
