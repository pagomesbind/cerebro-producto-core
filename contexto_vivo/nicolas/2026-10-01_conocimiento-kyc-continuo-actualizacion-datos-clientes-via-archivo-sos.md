---
id: 2026-10-01_conocimiento-kyc-continuo-actualizacion-datos-clientes-via-archivo-sos
pm: nicolas
fecha_captura: 2026-10-01
fuente: "Mail 'Actualización proceso de KYC continuo : Mar, 29 de sept de 2026 a las 17:00 – 17:30 (GMT-03)' — Gonzalo Rivera (Team Leader Integraciones y Soporte, Bind PSP), 2026-09-29"
producto: transversal
tema: KYC continuo — el banco empezará a actualizar datos de clientes de Bind PSP en SOS y los mandará a PSP en un archivo para que los actualice en sus bases
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/
tipo_destino: crear
contradice: "no"
confianza: media
estado: en_cola
---

**Nuevo proceso de KYC continuo (definido el 29/09/2026).** El 29/09 hubo una reunión con Diego Scaldaferri (Gerente de Cumplimiento y Prevención de LA/FT/FP, BIND) y Silvina Condal. Ahí se informó que **se empezarán a actualizar los datos de los clientes de Bind PSP**. Así funciona:

1. **El equipo de Silvina Condal junta la información** y la **modifica en SOS**. SOS es el sistema de origen del lado del banco. Su nombre completo y su función no están documentados en el Cerebro.
2. **Desde SOS se manda un archivo** a Bind PSP con los datos actualizados.
3. **Bind PSP recibe el archivo y actualiza sus propias bases de datos.**

Rivera sumó al hilo a María Victoria Simonetti (Analista Sr PLA/FT/FP). Va a hacer falta reunirse con SOS para entender **el formato del archivo** y los detalles del intercambio.

**Puntos abiertos (el mail no los define):**
- A qué base o producto aplica: legajos de Wallet, comercios de Adquirencia/Onboarding, o ambos. Tampoco dice qué dato manda si hay conflicto entre SOS y PSP.
- Frecuencia del archivo, formato y canal.
- Quién hace el proceso de ingesta del lado de PSP: un desarrollo en Fintexa, un proceso operativo o un batch existente. Hoy no se conoce ningún mecanismo de ingesta así.
- Relación con la actualización masiva de domicilios de Wallet (491.495 cuentas, ver `contexto_vivo/2026-09-15_conocimiento-wallet-actualizacion-masiva-domicilios-faltantes.md`), que también regulariza datos KYC.

Nota: el 30/09 Luciana Rudaz respondió en el mismo hilo con los TyC del producto "sol de cobros" para pequeños comercios del nuevo flujo de OB. Una hora después pidió por "fe de erratas" que se desestimara ese mail (fue al hilo equivocado). Por eso no se captura como contenido. El adjunto `TyC Pequeños Comercios Bind PSP 09.2026.pdf` no se descargó.

> Fuente: Mail "Actualización proceso de KYC continuo" — Gonzalo Rivera (2026-09-29 17:23 ART); respuestas de Luciana Rudaz (2026-09-30 17:49 y 18:15 ART, desestimadas por la autora).
