---
id: 2026-08-19_portal_comercio_portal2-rollout
pm: pablo
fecha_captura: 2026-08-19
fuente: "/sync_meetings — reunión 'Portal 2.0' (docId 10t8JAUmY-r2O_RLYi_GjNl4GI5x9lOjejgl7gJwVT1E), 2026-08-19 14:01, minuta Gemini (compartida, owner malzogaray@bind.com.ar, Fintexa)"
producto: portal_comercio
tema: Estado técnico del Portal 2.0 y estrategia de lanzamiento gradual (piloto por entidad)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/portal_comercio/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 5f0974a
---

**Contexto:** el Portal 2.0 (nueva versión del portal de comercios, migrado a una versión más reciente de Next.js) había completado pruebas hace tiempo pero quedó frenado. Reunión de retomada entre Bind (Matías Alzogaray, Andrea Orsini, Gonzalo Rivera, Pablo Gomes) y el proveedor Fintexa (Emiliano Santi, Agustín Grau, Mariela Marin, Melisa Belpassi).

**Estado técnico encontrado:**
- Tras la actualización de Next.js, Emiliano Santi (Fintexa) detectó que el portal no mostraba correctamente los mensajes de error esperados: cuando un usuario sin permiso intenta una acción no autorizada, la validación y el bloqueo funcionan bien (no se le permite hacer lo que no debe), pero el mensaje que se le muestra está mal mapeado. Mismo problema al acceder a una página inexistente (debería dar un 404 informativo).
- Durante una demo reciente a Coca-Cola (Andina) se encontraron detalles menores adicionales: una fecha con formato erróneo y un filtro que no funcionaba.
- Estos hallazgos están trackeados en el tablero de Fintexa/Querencia, pero al momento de la reunión **todavía no estaban desplegados en ambiente de staging**.
- Agustín Grau (Fintexa) planteó una mejora de UX de soporte transversal: hoy los mensajes de error silenciosos obligan al usuario a mandar una captura de pantalla sin contexto (sin trace ID, sin hora, sin saber qué página/botón); pidió que el sistema entregue siempre un mensaje claro, un trace ID o una redirección adecuada en vez de fallar en silencio, para poder dar soporte con trazabilidad real.

**Decisión (acordada en la reunión):** en lugar de esperar a resolver todos los detalles menores antes de avanzar, se aprobó un **despliegue controlado/piloto**: habilitar el Portal 2.0 primero para 1-2 entidades específicas (sin impacto en el resto), evaluando ahí las mejoras de UX antes de una migración masiva. Gonzalo Rivera fue explícito en que, al no haber ningún cliente operando hoy en Portal 2.0, el pasaje es flexible en fecha/horario mientras no haya clientes habilitados — una vez habilitado el primero, sí requerirá ventana controlada fuera de horario transaccional.

**Logística de la transición (confirmada por Emiliano Santi):** la migración de Portal 1.0 a 2.0 es transparente para el usuario final — mismas credenciales, mismas URLs, y las rutas viejas redirigen automáticamente a las nuevas (Emiliano tiene el mapeo completo ruta vieja → ruta nueva). El rollback a Portal 1.0 es técnicamente posible.

**Próximos pasos acordados:**
- Andrea Orsini se reúne en privado con Emiliano Santi para repasar en detalle los errores pendientes y confirmar fecha de salida (apuntando a un piloto lunes a la mañana).
- Gonzalo Rivera gestiona un ticket a Infraestructura para tener lista la migración de la primera entidad piloto a primera hora de un lunes.
- Emiliano Santi entrega a Andrea el listado de transformación de rutas antiguas → nuevas.
- Matías Alzogaray distribuye el resumen de la reunión a todos los asistentes.
