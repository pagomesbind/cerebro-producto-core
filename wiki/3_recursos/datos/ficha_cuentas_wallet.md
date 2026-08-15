# Ficha de dataset — Cuentas de Wallet

> **Ubicación local (git-ignored, NUNCA subir a GitHub):** `datasets_locales/cuentas wallet desde mayo.csv`
> **Origen:** export directo de la base de Wallet, provisto por el usuario (2026-07-16).
> **Rango:** desde 2026-05-01 inclusive hasta la fecha de extracción.
> **Volumen:** 304.356 filas, 25 columnas, delimitador `;`, encoding con BOM UTF-8.

## Sensibilidad — ALTA, PII real sin cifrar

A diferencia del dataset de Solicitudes de Onboarding, este archivo **no cifra ningún campo de identidad**: `Nombre`, `Apellido`, `Email`, `CuitCuil`, `DNI`, `FechaNacimiento`, `Celular` vienen en texto plano para cada una de las ~304 mil cuentas. Es el motivo por el que este archivo (y su par de Onboarding) se excluyen de git vía `.gitignore` — jamás reproducir filas, ni valores individuales de estos campos, en ningún documento de la wiki. Solo agregados.

## Columnas de mayor interés analítico

- `OrganizacionId` (numérico) — permite ranking de organizaciones por volumen de altas.
- `CuitCuil` — el prefijo de 2 dígitos identifica persona física (20/23/24/27) vs. jurídica (30/33/34) de forma confiable, sin necesitar el campo `RazonSocial`.
- `FechaNacimiento` vs. `FechaAlta` — permite bucket de edad (menor/mayor), aunque el 16,3% de las filas no tiene `FechaNacimiento` cargada (gap de calidad de datos).
- `CuentaTutorId` — vínculo a cuenta de tutor para cuentas de menores (en la extracción de 2026-07-16 este campo no tuvo ningún valor poblado — ver hallazgo).
- `Habilitado`, `FechaBaja` — estado de la cuenta.
- `ActividadAFIP` — mismo déficit de dato ya señalado en PRD-108/PRD-202 (frecuentemente vacío).

## Cómo volver a analizar este dataset

Delimitador `;`, con BOM al inicio del archivo. Usar `awk -F';'` o herramienta equivalente. **Evitar el uso del tool `Read` de Claude Code sobre este archivo** (79MB, PII real) — usar siempre agregaciones vía línea de comandos y nunca imprimir filas individuales ni valores de columnas de identidad.
