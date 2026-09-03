# Notas de diseño — /idea_newsletter

Esto documenta las decisiones y los errores concretos que salieron de armar
y mandar el primer newsletter de este tipo (el de "Mejora de tiempos en
operaciones Wallet", disparado por el caso de Pagos QR). Los números
matchean los comentarios `<!-- ver design-notes.md #N -->` de las dos
plantillas. Leelo antes de tocar las plantillas, no solo antes de usarlas.

## 1. Por qué el header y el bloque "Importante" no reusan `--primary-dark`

La primera versión del artifact usaba `var(--primary-dark)` como fondo del
header (bloque azul oscuro con texto blanco). Funciona en modo claro, pero
`--primary-dark` está pensado como color de **texto** sobre fondos claros,
así que en modo oscuro se redefine más CLARO (para que el texto se siga
leyendo sobre fondos oscuros) — y un token pensado para texto, usado como
fondo sólido, se invierte: en modo oscuro el header quedaba con fondo
lavanda claro y texto blanco encima, ilegible.

Por eso existen `--brand-block-bg` / `--brand-block-fg` / `--brand-block-fg-soft`,
declarados **una sola vez en el `:root` de base y nunca redefinidos** en los
bloques de modo oscuro — son para "bloques sólidos de marca" (fondo navy +
texto blanco), un rol distinto del texto-sobre-tinte. Cualquier bloque
nuevo con fondo sólido de marca (no una tarjeta clara) usa estos tokens,
no `--primary-dark`.

## 2. Por qué "Importante" va al final, después de "Más información"

Se probaron tres ubicaciones: antes de "¿Cuánto nos beneficia?", justo
después, y al final. El PM la quiso al final por dos motivos que van a
seguir aplicando a otras ideas: (a) no quiere que la sección de otro color
corte la "estética constante" del resto del newsletter en el medio del
flujo de lectura — mejor que aparezca como cierre; (b) es la sección menos
crítica para el lector promedio (un caveat de alcance), así que tiene
sentido que sea lo último, no lo que se lee justo después del dato fuerte
de beneficio.

## 3. Botón "a prueba de clientes de correo" (versión mail únicamente)

**Nunca** pongas el texto del botón en un `<p>`/`<div>` dentro del `<a>`
esperando que herede el color de un padre — varios clientes de correo
(especialmente apps de Android/iOS y Outlook) ignoran el color/decoración
de texto de los hijos y le aplican al link su propio azul-subrayado por
default. El color y `text-decoration:none` van **directo en el `<a>`**, y
el contenido adentro son `<span style="display:block">`, no `<p>`.

## 4. La franja blanca suelta antes de un bloque de color

Si un separador (fila con solo una línea de 1px) va en una fila propia
justo antes de una sección con fondo de color (como "Importante"), queda
una franja blanca metida entre el contenido anterior y el color — se ve
como un corte, no como aire. La solución: el borde superior va **en el
mismo `<td>`** que ya tiene el `background-color` de la sección coloreada,
nunca en una fila separada. El aire real (para que no quede todo pegado)
se agrega como `padding-bottom` en la sección anterior (24px en vez de 0),
no como una fila extra.

## 5. Los divisores usan `font-size:1px`, no `0`

El patrón de "línea divisoria" en email es un `<div>` con
`border-top:1px solid`, `line-height:1px` y una altura forzada a casi cero
con `font-size`. Usar `font-size:0` hace que algunos clientes de Windows/
Outlook no lo respeten y el divisor salga más alto de lo esperado.
`font-size:1px` es el valor seguro.

## 6. Íconos: SVG en el artifact, emoji en el mail — nunca al revés

El artifact puede usar los `<svg>` de línea en chips de color (mismo
lenguaje visual que `/pdf_build`). La versión de mail **no** — la mayoría
de los clientes de correo (Outlook en particular) no renderiza SVG inline,
así que ahí se usa el mismo criterio que ya traía el newsletter original
de referencia: un emoji por sección (🎯 por qué, 🔧 qué se hizo, 🚫 qué no
se hizo, 📈 cuánto nos beneficia, 📚 más información, ⚠️ importante), un
espacio normal después, nunca `&nbsp;` doble. Tampoco pongas una flecha de
texto (`→`) al final del label de un botón — se ve inconsistente entre
clientes/fuentes; si el botón necesita comunicar acción, alcanza con que
sea un botón de color.

## 7. Radio de los botones en el mail

Los botones de "más información" van con `border-radius:14px` (no el 8px
que usan las tarjetas del rótulo) — más redondeado se ve más a tono con el
resto de la pieza, es un ajuste que pidió el PM después de ver el primer
envío real en su bandeja.

## 8. El rótulo separa "publicado" de "activo"

Son dos hechos distintos y a veces tienen fechas distintas: una versión se
despliega a producción en una fecha, y el cambio se activa (por config,
flag, etc.) en otra. No los combines en un solo campo ambiguo. La versión
va entre paréntesis pegada a la fecha de publicación
(`{{FECHA_PUBLICADO}} ({{VERSION}})`) para ahorrar un tile — no le hace
falta su propio box.

## 9. La tabla de beneficios es flexible: medido vs. esperado

El header de la segunda columna (`{{COLUMNA_AHORA}}`) normalmente es
"Ahora", pero si la idea todavía no tiene medición real post-lanzamiento,
usá "Esperado" y ajustá `{{BENEFICIO_NOTA}}` para decirlo explícito ("Aún
sin medición post-lanzamiento — valor estimado en el diseño de la
solución", en vez de "Confirmado con X días de datos..."). Nunca dejes que
la tabla insinúe un dato medido si en realidad es una proyección.

## 10. Nunca inventar un número

Si una fila de la tabla de beneficios no tiene dato duro (ni medido ni
estimado con base), no se rellena con un número inventado — se resume la
fila en texto cualitativo dentro de `{{BENEFICIO_EN_CRIOLLO}}` en vez de
forzarla a la tabla, o se le pregunta al PM el número antes de mandar
nada.

## 11. La firma del footer

"Equipo de Producto de **Bind PSP**" (con "Bind PSP" en negrita) — no
"Bind PSP — Equipo de Producto" ni ninguna otra variante. Es un ajuste
explícito del PM sobre la primera versión.

## 12. Al mandar el mail: pasá el HTML de verdad, no un placeholder

Error real cometido en la sesión que originó esta skill: la primera llamada
a la herramienta de envío de Gmail mandó un fragmento de texto escapado
(`&lt;div...&gt;`) en vez del HTML real como `htmlBody`, y el mail salió
roto. Antes de dar un envío por bueno, leé el mensaje recién enviado con
`get_message` (formato `PLAIN_TEXT` o mirando el `snippet`) y confirmá que
el contenido visible es el newsletter real, no una etiqueta suelta ni HTML
escapado.
