---
id: 2026-09-03_arquitectura_coe_informe_agosto
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_mails — mail 'RE: INFORME Mensual Comité de Arquitectura COE', Alejandro Sfrede (Fintexa), threadId 19fdd426c2490389, mensaje 2026-09-02 (resumen de agosto 2026)"
producto: transversal
tema: Comité de Arquitectura COE — estado consolidado agosto 2026 (avance respecto del informe de julio ya conocido)
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/relacion_con_fintexa.md
tipo_destino: actualizar
contradice: "3_recursos/arquitectura_sistema/relacion_con_fintexa.md — estado del Comité de Arquitectura COE probablemente todavía refleja el corte de julio 2026 (ítems 'en progreso'/'en diseño'), este item trae el corte de agosto con varios ítems que avanzaron de categoría"
confianza: alta
estado: ingestado
merge_commit:
---

**Fuente:** mail "RE: INFORME Mensual Comité de Arquitectura COE", Alejandro Sfrede (Fintexa), 2026-09-02, a Emma Vignoles con copia a varios técnicos de Fintexa y Pablo Gomes. Adjunto PDF "COE-TAREAS-30DIAS-SEP2026.pdf" (no descargado). Continúa el mismo thread cuyo informe de julio (2026-08-07) ya está reflejado en `relacion_con_fintexa.md`.

**Delta agosto 2026 vs. julio 2026 (mismo formato de categorías del proveedor):**

- ✅ **Listo / en producción** (antes "Listo / Disponible a Verticales"): **Autenticación externa (Wallet y Aceptador) — migración productiva COMPLETA** (en julio decía "resta 1 fase"). **Procedimiento de corrección rápida (HOTFIX)** pasa de "listo" a "operativo, con prueba real de punta a punta programada para cerrar la validación". Feature flags siguen disponibles. Ya no se menciona "Notificaciones estabilizadas en Wallet" ni "Api buffer" como ítems propios en el resumen de agosto (posible consolidación del texto, no necesariamente reversión).
- 🟢 **En progreso:** **Zero-Downtime — roadmap ampliado a 40+ servicios de Wallet** (en julio no tenía alcance cuantificado). **Red de seguridad de mensajería** — pasa a "ya en ambiente de prueba productivo, validación final" (antes solo "en progreso" sin detalle). Nuevo ítem: **"Cierre del componente anterior de autenticación"**. **Onboarding unificado** — sube de categoría: estaba en julio "🔵 En diseño o definición" y en agosto ya tiene "base en ambiente de prueba" (dato relevante para el foco de Onboarding de Pablo Gomes — no hay un PRD propio de Pablo que dependa de esto todavía, pero es la misma iniciativa que se menciona en otros hilos de arquitectura). Resto de ítems en progreso repetidos sin cambio aparente (depuración/retención de datos, protección de datos en registros, control de salidas de red, monitoreo de salud, modernización .NET 10, colas Quorum, programa de eficiencia/gobierno IA, políticas de workers).

**Nota:** el mail no llegó a copiar el texto completo de las categorías 🔵 En diseño/definición, ⚪ Backlog y 🔴 Bloqueado del corte de agosto (el cuerpo plano se cortó antes de esas secciones) — el detalle completo está solo en el PDF adjunto, no descargado por esta skill. El merge debería tratar este item como una actualización parcial (solo las categorías ✅ y 🟢 confirmadas) y no asumir que 🔵/⚪/🔴 no cambiaron.
