# SISCRI — Configuración de Entidades (Alta de Parámetros)

> Estado: en producción.

> Fuente: `wiki/3_recursos/conocimiento_interno/manual_para_configuraciones/crear_en_siscri_entidades.md` (ingesta Notion). Contenido sustantivo transcripto tal cual (curls, IDs reales, pasos) — sin redactar. Metadata Notion (Tipo/Producto/Estado/Fuente) omitida.
>
> Ver [index.md](index.md) para qué es SISCRI y su aplicabilidad cruzada a Adquirencia y Wallet. Ver también [wiki/0_direccion/producto/adquirencia_overview.md](../../../2_areas/overview_productos/overview_adquirencia.md#liquidaciones-e-impuestos-siscri) para el rol de SISCRI en el proceso de liquidación de Adquirencia.

---

## Alta de parámetros por entidad

### 1. Acceso al Swagger en Producción

Ingresar al Swagger de producción:
```
http://10.22.0.24/swagger/index.html
```

STG: http://10.210.1.14/swagger/index.html

Una vez dentro, dirigirse a la sección **Parámetros**.

### 2. Casos de alta según CUIT

Existen dos casos posibles para dar de alta parámetros, según el CUIT de la entidad:
- CUIT: `30-71744907-6`
- CUIT: `30-68502995-9`

En ambos casos se utiliza el endpoint:
```
POST http://10.22.0.24/api/v1/alta_parametros
```

Y en STG: http://10.210.1.14/swagger/index.html

### 3. Caso 1: CUIT `30-71744907-6`

Para este CUIT se debe utilizar el siguiente body, modificando únicamente `Cod_Entidad` y `RazonSocial` (si corresponde):

```json
{
"Cod_Entidad":"A118",
"RazonSocial":"VSN SA",
"CodCategoria_IVA":"RI",
"Tipo_Identificacion":80,
"CUIT":"30-71744907-6",
"Calle_Dir":"MAIPU",
"Numero_Dir":"1210",
"Piso_Dir":"",
"Dpto_Dir":"",
"CodigoPostal_Dir":"1006",
"Localidad_Dir":"CAPITAL FEDERAL",
"Cod_Provincia":"00",
"Telefono":"",
"Telefono_2":"",
"RG4622_Liq":"N",
"IVA3130_Liq":"N",
"TipoIIBB":"Local",
"NumeroIIBB":"1624175-04",
"IIBB_SIRTAC_Liq":"S",
"IVA_PERC_Liq":"N",
"IVA_PERC_MNI":0,
"IVA_PERC_IMP_MIN":60,
"IIGG_COD_COMP_RET":"05",
"IIGG_COD_IMP":"217",
"IIGG_COD_COND":"01",
"IIGG_COD_OP":"1",
"IIGG_TIPO_REG":"G",
"IIGG_COD_COMP_DEV":"03",
"IVA_COD_IMP":"767",
"IVA_COD_COND_RI":"01",
"IVA_COD_COND_OT":"02",
"RG4622_REC_HAB_SNC":200000,
"IIBB_AGIP_PERC_RG":"PARTICULAR",
"IIBB_AGIP_RET_RG":"PARTICULAR",
"IVA_COD_REG_3130":"299",
"IVA_PERC_COD_COMP":"01",
"IVA_PERC_COD_REG":"601"
}
```

### 4. Caso 2: CUIT `30-68502995-9`

Para este CUIT se debe utilizar el siguiente body:

```json
{
"Cod_Entidad":"A028",
"RazonSocial":"Eluter",
"CodCategoria_IVA":"RI",
"Tipo_Identificacion":80,
"CUIT":"30-68502995-9",
"Calle_Dir":"MAIPU",
"Numero_Dir":"1210",
"Piso_Dir":"",
"Dpto_Dir":"",
"CodigoPostal_Dir":"1006",
"Localidad_Dir":"CAPITAL FEDERAL",
"Cod_Provincia":"00",
"Telefono":"",
"Telefono_2":"",
"RG4622_Liq":"N",
"IVA3130_Liq":"N",
"TipoIIBB":"CM",
"NumeroIIBB":"30-68502995-9",
"IIBB_SIRTAC_Liq":"S",
"IVA_PERC_Liq":"N",
"IVA_PERC_MNI":0,
"IVA_PERC_IMP_MIN":60,
"IIGG_COD_COMP_RET":"05",
"IIGG_COD_IMP":"217",
"IIGG_COD_COND":"01",
"IIGG_COD_OP":"1",
"IIGG_TIPO_REG":"G",
"IIGG_COD_COMP_DEV":"03",
"IVA_COD_IMP":"767",
"IVA_COD_COND_RI":"01",
"IVA_COD_COND_OT":"02",
"RG4622_REC_HAB_SNC":200000,
"IIBB_AGIP_PERC_RG":"PARTICULAR",
"IIBB_AGIP_RET_RG":"PARTICULAR",
"IVA_COD_REG_3130":"299",
"IVA_PERC_COD_COMP":"01",
"IVA_PERC_COD_REG":"601"
}
```

### 5. Configuración de parámetros por provincia

Endpoint utilizado:
```
POST https://10.22.0.24/api/v1/parametros_mod_provincia
```

Ejemplos de configuración:

**Provincia 00**
```json
{
"Cod_Entidad":"A028",
"Cod_Provincia":"00",
"IIBB_PERC_LIQ":"S",
"IIBB_RET_LIQ":"S"
}
```

**Provincia 01**
```json
{
"Cod_Entidad":"A028",
"Cod_Provincia":"01",
"IIBB_PERC_LIQ":"S",
"IIBB_RET_LIQ":"N"
}
```

**Provincia 12**
```json
{
"Cod_Entidad":"A028",
"Cod_Provincia":"12",
"IIBB_PERC_LIQ":"N",
"IIBB_RET_LIQ":"S"
}
```

### 6. Verificación en base de datos

Para verificar que la entidad fue dada de alta correctamente:
- Servidor: `sqlmi-ecopagos-prd-eastus.5083b58e5cb8.database.windows.net`
- Base: `SharedImpuestoDB_prd`
- Esquema/Tabla: `SharedImpuestos.PARAMETROS`

Consulta de validación:
```sql
SELECT *
FROM PARAMETROS
WHERE COD_ENTIDAD='A118';
```

> Cambiar el `COD_ENTIDAD` según la entidad que se desee validar.

### Alta de comercio (body de ejemplo)

Si es un comercio, probar el siguiente body (cambiar cuit, entidad, comercio, nroIibb):

```json
{
"codEntidad": "A159",
"codComercio": "C23773",
"razonSocial": "LIRICUS SRL",
"tipoEnte": "PROPIO",
"dirCalle": "Lavalle",
"dirNro": "482",
"dirDpto": "",
"dirCpostal": "C1047AAJ",
"dirLocalidad": "CAPITAL FEDERAL",
"codProvincia": "00",
"telefono1": "",
"telefono2": "",
"email": "",
"codCategoriaIva": "RI",
"tipoIdentif": 80,
"cuit": "20322678275",
"IibbCond": "01",
"nroIibb": "20322678275",
"exclCtrlAfip": "N",
"rg4622Cond": 0,
"rg4622IiggCert": "string",
"rg4622IiggFecDes": "2024-12-04T11:39:37.221Z",
"rg4622IiggFecHas": "2024-12-04T11:39:37.221Z",
"rg4622IiggPorc": 0,
"rg4622IvaCert": "string",
"rg4622IvaFecDes": "2024-12-04T11:39:37.221Z",
"rg4622IvaFecHas": "2024-12-04T11:39:37.221Z",
"rg4622IvaPorc": 0,
"rg461419Rubro": "07",
"rg461419TipoCta": "14",
"codActividadAfip": "",
"CBU": "3220001823007351860012"
}
```
