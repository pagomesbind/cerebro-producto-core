---
id: 2026-10-05_wallet_riesgo_cuentas_faltantes_ardid_v73
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_mails — mail \"Informe Estado Proyectos Emisión al 02/10/2026\" (threadId `1a0fdfa3c6f68d66`), Nicolas Pomponio (Fintexa), 2026-10-02"
producto: wallet
tema: Desde la V73, todas las operaciones de Wallet pasan por Ardid — cuentas no dadas de alta quedan rechazadas
tipo: riesgo
proyecto: —
pm_destino: Nicolás Colón
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no — riesgo operativo nuevo, no reemplaza ninguna entrada existente"
confianza: alta
estado: ingestado
merge_commit: c0d6964
---

El informe semanal de Wallet (Fintexa, Nicolas Pomponio, informe al 02/10/2026) confirma que, desde la publicación de la versión W73 (pase a producción confirmado jueves 08/10/2026), **todas las operaciones de Wallet van a pasar por Ardid** (motor antifraude). Es clave dar de alta en Ardid, antes del pase, las cuentas que todavía no estén registradas — de lo contrario empiezan a rechazarse sus operaciones apenas se publique la versión.

**Próximo accionable confirmado en el informe:** Nicolás Colón (Bind PSP) se encarga del alta de las cuentas faltantes en Ardid. Por eso este item se marca con `pm_destino: Nicolás Colón` — es su proyecto/responsabilidad, Pablo Gomes queda en copia del hilo.

**Relacionado:** la misma versión W73 despliega el QR GetNet (proyecto `getnet_oauth2_resolve/`, PRD-237) con el flag de autenticación configurable apagado el jueves, activándolo recién el viernes 09/10 fuera de horario transaccional — ya documentado en `getnet_oauth2_resolve/proyecto.md`, sin novedad adicional sobre ese punto en este mail.

> Fuente: mail "Informe Estado Proyectos Emisión al 02/10/2026", Nicolas Pomponio (Fintexa), 2026-10-02.
