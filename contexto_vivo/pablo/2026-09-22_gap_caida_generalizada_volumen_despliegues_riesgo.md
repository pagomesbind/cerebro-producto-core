---
id: 2026-09-22_gap_caida_generalizada_volumen_despliegues_riesgo
pm: pablo
fecha_captura: 2026-09-22
fuente: "/sync_metrics — análisis semana 202638, cruzado con wiki/2_areas/direccion/decisiones.md"
producto: transversal
tema: Caída generalizada de volumen (NSM#1 y NSM#2) en la semana 202638, posible correlación con dos despliegues de riesgo en Producción
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: crear
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

**Severidad:** Alta

**Descripción:** En la semana 202638 (14 al 21 de septiembre de 2026) las dos North Star Metrics cayeron
fuerte y de forma pareja: NSM#1 (Volumen API BANK) −38,8% WoW y −24,3% contra el baseline de 13 semanas;
NSM#2 (Volumen Payway) −34,5% WoW y −11,1% contra baseline. La baja no está concentrada en un cliente o
producto puntual — se repite en casi todas las líneas de negocio de ambas métricas (Wallet, Agente de
Cobros, Botón Simple/2.0, todos los medios de pago de Payway). Cruzando con `direccion/decisiones.md`, en
la misma ventana se ejecutaron dos cambios de riesgo en Producción:
1. **[2026-09-15]** Actualización masiva en Producción de domicilios faltantes en cuentas Wallet (491.495
   registros).
2. **[2026-09-17]** Despliegue de W72.3 (Pagos FX) a producción, con riesgo explícito registrado en la
   decisión: *"exige seguimiento cerrado de la conciliación para no perder transacciones durante la
   ventana"* (conciliación de transferencias sin herramienta operativa).

No hay ninguna entrada en la wiki que confirme (ni descarte) que alguno de estos dos despliegues haya
afectado el volumen transaccional real. Es una correlación temporal plausible, no una causa confirmada.

**Pregunta para el usuario:** ¿Ingeniería/Fintexa puede confirmar si la actualización masiva de domicilios
del 15/9 o el despliegue de Pagos FX (W72.3) del 17/9 generaron fricción operativa, ventanas de
indisponibilidad, o pérdida/demora de transacciones durante la semana del 14 al 21 de septiembre? Si la
respuesta es sí, esto explicaría la caída generalizada sin necesidad de buscar una causa comercial. Si es
no, la caída queda sin explicación y amerita revisión propia la semana que viene (¿se sostiene en 202639 o
fue puntual?).

**Impacto mientras esté pendiente:** el reporte semanal de `/sync_metrics` va a seguir marcando esta caída
como hallazgo de severidad Alta hasta que se confirme o descarte la causa operativa.

**Estado:** Pendiente
