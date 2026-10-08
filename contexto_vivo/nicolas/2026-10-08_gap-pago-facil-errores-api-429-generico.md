---
id: 2026-10-08_gap-pago-facil-errores-api-429-generico
pm: nicolas
fecha_captura: 2026-10-08
fuente: "Mail 'Re: Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 7-10' — Adriana Endzeliz (Comercial Bind PSP) a Western Union, 2026-10-07"
producto: servicios
tema: Pago Fácil — Comercial le dijo a Western Union que "en general" los errores de las APIs de Bind son 429, lo que no cierra con la semántica de ese código ni con los flujos de error documentados
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/servicios/pago_facil.md — sección Flujo UX/UI (flujos de error, ej. Flujo K: error general al actualizar la deuda en BPG) y secciones de API (responses)"
confianza: media
estado: en_cola
---

**Severidad: Media.**

**Qué se dijo.** Western Union (Brian Yuzefoff) pidió en el seguimiento del 07/10 un **mapeo de errores** de las APIs. Adriana Endzeliz (Comercial) respondió ese mismo día por mail: "en general, si alguna de nuestras APIs presenta algún error, el error que genera es el **429 (too many requests)**", y si hay una caída o interrupción, la respuesta es **500**. Le pidió a WU que confirme si con eso alcanza.

**Por qué es un gap.** El 429 es el código estándar de límite de tasa (demasiadas peticiones), no un error genérico. Que todas las APIs devuelvan 429 ante cualquier error no cierra con:
- la semántica estándar de HTTP, donde un error de validación o de negocio se espera como 4xx específico (400, 401, 404, 422, etc.);
- los flujos de error que ya están documentados para Pago Fácil en `pago_facil.md` (por ejemplo, el Flujo K, error general al actualizar la deuda en BPG), que no hablan de 429.

Puede ser una simplificación de Comercial, o puede ser que alguna capa (APIM, gateway) devuelva 429 de verdad en más casos de los esperables. **No se asume ninguna de las dos.** Si WU construye su manejo de errores sobre esa respuesta, puede tratar como rate limit errores que no lo son.

**Para resolver:** confirmar con el equipo técnico (Keep IT Simple / Fintexa) qué códigos devuelven realmente las APIs que consume WU, y si corresponde, mandarle a WU el mapeo correcto. Relacionado con el pendiente de manual funcional y casos borde de Pago Fácil (T-089).

> Fuente: Mail "Re: Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 7-10" — Adriana Endzeliz, 2026-10-07.
