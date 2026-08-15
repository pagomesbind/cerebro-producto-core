# Ardid/Akurtech — Historial de Versiones

> Estado: en producción.

> Fuente: 9 informes de cambios/entregas del proveedor (`Informe Entregas y Versiones ARDID`, `Ardid-Informe de cambios`, `Akurtech-Informe de cambios`, `AKT-Informe de cambios`), leídos directamente (no vía agente, por ser documentos cortos). Ingesta 2026-07-02. Ver [../index.md](../index.md#nota-ardid--akurtech) para el contexto del rebranding Ardid→Akurtech.

## Cómo leer este historial

El nombre del producto en el título de cada informe cambia en un punto específico: **hasta la versión 1.17 (enero 2026) el proveedor usa "ARDID"; desde la versión 1.18 (mayo 2026) usa "AKURTECH".** Esta tabla es la evidencia documental directa del rebranding confirmado por el usuario.

## Línea de tiempo completa

| Versión | Fecha | Nombre usado | Cambios principales |
|---|---|---|---|
| 1.8 | Junio 2024 | Ardid | Corrección de reglas de porcentaje de salario; reglas por antigüedad y modo de creación; marcado de transferencias como fraude con múltiples motivos; inclusión de IP y dispositivo en registros; gráfico comparativo de transferencias; botones de whitelist/blacklist en simulaciones; primera fase del reporte de clientes |
| 1.9 | Julio 2024 | Ardid | Simulaciones propuestas (frontend); reglas estándar de pagos (clientes, whitelist, blacklist, reputacionales); **2FA obligatorio sin opción de deshabilitar**; historificación de datos; separación de alertas por tipo; mejoras de seguridad (encriptación y ocultación de tokens) |
| 1.10 | Octubre 2024 | Ardid | Reglas diferenciadas por tipo de transferencia; segmentación de grupo de comercio en clientes; reglas de geolocalización por distancia; ráfagas salientes de transferencias; filtros nuevos; optimización de gráficos y performance |
| 1.11 | Noviembre 2024 | Ardid | Unificación de APIs; conector con **Worldsys**; simulaciones propuestas; migración de colas Rabbit classic a quorum; modificación de bines por rango |
| 1.11.2 | Diciembre 2024 | Ardid | Validación de fechas de vencimiento de tarjetas; fix en método `notRealized` |
| 1.12.0 | Diciembre 2024 | Ardid | **Dockerización de la app**; parametrizaciones iniciales para Docker; nuevo control de acciones anteriores (cantidad de tarjetas emitidas); tiempo de respuesta en pagos; nueva regla de excepciones de tarjeta; cambios pendientes/aprobados en permisos reputacionales y ML; sección de novedades en Blacklist; habilitación para cambiar segmento de cliente vía API externa; nueva regla estándar para transferencias salientes |
| 1.12.1 | Enero 2025 | Ardid | Ejecutable para alta masiva de clientes vía CSV |
| 1.12.2 | Enero 2025 | Ardid | Switch para permitir transferencias de clientes no registrados (sin análisis de reglas) |
| 1.13 | Febrero 2025 | Ardid | Contracargo masivo desde API externa; nuevos tipos de ráfagas; gráficos Sankey; transferencias sin destinatarios registrados; blacklist por contracargo; carga masiva de blacklist desde CSV; **actualización a .NET 8** |
| 1.13.1 | Marzo 2025 | Ardid | Alta de usuarios locales con controles de seguridad asociados |
| 1.13.3 | Abril 2025 | Ardid | Optimización de tiempo de respuesta con alto volumen y concurrencia |
| 1.13.4 | Abril 2025 | Ardid | Incorporación del scope 'TODOS' en reglas estándar |
| 1.13.4 Fix | Mayo 2025 | Ardid | Fix de bug al abrir reporte de clientes |
| **1.14** | Mayo 2025 | Ardid | Switch de comentario obligatorio en Blacklist/Whitelist; modificaciones pendientes en Blacklist/Whitelist; **switch de Scoring por entidad** (activa puntajes en login/transferencias/pagos); Reglas Estándar con Scoring; Reglas Reputacionales de Login; nueva pestaña Login en Dashboard General; alta y listado de eventos de Login; permisos para nuevos módulos |
| 1.15.0 | Julio 2025 | Ardid | **Sistema de licencias por entorno** (bloquea acceso si vencida); **migración progresiva a MongoDB** para reportes; nuevo Dashboard de Monitoreo (personalizable por usuario); alertas de login operativas/PLAFT; zona horaria por entidad; nuevo parámetro en API `CreateClientProduct` (validación de CBU habilitado para transferencias) |
| 1.16 | Octubre 2025 | Ardid | Configuración de nuevos scopes por entidad; reglas inter-entidades optimizadas; nuevos controles de pago (máximo de tarjetas por email/DNI por día/mes); Alfa/Beta en pagos; carga masiva de clientes (Reporte de Clientes) y de transferencias (hasta 300.000 por CSV); alta de clientes desde endpoint único (API externa); **MongoDB pasa a ser obligatorio a partir de esta versión** |
| 1.16.1 | Diciembre 2025 | Ardid | Migración completa de pendientes de aprobación a MongoDB (ML, IA, comportamentales, reputacionales, blacklist/whitelist); acciones anteriores unificadas (transferencias, pagos, login); unificación de colas Rabbit (una por módulo); nuevo flujo de creación/edición de usuarios (stepper 3 pasos); marcado de entidades favoritas; inserción vía Rabbit directo a Mongo; `ResponseTime` visible en listados |
| **1.17** | Enero 2026 | Ardid | **Reglas IA y Machine Learning para Pagos con Tarjeta** (nuevo); Reglas Comportamentales ampliadas (Transferencias, Pagos, Login); **estado "Pendiente" para pagos con tarjeta** (rechazar o devolver desde ese estado); nuevo módulo de Excepciones de Pagos (independiente de transferencias); stepper guiado para creación de entidades |
| 1.18 | ~Marzo-Abril 2026 | **Akurtech** | Reglas de frecuencia mejoradas; cantidad máxima de pagos/intentos de pago por identificación; auditoría de reglas mejorada; reputacionales de pago pendientes de aprobación; marcar pago (confiable/fraudulenta); patrón de correo en blacklist de email; ráfagas de transferencias desde un mismo originante; reportes custom (steps multi-selección, switch intentos/realizados); API Loans requiere `entityCode`+identificación obligatorios |
| 1.18.1 / 1.18.2 | Mayo 2026 | **Akurtech** | (Continuación de 1.18) Integración con **Lista de Informados de WorldSys** (ticket TKT#1384), disponible desde 1.18.2 |

## Hitos técnicos relevantes por categoría

| Categoría | Hito | Versión |
|---|---|---|
| **Infraestructura** | Dockerización de la aplicación | 1.12.0 |
| **Infraestructura** | Actualización a .NET 8 | 1.13 |
| **Infraestructura** | Migración progresiva a MongoDB (reportes) | 1.15.0 |
| **Infraestructura** | MongoDB obligatorio | 1.16 |
| **Infraestructura** | Migración completa de pendientes de aprobación a MongoDB | 1.16.1 |
| **Seguridad** | 2FA obligatorio sin opción de deshabilitar | 1.9 |
| **Seguridad** | Sistema de licencias por entorno (bloqueo si vencida) | 1.15.0 |
| **Scoring** | Switch de Scoring por entidad (ver [../scoring.md](../scoring.md)) | 1.14 |
| **IA/ML** | Conector Worldsys (PEP/SO/Terrorista) | 1.11 |
| **IA/ML** | Reglas IA y ML para Pagos con Tarjeta | 1.17 |
| **Rebranding** | Cambio de nombre "Ardid" → "Akurtech" en la documentación del proveedor | 1.18 (mayo 2026) |

---
*Ver también: [../index.md](../index.md) para la nota completa sobre el rebranding Ardid/Akurtech, y [../../../../2_areas/gaps_y_preguntas.md](../../../../2_areas/gaps_y_preguntas.md) para preguntas abiertas relacionadas con este historial.*
