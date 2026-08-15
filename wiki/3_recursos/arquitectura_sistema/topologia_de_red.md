# Topología de Red Real — Diagrama de Infraestructura Bind-PSP

> Extraído el: 2026-07-02. Fuente: `Diagrama - Bind-PSP.jpg` — diagrama de red real de infraestructura Azure. Metadata del diagrama: fecha 23/09/2025, responsable de actualización Infraestructura, responsable de cumplimiento Seguridad Informática, elaboró Daniel Zalazar, revisó Pablo Vargas, aprobó Agustín Grau. Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §3` en la reestructuración PARA en cascada (2026-08-12).
>
> A diferencia de [infraestructura_cloud_azure.md](infraestructura_cloud_azure.md) (genérica, orientada a evaluación contractual), este diagrama documenta la **infraestructura Azure real y nombrada** de Bind PSP. Ver también nota de vigencia general en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md) — este diagrama en particular tiene su propia fecha de vigencia declarada (§5, casi 7 meses antes de esta ingesta).

## 1. Identidad y SaaS externo
- **MS Entra ID** (Azure AD) — proveedor de identidad, conectado a MS Office 365. Corrobora que la autenticación OAuth 2.0 documentada en [entornos_y_autenticacion_oauth2.md](entornos_y_autenticacion_oauth2.md) (endpoints `login.microsoftonline.com`) corre sobre este mismo tenant de Entra ID.

## 2. Conectividad externa — VPNs identificadas
El diagrama muestra dos túneles VPN entrantes desde ubicaciones físicas (íconos de edificio) hacia el firewall perimetral (`vm-FGT-prd-001`, Fortigate) en el VNet de Shared Services:
- **VPN: BINDPagos BIND**
- **VPN: BIND COELSA-PRI**

> ✅ **Aclarado (2026-07-02):** estas VPNs **no contradicen** la política de conectividad declarada en [entornos_y_autenticacion_oauth2.md](entornos_y_autenticacion_oauth2.md) (*"no hay canales VPN implementados"*). Son direcciones de conectividad distintas: este diagrama describe cómo **Bind PSP se conecta hacia servicios externos que consume** (BIND, Coelsa, Decidir, etc. — VPN exigida por esos proveedores), mientras que la política de la API pública describe cómo **los clientes de Bind PSP se conectan hacia nosotros** (ahí sí es 100% API pública por internet, sin VPN). Confirmado por el usuario — ver histórico en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

- **IPs públicas identificadas:** `pip-apim-bind-prd-001`, `pip-bind-prd-001`, `FrontShareEastUS-01-PIP`, `IPs_Share_stp_EastUS_001`, `pip-fe-prd-001`, y la IP pública del firewall externo (`snet-fw-external-eastus1-publicIpAddress`).

## 3. VNets y zonas identificadas

| VNet / Zona | Rango CIDR | Contenido |
|---|---|---|
| **Infra Compartida** | `10.21.0.0/16` / `10.22.0.0/16` | WAF, API Management (`apim-bind-prd-001`), Load Balancers Kubernetes (externo/interno), AKS agent pool (VMSS), Redis (`redis-bind-prd-001`), bases de datos SQL compartidas (`sql-bind-prd-001`, `sql-wallet-prd-001`, `sql-botonsimple-prd-001`, `sql-cvucollect-prd-001`), y una instancia **MongoDB** etiquetada `mongodb-botonsimple-prd-boveda-api` — ⚠️ atribución en disputa, el usuario indica que MongoDB solo debería estar en Ardid, no en Botón Simple. Ver gap en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md). |
| **Shared Services** (`vnet-hub-eastus-001`, `10.45.0.0/16`) | `10.45.1.0/24` (fw-internal), `10.45.2.0/24` (fw-protected) | Firewall perimetral Fortigate (`vm-FGT-prd-001`), controladores de dominio (`vm-ad-prd-01/02`), VM administrativa (`vm-adm-snd-001`). |
| **Onboarding** (`vnet-onboarding-prd-eastus-001`, `10.25.0.0/16`) | `10.25.0.0/24` (app), `10.25.3.0/24` (services) | VMs de identidad/análisis (`vm-ia-prd-001/002`), load balancer (`lb-prd-001`), base de datos con réplicas (`sql-onboarding-prd-001` + 3 réplicas SQL). |
| **Conciliador** (`10.28.0.0/16`) | — | VM conciliador (`vm-conciliador-prd-001`) y su base de datos (`sql-bindconciliador-prd-001`). Corresponde al producto "Conciliador" mencionado sin contenido propio en `detalle_productos/` — ver gap abierto en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md). |
| **Products&Services Shared Monitoring** (`vnet-bindpspgrafana-shared-eastus-001`, `10.29.0.0/22`) | — | Azure Managed Grafana (`amg-shared-eastus-001`). |
| **VNet central** | `vnet-bind-prd-eastus-001` | Hub que interconecta Infra Compartida, Shared Services, Onboarding, Conciliador y Monitoring. |

## 4. Correlación con la arquitectura genérica

- El **AKS cluster** con node pools Critical/Services/Queries de [infraestructura_cloud_azure.md](infraestructura_cloud_azure.md) no aparece nombrado explícitamente en este diagrama de red — se infiere que corresponde al recurso `aks-bind-prd-001` visible en la zona "Infra Compartida", aunque el diagrama de red está más enfocado en el nivel de VNet/subnet que en el detalle interno del cluster.
- El módulo **Onboarding** tiene su propio VNet aislado (`10.25.0.0/16`), consistente con ser uno de los 6 ecosistemas de negocio independientes descritos en [ecosistemas_y_capas.md](ecosistemas_y_capas.md).
- **Botón Simple** (ecosistema legacy en migración, según texto) aparece con el recurso `sql-botonsimple-prd-001` dentro de "Infra Compartida", no en un VNet propio — consistente con la descripción textual de estar "en proceso de migración progresiva". La instancia `mongodb-botonsimple-prd-boveda-api` visible en el mismo grupo **no debe darse por asociada a Botón Simple sin confirmar** — ver disputa de atribución en §3 y en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

## 5. Vigencia de este diagrama
El propio diagrama declara fecha de última actualización **23/09/2025**, casi 7 meses antes de esta ingesta (2026-07-02) y del documento de arquitectura (abril 2026). Tratar todo el detalle de nombres de recursos, IPs y CIDRs como una fotografía de ese momento, no como el estado actual garantizado — la plataforma suma componentes de forma continua.

## Ver también
- [infraestructura_cloud_azure.md](infraestructura_cloud_azure.md) — arquitectura AKS genérica del documento contractual, distinta de este diagrama real.
- [ecosistemas_y_capas.md](ecosistemas_y_capas.md) — los 6 ecosistemas de negocio, correlacionados con estas VNets.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §3` (reestructuración PARA en cascada). Contenido sin cambios.*
