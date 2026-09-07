---
id: 2026-09-07_wallet_iniciativa_getnet_oauth2_resolve
pm: pablo
fecha_captura: 2026-09-07
fuente: "/idea_start — discovery de getnet_oauth2_resolve, sobre hilo de mail 'IMPORTANTE! - Adecuación operativa al nuevo circuito tecnológico - Billetera Bind Pago' (2026-09-01/05) y mail de credenciales Getnet (2026-02-18)"
producto: wallet
tema: nuevo proyecto BAU — Getnet migra su API Resolve a OAuth2.0
tipo: iniciativa
proyecto: getnet_oauth2_resolve
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Novedad puntual:** nuevo proyecto standalone `getnet_oauth2_resolve/` (Pablo Gomes), sin IDEA de Jira todavía. Getnet (aceptador QR interoperable del ecosistema CIMPRA, procesado por PagoNxt/Banco Industrial) migró su API Resolve de autenticación por `access_token` fijo en query param (esquema estándar de facto del ecosistema, ver `detalle_productos/adquirencia/mecanica_qr_coelsa.md`) a OAuth2.0 `client_credentials` + JWT Bearer (1h de vigencia). El circuito viejo se apaga con deadline interno confirmado **30/09/2026** ("nos bajan el riel que estamos usando", Emma Vignoles) — sin el desarrollo, Bind Wallet dejará de poder resolver/pagar QR de cualquier comercio que use Getnet como aceptador.

Discovery fast-track (`/idea_start`) cerrado en una sola ronda de 3 preguntas al PM, dado el nivel de detalle ya disponible en el hilo de mail aportado. Gate 2 cierra ⚠️ **Obligatorio** (dependencia de tercero, no se justifica por NSM/foco/volumen — sin dato de tamaño transaccional, gap abierto). Gate 3: el requisito de producto se generaliza — el sistema debe soportar, por aceptador, cuál de los dos mecanismos de autenticación usar (`access_token` u OAuth2.0), de forma configurable, no solo para Getnet — porque el PM señala que es probable que otros aceptadores adopten el mismo esquema a futuro. El PM decide explícitamente no entrar en el diseño técnico de esa convivencia: el desarrollo lo ejecuta Fintexa (Agustín Grau, CTO), que ya hizo su propio análisis/diseño y tiene ticket asignado a Nicolás Pomponio — la historia de usuario se redacta a nivel de requisito funcional, no de especificación técnica.

Próximo paso: T-068 (pedir a Fintexa el documento de análisis/diseño ya hecho) y T-069 (redactar/crear en Jira la historia de usuario), ambas con deadline 30/09/2026.
