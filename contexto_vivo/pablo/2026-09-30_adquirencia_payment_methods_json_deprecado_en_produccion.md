---
id: 2026-09-30_adquirencia_payment_methods_json_deprecado_en_produccion
pm: pablo
fecha_captura: 2026-09-30
fuente: "análisis propio de datos reales de producción (export de transacciones con tarjeta, formas de pago 60/80/90, mañanas del 2026-09-29 y 2026-09-30), a pedido del PM en el marco de rechazos_bines_payway (PRD-251)"
producto: adquirencia
tema: despliegue v73 (29/09) ejecutó la eliminación de la validación de payment_methods.json y la carga masiva de BINs — impacto confirmado con datos reales
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/validacion_bines_tarjetas.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/adquirencia/validacion_bines_tarjetas.md §4 (líneas ~93-97) — dice que la eliminación de la validación de payment_methods.json del frontend estaba 'empaquetado en el despliegue de la versión 73 (jueves 24/09)', tratándolo como plan a futuro. En los hechos el despliegue del 24/09 se canceló esa misma noche (atraso de QA, defectos de liquidaciones) y se reprogramó al martes 29/09 20:30hs, fecha en la que finalmente se ejecutó con éxito — el fix ya está en producción, no pendiente."
confianza: alta
estado: en_cola
merge_commit:
---

## Qué cambia respecto de lo ya mergeado

El canon (`validacion_bines_tarjetas.md` §4) describe correctamente el mecanismo de fondo (dos sistemas independientes resolviendo el tipo de tarjeta — `payment_methods.json` en el frontend e `IssuerIdentification` en el backend — con un chequeo de consistencia que rechaza con `400` si discrepan) y cierra con "Fintexa decidió ir más allá del ajuste temporal: eliminar la validación de bines del frontend directamente [...], empaquetado en el despliegue de la versión 73 (jueves 24/09)". Eso quedó desactualizado en dos sentidos: (1) el despliegue del 24/09 no salió esa noche (se canceló por atraso de QA y defectos bloqueantes en tickets de liquidaciones, ver `1_proyectos/rechazos_bines_payway/proyecto.md` §8), y se reprogramó al martes 29/09 a las 20:30hs; (2) esa nueva fecha **sí se cumplió**: el despliegue v73 salió en producción el 29/09 entre las 20:30 y las 23hs, con la eliminación de la validación del frontend y, en el mismo despliegue (bloque "Saneamiento de BD"), la aplicación del ticket AD-978 (carga masiva de ~89.717 BINs reales en `IssuerIdentification`, preparada desde el 17/09 y bloqueada en producción desde el 21/09 exactamente por este mecanismo).

## Evidencia de producción (30/09)

El PM aportó el export real de transacciones con tarjeta (formas de pago 60=prepaga, 80=crédito, 90=débito) de la mañana del 30/09 y pidió comparar contra la misma ventana horaria del día anterior, para verificar si el fix tuvo el efecto esperado. Ventana usada: 00:00:00–10:31:54 hora local, idéntica en ambos días (corte real del export del día de la medición).

- **Volumen:** 5.356 transacciones (29/09, pre-fix) → 6.168 transacciones (30/09, post-fix) — **+15,2%**. Consistente con la mecánica ya documentada: una tarjeta con BIN no reconocido antes ni siquiera generaba una fila de transacción (el checkout/POS la bloqueaba antes de intentar el cobro); al reconocerse el BIN, al menos llega a intentarse.
- **% de rechazo:** 18,82% (29/09) → 17,28% (30/09) — mejora de 1,5 puntos, consistente hora a hora (no concentrada en un pico puntual). La mezcla de motivos de rechazo no cambió de composición entre ambos días (mismos motivos dominan en proporciones similares: "Rechazada por Ardid", "No posee fondos suficientes", "Tarjeta denegada", errores de sistema) — coherente con que "BIN no reconocido" nunca aparece como motivo explícito de rechazo, precisamente porque esas transacciones no llegaban a registrarse.
- **BINs concretos antes inexistentes en el sistema:** el PM pidió una verificación más directa — ¿aparece alguna transacción real de un BIN que antes desconocíamos? Un primer cruce contra el archivo de referencia de Payway (`BINES_T1952.TXT`, snapshot del 19/08, usado como proxy) había dado una señal débil y, al revisarla con más cuidado, parcialmente errónea (dos de los BINs candidatos, al chequear el día completo y no solo la ventana matutina, ya tenían transacciones horas antes del despliegue). El cruce correcto usa la lista real de BINs que el ticket AD-978 dio de alta/reactivó en `dbo.IssuerIdentification` (89.721 BINs, `artefactos/rechazos_bines_payway-fintexa_altas.csv`/`-fintexa_reactivaciones.csv`) contra el día completo de transacciones, con el corte en el horario real del despliegue (29/09 20:30hs) en vez de la medianoche. Resultado: **37 BINs de esa tanda no registran ninguna transacción en todo el 29/09 antes de las 20:30, y suman 105 transacciones en total desde el despliegue en adelante** (29/09 20:30-23:59 + todo el 30/09 medido).
- **Casos testigo concretos (los 4 de mayor volumen, de los 37):** **244014** (Mastercard Crédito) — 36 transacciones, 27 acreditadas, primera transacción a las 23:04:22 del 29/09 (dentro de la ventana del despliegue). **233064** (Mastercard Prepaga) — 10 transacciones, 8 acreditadas, primera a las 23:22:43. **233081** (Mastercard Débito) — 8 transacciones, 6 acreditadas, primera a las 23:20:04 (rechazada por error de sistema, las siguientes 7 aprobadas normalmente). **376402** (Amex Crédito) — 7 transacciones, 4 acreditadas. Los tres primeros arrancan a operar en un rango de 18 minutos, todos dentro de la ventana misma del despliegue (20:30-23hs) — la señal más limpia posible de que el fix tuvo efecto inmediato.

**Caveat de método:** comparación de un solo día contra el anterior (martes vs. miércoles, no controla estacionalidad semanal) — la lectura es consistente y direccionalmente sólida, pero no reemplaza una medición formal sostenida en el tiempo. Importante para quien retome este análisis: verificar contra la lista real de BINs dados de alta (no contra un archivo de referencia externo) y usar el horario real del evento como corte, no la medianoche — restringir la comparación a una ventana horaria fija (ej. "la mañana") puede generar falsos positivos con BINs de bajo volumen que simplemente no transaccionaron temprano ese día por azar.

## Relevancia para el canon

Confirma en producción, con datos reales, que la resolución de fondo que Fintexa había anunciado el 22/09 (eliminar la validación del frontend en vez de sincronizarla) efectivamente se implementó y funciona como se esperaba — cierra de facto T-115 (`1_proyectos/rechazos_bines_payway/tareas.md`) y el gap G12 (bloqueante) sin necesidad de esperar la confirmación formal por escrito de Fintexa. Detalle completo de la medición y el seguimiento del proyecto en `1_proyectos/rechazos_bines_payway/proyecto.md` §7 y §9.
