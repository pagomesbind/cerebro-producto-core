---
id: 2026-09-03_onboarding_octagon_paquete_datos_integracion
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_mails — mail 'Re: Integración On Boarding', Diego Weledniger (Bind, Comercial) reenviando propuesta de Begoña Perez de Solay (Octagon), threadId 1a0623520bc8519e, 2026-09-02"
producto: onboarding
tema: OCTAGON — detalle del paquete de datos propuesto para la integración de onboarding de personas jurídicas
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Cliente:** OCTAGON (`log_clientes.md`: "Evolutivo en Intg" — QRI, Wallet, Onboarding). Continuación directa del item ya ingestado `2026-08-19_clientes_octagon-demo-onboarding-banco-industrial` (demo de onboarding propio + pedido de acceso de Compliance de Banco Industrial), que dejó pendiente "avanzar en un paquete de datos para automatizar la creación de CBU y alta del comercio".

**Novedad (2026-09-02):** Begoña Perez de Solay (Octagon) envió el detalle concreto del **paquete de datos** propuesto para la integración del onboarding de personas jurídicas, con un gráfico de la propuesta de integración (adjunto, no procesado por esta skill). Diego Weledniger (Comercial de Bind) respondió sumando al equipo técnico/producto de Bind para diagramar la integración, y a PLD cuando Luciano Dufain (Octagon) entregue el acceso a la plataforma.

**Campos del paquete de datos propuesto (personas jurídicas):**
- CUIT, razón social, fecha, hora, número de legajo digital.
- Firmante: nombre, mail, teléfono.
- Deudor ARCA (actividad).
- Verificación en listas — de la sociedad, de los firmantes y de los beneficiarios finales.
- Situación BCRA — última situación registrada y si tiene cheques rechazados en el último año.
- Domicilio fiscal y domicilio comercial.
- Validaciones/DDJJ cruzadas: `esFacta` (documento no registrado en FATCA, solo DDJJ), `esOcde` (la persona no paga impuestos fuera de Argentina, solo DDJJ), `esPEP` (estado del documento no consultado en sistema PEP), `esUIF` (persona registrada en UIF con una actividad).
- Estructura societaria: beneficiarios finales (sociedades/personas físicas con +10% de participación), listado de documentación que conforma el legajo digital verificado.
- Validación de identidad de los representantes legales contra RENAPER (confirmación de validación).

**Estado:** propuesta recibida, sin fecha de integración confirmada — el paso siguiente es que el equipo técnico/producto de Bind (recién sumado) diagrame la integración necesaria, y que Luciano Dufain (Octagon) entregue el acceso a la plataforma para que PLD se sume también.
