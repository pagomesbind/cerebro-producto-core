---
id: 2026-10-15_adquirencia_homologacion_billetera_cencopay_coelsa
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_mails — mails Coelsa 'Homologación Billetera Cencopay - Aceptador BindPagos ID 532' y 'Resolución del ticket 515975/515979' (threadIds 1a14101cd7988e1a, 1a1412bdb61787e7, 1a14123e387b6ba5), 2026-10-15"
producto: adquirencia
tema: Nueva billetera Cencopay (Cencosud) inicia y cierra homologación de interoperabilidad QR con los dos aceptadores de Bind el mismo día
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "no — mismo patrón ya documentado para la billetera YDI (2026-09-28_adquirencia_homologacion_billetera_ydi_coelsa, archivado en 4_archivos/contexto_ingestado/2026-09-29/)"
confianza: alta
estado: en_cola
merge_commit:
---

Coelsa (`icm@coelsa.com.ar`) notificó el 2026-10-15 el inicio del "Procedimiento Interno de Homologación para Billeteras y Aceptadores" (el mismo trámite ya documentado en `mecanica_qr_coelsa.md` para otros pagadores, ej. YDI) para una nueva billetera:

**Datos de la billetera nueva:**
- Denominación: **Cencopay**
- Razón social: CENCOSUD S.A.
- CUIT: 30590360763
- ID BILLETERA COELSA en HOMO: 20260925

Coelsa pidió a Bind los datos de ambos aceptadores para arrancar las pruebas cruzadas de acreditación. Alan Martínez (Bind, Área Técnica) respondió el mismo día (ya que "el PSP lo administramos nosotros") con los datos del aceptador BindPagos ID 532 (BIND PAGO SA, CUIT 30717449076, ID PSP PROD 184, misma URI de API Resolve/IEP de HOMO ya documentada) y ejecutó un pago de prueba que resultó **exitoso**: `"operacionIdExterno": "L18MKX9R10O6J5K9O6WYV4", "estadoExterno": "ACREDITADO"`, importe $100.

**A diferencia del proceso de YDI (que arrancó el 25/09 con pruebas en vivo recién desde el 19/10), el de Cencopay se resolvió el mismo día de inicio:** los tickets #515975 (aceptador Tecnología Financiera ID 531) y #515979 (aceptador BindPagos ID 532) llegaron a estado "resuelto" (encuesta de satisfacción de Coelsa) horas después de abrirse, sin incidencias visibles en el hilo — homologación cerrada sin objeciones.

**Cronograma formal del proceso (según el mail de Coelsa, aunque en la práctica cerró antes):**
- Comienzo de la homologación: 2026-10-15
- Reuniones vía Teams para pruebas en vivo: a partir del 2026-11-02

**Billeteras y aceptadores convocados a la prueba cruzada más amplia (invitación Teams separada, mismo día):** además de los dos aceptadores propios de Bind (531/Tecnología Financiera y 532/BindPagos), Coelsa convocó en paralelo a ULTRA (Cumar SA), Easypagos, 3SM Código Pago, BPN Pagos, Sipagos, Pagotic y Tach — confirma que el proceso de homologación de Cencopay no es exclusivo con Bind, sigue el mismo esquema de prueba cruzada multi-aceptador ya conocido.

> Fuente: hilo "Homologación Billetera Cencopay - Aceptador BindPagos ID 532" (threadId `1a14101cd7988e1a`), Coelsa/Alan Martínez, 2026-10-15; hilos "Resolución del ticket 515975/515979" (threadIds `1a1412bdb61787e7`, `1a14123e387b6ba5`), 2026-10-15.
