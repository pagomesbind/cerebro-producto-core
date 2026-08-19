---
id: 2026-08-15_dato_changelog_releases_tanda1
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — barrido incremental 2026-08-15, tanda 1/N"
producto: transversal
tema: Entrada de changelog de producto para AD 71.2 FIX (PNET) y ARDID V 1.18.2.1 HF
tipo: dato
destino_propuesto: 3_recursos/datos/changelog_releases.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 9306bc6b7cffeb57db264f132b0e0e6a1ec53d8e
---

Prepend (orden cronológico inverso) al changelog:

## 2026-08-12 — AD 71.2 FIX (PNET) (Adquirencia)

**Mejoras funcionales:**
- El proceso de carga masiva de deudas para ProvinciaNET ahora comprime los archivos de salida (evita fallos de descarga por tamaño) y puede procesar archivos de entrada comprimidos.
- Los archivos con datos mal generados que quedaban trabados indefinidamente en el proceso de carga masiva ahora se mueven automáticamente a una carpeta de fallidos, sin bloquear el resto de la cola.
- El historial de archivos procesados de la carga masiva ahora se archiva ordenadamente, liberando la carpeta de trabajo activo.

**Nota:** esta versión también incluyó cambios sobre el webhook de deudas y las devoluciones de Simple Button 2.0 (montoProximoVencimiento, integración con Carnot) — ya cubiertos en la entrada de novedades de producto correspondiente al release v71.2 (2026-08-10, vía minutas de reunión).

---

## 2026-07-22 — ARDID V 1.18.2.1 HF (Ardid)

**Arreglos de errores:**
- Hotfix de motor antifraude (proveedor Ardid/Pentass): se agregaron reintentos automáticos a los procesos internos de validación de pagos y transferencias que en algunos casos tardaban demasiado en responder — mitiga (sin resolver la causa de fondo) el incidente del 2-3 de julio en el que operaciones válidas fueron rechazadas por una falla en el reinicio de los límites diarios de transferencias/pagos.
