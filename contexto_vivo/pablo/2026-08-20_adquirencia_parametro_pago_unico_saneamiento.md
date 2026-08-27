---
id: 2026-08-20_adquirencia_parametro_pago_unico_saneamiento
pm: pablo
fecha_captura: 2026-08-20
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-08-20 12:05, docId 1Q3PZO-WuwDNq5HOyW-eoww1KEVJBvwL7-NP9nT3WMkE)"
producto: adquirencia
tema: Definición del parámetro "pago único" para diferenciar cuentas de Botón Simple vs. RXT + saneamiento de base
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

**Decisión acordada (2026-08-20):** el parámetro **"pago único"** se definió para diferenciar el producto asociado a una cuenta con CBU — **valor 1 = botón de pago**, **valor 0 = RXT**. Objetivo: poder identificar qué colecciones/cuentas corresponden a cada categoría.

**Saneamiento de base acordado:** Daniela Collia (Fintexa) y Nicolás Colón van a coordinar el saneamiento de la base de datos para identificar las cuentas de "pago único" existentes y diferenciarlas correctamente entre RXT y botón simple. Nicolás Colón queda a cargo de analizar qué colecciones corresponden a cada categoría. **Decisión de secuencia:** el saneamiento se ejecuta en conjunto con el despliegue del código correspondiente, para asegurar que quede todo alineado en producción al mismo tiempo (no antes, no después).

**Contexto relacionado ya documentado:** el 2026-08-06 (reunión "FAVACARD - Rxt y BS 2.0") ya se había identificado un bug de asignación automática de CBU corta en Botón Simple 2.0 **sin filtro por `pago_unico`** — este saneamiento y esta definición formal del parámetro parecen ser la resolución de fondo de ese hallazgo. A confirmar en el merge si ambos items se referencian cruzados.

**Confianza media:** no se identificó en la wiki actual una definición previa explícita de los valores 0/1 del parámetro "pago único" (sí se sabía que existía el campo, por el bug de FAVACARD) — el destino propuesto es el mejor candidato temático (`boton_simple_2_0.md`, que ya cubre el objeto Deuda con pool de CVUs compartido entre RxT y botón), a confirmar si corresponde mejor a `carga_masiva_cajas_rxt.md`.

> Fuente: Reunión "Análisis COBRO" (2026-08-20), minuta Gemini.
