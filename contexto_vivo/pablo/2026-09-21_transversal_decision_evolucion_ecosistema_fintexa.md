---
id: 2026-09-21_transversal_decision_evolucion_ecosistema_fintexa
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_mails — mail 'Fw: Evolución del ecosistema' (threadId 1a0b4559895e3fc4), Agustín Grau (CTO Fintexa), 2026-09-16, forwardeado 2026-09-18"
producto: transversal
tema: Fintexa formaliza el modelo de producto único/repo único/release periódico único para todos los clientes del ecosistema, con retrocompatibilidad como prioridad
tipo: decision
destino_propuesto: 3_recursos/arquitectura_sistema/index.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Agustín Grau (CTO de Fintexa) comunicó formalmente — y lo acordó con Emma Vignoles — cómo Fintexa va a encarar la incorporación de nuevos clientes al ecosistema que hoy usa BIND PSP (cada nuevo cliente trae productos/módulos nuevos, ajustes sobre lo existente e integraciones con terceros, ej. conexión con Payway por ISO para e-commerce):

- **Decisión de fondo:** sostener **un único producto, un único repositorio y un release periódico único**, instalado en distintos ambientes según el cliente (no forks ni ramas separadas por cliente).
- Fintexa comunica todo lo que vaya desarrollando, aun cuando no impacte directamente en la operación de BIND PSP.
- Todo lo nuevo se diseña de forma **modular, separable por producto y por feature**, para poder habilitarse o no por cliente.
- **La retrocompatibilidad es prioridad explícita:** lo que hoy funciona en BIND PSP tiene que seguir funcionando igual.
- **BIND PSP no prueba, en una primera instancia, los productos/features nuevos que no usa** — sí corre una regresión sobre su propio alcance para validar que nada se vio afectado por el cambio.
- Si más adelante BIND PSP (u otro cliente) necesita activar un producto/feature ya existente para otro cliente, se conversa en ese momento y se define cómo proceder — no hay activación automática.

Esta decisión encuadra formalmente por qué el ecosistema (Ardid/Akurtech, Wallet, Adquirencia sobre la misma base) evoluciona con roadmaps de release que incluyen features no usadas por Bind (ver por ejemplo el roadmap de Akurtech 1.19/1.19.1/1.20 en `2026-09-21_ardid_conocimiento_akurtech_release_119_roadmap`) — es la política general detrás de ese patrón, no un caso aislado.

> Fuente: mail "Fw: Evolución del ecosistema" (Pablo Serra reenviando el original de Agustín Grau, threadId `1a0b4559895e3fc4`), mensaje original 2026-09-16, reenviado y leído 2026-09-18.
