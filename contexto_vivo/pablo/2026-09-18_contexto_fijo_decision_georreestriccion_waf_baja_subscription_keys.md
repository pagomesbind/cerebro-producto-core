---
id: 2026-09-18_contexto_fijo_decision_georreestriccion_waf_baja_subscription_keys
pm: pablo
fecha_captura: 2026-09-18
fuente: "/sync_meetings — reunión 'Repaso Semanal líderes' (2026-09-08), minuta Gemini, con Fintexa (Hernan Clarich, Pablo Vargas)"
producto: transversal
tema: refuerzo de seguridad perimetral tras el fraude de Credicotas — georrestricción/lista negra en WAF y baja de subscription keys
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Contexto — incidente disparador

Emma Vignoles relató que **Credicotas** (entidad ajena a Bind PSP, mencionada como precedente de la industria) sufrió un incidente de fraude donde un servicio de backoffice quedó expuesto a internet, permitiendo consultar saldos y ejecutar transferencias salientes por **$175.000.000** en 270 cuentas CBU. A partir de ese antecedente, el equipo de seguridad (Hernan Clarich, Pablo Vargas de Fintexa) propuso dos medidas de refuerzo perimetral para las APIs de Bind PSP.

## Decisiones acordadas (2026-09-08)

1. **Georrestricción + lista negra de IP en el gateway de seguridad (WAF):** limitar el tráfico a Argentina y Estados Unidos, más una lista negra de IPs. Se implementa primero en **modo monitor** durante 2-3 semanas (para no generar bloqueos operativos inesperados) antes de pasar a **modo bloqueo** definitivo.
2. **Eliminación de subscription keys:** actualmente ~30% de los clientes actuales usan claves de suscripción (subscription keys) para autenticarse, un mecanismo que el equipo quiere discontinuar migrando a OAuth por motivos de seguridad. Emma Vignoles exigió fijar una fecha límite estricta para forzar la migración (mencionó fin de septiembre en la reunión). Hernan Clarich queda a cargo de identificar a los clientes afectados y coordinar la campaña de migración con Mariana Nadalin y Gonzalo Rivera.
3. **Nueva política de filtrado de acceso a las APIs internas:** para limitar a los equipos de usuarios internos exclusivamente a consultas (evitar que alguien inyecte transacciones manualmente vía API), con despliegue en staging para el viernes siguiente a la reunión.

## Seguimiento (confirmado en "Repaso Semanal líderes" del 2026-09-15)

Una semana después, Pablo Vargas (Fintexa) confirmó que la nueva política de acceso a APIs se desplegó en el ambiente Station y se enviaron credenciales de prueba a Ana; se generó además un ticket de infraestructura para adaptar el script de alta de consumer al producto de operaciones internas. La georrestricción/lista negra sigue en curso en modo monitor. Alejandro Sfrede (Fintexa) sumó en esa misma reunión un frente relacionado — limpieza de credenciales sensibles en App Settings (empezando por Producción) y definición de qué auditar por microservicio — en el marco de la **certificación PCI de la entidad, con vencimiento el 15 de octubre de 2026** (a 30 días de esa reunión).
