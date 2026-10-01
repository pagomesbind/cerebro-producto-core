---
id: 2026-10-01_onboarding_desactivacion_flujo_ob_bind_pagos
pm: pablo
fecha_captura: 2026-10-01
fuente: "/sync_mails — mail \"Desactivación del flujo de OB entidad Bind Pagos\", Gonzalo Rivera, 2026-10-01"
producto: onboarding
tema: "A pedido del banco se desactivó el flujo de OB de pequeños comercios (entidad Bind Pagos)"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/onboarding/hallazgos_operativos_historicos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Gonzalo Rivera (Team Leader de Integraciones y Soporte) informó el 2026-10-01 que, a pedido del banco, se desactivó ese mismo día el flujo de Onboarding de pequeños comercios — es decir, el correspondiente a la entidad **Bind Pagos** (distinta de la entidad PSP/Tecnología Financiera bajo la que opera el resto del onboarding). El mail no explica el motivo de negocio detrás del pedido del banco; solo confirma la ejecución técnica.

**Cómo se ejecutó:** se modificó el campo identificador de la entidad en el Backoffice. El identificador anterior (necesario para poder reactivar el flujo en el futuro, dado que Fintexa no lo tiene resguardado en ningún lado) quedó registrado:

```
03b46cd3-127c-4e58-b849-34df08af5383
```

Destinatarios directos del aviso: Emma Vignoles, Mariana Nadalin, Pablo Gomes.

**Nota de contexto (no confirmada por este mail):** el mismo día circuló por otro hilo ("Actualización proceso de KYC continuo") un adjunto de "TyC Pequeños Comercios Bind PSP 09.2026" que Luciana Rudaz retiró minutos después por error ("Fe de erratas, desestimar el mail anterior") — no está claro si ese adjunto estaba relacionado con esta desactivación o era para otro propósito; no se pudo confirmar vínculo alguno entre ambos hilos.

> Fuente: mail "Desactivación del flujo de OB entidad Bind Pagos" — Gonzalo Rivera, 2026-10-01, threadId `1a0f777b988e924c`.
