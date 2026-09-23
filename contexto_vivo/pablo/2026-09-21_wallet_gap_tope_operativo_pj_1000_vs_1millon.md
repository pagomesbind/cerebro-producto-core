---
id: 2026-09-21_wallet_gap_tope_operativo_pj_1000_vs_1millon
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_meetings — reuniones \"Daily producto\" (09:30) y \"Producto\" (14:01, con Emma Vignoles), ambas del 2026-09-21"
producto: wallet
tema: Dos topes operativos distintos citados el mismo día para personas jurídicas restringidas ($1.000 vs. $1.000.000), sin reconciliar
tipo: gap
destino_propuesto: 3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md
tipo_destino: actualizar
contradice: "posible contradicción interna entre dos reuniones del mismo día (2026-09-21), no contra el canon existente"
confianza: media
estado: ingestado
merge_commit: 72d6140
---

**Descripción:** el mismo día (2026-09-21), en dos reuniones distintas sobre la misma arquitectura de segmentación PJ (ver item `2026-09-21_wallet_decision_segmentacion_pj_tipos_banca_segmentos`), se citaron dos topes operativos diferentes para una cuenta de persona jurídica mientras espera aprobación de Cumplimiento:

- **"Daily producto" (09:30):** Pablo Gomes planteó explícitamente que "se requiere implementar una regla en Ardid que limite las operaciones de personas jurídicas a **1000 pesos** para obligar a una revisión por cumplimiento" — este es el tope que después se confirma como default de alta automática en la reunión "Ardid - Persona Jurídica" (10:01, mismo día).
- **"Producto" (14:01, con Emma Vignoles):** se estableció que "para permitir la operación se aplicará un **tope temporal de un millón de pesos** hasta que el legajo sea aprobado por cumplimiento" — en el contexto específico de entidades que no usan el onboarding propio de Bind (legajo cargado a mano en un Drive de Cumplimiento).

**Hipótesis sin confirmar:** podrían ser dos escenarios legítimamente distintos — $1.000 para el alta automática estándar de cualquier PJ nueva, $1.000.000 como tope intermedio más permisivo para el proceso manual asistido por Soporte cuando la entidad no tiene onboarding propio. Pero ninguna de las dos reuniones lo explicita así, y no hay ninguna mención cruzada entre ambas cifras en ninguna de las dos transcripciones.

**Pregunta para el usuario:** ¿los $1.000 y el $1.000.000 son dos topes de escenarios distintos (alta automática vs. proceso manual sin onboarding), o uno de los dos quedó mal citado en la reunión? Condiciona cómo se documenta la regla en Ardid y qué le comunican a Nicolás Colón (Wallet) para implementar.

**Estado:** Pendiente — no resuelto en ninguna de las 2 reuniones del 2026-09-21.
