---
id: 2026-09-03_wallet_reintento_alias_demora_coelsa
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_meetings — reunión 'Analisis de Riesgo - Emisión V 72.2' 2026-09-02 16:01 (docId 1IIQISfL0wNcXfMPvRhZtQmdGViaCcZzj9_z9P7wj62g), minuta Gemini"
producto: wallet
tema: Mecanismo de reintento automático en la asignación de alias de cuentas nuevas, por demora de Coelsa en registrar el CBU
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/validaciones_y_alias_cvu.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Mecánica confirmada (tickets WS-1556 / DEM-1828, parte del lote de despliegue V72.2):**

Cuando se crea una CBU nueva y Wallet intenta asignarle un alias automáticamente, Coelsa puede tener un delay en registrar esa CBU en (según Juan Pablo Carubelli, Fintexa) "una parte de su sistema" — mientras ese delay no se resuelve, el intento de asignación de alias devuelve un error de "CBU no existe", y la cuenta queda con **alias nulo/bloqueado**.

**Fix:** se incorpora un mecanismo de **reintento automático con espera fija corta** para la asignación de alias en cuentas nuevas — cubre tanto el flujo automático de creación de CBU como el endpoint de asignación directa de alias (mismo motivo de fondo en ambos casos). Semáforo asignado: amarillo (con seguimiento post-implementación).

**Seguimiento post-deploy acordado:** Gonzalo Rivera controla que disminuya la cantidad de altas de CBU corta que quedan con alias nulo tras la implementación — hoy es un problema activo ("nos quedan un montón de CBU corta con el alias nulo", cita textual de la reunión) que además genera reclamos de clientes.

**Contexto de despliegue:** el lote completo V72.2 (que incluye este fix + regularización de cuenta corriente/movimientos WS-1554 + conciliación de cash out WS-1552) se reprogramó del jueves 2026-09-03 al lunes 2026-09-07 8:00hs, por falta de tiempo de pruebas y por política de Fintexa de no desplegar los viernes.

**Relación con hallazgos previos del Cerebro:** este mecanismo de reintento es el mismo problema de fondo ya trackeado en `1_proyectos/asignacion_alias_cvu/` (PRD-224) y en la tarea T-032 de `tareas.md` — confirma que el fix ya avanzó a ticket de desarrollo concreto (WS-1556/DEM-1828) y está en camino de despliegue.

> Fuente: reunión "Analisis de Riesgo - Emisión V 72.2" (2026-09-02 16:01), minuta Gemini. Participantes: Matías Alzogaray, Gonzalo Rivera, Nicolás Colón, Andrea Orsini, María Eugenia Vila, Pablo Gomes, Mariana Nadalin, Juan Pablo Carubelli (Fintexa), Nico Pomponio (Fintexa), Pablo Serra (Fintexa).
