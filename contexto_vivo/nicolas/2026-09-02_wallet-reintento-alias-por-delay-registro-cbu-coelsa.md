---
id: 2026-09-02_wallet-reintento-alias-por-delay-registro-cbu-coelsa
pm: nicolas
fecha_captura: 2026-09-02
fuente: "Reunión \"Analisis de Riesgo - Emisión V 72.2\" (2026-09-02)"
producto: wallet
tema: Nuevo mecanismo de reintento en la asignación de alias de cuentas nuevas, por delay de Coelsa en registrar la CBU recién creada (distinto de los dos reintentos ya documentados)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/validaciones_y_alias_cvu.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "Analisis de Riesgo - Emisión V 72.2" (2026-09-02, análisis de riesgo de despliegue con Matias Alzogaray, Juan Pablo Carubelli, Gonzalo Rivera, Mariana Nadalin, Nicolás Colón, Maria Eugenia Vila, Nico Pomponio, Andrea Orsini), se aprobaron para pase a producción los tickets WS-1556 (BIND) / DEM-1828 (Fintexa): **reintento automático con espera fija corta en la asignación de alias de cuentas nuevas**.

Mecanismo explicado por Juan Pablo Carubelli: cuando se crea una CBU y a continuación se intenta asignar el alias, Coelsa a veces todavía no registró esa CBU en la parte de su sistema que resuelve la asignación de alias — la asignación devuelve un error indicando que el CBU no existe, aunque acaba de crearse. El reintento con espera corta sortea esta ventana de propagación. Objetivo declarado: evitar que queden cuentas nuevas con **alias nulo** por este motivo (hoy es lo que está pasando — "nos quedan un montón de CBU corta con el alias nulo", Gonzalo Rivera). Seguimiento post-implementación asignado a Gonzalo Rivera: verificar que bajen las altas de CBU sin alias.

**Distinción con los mecanismos ya documentados en el archivo destino:** no es el fix de 700ms de MDA-292391/Banco Industrial (ese es por error del banco emisor al consultar Coelsa antes de responder la asignación) ni el reintento genérico ante error de APIBank mencionado en la reunión "Weekly - Producto / Operaciones" del 2026-08-31 (ese no detalla causa). Este tercer mecanismo tiene una causa raíz específica y distinta: **delay de Coelsa en registrar/propagar la CBU recién creada**, no un error del banco emisor ni de APIBank.

Contexto de despliegue: forma parte de un paquete de 3 tickets con impacto medio / urgencia alta (vertical Emisión), reprogramado de jueves a **lunes 2026-09-08 a las 8:00hs** por falta de tiempo de testing (ver decisión relacionada en `1_proyectos/tareas.md` si aplica seguimiento). Semáforo asignado: verde (no funcional), con seguimiento post-implementación por Gonzalo Rivera.

> Fuente: Reunión "Analisis de Riesgo - Emisión V 72.2" (2026-09-02), minuta Gemini.
