# Guía — ¿Cómo tratar los contracargos?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-contracargodebin
> Producto: Wallet — Debin recurrente

## Descripción

Por norma, un usuario tiene hasta **30 días** para desconocer una operación de debin recurrente desde la cuenta comprador (la cuenta desde donde se debitó el dinero).

Llegado el caso, la entidad (banco o billetera) dueña de la cuenta compradora para concretar este desconocimiento crea la operación contracargo debin en Coelsa, quien se encarga de debitar el dinero de la cuenta recaudadora de la cuenta vendedora (la cuenta donde se acreditó el dinero del debin) y acreditarla en la cuenta compradora original.

Coelsa lleva a cabo este movimiento arbitrariamente **sin esperar una validación de la entidad vendedora**, es decir que no espera una validación de saldo de la cuenta vendedora. Esto significa que un usuario puede hacernos un contracargo y se le devolverá el dinero por más que no registre saldo suficiente en su cvu.

## Flujo al recibir un contracargo

1. Otro banco instruye un contracargo de debin recurrente con Coelsa.
2. Coelsa debita el saldo de nuestra recaudadora, acredita en la recaudadora externa y crea el contracargo exitoso.
3. Nuestro banco (Banco Industrial) informa el contracargo a Bind PSP.
4. Bind PSP intenta debitar saldo al usuario, registra la operación de contracargo en el sistema y avisa a la organización.

## Escenarios posibles al registrar el contracargo

| Escenario | Estado resultante |
|-----------|-------------------|
| La cuenta tiene saldo suficiente → se debita el total. | `Devuelta` |
| La cuenta tiene saldo = 0 → se registra el débito pendiente de recycle (se monitoreará la cuenta para debitarle la deuda al próximo ingreso suficiente). | `Devuelta pendiente` |
| La cuenta tiene saldo parcial → se debita lo disponible y se registra el resto como pendiente de recycle. | `Devuelta parcial` |

> **Importante:** Un usuario puede desconocer un DEBIN recurrente desde su banco e iniciar un contracargo para que se reverse arbitrariamente la operación por más que el usuario no tenga saldo en su cuenta.
