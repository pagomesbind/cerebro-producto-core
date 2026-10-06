---
id: 2026-10-05_onboarding_decision_encriptacion_base_aes256
pm: pablo
fecha_captura: 2026-10-05
fuente: "sesión de trabajo del proyecto bcra_anexo_b — definición del PM al revisar P-01"
producto: onboarding
tema: Cifrado de los datos personales en la base de Onboarding: AES-256
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/arquitectura_solicitud_y_flujos.md
tipo_destino: actualizar
contradice: "no — confirma el AES-256 del item ya ingestado 2026-10-05_onboarding_conocimiento_pf_comportamiento_confirmado_encriptacion_config_flujos; el mismo día el PM había dicho SHA-256 por error y lo corrigió el 2026-10-06."
confianza: media
estado: en_cola
merge_commit:
---

El PM definió (y el 2026-10-06 corrigió el dato anterior) que el cifrado de los datos personales en la base de datos de Onboarding es **AES-256**, sobre la lista de datos ya definida: nombre y apellido, fecha de nacimiento, DNI, CUIL, número de trámite, imágenes de frente y dorso del documento, dirección, teléfono, correo e identificador de dispositivo (hash). AES-256 es un cifrado simétrico por bloques con clave de 256 bits.

Por verificar con Ingeniería (tarea T-169): que esté implementado y cómo se gestionan y rotan las claves.
