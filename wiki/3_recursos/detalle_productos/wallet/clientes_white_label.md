# Clientes white-label de Wallet — casos operativos (Astropay, WICO, APK básica)

> Estado: en producción.

> Fuente: Notion histórico, Epics **"Astropay Wallet"**, **"WICO"** y **"APK para wallet básica"**. A diferencia de otras Epics de esta wiki (que documentan una funcionalidad), estas tres describen la puesta en marcha operativa de instancias white-label de Wallet para clientes/casos de uso específicos — quedan agrupadas acá por ser del mismo tipo de conocimiento (onboarding de cliente, no feature de producto).

## 1. Astropay Wallet — dimensionamiento de un cliente de alto volumen

Astropay es, según referencias cruzadas en otras Epics de esta wiki ([crypto.md](crypto.md), [pix_rol_emisor.md](pix_rol_emisor.md), [debin_y_fondeo.md](debin_y_fondeo.md), [conciliacion_y_totalizadores.md](conciliacion_y_totalizadores.md)), el **cliente de mayor volumen y con más requerimientos especiales de Wallet** — DIRECTA, PIX Rol Emisor, la contingencia Coelsa y el endpoint de conciliación dedicado fueron todos requerimientos originados por o para Astropay.

- **Dimensionamiento pre-lanzamiento**: 2 millones de transacciones/mes, 350.000 CVU.
- **Riesgo identificado y luego descartado**: "no soportamos los procesos nocturnos" — quedó tachado en la fuente, indicando que se resolvió antes del lanzamiento.
- **Stress test dedicado**: se corrió un test de estrés específico para Astropay sobre Wallet Service — 2.000.000 de transacciones simuladas sobre 500.000 cuentas (alta de cuentas, transferencias entrantes/salientes, débitos/créditos internos, consulta de saldo), con **prioridad por sobre cualquier otro proyecto de Wallet Service** en ese momento. Metodología: prueba incremental de hilos concurrentes (1 → 5 → 7 → 10) por tipo de operación, más una segunda prueba inyectando un lote de 500.000 comprobantes en paralelo, apuntando a sostener 100.000 comprobantes/día (volumen necesario para poder probar la generación de archivos de reportería en un día normal y en un fin de semana largo).
- **Lectura para futuros clientes de volumen similar**: Astropay es la referencia de "cliente grande" en esta wiki — cualquier nuevo cliente que se acerque a sus órdenes de magnitud (millones de tx/mes, cientos de miles de cuentas) debería anticipar la misma necesidad de stress test dedicado y probablemente los mismos pedidos de contingencia/conciliación a medida.

## 2. WICO — configuración de marca (branding), sin mecánica de producto propia

Epic mayormente de **identidad visual**: manual de marca (`WI_MANUAL_DE_MARCA.pdf`) y logos en variantes de color. Los tickets de desarrollo relevados son de **ajuste pixel-perfect de UI** (posición de textos e íconos en pantallas de onboarding/login) — no aportan mecánica de negocio nueva más allá de ser un despliegue white-label estándar de Wallet con la marca WICO.

## 3. APK para wallet básica — caso de uso transporte/pasajero

A diferencia de WICO, esta Epic sí revela un **caso de uso concreto**: la app está pensada para un **pasajero de transporte** que necesita loguearse para ver su saldo y su QR "para viajar" — es decir, una instancia de Wallet aplicada a pagos de transporte público o similar.

Requisitos de producto relevados en el ticket de Login:
- **Login sin conexión a internet** — requisito explícito, no trivial para una wallet (implica cache local de sesión/credenciales).
- **Desbloqueo por biometría del dispositivo** (huella/FaceID/patrón) como método de login alternativo.
- **Recuperación de contraseña.**
- **Multi-organización**: un mismo usuario puede pertenecer a **dos organizaciones** a la vez — regla de negocio explícita del modelo de cuentas, relevante para cualquier feature que asuma una relación 1:1 usuario↔organización.
- Manejo de cuenta deshabilitada: debe informarse explícitamente en el login, no fallar en silencio.
