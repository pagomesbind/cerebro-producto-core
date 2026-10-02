---
id: 2026-10-01_onboarding_mecanica_lectura_dni_pdf417_mrz
pm: pablo
fecha_captura: 2026-10-01
fuente: "/sync_meetings — reunión 'Revisión OB Coppel | Casos de Rechazo' (docId 1Lcwat21mBuzIEJL6epuo7aim5A37HkttEcHn5TvABSU), 2026-10-01 16:01, compartida (aendzeliz)"
producto: onboarding
tema: Mecánica de lectura automática de DNI (PDF417/QR/MRZ) y workaround propuesto para fallos de lectura
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "no — complementa la mención ya existente en arquitectura_solicitud_y_flujos.md §1bis sobre reintentos configurables de PDF417, sin describir hasta ahora la cadena completa de fallback ni la librería usada"
confianza: alta
estado: en_cola
merge_commit:
---

Pablo Gomes le explicó a Adriana Endzeliz (Soporte) el mecanismo real de lectura automática de documento en Onboarding, usando casos reales de rechazo de Coppel como ejemplo. Completa el detalle técnico que `arquitectura_solicitud_y_flujos.md §1bis` ya documenta parcialmente (reintentos de PDF417 configurables por flujo).

**Cadena de lectura, en orden:**
1. El request de onboarding llega con las imágenes en base64 (frente, dorso, selfie) más los datos declarativos (email, teléfono, estado civil, ocupación, declaración). En ese momento el sistema **no tiene ningún dato estructurado del DNI** — solo las fotos.
2. Primer intento: leer el código de barras **PDF417** del frente del documento. Esto se hace con una librería paga externa llamada **Aspose**, integrada por Fintexa — Bind PSP paga por cada lectura efectuada. Si el PDF417 se lee bien, se obtienen número de trámite, nombre, apellido, documento y sexo, y con eso el flujo puede continuar a la consulta a Renaper Datos.
3. Si no se puede leer el PDF417 (típico en **DNI nuevo**, donde el PDF417 está en el frente pero a veces no es legible), el sistema busca el **código QR del dorso**. El problema: el QR **no incluye el dato de sexo/género** — campo que Renaper exige para la consulta.
4. Por eso hay un tercer intento: leer la **zona de lectura mecánica (MRZ)** del dorso, que sí contiene el sexo. Si tampoco se puede leer el MRZ, el flujo se frena ahí — no hay más fuentes de las que extraer los 3 datos mínimos (documento, número de trámite, sexo) necesarios para consultar a Renaper.
5. En **DNI viejo**, la cadena es la misma pero sin el paso de QR (los DNI viejos no tienen QR en el dorso) — si el PDF417 no se lee, se intenta directo con el MRZ.

**Limitación central de la librería:** Aspose (vía Fintexa) frecuentemente no logra detectar el código o el texto aun con fotos de buena calidad — un patrón observado es que falla más seguido con fotos tomadas desde iPhone, por el procesamiento de imagen que aplican esos dispositivos. El sistema hace **un solo intento de lectura por imagen enviada** — no hay reintento automático sobre la misma imagen con otro parámetro, solo reintento de todo el flujo si el cliente reenvía (esto es lo que la wiki ya documentaba como "reintentos configurables por flujo").

**Propuesta del PM (no implementada, directiva a comunicar a clientes):** dado que mejorar la librería de lectura requiere una inversión que hoy no se justifica (onboarding no es el producto principal de Bind PSP), la solución recae en las aplicaciones cliente: si el cliente tiene su propia librería de OCR superior (o reintenta pidiéndole al usuario otra foto), puede extraer él mismo documento, número de trámite y género, y enviarlos **en crudo** junto con las imágenes del DNI. Si Onboarding no puede leerlos de las imágenes pero el cliente los manda explícitamente, el sistema los toma y continúa el flujo normal (consulta a Renaper) sin bloquear. Esto no está comunicado hoy a los clientes que ya integraron (ej. Coppel, Arcos Dorados) — quedó como vector de reclamo recurrente de soporte.

**Patrón de rechazo observado:** la mayoría de los casos de Coppel no son por DNI nuevo con MRZ no legible (como el cliente asumía), sino que la falla de lectura ocurre en proporción similar en DNI viejos y nuevos — la causa de fondo es la limitación de la librería de lectura en general, no una particularidad del formato nuevo.

**Acción de seguimiento:** Pablo Gomes reportará internamente a Cristian (Fintexa) el caso puntual de falla de MRZ detectado en la reunión, para análisis — ver `tareas.md` T-159. Adriana Endzeliz le pedirá a Coppel que levante un ticket de soporte formal (no hay ninguno abierto hoy pese a los reclamos informales) para poder acompañarlos con la incidencia sin que Soporte termine resolviendo temas técnicos por canal informal.
