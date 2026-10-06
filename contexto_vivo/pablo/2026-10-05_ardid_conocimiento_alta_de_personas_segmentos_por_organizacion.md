---
id: 2026-10-05_ardid_conocimiento_alta_de_personas_segmentos_por_organizacion
pm: pablo
fecha_captura: 2026-10-05
fuente: "sesión de trabajo del proyecto bcra_anexo_b — definición del PM para los procedimientos de alta de personas (P-01, P-02, P-03)"
producto: ardid
tema: Alta de las personas en Ardid con un segmento por defecto (estándar, restringido o exclusivo de la organización) como capa adicional de seguridad
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

Definición del PM (2026-10-05): luego de crear una cuenta, el sistema la registra en la herramienta de monitoreo transaccional de fraude (Ardid) asignándole un **segmento**. El segmento puede ser, por defecto, **estándar** o **restringido**, y también **exclusivo de la organización** (el mensaje del PM quedó cortado en "exclusivo para …"; se interpretó como exclusivo de la organización, confirmar).

- **Para qué sirve:** permite personalizar, por organización, restricciones y reglas de monitoreo para las personas de un tipo específico que se acaban de crear en una organización determinada. Es una capa adicional de seguridad.
- **Quién define la configuración por defecto de los segmentos:** el equipo de Soporte junto con Cumplimiento (Compliance).
- **Cómo se documenta:** en los procedimientos de alta (P-01 personas humanas, P-02 personas jurídicas y P-03 alta con onboarding de la organización) se menciona de forma breve y se remite a un **Procedimiento de Alta de Personas en Ardid**, que se redacta aparte (P-07 del proyecto `bcra_anexo_b`).
- **Contexto ya documentado en la wiki:** `wallet/organizaciones_y_configuracion.md` §1 registra el alta de cuenta y CVU en Ardid con segmentos por organización y reintentos 3x; `referencia_estimaciones.md` menciona la segmentación diferenciada para cuentas de menores.
