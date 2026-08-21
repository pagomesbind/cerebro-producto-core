---
id: 2026-08-20_adquirencia_bines_payway_decidir
pm: pablo
fecha_captura: 2026-08-20
fuente: "/sync_mails — hilo 'Análisis BINES Payway/Decidir' (threadId 19e45906aa2152c4), Agustín Grau (CTO Fintexa), mensaje del 2026-08-19"
producto: adquirencia
tema: Desalineación entre la base de BINES de Payway y lo que responde Decidir al rechazar — investigación en curso
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/pos_multiadquirencia.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

Investigación técnica abierta de Fintexa (Agustín Grau, CTO) sobre rechazos de transacciones con tarjeta relacionados a la identificación de BINES, cruzando tres fuentes: la configuración/identificación de BINES propia de Bind PSP, la base de datos de BINES de Payway (provista por Gonzalo Rivera) y lo que responde Decidir cuando rechaza una transacción.

**Hallazgo confirmado (primer análisis, mensaje original 2026-05-20, sobre una muestra de transacciones de un día):** no se puede concluir que los rechazos se expliquen por las diferencias entre bases — existen transacciones con los mismos atributos que sí están aprobadas. Hay que ajustar la base de BINES propia, pero no está claro **qué** cambiar: lo que dice Decidir no coincide con la BD de BINES de Payway, y además hay BINES obtenidos de Global Processing (GP) que sí coinciden con los de Payway. El caso está vinculado al ticket de soporte Fintexa `AD-681` (mencionado por Gonzalo Rivera, 2026-06-12).

**Novedad de este barrido (mensaje del 2026-08-19):** Agustín Grau corrió un segundo análisis, esta vez sobre una muestra completa de aprobadas y rechazadas del log de comunicación con Decidir del día 18/08 completo (no ya una muestra parcial). Conclusión de este segundo análisis: **hay acciones concretas que se pueden tomar ya y que darían mejoras instantáneas** — Grau ofrece reunión para definirlas. El hilo se amplió sumando a Mariana Nadalin, Gustavo Álvarez y Adriana Endzeliz del lado Bind PSP.

**Estado:** sin cierre — pendiente que alguien de Bind PSP (Gonzalo Rivera es el interlocutor natural, Pablo Gomes está en copia) acepte la reunión propuesta por Fintexa para definir e implementar las acciones de mejora identificadas. El informe interactivo (adjunto HTML, no legible desde el mail) no se pudo abrir desde este flujo — si el detalle de "qué BINES corregir" importa para el merge, hay que pedirlo aparte.
