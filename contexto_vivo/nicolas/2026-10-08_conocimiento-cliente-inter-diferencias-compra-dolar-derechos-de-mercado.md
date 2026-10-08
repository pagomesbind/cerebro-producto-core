---
id: 2026-10-08_conocimiento-cliente-inter-diferencias-compra-dolar-derechos-de-mercado
pm: nicolas
fecha_captura: 2026-10-08
fuente: "Mail 'Re: Diferencias Compra DOLAR Septiembre' — Josefina Cereijo y Daniel B. Martinez (Inter) 2026-10-07; mensajes previos de Mariano Ferrari (BIND INVERSIONES) 2026-09-17 y Mariano Zanier (Poincenot) 2026-09-21"
producto: wallet
tema: Inter — diferencias recurrentes de centavos entre el monto de compra de dólares informado por la API y el liquidado, atribuidas a derechos de mercado del broker; Inter pide definir quién los absorbe
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

Complementa la sección de **Inter** en `casos_de_uso_clientes.md` ("Particularidades / cronología"). Toca la operatoria de compra de dólares (Dólar CCL vía IVSA/Poincenot) que Inter consume por API de Bind PSP, la misma del proyecto `inter_trazabilidad_ccl` (PRD-259), aunque el tema no es de ese alcance.

- **Desde principios de septiembre 2026** Inter ve diferencias de centavos, en forma consistente, entre el valor que le informa Bind y el que liquida en su cuenta. Ejemplos de septiembre: 09/09 USD 1.000,78 recibidos contra 1.000,68 liquidados (10 centavos de más, ticket BP-52506); 10/09 91,71 contra 91,72 (BP-52505); 11/09 132,86 contra 132,87 (BP-52504); otro de 61,79 contra 61,80 (BP-52566). Según Inter, antes de septiembre no pasaba.
- **17/09. Explicación de BIND INVERSIONES (Mariano Ferrari):** la diferencia son los **derechos de mercado**. BIND INVERSIONES recibe el neto de la operación, que ya descuenta esos derechos (en una operación de USD 1.000 fueron 10 centavos).
- **21/09. Soporte en dos portales:** Poincenot pidió que Inter levante estos pedidos en su propio Jira de operaciones. Inter respondió que no es viable cargar tickets en dos portales y pidió que Bind PSP derive los tickets de su front a Poincenot. No consta respuesta.
- **07/10. Inter retoma el tema** (Josefina Cereijo): adjunta la lista de valores que obtiene de las APIs (`report-LOAD_UNLOAD_OPERATIONS_AR2026-09-30.xlsx`, sin descargar) y pide que **el valor informado por API coincida con el efectivamente ejecutado en el mercado**. Agenda una reunión para fin de esa semana para encontrar la causa raíz.
- **07/10. Inter pide una definición comercial** (Daniel B. Martinez, US Investment Operations): por los tickets de soporte de BIND y lo hablado con el broker IVSA, entiende que las diferencias vienen de **comisiones del broker / derechos de mercado** descontados del monto total. Su expectativa es **recibir el monto total solicitado**. Pide definir cuanto antes si esos cargos los absorbe **Inter o BIND**, para fijar el tratamiento operativo.

**Lectura:** el tema escaló de un reclamo de conciliación a una definición comercial pendiente (quién absorbe los derechos de mercado) y a una discusión de producto (qué monto informa la API: bruto o neto). Nicolás Colón está en copia, sin pregunta directa. Si la respuesta termina siendo cambiar el monto que informa la API, puede cruzarse con el webhook de Dólar CCL de PRD-259. Sigue siendo, en primer lugar, un tema de BIND INVERSIONES / Poincenot y Comercial.

> Fuente: Mail "Re: Diferencias Compra DOLAR Septiembre" — Josefina Cereijo y Daniel B. Martinez (Inter), 2026-10-07; Mariano Ferrari (BIND INVERSIONES), 2026-09-17; Mariano Zanier (Poincenot), 2026-09-21.
