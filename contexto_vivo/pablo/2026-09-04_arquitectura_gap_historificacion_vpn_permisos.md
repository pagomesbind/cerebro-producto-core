---
id: 2026-09-04_arquitectura_gap_historificacion_vpn_permisos
pm: pablo
fecha_captura: 2026-09-04
fuente: "Reunión Relevamiento WH PSP (2026-09-04 09:30), minuta y transcripción Gemini"
producto: transversal
tema: frecuencia de historificación SQL sin definir + configuración VPN/permisos Seginf pendiente para integración Atenas
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: pendiente
---

# Gap: Historificación SQL y configuración de acceso VPN

## Problema detectado (2026-09-04)
Durante el relevamiento con Banco Industrial para acceso a datos históricos de PCP:

### **Gap 1: Frecuencia de historificación**
Banco Industrial necesita datos históricos con profundidad de ~1 año para auditoría. Actualmente se desconoce:
- **¿Cada cuánto se actualiza el nodo SQL histórico de Bind PSP?** (diario, semanal, mensual)
- **¿Se pueden acomodar los rangos según requerimientos de Atenas?** (alerts mensuales, pero queremos histórico viejo)

**Impacto:** Define factibilidad de resolver queries mensualmente vs. real-time

### **Gap 2: Configuración VPN y permisos Seginf**
Se dispone de VPN existente (limitada a APIBank). Se necesita:
- Refinar esa VPN para habilitar tráfico al nodo SQL de historificación
- Cargar permisos en Seginf del banco + Bind PSP
- Provisión de credenciales de backend para Atenas

**Complejidad:** Ambos lados deben coordinar (Banco Industrial Seginf + Bind PSP Seginf)

## Contexto
- **Reunión:** Relevamiento WH PSP, 2026-09-04
- **Stakeholders:** Banco Industrial (María Victoria Simonetti, Alfredo Rey, DBA), Bind PSP (Hernan Clarich, Gonzalo RIVERA, Giuliana Batista)
- **Sistema:** Atenas (alertas) requiere acceso a warehouse de Bind PSP

## Próximos pasos
[Hernan Clarich] Consultar **DBA de Bind PSP:** frecuencia actual de historificación al nodo SQL  
[Hernan Clarich] Coordinar con **Seginf Bind PSP + Seginf Banco Industrial:** refinamiento VPN, credenciales, permisos  
[Todas las partes] Validar que el ajuste de VPN y permisos no afecte otras integraciones (APIBank, etc.)

> Fuente: Reunión "Relevamiento WH PSP" (2026-09-04 09:30), minuta y transcripción Gemini
