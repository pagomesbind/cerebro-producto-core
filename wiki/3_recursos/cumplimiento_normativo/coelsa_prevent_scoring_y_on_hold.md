# COELSA.PREVENT — scoring de fraude, umbrales de rechazo y ON HOLD

> Ingesta: 2026-09-11. Fuente: documentación pública de Coelsa (VPN habilitada), https://documentacion.coelsa.com.ar/prevent/#introduccion, sitio completo (Introducción, Objetivo, PREVENT, CPF, Configuración de Rechazos, ON HOLD, Versionado).
>
> **Conexión con un gap ya abierto:** `adquirencia/mecanica_qr_coelsa.md` ya registró (2026-07-17) el anuncio de la nueva funcionalidad **ON HOLD** de COELSA.PREVENT, dejando explícitamente pendiente de confirmar si Bind PSP (como aceptador/billetera) necesita opt-in, configurar algo de su lado, o si el hold lo gestiona Coelsa de forma transparente — ver `2_areas/gaps_y_preguntas.md`. Esta ingesta trae el **detalle funcional completo** de ON HOLD y de todo COELSA.PREVENT — no confirma si Bind ya lo activó operativamente (eso sigue siendo una pregunta de negocio, no algo que la documentación pública resuelva por sí sola), pero sí aporta el contexto necesario para evaluar la respuesta con conocimiento completo del mecanismo. El gap sigue abierto, ahora con más contexto para resolverlo.

## Qué es COELSA.PREVENT

Es la capa de prevención de fraude que corre transversalmente sobre **todas** las operaciones de MPO/COELSA.PAYMENTS (DEBIN, CVU, PCT/QR) — asigna a cada transacción un **score de riesgo de 1 a 99** mediante un modelo de IA (factores: monto, tiempo, patrones de comportamiento), acompañado de **códigos de motivo** que indican dónde se detectó el riesgo. El score viaja en la respuesta de creación/confirmación del DEBIN como `evaluacion.puntaje`/`evaluacion.reglas` (ver [detalle_productos/wallet/coelsa_debin_api_referencia.md §9](../detalle_productos/wallet/coelsa_debin_api_referencia.md)). El servicio salió de beta y está en uso pleno según el changelog de Coelsa (nov. 2024 en adelante).

Tiene **dos frentes de acceso** desde una web propia (`coelsaprevent.coelsa.com.ar`, sistema `PREVENT_WEB` en CoelsaAdmin):

1. **Acceso a CPF** (Central de Prevención de Fraude) — redirección a la plataforma existente, ver [coelsa_cpf_central_prevencion_fraude.md](coelsa_cpf_central_prevencion_fraude.md).
2. **Configuración de Umbrales** — gestión de los umbrales de scoring para rechazo automático (esto es lo nuevo/propio de esta web, distinto de CPF).

## Servicio de Rechazos Automáticos (configuración de umbral)

- Cada entidad configura un **umbral general** (slider 1-100): toda operación con score **≥** umbral se **rechaza automáticamente**. Umbral `100` = no rechaza nada.
- Puede configurarse un **umbral específico por PSP/billetera**, además del general de la entidad — si un PSP no tiene umbral propio asignado, hereda el general.
- Existe una función "Aplicar a todos" para configurar el mismo umbral a varios PSP a la vez.
- Cada cambio de umbral (general o por PSP) dispara una **notificación por email** con el detalle del nuevo valor, y queda registrada la fecha de última modificación.
- **Excepciones de rechazo**: permite marcar cuentas puntuales (por CBU/CVU + CUIT, con ventana de fecha/hora desde-hasta opcionalmente abierta) para que **nunca** sean rechazadas automáticamente aunque su score supere el umbral. Se pueden cargar manualmente (una por una) o por archivo CSV (hasta 50 por carga). Hay una vista de "Excepciones activas" con filtros y exportación a Excel.
- Notificación diaria automática a las entidades y al equipo de Prevención de Fraude con el resumen de excepciones activas.

## Servicio ON HOLD (nuevo, disponible desde 2026-07-28)

- **Qué hace:** en vez de solo detectar fraude después del hecho (scoring + rechazo), **retiene temporalmente en espera** una operación con indicadores de riesgo antes de completarla — capa de control preventivo automatizado.
- **Driver regulatorio:** Comunicación "A" 7463 del BCRA (medidas de prevención/gestión de fraude en transferencias inmediatas) — la misma norma que originó Transferencia 3.1 (ver `adquirencia/mecanica_qr_coelsa.md` Parte 2).
- **Beneficios declarados por Coelsa:** reducción inmediata del riesgo al impedir que la transacción sospechosa se complete (a diferencia del rechazo post-hecho o el contracargo), reglas de detección configurables por entidad, control de CUIT con historial de irregularidades.
- **No se documenta en el sitio público** el detalle técnico de la integración (qué endpoint/webhook debe implementar la entidad para operar con On Hold, ni si requiere opt-in explícito) — el sitio solo linkea a un "Manual de Servicio COELSA.PREVENT On Hold" restringido a VPN/descarga, no accesible como texto en la página. **Esto es lo que sigue pendiente de confirmar para cerrar el gap ya abierto.**
- Cross-referencia técnica: el sitio DEBIN (`#novedades`, 2026-07) menciona en simultáneo mejoras al "Archivo Parcial de Conciliación" con una sección nueva **"Archivo Parcial vs. On Hold (MPV1)"** — sugiere que On Hold sí tiene impacto en el archivo de conciliación diaria (posiblemente las operaciones retenidas aparecen marcadas de forma distinta). Otro hilo a seguir si se decide profundizar.

## Confianza y gaps

Confianza alta en lo leído; el propio contenido deja explícito que el detalle técnico de integración de On Hold está en un manual restringido no incluido en el HTML público. Queda pendiente que el PM decida si vale la pena descargar ese manual (requiere sesión VPN activa) para cerrar el gap de `gaps_y_preguntas.md` sobre necesidad de opt-in.

## Ver también

- [coelsa_cpf_central_prevencion_fraude.md](coelsa_cpf_central_prevencion_fraude.md) — Central de Prevención de Fraude (base colaborativa manual de cuentas sospechosas), accesible desde la misma web `PREVENT_WEB`.
- [gestion_riesgo_fraude_bcra.md](gestion_riesgo_fraude_bcra.md) — Comunicaciones "A" 8471/8473 BCRA (programa de gestión de riesgo de fraude y score obligatorio por CUIL/CUIT).
- [detalle_productos/wallet/coelsa_debin_api_referencia.md](../detalle_productos/wallet/coelsa_debin_api_referencia.md) — API DEBIN, que expone el score de Prevent en su respuesta.

---
*Creado: 2026-09-11 — `/context_merge`, desde ingesta manual de documentación pública de Coelsa (Pablo Gomes).*
