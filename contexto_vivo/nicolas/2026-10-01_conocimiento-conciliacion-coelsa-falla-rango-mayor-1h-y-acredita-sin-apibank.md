---
id: 2026-10-01_conocimiento-conciliacion-coelsa-falla-rango-mayor-1h-y-acredita-sin-apibank
pm: nicolas
fecha_captura: 2026-10-01
fuente: "Charla directa con el PM (Nicolás Colón) durante el discovery /idea_start de PRD-240 (conciliacion_entrantes), 2026-09-29 / 2026-10-01"
producto: wallet
tema: Conciliación de entrantes contra Coelsa — la falla de septiembre era por rangos mayores a 1 hora (no herramienta rota), acredita aunque ApiBank esté caído, y cómo se detectan hoy los faltantes
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/conciliacion_y_totalizadores.md
tipo_destino: actualizar
contradice: "2_areas/riesgos.md, riesgo 'Herramienta de conciliación de transferencias entrantes rota — agravado por el despliegue del 17/09' (dice que la herramienta está rota y que la conciliación depende de insertar a mano); y conciliacion_y_totalizadores.md §5 / WS-413 (documenta una amplitud máxima de rango de 24 hs)"
confianza: alta
estado: en_cola
---

Tres precisiones sobre el proceso de conciliación de transferencias entrantes contra Coelsa (`POST /Operaciones/ConciliacionCoelsa`, ver `conciliacion_y_totalizadores.md` §5), confirmadas por el PM dueño del tema:

1. **La herramienta funciona; la falla de septiembre 2026 era por amplitud del rango.** El problema reportado por Maria Eugenia Vila (2026-09-10/11) y registrado en `2_areas/riesgos.md` como "herramienta rota" era que el proceso **fallaba cuando el rango de fechas era más amplio que 1 hora**. Con rangos de hasta 1 hora funciona "bien" (palabras del PM, 2026-10-01). Esto **matiza el riesgo** de `2_areas/riesgos.md` (no es una herramienta inoperativa, es una limitación práctica de rango) y **tensiona** lo documentado en §5 (WS-413): la amplitud máxima admitida es 24 hs, pero en la práctica rangos > 1 h fallaban. No se sabe si la falla se corrigió en una versión posterior ni si aplica solo sin `cvuDestino` — pregunta abierta para el merge / Ingeniería.

2. **La conciliación directa contra Coelsa registra la operación y acredita el saldo aunque ApiBank esté caído.** El criterio del PM: *"COELSA siempre tiene la posta. Si el banco no la tiene es problema de ellos."* — es decir, Coelsa es la fuente de verdad de las transferencias entrantes; si Coelsa la acreditó, Bind PSP la registra y acredita en Wallet aunque la API del banco (ApiBank) no la tenga.

3. **Cómo se detectan hoy los faltantes.** Las transferencias entrantes que Coelsa acreditó y Bind no registró se descubren **sobre la marcha, por queja de los clientes**, o recién en la **conciliación del día posterior contra el banco**, que a veces también las inserta. No hay detección proactiva intradiaria. El caso de uso principal que motiva automatizarlo son las caídas de ApiBank (estimadas por el PM en ~1 por mes, sin dato duro), en especial fuera de horario, cuando no hay nadie de Soporte disponible.

> Contexto: discovery del proyecto `conciliacion_entrantes` (IDEA PRD-240, "Automatizar conciliación entrantes contra Coelsa cada 1 hora de todas organizaciones").
