---
id: 2026-09-04_adquirencia_qr_masivo_provincia_net
pm: pablo
fecha_captura: 2026-09-04
fuente: "Reunión 'Producto - Prioridades' (2026-09-04 14:01 + 14:12), minutas y transcripción Gemini — frontmatter corregido y ampliado 2026-09-08 con análisis de datos propio (ver actualización abajo)"
producto: adquirencia
tema: Saturación de cola de generación de QR por carga masiva de Provincia Net
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

# Generación masiva QR Provincia Net — impacto en latencia

## Problema detectado (2026-09-04, reunión "Producto - Prioridades")

Provincia Net **genera códigos QR de forma masiva** (batch, a través de API o endpoint), saturando la cola general de generación de QR de Bind PSP. Impacto:
- Latencia en generación de QR para **todos los clientes** afectados: **hasta +35 segundos**.
- Clientes identificados con reclamos en la reunión: **Provincia Net (P1)** y **"Pay"** (también afectado) — ver actualización 2026-09-08: "Pay" es **DEPAY**, confirmado por un reclamo separado del mismo cliente el 08/09.
- Recurrencia: **Principios de mes** (cuando hay más deudas/facturación).

## Solución propuesta (en evaluación al 2026-09-04)

Crear una **cola diferenciada** para generación masiva de QR:
- Ruta para batch/masivo (Provincia Net).
- Ruta para generación normal (resto de clientes).
- Evita contaminación cruzada.

## Análisis (2026-09-04)

- **Ticket:** AD935 (sin cotización inicial).
- **Prioridad:** **1** (urgencia máxima).
- **Urgencia:** Resolver cuanto antes (principios de mes son críticos).
- **Posible como fix:** Sí, según Matías Alzogaray.
- **Riesgo:** Bajo (cambio de cola, no de lógica central).

## Próximos pasos (al 2026-09-04)

[Nicolás Colón] Consultar a Alan (Provincia Net): detalles técnicos de uso QR masivo.
[Matías Alzogaray] Evaluar si puede salir como fix o requiere despliegue estándar.
[Matías Alzogaray] Confirmar fecha de resolución con Meli (Fintexa).
[Equipo] Registrar ticket de desarrollo en calendario.

> Fuente: Reunión "Producto - Prioridades" (2026-09-04 14:01 + 14:12), minutas y transcripción Gemini.

---

## Actualización 2026-09-08 — confirmación cuantitativa vía análisis de datos

Sesión de análisis de `dbo.Deuda` (export por entidad/día/estado, agosto completo + semana del 31/08-06/09, `raw/analisis cantidad de deudas.xlsx`) a raíz de un reclamo repetido del mismo cliente **DEPAY** (WhatsApp, Gono, 2026-09-08 16:27hs — "siempre recibimos PRECARGADO" al consultar el QR, timeout de 30s del lado del cliente) y del ticket de Soporte [AD-1676](https://bindpsp.atlassian.net/browse/AD-1676) (2026-09-04, mismo síntoma con 35s, atribuido a Provincia NET). **Confirma con datos lo que esta reunión ya había diagnosticado cualitativamente el mismo día:**

- **PNET (código A066) es el driver casi exclusivo de los picos de volumen** — 899.914 deudas en 37 días, 2,5× la entidad #2 (RIPSA) y más que todas las demás ~40 entidades sumadas.
- **El volumen de PNET creció de forma sostenida, no es un pico aislado**: promedio diario de agosto 18.820/día → 49.917/día en la semana del 31/08-06/09 (2,65×). El quiebre de nivel coincide con el pase a producción del proceso de **carga masiva por SFTP** de PNET el 2026-08-13 (ver `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §7`).
- **Pico extremo el 2026-09-01: 210.431 deudas de PNET en un solo día — 78,9% de todo el volumen del sistema esa jornada** (266.736 en total) — confirma la recurrencia "principios de mes" ya señalada en la reunión del 09-04 (ciclo de facturación mensual de municipios).
- **DEPAY (código A042, el "Pay" mencionado en la reunión del 09-04) no incrementó su propio volumen**: 1.174 → 1.204 deudas/día, sin cambio en 5+ semanas — confirma que DEPAY es un tercero afectado por la cola compartida, no un contribuyente del problema.
- **No hay evidencia de deudas trabadas para siempre**: de todo lo creado antes del 1/9, solo 13 filas en total siguen en PRECARGADO — la demora es de cola bajo pico de carga (consistente con la solución de "cola diferenciada" ya propuesta acá), no una falla de procesamiento.

**No se identificó ninguna otra entidad nueva** generando volumen relevante — el único contribuyente secundario con crecimiento notable es CobroExpress (código `C`, 2,29×), en un orden de magnitud muy por debajo de PNET.

Análisis completo (gráfico diario por entidad + ranking) armado como artifact para discusión con Fintexa. Tarea de seguimiento: T-072 en `1_proyectos/tareas.md` (confirmar con Provincia NET su volumen productivo real y llevar a Fintexa el estado de AD935/la cola diferenciada a la luz de este volumen ya varias veces mayor al de la prueba de carga de 150K acordada el 08-20).

## Ampliación 2026-09-08 (misma sesión) — junio-julio como control, y objeción del PM que deja la causa sin confirmar

El PM pidió sumar el mismo export para junio-julio (98 días de historia en total) para poner a prueba con más rigor si PNET "cambió su forma de operar". Primer resultado — **corrige la lectura de "creció 2,65×" de arriba, que comparaba solo 4 semanas**: el volumen de los picos de PNET no es nuevo (4 picos ≥100.000/día ya en junio-julio, uno de ellos —17/06: 237.958— más grande que el del 01/09); agosto fue, de hecho, un mes más tranquilo que junio/julio en promedio diario.

Una primera lectura de la "anatomía del pico" (estallido aislado antes del 13/08 vs. rampa sostenida después) **quedó en duda tras objeción directa del PM, verificada con los propios datos**: la concentración de PNET en el volumen total del sistema durante los picos de junio-julio (94,8%-96,7%) fue igual o mayor que la del pico del 01/09 (78,9%) — si la sola dominancia de PNET saturara la cola, junio/julio deberían haber tenido el mismo problema, y no hay evidencia de reclamos esos meses. Se encontró un lead alternativo sin confirmar: el ajuste de tiempos de **resolución de pagos** QR de PRD-199 (`bajar-tiempos-pagos-qr`, Nicolás Colón — ver `mecanica_qr_coelsa.md §"Parte 5"`) entró en producción el 2026-08-31, un día antes de la ventana de reclamos — mecanismo distinto al que reporta DEPAY, pero coincidencia temporal fuerte.

**Sin conclusión cerrada.** DEPAY sí se confirma estable en los 4 meses completos (1.035-1.346/día, sin tendencia) y no hay backlog permanente ni con ventana de 30 días. Pero la causa raíz de "por qué ahora y no en junio/julio" sigue abierta — ver gap y tarea T-072 en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/gaps.md`/`tareas.md`. Detalle completo en `proyecto.md §7`.
