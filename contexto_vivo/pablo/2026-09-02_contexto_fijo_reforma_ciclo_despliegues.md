---
id: 2026-09-02_contexto_fijo_reforma_ciclo_despliegues
pm: pablo
fecha_captura: 2026-09-02
fuente: "/sync_mails — mail \"MINUTA - Repaso Semanal líderes: Mar, 1 de sept de 2026\" (threadId 1a05e97ebeb0061d), Matías Alzogaray (PM, minuta directa — no Gemini), 2026-09-01"
producto: transversal
tema: Reforma del ciclo de despliegues — vuelta a ciclos quincenales con Release Candidates, desacople AD/Wallet, protocolo de hotfix formalizado
tipo: decision
destino_propuesto: 2_areas/procesos/publicaciones_mensuales.md
tipo_destino: actualizar
contradice: "2_areas/procesos/publicaciones_mensuales.md — el documento describe un ciclo mensual de 4 ceremonias; esta decisión lo reemplaza por un ciclo quincenal con Release Candidates congelados 10-15 días"
confianza: alta
estado: en_cola
merge_commit:
---

**Fuente:** reunión "Repaso Semanal líderes" del 2026-09-01, minuta redactada y enviada directamente por Matías Alzogaray (PM) al equipo ampliado (Fintexa, Tecnológica Financiera, Bind) — no es la minuta automática de Gemini, es un documento propio del PM con resumen ejecutivo, tabla de acciones y detalle de temas tratados.

**Disparador:** sobrecarga operativa crítica tras realizar **cinco lanzamientos en 24 horas**, con fallas graves de coordinación y jornadas laborales insostenibles. Se mencionó explícitamente el impacto de una **multa (monto redactado en la minuta) originada por errores en las pruebas de bloqueo de transacciones de Ardid** — ver item de riesgo relacionado `2026-09-02_riesgo_multa_pruebas_bloqueo_ardid`.

**Decisión tomada — reforma del ciclo de despliegue:**
1. **Vuelta a ciclos quincenales acotados**, abandonando la planificación desestructurada actual. Se adopta un formato de **Release Candidates**: versiones cerradas y congeladas durante 10 a 15 días para garantizar estabilidad en producción.
2. **Desacoplamiento de verticales**: los lanzamientos de Adquirencia (AD) y Wallet dejan de ir acoplados — cada vertical evalúa sus propios tickets pendientes y define su cronograma, evitando implementar la misma semana.
3. **Limpieza obligatoria de Staging**: el ambiente está saturado por acumulación histórica de tickets sin resolver; es mandatorio vaciarlo para permitir lanzamientos más controlados (arrastre de microservicios interconectados identificado como causa raíz de la congestión).
4. **Alineación negocio-desarrollo previa**: el análisis de alcance técnico debe hacerse **antes** de iniciar el desarrollo, no en paralelo — se evidenció que el equipo técnico desconocía las prioridades reales del negocio, generando cuellos de botella y compromisos comerciales no viables.
5. **Protocolo de hotfix formalizado**: las correcciones críticas de producción deben canalizarse obligatoriamente por el mecanismo de hotfix ya existente (el mismo usado en FCI), para no contaminar el ciclo principal de 15 días.

**Temas en stand-by (parking lot, sin decisión todavía):**
- Revisión de la arquitectura de microservicios para reducir dependencias cruzadas que hoy obligan a arrastrar componentes no prioritarios en los despliegues (propuesta de Nicolás Pico, Fintexa).
- Planificación de mantenimientos mensuales estandarizados y alineación operativa entre QA de Fintexa y QA de Bind PSP.

**Plan de acción con dueños y fechas (semana del 1-8 de septiembre 2026):**
| Acción | Responsable | Fecha límite |
|---|---|---|
| Presentar propuesta de alcance y tickets para la versión 73 | Melisa Belpassi, Nicolás Pomponio | Jue 3/9 |
| Definir, consolidar y compartir alcance final de la versión 73 | Matías Alzogaray, Pablo Serra | Vie 4/9 |
| Entrega y publicación del primer Release Candidate en Staging | Juan Pablo Carubelli | Lun 7/9 |
| Solicitar al banco habilitación de permiso Coelsa admin en consola | Gonzalo Rivera | Próxima reunión |
| Revisar, limpiar y cerrar tickets pendientes en Staging | Melisa Belpassi | Vie 4/9 |
| Establecer rutina de priorización de negocio con Comercial/Producto | Matías Alzogaray | Vie 4/9 |
| Sumar referente de Ardid a las reuniones de coordinación | Hernán Clarich | Próxima reunión |
| Coordinar reuniones para optimizar soporte y QA | Matías Alzogaray, Hernán, Maru | Vie 4/9 |
| Coordinar con QA la viabilidad del alcance de cada versión | Melisa Belpassi, Nicolás Pomponio | Permanente |
| Desarrollar planificación mensual de fechas/responsables/alcance | Equipo producto | Permanente |

**Próxima revisión:** martes 8 de septiembre de 2026 — evaluar impacto y estabilidad del primer Release Candidate publicado en Staging el 7/9, avance de la depuración de Staging, y validación de la nueva dinámica quincenal.

> Pablo Gomes está en copia como PM de Onboarding/Wallet/Adquirencia (afecta sus propios proyectos: AD-1434/PRD-216, PRD-66, PRD-113, etc.), no es el owner de la decisión — la lidera Matías Alzogaray (PM Fintexa) junto con el equipo de líderes técnicos.
