---
id: 2026-08-19_onboarding_demo-propio-compliance-console
pm: pablo
fecha_captura: 2026-08-19
fuente: "/sync_meetings — reunión 'Demo ON BOARDING propio - Octagon' (docId 15bAV3zwZmPETPHhJD-OexAmAmiRdk_UIuj3k9rQwn-4), 2026-08-19 11:00, minuta+transcripción Gemini (compartida, owner dweledniger@bind.com.ar)"
producto: onboarding
tema: Demo completa del flujo de Onboarding PJ propio de Bind (front + consola de cumplimiento) a Octagon y Banco Industrial
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Contexto:** Luciano Dufain (Bind) hace una demo end-to-end del onboarding propio de persona jurídica a Octagon (cliente ya en producción, en integración evolutiva) y al equipo de Compliance de Banco Industrial (María Mercedes Carrasco), con Luciana Rudaz, Emma Vignoles, Adriana Endzeliz, Diego Weledniger y Pablo Gomes de Bind. Complementa lo ya documentado en `onboarding_personas_juridicas.md` (MVP OB PJ) y `propuesta_fintexa_onboarding_juridico.md` (base funcional del proveedor) con el detalle de cómo se ve/vende el flujo hoy en una demo real a un cliente.

**Flujo de alta demostrado (front, persona jurídica):**
1. Registro con CUIT/CUIL, validado automáticamente contra los servicios web de ARCA (inscripto y activo).
2. Carga de documentación societaria (estatutos, DNI del representante legal, acta de designación de autoridades) — la plataforma usa IA para extraer automáticamente los datos de estos archivos; el cliente puede revisar y reemplazar un documento si la carga fue incorrecta.
3. Alta de beneficiarios finales, con documento de identidad vía IA y validación de que la suma de porcentajes de participación cierre en 100%.
4. Verificación biométrica de los firmantes: escaneo de DNI (frente/dorso) + prueba de vida (liveness), con tecnología de **Neurotecnology**, validando identidad contra Renaper.

**Consola del oficial de cumplimiento (admin):**
- Cola de casos con resumen de la estructura societaria.
- Barrido automático inicial contra listas de sanciones: **OFAC, ONU, UIF, Repet, PEP**.
- Revisión documento por documento, con aprobación/rechazo individual y posibilidad de pedir aclaraciones/documentación adicional al cliente (ida y vuelta con notificación).
- KIC (Know Your Customer) completado por el oficial con tipo de cliente, volúmenes anuales y origen de fondos — el sistema calcula una matriz de riesgo/alertas en base a reglas de negocio configuradas, ajustable según la operación.
- Configuración de políticas internas por entidad: reglas de negocio parametrizables (ej. prohibir industrias específicas o estructuras societarias complejas) que aprueban, rechazan o alertan automáticamente según los criterios definidos (explicado por Begoña Perez de Solay).
- Trazabilidad/auditoría completa desde el inicio de la solicitud hasta el veredicto final (todo cambio, aprobación, rechazo u observación queda registrado).

**Pedido de acceso de Compliance de Banco Industrial:** María Mercedes Carrasco y su equipo pidieron acceso directo a la plataforma para auditar el legajo digital sin tener que solicitar documentos manualmente — Bind acordó otorgarlo (Diego Weledniger gestiona el acceso).

**Integración técnica pendiente de definir:** Begoña Perez de Solay y Diego Weledniger acordaron definir un "paquete de datos" para automatizar, una vez aprobada la solicitud de onboarding, la creación de la CBU y el alta del comercio en los sistemas de Bind (hoy manual). Pablo Gomes aclaró que aunque hoy pueden usarse los endpoints actuales para el alta directa, en los próximos meses habrá que migrar a nuevos endpoints por requerimientos normativos internos — un cambio que se describe como administrativo, no traumático para el cliente (sin mayor detalle técnico todavía).

**Potencial como producto externo (marca blanca):** se discutió explícitamente que el núcleo de esta solución de onboarding es modular y podría configurarse como producto adaptable para otros clientes externos, no solo para uso interno de Bind — ver oportunidad relacionada `2026-08-19_onboarding_oportunidad-marca-blanca-cumplimiento`.

**Próximos pasos:**
- Luciano Dufain envía un link para que el equipo se registre y pruebe el flujo como persona humana.
- Diego Weledniger coordina una reunión técnica con sistemas y producto para definir la integración (paquete de datos).
- Begoña Perez de Solay envía un paquete de datos estimado (basado en el onboarding actual) para la apertura de cuentas.
- Pablo Gomes: comunicar los detalles de la migración de API/nuevos endpoints (ver tarea T-020) y abrir un canal de integraciones (T-021).
