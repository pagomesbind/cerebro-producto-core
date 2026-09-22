---
id: 2026-09-22_onboarding_nivel3_automatico_cvu_comercio_y_etiqueta_cbu
pm: pablo
fecha_captura: 2026-09-22
fuente: "sesión libre — capturas de pantalla del backoffice de Onboarding Jurídico sobre una solicitud de test (CLARO S.A.) que sí llegó a completar la aprobación final, aportadas por el PM para cerrar el manual de uso del flujo de 4 pasos"
producto: onboarding
tema: nivel 3 automático post-Paso 4 (alta de Wallet/CVU y comercio) y etiqueta "CBU" que en realidad muestra el CVU
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/onboarding/onboarding_personas_juridicas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Cierre del flujo de 4 pasos ya documentado (carga → Nivel 1 → Nivel 2/cumplimiento → onboarding personal del representante legal): una vez que el representante legal completa el Paso 4, corre un **Nivel 3 automático, sin intervención de ningún operador**, que termina de aprobar la solicitud y provisiona la cuenta.

**Progresión de estados observada en "Historial" (todo con el mismo trigger — la conformidad del representante legal):**
1. `Pendiente Revisión` (Nivel 1 — Oficial De Negocio) → Aprobada
2. `Pendiente Revisión` (Nivel 2 — Cumplimiento) → Aprobada
3. `Pendiente Representante Legal` (Nivel 2 — Cumplimiento) → "Aprobada por niveles - Emails enviados a RL" (acá se dispara el Paso 4)
4. `Aprobado a revisar` (Nivel 3) → comentario "Alta Wallet OK"
5. `Aprobada` (Nivel 3) → comentario "Solicitud completa"

Los pasos 4 y 5 son el Nivel 3 automático: no hay ningún actor humano entre "Aprobada por niveles" y "Solicitud completa". La sección "Documentación" de la derecha muestra en paralelo `DDJJ`, `Alta Wallet`, `Comercio - Alta` y `Asignar Comercio`, cada una con su propio timestamp — son las tareas internas que ese Nivel 3 ejecuta.

**Qué queda creado, visible en "Datos de la Solicitud" con estado final "Aprobada":**
- **Datos Bancarios**: se completa un campo que la pantalla etiqueta como **"CBU"**, pero que en realidad contiene el **CVU** de la cuenta recién creada — no hay un CBU real involucrado en ningún punto de este flujo. Es una etiqueta heredada/incorrecta en esa pantalla puntual del backoffice de Onboarding Jurídico, no un problema de terminología del producto Wallet en general (que sí distingue CBU/CVU correctamente en su propia documentación — ver `detalle_productos/wallet/validacion_totalizadores_cbu_cvu.md` y `apis_expuestas/cvu/`). Vale la pena que quien lea esa pantalla del backoffice no se confunda pensando que se generó un CBU.
- **Datos Comerciales**: ID del comercio, Código de caja y Código de sucursal, es decir el comercio queda dado de alta y vinculado a la cuenta en el mismo paso.

**Nota de método, no de producto:** estas capturas se tomaron sobre otra solicitud de test (CLARO S.A.), no sobre FIAT CHRYSLER RIMACO ARGENTINA S.A. (la usada en el resto del manual/relevamiento), porque un error de ambiente impidió completar la aprobación de Nivel 3 sobre esta última. El comportamiento y las pantallas son las mismas para cualquier solicitud que llegue a este punto.

Fuente: manual de uso — ver [`2026-09-21_manual_onboarding_pj_operador.html`](../proyecto-la-virginia-ob-pj/artefactos/2026-09-21_manual_onboarding_pj_operador.html), último ítem del Paso 4.
