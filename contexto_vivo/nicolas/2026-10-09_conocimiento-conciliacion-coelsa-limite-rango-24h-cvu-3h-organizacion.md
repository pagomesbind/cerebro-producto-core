---
id: 2026-10-09_conocimiento-conciliacion-coelsa-limite-rango-24h-cvu-3h-organizacion
pm: nicolas
fecha_captura: 2026-10-09
fuente: "Charla directa con el PM (Nicolás Colón) durante el discovery /idea_start de PRD-240 (conciliacion_entrantes), 2026-10-09"
producto: wallet
tema: Conciliación Coelsa — el máximo de 24 hs aplica solo conciliando una CVU; para toda la organización el límite funcional es 3 hs (resuelve la tensión capturada el 2026-10-01)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/conciliacion_y_totalizadores.md
tipo_destino: actualizar
contradice: "Resuelve la '⚠️ Tensión sin resolver con la amplitud documentada (2026-10-01)' de conciliacion_y_totalizadores.md §5 y el gap [2026-10-01] asociado en 2_areas/gaps_y_preguntas.md"
confianza: alta
estado: en_cola
---

Actualiza lo mergeado desde el item `2026-10-01_conocimiento-conciliacion-coelsa-falla-rango-mayor-1h-y-acredita-sin-apibank` (ya ingerido y archivado), que dejó en `conciliacion_y_totalizadores.md` §5 una tensión sin resolver entre el máximo documentado de 24 hs (WS-413) y la falla práctica con rangos de más de 1 hora.

**Aclaración del PM (2026-10-09):** los dos límites aplican a modos distintos del proceso `POST /Operaciones/ConciliacionCoelsa`:

- **Conciliando una sola CVU** (`cvuDestino` informado): el rango admite **hasta 24 hs** — es lo que documenta WS-413 y sigue vigente.
- **Conciliando toda la organización** (sin `cvuDestino`): el **límite funcional es de 3 hs**. Pedir rangos más amplios para toda la organización es lo que hacía fallar el proceso en septiembre 2026 (la falla que Soporte había reportado como "herramienta rota").

Consecuencia práctica: cualquier corrida periódica sobre toda una organización tiene que usar ventanas de 3 hs como máximo. El "funciona bien hasta 1 hora" capturado el 2026-10-01 es consistente con esto: una ventana de 1 hora queda holgadamente dentro del límite.

Propuesta para el merge: reemplazar el bloque "⚠️ Tensión sin resolver..." de §5 por esta distinción, y cerrar el gap [2026-10-01] de `2_areas/gaps_y_preguntas.md` como resuelto.

> Contexto: discovery del proyecto `conciliacion_entrantes` (IDEA PRD-240).
