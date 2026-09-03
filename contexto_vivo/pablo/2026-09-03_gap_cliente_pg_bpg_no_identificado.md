---
id: 2026-09-03_gap_cliente_pg_bpg_no_identificado
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_mails — mail 'Estimación volumen BPG 08.26 a 03.27', Emma Vignoles, threadId 1a0624b5968ba679, 2026-09-02"
producto: servicios
tema: Cliente referido como "PG" en una estimación de volumen de BPG — no matchea contra log_clientes.md
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: baja
estado: ingestado
merge_commit:
---

**Texto literal del mail (cuerpo completo, sin adjunto procesado):** "Les comparto la estimación de volumen del cliente PG por el uso de BPG" — Emma Vignoles, 2026-09-02, a Alberto Murad, Diego Weledniger, Gonzalo Lazzaro, Adriana Endzeliz, Juan Pablo Carubelli, Pablo Gomes, Hernán Clarich, Nicolás Pomponio (Fintexa). Adjunto un Excel ("Ejercicio BIND V3.xlsx") con el detalle numérico — no descargado ni procesado por esta skill (regla de adjuntos).

**El gap:** "PG" no matchea ningún cliente de `2_areas/clientes/log_clientes.md`. Podría ser una sigla interna corta para un cliente ya conocido (candidatos por contexto de dominio — BPG/"Botón Pago Grande" aparece asociado a Pago Fácil en `1_proyectos/alias_cvu_checkout/proyecto.md §Anexo` y en la oportunidad OP-012 de `2_areas/direccion/oportunidades.md`, pero Pago Fácil se gestiona como "ente" de Servicios sin ficha propia, no como "PG") o un cliente/entidad nuevo sin ficha todavía. No se resuelve por inferencia — se deja el texto literal para que el PM o `/sync_customers` lo confirme contra Notion.
