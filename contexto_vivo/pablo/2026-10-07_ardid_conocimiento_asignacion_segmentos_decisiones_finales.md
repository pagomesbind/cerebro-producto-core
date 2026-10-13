---
id: 2026-10-07_ardid_conocimiento_asignacion_segmentos_decisiones_finales
pm: pablo
fecha_captura: 2026-10-07
fuente: "/sync_mails — mail 'Re: Asignacion de segmentos al crear la cuenta.' (threadId 1a117024a775d326), Martín Hovanyecz (Keep IT Simple), 2026-10-07, cierre del análisis técnico WS-1743/WS-1742 (Nicolás Colón/Pablo Gomes en destinatarios)"
producto: ardid
tema: Decisiones finales del análisis técnico de asignación/cambio de segmentos de Ardid al crear la cuenta (WS-1742/WS-1743) — documento "listo para desarrollo"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/configuracion_inicial.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Cierre del ida y vuelta técnico entre Keep IT Simple (Martín Hovanyecz) y Nicolás Colón sobre dos historias de Ardid — [WS-1742](https://bindpsp.atlassian.net/browse/WS-1742) y [WS-1743](https://bindpsp.atlassian.net/browse/WS-1743) ("Asignación de segmentos al crear la cuenta" / "Cambio de segmento de una cuenta"). Martín entrega el documento final de decisiones y lo pasa a "listo para desarrollo"; Nicolás Colón confirma todas las definiciones. No es un proyecto trackeado en `1_proyectos/` de Pablo Gomes — Nicolás Colón es quien lo lleva; Pablo queda en copia/destinatario del cierre.

**Retrocompatibilidad de Organizaciones preexistentes:**
- Las Organizaciones ya creadas antes de esta funcionalidad son retrocompatibles sin acción automática — el reproceso del alta completa de segmentos para una Organización existente lo ejecuta manualmente el equipo de Integraciones y Soporte de BindPSP vía Swagger (no hay automatización ni UI para esto).
- Limitación técnica detectada por Nicolás Colón: el Calculador **no permite crear 2 Segmentos con el mismo Nombre**, pero Ardid **sí permite crear 2 Organizaciones con el mismo Nombre** — si eso ocurre, el alta de sus segmentos en el Calculador fallaría por choque de nombre. No es bloqueante porque no hay casos de negocio reales con 2 Organizaciones de nombre idéntico, pero es técnicamente posible.

**Contrato de respuesta de Ardid (comportamiento confirmado):**
- Crear un `BankType` duplicado es posible — Ardid no lo valida.
- Crear un `ClientBankType` duplicado con la misma información **no** es posible; Ardid responde `{"message": null, "messageEs": "El ClientBankType ya existe.", "messageEn": "The ClientBankType already exists.", "code": 2, "data": null}`.
- `personTypeId` **no es requerido** enviarlo a Ardid — confirmado tras chequeo explícito, se decide no enviarlo.
- **Nivel por defecto en Organizaciones existentes:** se confía inicialmente en el fallback (configuración default), para no "ensuciar" de especificaciones la tabla.
- **Nombre que se envía a Ardid para personas jurídicas:** no se modifica, queda como está hoy.

**Cambio de segmento de una cuenta (WS-1743) — los 3 puntos pendientes se resuelven todos por "la opción recomendada" (sin detalle adicional del contenido de esas opciones en este mail, remitir al documento HTML adjunto "FLUJO-FUNCIONAL-DEM-2189-DEM-2188-v2-20261007.html" para el detalle completo):**
1. Punto 1 — Falla a mitad de camino: se va por la opción recomendada.
2. Punto 2 — Wallet no actualiza su copia: se va por la opción recomendada.
3. Punto 3 — Desasignar un segmento: se va por la opción recomendada.

**Pendiente, no resuelto en este hilo:** el documento final (adjunto HTML) incluye una sección "Pendientes" con definiciones que Nicolás Colón ya respondió en este mismo correo (ver arriba), pero el adjunto en sí no fue leído por esta skill — si hace falta más detalle técnico de la implementación, está en el adjunto `FLUJO-FUNCIONAL-DEM-2189-DEM-2188-v2-20261007.html` del mail.

**Actualización 2026-10-08 — el cierre "listo para desarrollo" no fue definitivo:** Martín Hovanyecz escribió un nuevo mensaje en el mismo hilo (2026-10-08 21:21) indicando que, ya en desarrollo, "surgieron los siguientes puntos que debemos definir" — adjunta un nuevo HTML (`PUNTOS-A-DEFINIR-DEM-2189-20261008.html`, no leído por esta skill) con el detalle. De los puntos nuevos, Martín ya propone resolución para 2:
- **BIND-1 · H-26 (dónde se guardan los ids de la estructura de Ardid):** ya se había confirmado que se dejaba en `organizacionesArdid` — Martín confirma que sigue siendo la opción vigente (opción A).
- **BIND-2 · H-27 (menores de las Organizaciones que ya existen):** según lo charlado, se debería aceptar el riesgo, dejando en claro que los menores de organizaciones ya existentes deben resolverse a mano.
- El resto de los puntos nuevos queda sin resolver en este mensaje — pendiente de respuesta de Nicolás Colón.

Esto corrige el `tema` del frontmatter: la decisión de "listo para desarrollo" del 07/10 fue el cierre del análisis funcional, no de la implementación — en desarrollo siguieron surgiendo puntos a definir al día siguiente. No se detectó still una respuesta de Nicolás Colón a estos nuevos puntos al cierre de esta corrida (2026-10-09).

> Fuente: mail "Re: Asignacion de segmentos al crear la cuenta." (threadId `1a117024a775d326`), Martín Hovanyecz (Keep IT Simple) → Nicolás Colón / Pablo Gomes, 2026-10-07 y 2026-10-08.
