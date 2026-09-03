---
id: 2026-09-02_onboarding_oportunidad_exponer_motivo_rechazo_totalizadores
pm: pablo
fecha_captura: 2026-09-02
fuente: "ingesta directa de Jira a pedido del PM (cierre/go-live PRD-200) — hallazgo documentado en WS-1486 (pruebas de QA), 2026-08-13"
producto: onboarding
tema: transparencia de errores en altas de cuenta rechazadas por validación de totalizadores
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 57c0e9b
---

## Señal de demanda

Detectada por QA durante las pruebas de cierre de **PRD-200** (validación de totalizadores CBU/CVU), no por un pedido externo de cliente. Al probar una alta de cuenta vía **Onboarding** (BFF `orquestador/api/v1/onboarding-cuenta-comitente`) que debía rechazarse por superar el límite de totalizadores, se confirmó que Onboarding sí ejecuta la misma validación que Wallet (mismo `eventId` de dominio, 1273 en el caso probado) — pero **no expone el motivo del rechazo a quien llama**. La respuesta pública solo devuelve `cuenta`/`cuentaCvu`/`cuentaInvestment` en `null`, sin ningún código ni detalle. Para conocer la causa real hay que ir a la herramienta interna "Respuestas Servicios" (pestaña específica del flujo) o consultar `dbo.Solicitud` directamente — algo que un integrador externo (organización u onboarding de un cliente) no puede hacer.

## Por qué importa

Cualquier organización que dé altas de cuenta a través de Onboarding y sea rechazada por totalizadores (o, potencialmente, por cualquier otra validación interna del mismo motor) recibe una respuesta sin causa aparente — no sabe si fallar reintentar, corregir un dato, o escalar a soporte. Golpea la experiencia de integración y genera tickets de soporte evitables ("¿por qué no se creó la cuenta?").

## Foco estratégico que alimentaría

Onboarding / calidad de integración — relacionado directamente con **PRD-118** (la versión definitiva de esta misma validación de totalizadores, integrada a Onboarding) y, más en general, con cualquier mejora a la trazabilidad de errores que expone el BFF de Onboarding a organizaciones integradas.

## Estado

Nueva — sin IDEA de Jira todavía. Candidata a sumarse al alcance de PRD-118 cuando ese proyecto arranque, o a resolverse como mejora puntual e independiente si PRD-118 sigue demorado.
