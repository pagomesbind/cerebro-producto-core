# Guía — ¿Cómo funciona el recycle?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-recycle
> Producto: Wallet — Recycle

## Descripción

En nuestro sistema pueden configurarse algunos tipos de comprobante de débito para que sean monitoreados por un sistema de recycle.

Lo que significa que si al momento de crear un comprobante de débito de este tipo, este falla por saldo insuficiente en la cuenta, será registrado para intentar crearse automáticamente en otro momento en que la cuenta tenga saldo.

Entonces, se monitorea la cuenta deudora y al momento de registrarse un crédito en ella, se intenta crear los débitos pendientes inmediatamente.

Es posible configurar tipos de comprobante específicos de la organización para que no se tengan en cuenta para cálculo de impuestos. Esta configuración debe ser solicitada al equipo de soporte técnico de Bind PSP.

El sistema dispara un evento para avisar cuando el sistema de recycle registra un nuevo débito a monitorear y también cuando el sistema de recycle logra crear un débito.

Por defecto, están configurados para recycle los tipos de comprobante de impuestos que crea el sistema. Pero la organización puede considerar utilizar esta funcionalidad para cualquier tipo de comprobante.

## Flujo — Débito fallido con recycle

```
1. Sistema (o entidad) intenta crear comprobante de DÉBITO en una cuenta
   → La cuenta NO tiene saldo suficiente → falla

2. El tipo de comprobante está configurado para recycle:
   → El sistema registra el débito como PENDIENTE de recycle
   → EVENT "nuevo.debito.reciclar" → webhook a la entidad (aviso de deuda pendiente)

3. Más adelante: la cuenta recibe un CRÉDITO (de cualquier origen)
   → El sistema de recycle detecta el nuevo saldo disponible
   → Intenta crear el/los débitos pendientes inmediatamente

4. Si hay saldo suficiente:
   → Débito creado exitosamente
   → EVENT "comprobante.reciclado" → webhook a la entidad

Si el crédito no es suficiente para cubrir todos los débitos pendientes:
   → Se atienden en orden hasta agotar el saldo disponible
   → Los restantes siguen pendientes hasta el próximo crédito

Configuración por defecto: tipos de comprobante de impuestos tienen recycle activado.
La organización puede solicitar a soporte activar recycle para sus propios tipos de comprobante.
```

## Endpoints del módulo

| Tipo | Descripción | Archivo |
|------|-------------|---------|
| `EVENT` | Aviso de comprobante reciclado | [endpoint_event_comprobante_reciclado.md](endpoint_event_comprobante_reciclado.md) |
| `EVENT` | Aviso de nuevo débito a reciclar | [endpoint_event_comprobante_pendiente.md](endpoint_event_comprobante_pendiente.md) |
