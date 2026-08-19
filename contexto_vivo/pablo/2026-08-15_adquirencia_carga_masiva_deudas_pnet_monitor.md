---
id: 2026-08-15_adquirencia_carga_masiva_deudas_pnet_monitor
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión AD 71.2 FIX (PNET) (publicada 2026-08-12), tickets AD-1515, AD-1516, AD-1517, AD-1518"
producto: adquirencia
tema: Carga masiva de deudas ProvinciaNET — mejoras al Monitor de archivos
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/botones_de_pago_y_qr.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Ampliación de la sección **"Carga masiva de deudas — cliente ProvinciaNET"** (hoy solo cubre AD-496 y AD-660): 4 tickets de ajuste al **Monitor de API Deuda** que procesa los archivos de carga masiva, todos "Desarrollo para PNET, no requiere testing" (comentario de Andrea Orsini, 2026-08-12).

- **Manejo de archivos fallidos (AD-1518):** si un archivo está bien nombrado pero mal generado (ej. falta un dato obligatorio en alguna fila), hoy queda indefinidamente en la carpeta `En_Proceso` con estado `ERROR` en `dbo.EjecucionFlujo`, bloqueando el procesamiento del resto de los archivos en `A_Procesar`. Fix: se crea una carpeta `Fallidos` en el Storage; el Monitor mueve ahí los archivos con estado `ERROR`. El archivo queda comprimido (se elimina el `.csv` suelto si existe) y descargable desde el endpoint de la API `FileManager`.
- **Salida comprimida (AD-1517):** los archivos de salida del proceso ahora se generan en `.zip`, para evitar problemas de descarga por tamaño.
- **Entrada comprimida (AD-1516):** el Monitor ahora descomprime los `.zip` de entrada para poder procesar el `.csv` (contraparte de AD-1517, del lado de ingesta).
- **Archivado histórico (AD-1515):** se deja copia del archivo histórico procesado (`{nombre-archivo}_{fecha-proceso}.csv`) en `rendiciones/entidades/A026/QrMasivo/Historico`, se deja de copiar a `rendiciones/entidades/A026/QrMasivo/Procesados`, y una vez que el proceso del archivo actual queda `NOTIFICADO`, se mueven a `Historico` los archivos del procesamiento anterior que no correspondan al nombre recién generado.

Los 4 tickets referencian internamente el Jira de Fintexa (DAD-2045, DAD-2001, DAD-2000, DAD-1778) — sin Epic Link de Bind PSP, sin SP cargados.

**Nota — no cruza con `1_proyectos/`:** esta versión (AD 71.2 FIX (PNET)) también publicó AD-861, AD-860 y AD-1140, que ya están documentados en la wiki vía `/sync_meetings` (`botones_de_pago_y_qr.md` §"Ampliación del webhook de Deuda y cálculo de vencimientos", release v71.2 2026-08-10) y en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md` (AD-861/AD-860) y `1_proyectos/proyecto-ministerio/prd-134_ministerio_productos_bs20_pos/proyecto.md` (AD-860/AD-861, antes "En curso"). Esta ingesta solo confirma la versión de publicación de esos tres — el PM puede querer marcar esos tickets como Finalizados/publicados en sus proyectos si aún no lo reflejaron.
