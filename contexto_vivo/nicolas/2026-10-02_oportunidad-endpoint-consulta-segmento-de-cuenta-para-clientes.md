---
id: 2026-10-02_oportunidad-endpoint-consulta-segmento-de-cuenta-para-clientes
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Hilo de mail 'Consultas integración' — Juan Ignacio Bigourdan (Credicuotas), 2026-09-30"
producto: wallet
tema: Exponer a los clientes un endpoint para consultar el segmento (ClientBankType) de una cuenta
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

- **Oportunidad:** exponer en la API pública de Wallet un endpoint para que la entidad cliente **consulte el segmento de una cuenta**: tipo de banca y segmento estándar/restringido, que hoy se asignan en Wallet y se replican en Ardid.
- **Producto:** Wallet (con dependencia de Ardid).
- **Origen:** Mail "Re: Consultas integración" (2026-09-30).
- **Señal de demanda:** Credicuotas (Juan Ignacio Bigourdan, PM) lo pidió explícitamente. Quieren usar más segmentos para su propio monitoreo y armar reglas por segmento, y hoy no pueden consultar el dato. Es un solo cliente y sin volumen cuantificado.
- **Foco estratégico que alimentaría:** — (a evaluar). Tiene sinergia directa con la segmentación de PRD-263, que multiplica los segmentos por organización (3 tipos de banca × 2 segmentos) y vuelve más útil que el cliente pueda leerlos.
- **Nota:** podría resolverse dentro de PRD-263 o como IDEA aparte. Lo decide el PM (T-097 en su backlog).

> Fuente: Mail "Re: Consultas integración" — Juan Ignacio Bigourdan (2026-09-30).
