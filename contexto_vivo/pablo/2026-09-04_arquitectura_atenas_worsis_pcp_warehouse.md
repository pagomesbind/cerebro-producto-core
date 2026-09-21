---
id: 2026-09-04_arquitectura_atenas_worsis_pcp_warehouse
pm: pablo
fecha_captura: 2026-09-04
fuente: "Reunión Relevamiento WH PSP (2026-09-04 09:30), minuta y transcripción Gemini"
producto: transversal
tema: arquitectura Atenas (núcleo alertas) + Worsis (monitoreo SAS) para historificación de datos PCP con Banco Industrial
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/integraciones_alertas_cumplimiento.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
---

# Arquitectura Atenas + Worsis — integración datos históricos PCP

## Contexto: Relevamiento WH PSP con Banco Industrial (2026-09-04)
Banco Industrial requiere acceso a datos históricos de transacciones de Bind PSP (mínimo 1 año de auditoría) para alertas de cumplimiento (PLD/ROS). La solución involucra dos sistemas interconectados:

## Arquitectura propuesta

### **Atenas** — Núcleo de alertas
- Sistema interno en premisas de Banco Industrial
- Recibe datos históricos de Bind PSP vía consultas SQL
- Procesa alertas mensualmente (no real-time)
- Conecta con Worsis (sistema de monitoreo del banco en SAS)
- No almacena transacciones (restricción del banco por volumen)

### **Worsis** — Sistema de monitoreo SAS
- Sistema del banco (SAS)
- Acumula alertas por cliente a través de múltiples entidades
- Genera reportes consolidados

### **PCP** — Dos verticales de negocio
1. **Comercios:** QR, botones de pago
2. **Wallet:** Bind proporciona tecnología CVU corta a entidades (Cencosud, Carrefour, BCF, Astropay)
   - Un cliente final puede tener presencia en múltiples entidades dentro del mismo PCP
   - Ejemplo: cliente "Juliana" aparece en Carrefour, Astropay, Sencos → una sola alerta consolidada

## Integración técnica

### **Acceso a datos históricos:**
- Consultas SQL desde Atenas hacia nodo de historificación de Bind PSP
- Frecuencia de historificación: A confirmar con DBA (pendiente)
- Rango: 1 año mínimo para auditoría

### **Conectividad:**
- VPN existente limitada a APIBank → **refinar VPN** para habilitar tráfico a nodo SQL histórico
- Credencial de backend para Atenas (suministrar desde Bind PSP)
- Entornos: Desa/CUA/Producción (banco) conectado a Staging/Producción (Bind PSP)

### **No requiere ETL:**
- Queries ejecutadas **directamente desde Atenas** sobre warehouse de Bind PSP
- Atenas es proveedor de datos a Worsis, no transformador

## Próximos pasos
[Hernan Clarich] Consultar DBA: frecuencia de historificación actual  
[Hernan Clarich] Coordinar con Seginf: refinar VPN existente + proveer credenciales backend para Atenas  
[Alfredo Rey/AiCore] Enviar especificación técnica de datos requeridos  
[Giuliana Batista] Compartir queries SQL actuales y ejemplos Excel de mapeo de datos (wallet + comercios)  
[María Victoria Simonetti] Coordinar reunión separada con Worsis para conexión de alertas PCP  

> Fuente: Reunión "Relevamiento WH PSP" (2026-09-04 09:30), minuta y transcripción Gemini
