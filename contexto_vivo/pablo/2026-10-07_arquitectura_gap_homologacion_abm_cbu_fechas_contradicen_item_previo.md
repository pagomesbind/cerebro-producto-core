---
id: 2026-10-07_arquitectura_gap_homologacion_abm_cbu_fechas_contradicen_item_previo
pm: pablo
fecha_captura: 2026-10-07
fuente: "/sync_mails — mail 'Homologación ABM de CBU' (threadId 1a1118409920cd9e), icm@coelsa.com.ar, 2026-10-06"
producto: transversal
tema: Fechas de homologación/producción del ABM de CBU (Totalizador de cuentas) no coinciden con lo ya capturado sobre el mismo tema
tipo: gap
destino_propuesto: wiki/3_recursos/arquitectura_sistema/ (archivo temático de homologación ABM CBU/Totalizador, ya referenciado por un item previo)
tipo_destino: actualizar
contradice: "ítem previo (2026-10-02, `arquitectura_conocimiento_homologacion_abm_cbu_totalizador`, ya ingestado al canon según el pull del 2026-10-02) decía: homologación disponible hasta 16/10/2026, producción desde 18/10/2026. Este mail de Coelsa (06/10) dice: ventana de homologación 24/08/2026 a 13/11/2026 inclusive, salida a producción a partir del 15/11/2026 — casi un mes de diferencia en producción (18/10 → 15/11)."
confianza: alta
estado: en_cola
---

Coelsa reenvía el aviso de homologación del servicio ABM de CBU vinculado al Totalizador de cuentas (dirigido a "equipo Banco Industrial", con Pablo Gomes en copia), con fechas que no coinciden con las que ya están documentadas en el canon sobre el mismo desarrollo:

- **Lo ya mergeado (2026-10-02):** "Coelsa actualiza el ABM de CBU del Totalizador de cuentas, homologación hasta 16/10 y producción 18/10."
- **Lo que dice este mail (06/10/2026, remitente `icm@coelsa.com.ar`, destinatarios `desarrollo@bancoindustrial.com.ar`, `productos@bancoindustrial.com.ar`, Pablo Gomes, entre otros):**
  - Ventana de homologación: **desde el 24/08/2026 hasta el 13/11/2026, inclusive** (ya está disponible el ambiente de Homologación para iniciar pruebas).
  - Salida a producción: **a partir del 15/11/2026** (no el 18/10 que decía el item anterior).
  - La nueva versión agrega registro de fecha de alta y fecha de baja de las cuentas bancarias, "en línea con los requerimientos normativos vigentes" (sin especificar cuál normativa).
  - Documentación técnica pública: `https://documentacion.coelsa.com.ar/aliascbu/#api-cbu-nuevo` (API) y `#batch-cbu-nuevo` (BATCH).
  - Contacto Coelsa para consultas: `icm@coelsa.com.ar`.

No hay forma de saber desde este mail solo si la fecha de producción se corrió (18/10 → 15/11) o si el item previo tenía mal la fecha desde el origen — el mail no hace referencia explícita a un cambio de cronograma, solo informa el estado vigente. Dado que hay casi un mes de diferencia y el servicio toca directamente el Totalizador de cuentas (relevante para BCRA Anexo B / normativa de cuentas), conviene que el PM confirme con Hernán Clarich o directamente con Coelsa cuál de las dos fechas de producción es la vigente antes de dar el item anterior por correcto.
