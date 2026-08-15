# Plan de Mantenimiento AKS (Agosto 2026) — Reversión Post-Incidente + Optimización

> Reubicado desde `arquitectura_sistema/index.md §12` en la reestructuración PARA en cascada (2026-08-12). Fuente: Mail "Ajuste AKS Bind PSP" — daniel.zalazar@fintexa.tech (Infrastructure Leader, Fintexa), 2026-08-06.

Fintexa (SRE) propuso un plan de mantenimiento sobre la infraestructura de procesamiento del tenant Bind PSP, en 2 bloques, todavía pendiente de conformidad/aprobación de Bind PSP a la fecha del barrido original.

- **Contexto:** a raíz del incidente de julio vinculado a los balanceadores de carga (ver `detalle_productos/wallet/otros_manuales.md §7.2` para el diagnóstico de esas caídas), se habían escalado preventivamente varios recursos de procesamiento por encima de lo habitual. Con la situación normalizada, el plan busca devolverlos a su configuración previa y aplicar mejoras.
- **Bloque 1 — reducción de costos (riesgo bajo, sin corte de servicio):** pods del webhook sender de 32→16; nodos de procesamiento de 46→28; VM scale set de 18→9.
- **Bloque 2 — optimización de plataforma:** actualización de AKS (sin corte, con logs de Ingress como contingencia); reconfiguración del balanceador de carga externo (timeout de conexión inactiva de 30 min→4 min) — **única tarea con corte de servicio previsto, ~30 min, en ventana de bajo tráfico a coordinar**; distribución más uniforme de pods egress/webhooksender entre nodos.
- **Cronograma tentativo:** Bloque 1 la semana del 2026-08-10; Bloque 2 sin fecha confirmada, sujeto a aprobación de la ventana de mantenimiento.
- **Ticket de seguimiento (2026-08-07):** Fintexa cargó `INF-1516` (fintexa.atlassian.net) para la desescalada de AKS de la semana del 2026-08-10. Hernán Clarich (Bind) pidió puntualizar qué monitorear durante el cambio y si hace falta soporte del equipo de Pablo Serra (Fintexa) o de QA PSP.
- **Ejecución del Bloque 1 (2026-08-10/11):** plan de acción confirmado por Fintexa — martes 11/08 7:30-8:00hs, desescalado de pods sin reinicio de servicio (WebHookSender Wallet 32→16, Walletbind 20→15, Walletoperaciones 24→12); miércoles 12/08 7:30-9:00hs, desescalado de nodos (2 nodepools de 18→10 nodos cada uno, drenado gradual sin afectar todos los nodos a la vez; el nodepool de Rabbit —9 nodos— no se toca). Complementariamente se aplicará anti-affinity a los pods de comprobante/egress/webhooksender aceptador en cada despliegue futuro. **Confirmado 2026-08-11:** el desescalado de pods del martes se ejecutó según lo planeado, sin afectación de servicios; continúa el desescalado de nodos el miércoles.
- **Bloque 1 completado (2026-08-12/13):** el desescalado de nodos se ejecutó en 2 días (uno por nodepool) en vez de uno solo, por conflicto de agenda con otros despliegues — 12/08 un nodepool bajó de 18 a 10 nodos, monitoreado sin degradación; 13/08 se completó el segundo nodepool en las mismas proporciones, también sin afectación (Hernán Clarich confirmó: sin cambios en tasa de error ni en tiempo de respuesta). **Bloque 1 cerrado.** Bloque 2 (actualización de AKS + reconfiguración del balanceador, única tarea con corte de servicio) sigue sin fecha confirmada.
- **Nota operativa (2026-08-12):** la prueba de parametrización del Egress en STG (ver [`incidentes_de_plataforma.md` §7](incidentes_de_plataforma.md)) se suspendió el mismo día por falta de capacidad del equipo de SRE, que tenía en paralelo un despliegue de Aceptador y el desescalado de nodos — reagendada sin fecha nueva.

## Ver también
- [relacion_con_fintexa.md](relacion_con_fintexa.md) — dotación de recursos y gobierno de arquitectura del mismo proveedor.
- [infraestructura_cloud_azure.md](infraestructura_cloud_azure.md) — cluster AKS afectado por este plan.

---
*Última actualización: 2026-08-14 — `/sync_mails`: Bloque 1 (desescalado de nodos) completado 12-13/08 sin degradación de servicio; nota sobre suspensión de la prueba de Egress en STG por conflicto de capacidad.*
*Última actualización anterior: 2026-08-12 — Reubicado desde `arquitectura_sistema/index.md §12` (reestructuración PARA en cascada). Contenido sin cambios.*
