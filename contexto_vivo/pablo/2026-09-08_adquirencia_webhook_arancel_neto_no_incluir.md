---
id: 2026-09-08_adquirencia_webhook_arancel_neto_no_incluir
pm: pablo
fecha_captura: 2026-09-08
fuente: "Reunión 'Producto' (2026-09-08, minuta Gemini), Luciana Rudaz/Emma Vignoles/Pablo Gomes"
producto: adquirencia
tema: decisión de no incluir el arancel neto en el webhook de notificación de pago, para no romper integraciones de clientes que hacen pasamano
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Contexto/Problema:** Luciana Rudaz planteó sumar el arancel neto (después de Coelsa) al webhook de notificación de pago que Bind PSP envía a las entidades — hoy el webhook manda el importe bruto, y algunas entidades (ej. Ripsa) ya lo usan para calcular ellas mismas el resto de las liquidaciones impositivas asumiendo una fórmula fija (0,8% + 21% IVA sobre ese arancel). El equipo de Luciana (Dani/Julie) ya tenía el cambio en desarrollo.

**Decisión tomada:** se detiene el desarrollo. Emma Vignoles y Pablo Gomes objetaron: agregar campos nuevos al webhook puede romper la integración de clientes que no esperan recibirlos, y además expondría información comercial confidencial (el arancel real que Bind PSP negocia con cada entidad, hoy no visible para ellas). El modelo actual funciona precisamente porque esas entidades no acceden al front/backoffice de Bind PSP y no reciben ningún dato adicional al bruto — cambiar eso rompe tanto la integración técnica como el negocio (expone comisiones). Luciana Rudaz se comprometió a avisarle a su equipo (Dani y Julie) que frenen el cambio.

**Impacto en el Roadmap/Producto:** ninguna IDEA de Jira involucrada — es un desarrollo interno que se frena antes de llegar a producción. Afecta a todas las entidades que hoy reciben webhooks de pago sin acceso directo al front/admin de Bind PSP (modelo "pasamano", ej. Ripsa/Coelsa) — cualquier futuro pedido similar (exponer más datos en el webhook) debería evaluarse contra el mismo riesgo de romper integraciones existentes y de exposición comercial.

**Estado:** Aprobado.

> Fuente: Reunión "Producto" (2026-09-08), minuta Gemini, ~00:57:39-01:02:25.
