---
id: 2026-08-26_dato_changelog_releases
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — barrido incremental 2026-08-26 (delta desde 2026-08-15)"
producto: transversal
tema: Entradas nuevas para el changelog de producto
tipo: dato
destino_propuesto: 3_recursos/datos/changelog_releases.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

Aplicar byte a byte (prepend al changelog, orden cronológico inverso por `releaseDate` — el orden final queda AD 71.3 (08-24) → W 72 (08-18) → W 71.8 (08-10) → W 71.7 FIX ya existente):

```
## 2026-08-24 — AD 71.3 (Adquirencia)

**Mejoras funcionales:**
- Se completó el pasaje a producción del nuevo esquema de autenticación externa (AuthExternal V2) para los microservicios compartidos de CVU, DEBIN y Alias Coelsa — última etapa (3 de 3) de una migración de infraestructura que venía en curso desde julio. Sin cambio de comportamiento visible para el usuario final; mejora la base de autenticación de estos servicios compartidos.

## 2026-08-18 — W 72 (Wallet)

**Arreglos de errores:**
- La cache de credenciales de proveedores externos (Poincenot, Lirium, PagBrasil, Payway, etc.) nunca había funcionado desde su creación — todas las consultas de token pegaban innecesariamente a la base de datos. Corregido; sin impacto para el usuario final, pero reduce carga innecesaria en momentos de tráfico alto.
- Corregido un error de configuración que impedía dar de alta correctamente una organización nueva en el módulo antifraude (Ardid).
- Eliminar solo el CVU de una cuenta (sin eliminar la cuenta completa) ya no deshabilita la cuenta por error.
- Corregidos dos casos donde un contracargo de DEBIN recurrente no se procesaba correctamente: uno por una consulta incorrecta al banco central de cámara compensadora, y otro cuando el aviso del contracargo llegaba antes de que la operación original terminara de confirmarse.
- Corregido que una compra de dólar CCL fallida, con comisión de $0, no devolvía el dinero al usuario.
- El endpoint de liquidaciones por usuario (en desarrollo) ahora valida correctamente que la cuenta consultada pertenezca a la organización y esté habilitada para operar con cuentas remuneradas.

**Nuevos comportamientos:**
- El sistema ahora rechaza explícitamente (en vez de propagar sin control) cualquier CVU o CBU que no tenga el formato correcto (22 dígitos numéricos), en los tres microservicios principales de Wallet. Endurece la integridad de datos de cara a normativa BCRA. Cambio de comportamiento: una integración que hoy envía datos mal formados empezará a recibir un error explícito en vez de un comportamiento indefinido aguas abajo.
- La consulta de una operación por su identificador externo ahora encuentra operaciones de hasta 6 meses de antigüedad (antes, solo 3 días).

**Mejoras funcionales:**
- Se completó la migración de infraestructura de mensajería del flujo de transferencias entrantes a un mecanismo más resiliente a fallas de conexión (ya cubría solo una parte del flujo, ahora lo cubre completo).
- El tiempo de espera para reconsultar el estado de una operación (pago con QR, transferencia saliente, DEBIN recurrente) ahora es configurable sin necesidad de un nuevo despliegue — funcionalidad todavía en pruebas de calidad al momento de esta publicación.
- Mejoras de resiliencia en el proceso diario de cuentas remuneradas (FCI) ante errores temporales del proveedor externo.

## 2026-08-10 — W 71.8 (PagosFX) (Wallet)

**Nuevos requerimientos:**
- Configuración de infraestructura en producción: se completaron hosts faltantes de varios microservicios de Wallet (Comprobantes, Consulta de Cuenta, Inversiones, Operaciones, Mastercard) y de la integración con Ardid. Cambio de configuración pura, sin impacto funcional para el usuario.
```
