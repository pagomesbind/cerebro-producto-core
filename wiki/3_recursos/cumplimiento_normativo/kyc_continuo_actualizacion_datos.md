# KYC continuo — actualización de datos de clientes vía archivo desde SOS

> Estado: discovery — no construido. Proceso nuevo, definido el 2026-09-29, todavía sin mecanismo de ingesta del lado de Bind PSP.

## Qué se definió

El 2026-09-29 hubo una reunión ("Actualización proceso de KYC continuo") entre Diego Scaldaferri (Gerente de Cumplimiento y Prevención de LA/FT/FP, BIND), Silvina Condal y Gonzalo Rivera (Team Leader Integraciones y Soporte, Bind PSP). Se informó que **el banco empezará a actualizar los datos de los clientes de Bind PSP** como parte del proceso de KYC continuo:

1. El equipo de Silvina Condal junta la información actualizada y la **modifica en SOS** (sistema de origen del lado del banco — nombre completo y función no documentados todavía en el Cerebro).
2. **Desde SOS se manda un archivo** a Bind PSP con los datos actualizados.
3. **Bind PSP recibe el archivo y actualiza sus propias bases de datos.**

Gonzalo Rivera sumó al hilo a María Victoria Simonetti (Analista Sr PLA/FT/FP). Queda pendiente una reunión con SOS para definir el formato del archivo y el detalle del intercambio.

## Puntos abiertos (sin definir en la fuente)

- **Alcance:** a qué base/producto aplica — legajos de Wallet, comercios de Adquirencia/Onboarding, o ambos.
- **Resolución de conflicto:** qué dato prevalece si SOS y Bind PSP difieren para el mismo cliente.
- **Frecuencia, formato y canal** del archivo.
- **Dueño de la ingesta del lado de Bind PSP:** un desarrollo en Fintexa, un proceso operativo manual, o un batch ya existente — hoy no se conoce ningún mecanismo así.
- **Relación con la actualización masiva de domicilios de Wallet** (491.495 cuentas, ver `detalle_productos/wallet/` — también regulariza datos KYC; a confirmar si son el mismo esfuerzo o dos iniciativas paralelas).

Ver oportunidad asociada (construir el proceso de ingesta) en [`2_areas/direccion/oportunidades.md`](../../2_areas/direccion/oportunidades.md) (OP-033).

> Fuente: Mail "Actualización proceso de KYC continuo : Mar, 29 de sept de 2026 a las 17:00 – 17:30 (GMT-03)" — Gonzalo Rivera (2026-09-29 17:23 ART).

---
*Última actualización: 2026-10-01 — `/context_merge`: archivo nuevo, desde contexto_vivo de Nicolás Colón.*
