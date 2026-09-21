---
id: 2026-09-16_adquirencia_pnet_mejoras_performance_distribucion_pedidos
pm: pablo
fecha_captura: 2026-09-16
fuente: "Email minuta Facundo Collerone (11/09) + follow-up Pablo (16/09)"
producto: adquirencia
tema: performance, escalabilidad, pedidos masivos PNET
tipo: iniciativa
destino_propuesto: wiki/2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: pendiente
proyecto: PRD-66
---

# Mejoras de Performance Provincia NET <> BIND (PNET)

**Reunión bilateral:** 10/09/2026  
**Minuta formal:** 11/09/2026 (Facundo Nicolas Collerone, Gerencia Pagos Digitales PNET)  
**Actualización implementación:** 16/09/2026 (Pablo Gomes)

## Problema identificado

PNET reporta picos de demora en procesamiento de pedidos, especialmente en lotes masivos. Necesidad de:
- Distribuir pedidos para evitar concentración de picos
- Mejorar capacidad de BIND para absorber y procesar en paralelo
- Evaluar alternativa SFTP para casos específicos

## Compromisos BIND (ejecutados al 16/09)

✅ **Mejoras de infraestructura implementadas:**
1. Subir límite en cola `Deuda + QR`
2. Duplicar cantidad de pods Workers
3. Escalar recursos de Base de Datos (acorde al escalamiento horizontal de pods)

**Status:** Sistema mostrando mejor performance tras cambios.

📋 **Pendiente (en evaluación):**
- Alternativas para escalar uso de SFTP (paralelismo + menores tiempos para lotes chicos)
- Una vez disponible, PNET podría adoptarlo para todos sus casos de uso

## Compromisos PNET (en curso)

- Revisar distribución de pedidos para evitar picos innecesarios
- Ajustar lógica de reintentos cuando detecte demoras
- Medir tráfico y performance post-ajustes

## Plan de medición

Una vez aplicados los ajustes bilaterales, **medir comportamiento y validar cuánto mejora la operación** antes de escalar a otros volúmenes/clientes.

## Participantes

**BIND:** Pablo Gomes, Alan Martinez, Hernan Clarich, Mariana Nadalin  
**PNET:** Facundo Nicolas Collerone, Ricardo Andres Lavia, Federico Nicolas Acuña

---

**Próximos pasos:** 
- Completar evaluación de alternativas SFTP (BIND, Pablo owner)
- Medir impacto de mejoras implementadas (conjunta, ~10 días)
- Reportar calibración a direccion si hay cambio de capacidad o SLA

**Categoría:** Mejora operativa bilingual, de duración media (~30 días de seguimiento)
