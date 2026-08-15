# Guía — CVU (Wallet)

> Fuente: https://psp.bind.com.ar/developers/apis/guia-cvu
> Producto: Wallet — CVU

## ¿Qué debes saber sobre los CVU?

El CVU (Clave Virtual Uniforme) es una cuenta virtual que se utiliza para recibir y enviar pesos argentinos mediante operaciones en el Sistema Financiero Argentino con otras CBU o CVU de bancos o fintech del país.

El CVU se crea asociado al titular de una cuenta de wallet.

Puede eliminarse un CVU para que deje de existir y ser visible por otras entidades financieras. Entonces, el usuario no podrá operar con la misma de ninguna forma. Eliminar el CVU no elimina el saldo, ya que este está asociado a la cuenta.

Puede volver a reactivarse un CVU eliminado previamente simplemente volviendo a crear nuevamente el CVU para la cuenta.

Puede asociarse un alias al CVU utilizable para identificarla al recibir transferencias. En general, puede usarse cualquier valor de alias mientras que no esté usado y no haya sido utilizado en otra cuenta de distinta titularidad en Argentina. Entonces, puede asignarse un alias ya utilizado mientras que este pertenezca o haya pertenecido a una cuenta de misma titularidad, por más que haya sido de otra entidad financiera.

Sólo puede asignarse el alias a un CVU una vez cada 24hs. Si ocurre que Coelsa asigna uno automáticamente en la creación del CVU también deberá esperarse 24hs para asignarle uno nuevo.

Todas las CVU deben tener un alias obligatoriamente. Entonces, al momento de crear un CVU, Coelsa le asignará un alias aleatorio a menos que la entidad le asigne un alias válido dentro de los 5 segundos desde la creación.

Solo se puede asignar un alias en un CVU cada 24 horas.

## Flujo — Ciclo de vida de un CVU

```
CREAR CVU:
  1. POST /cvu (asociado a una cuenta de wallet por ID de cuenta)
     → Coelsa asigna un alias aleatorio al momento de creación
     → Si la entidad quiere un alias propio: tiene 5 segundos para asignarlo
        PATCH /alias → asignar alias válido (no usado por otra titularidad)
     → Restricción: 1 alias cada 24hs (incluye el que asignó Coelsa)

OPERATORIA NORMAL:
  → CVU habilitado puede recibir y enviar ARS en el sistema financiero argentino
  → Identificable por número de CVU o por alias

BAJA DE CVU:
  DELETE /cvu → el CVU deja de existir en el sistema y deja de ser visible
  → El saldo NO se elimina (queda en la cuenta de wallet)
  → Para reactivar: POST /cvu nuevamente con los mismos datos

RESTRICCIONES DE ALIAS:
  - Solo 1 cambio de alias cada 24hs
  - Puede reutilizarse un alias que fue de misma titularidad (aunque sea de otra entidad)
  - NO puede usarse un alias activo de otra titularidad
```

## Endpoints

| Método | Operación | Archivo |
|--------|-----------|---------|
| `POST` | Crear CVU | endpoint_post_crear_cvu.md |
| `DELETE` | Eliminar CVU | endpoint_delete_eliminar_cvu.md |
| `PATCH` | Asignar alias | endpoint_patch_asignar_alias.md |
| `GET` | Consultar cuenta x CBU/CVU/alias | endpoint_get_consultar_por_cbu_cvu_alias.md |
| `GET` | Consultar cuentas CVU | endpoint_get_listar_cuentas_cvu.md |
