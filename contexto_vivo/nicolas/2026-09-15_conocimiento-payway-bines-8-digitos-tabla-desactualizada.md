---
id: 2026-09-15_conocimiento-payway-bines-8-digitos-tabla-desactualizada
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Reuniones 'Weekly - Producto / Operaciones' (2026-09-14) y 'Análisis COBRO' (2026-09-14), con antecedente en 'Producto' (2026-09-14)"
producto: adquirencia
tema: Tabla de BINs de tarjeta desactualizada (Bind toma 6 dígitos, Payway usa 8) — causa rechazos y mala clasificación crédito/prepaga
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/validacion_bines_tarjetas.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
---

**Hallazgo (Mariana Nadalin / Gonzalo Damian Rivera, reunión "Weekly - Producto / Operaciones", 2026-09-14):** Bind PSP identifica el BIN de una tarjeta tomando los primeros **6 dígitos**, mientras que Payway usa **8 dígitos** para el mismo campo. Consecuencia concreta: tarjetas prepagas quedan mal clasificadas como tarjetas de crédito (y viceversa) porque el 7º/8º dígito es justamente el que distingue el tipo (ej. BIN `454622`: Bind lo tiene cargado como prepaga, pero en el archivo de Payway aparece 4 veces con distintos 7º-8º dígitos — 3 como crédito, 1 como prepaga real). Esto genera **rechazos operativos en producción hoy**: *"a nivel operativo estamos fallando, no estamos cobrando un montón de tarjetas por error de no tener la tabla de bines actualizada"* (Gonzalo Damian Rivera).

**Antigüedad del problema:** la tabla de BINs de Bind no se actualiza, según estimación de Gonzalo Damian Rivera, desde que se creó (~3-4 años atrás) — Payway deja un archivo actualizado todos los lunes en un portal propio, pero Bind nunca automatizó ni programó su descarga/carga.

**Decisiones tomadas en la reunión:**
- **Prioridad 1 (acordada):** actualización **manual** de la tabla de BINs con el archivo que provee Payway — Pablo Gomes toma la tarea de revisar el acceso al portal de Payway y evaluar la carga inmediata del archivo más actualizado que le pasen Gonzalo Damian Rivera / Mariana Nadalin.
- **Prioridad 2 (diferida):** automatizar la descarga/actualización semanal del archivo (hoy manual, "una fiaca" según Mariana Nadalin, peroviable como hábito semanal mientras no se automatice).
- **Requiere más debate (sin cerrar, se aplaza con Pablo Gomes):** si conviene además cambiar la lógica de evaluación de BIN de 6 a 8 dígitos en el motor de pagos — impacto no evaluado todavía (afecta procesos de validación en Payway y potencialmente en la lógica propia de determinar bines nuevos/soportados). Mismo tema aplazado también en la reunión "Análisis COBRO" (2026-09-14) por ausencia de Pablo Gomes, y consultado de nuevo por Nicolás Colón en la reunión "Producto" (2026-09-14) sin resolución ("no se toma una decisión final").

**Nota de alcance:** el mismo BIN 6 dígitos también es relevante para el proyecto `titularidad_tarjeta` (consulta a MODO usa BIN + últimos 4 + DNI) — la ambigüedad de 6 vs. 8 dígitos podría afectar la implementación de esa validación también, a confirmar cuando se cierre esta definición.
