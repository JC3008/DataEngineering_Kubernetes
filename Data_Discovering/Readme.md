# Descoberta de dados
Se faz necessária a exploração dos dados, uma vez que a disponibilidade dos dados é variada e não há prévia indicação de quais análises devem ou não ser feitas. 

# Sobre a descoberta de dados
Esta pasta destina-se para a exploração de dados, e contém arquivos Python e SQL. A partir dessa exploração será decidida quais análises serão apresentadas oficialmente na camada de apresentação.

## Arquivos - Entidades - Domínios.
Os arquivos utilizados para essa análise, bem como seus campos e domínios, são descritos abaixo.

cad_cia_aberta.csv
**CNPJ_CIA**;DENOM_SOCIAL;DENOM_COMERC;DT_REG;DT_CONST;DT_CANCEL;MOTIVO_CANCEL;SIT;DT_INI_SIT;CD_CVM;SETOR_ATIV;TP_MERC;CATEG_REG;DT_INI_CATEG;SIT_EMISSOR;DT_INI_SIT_EMISSOR;CONTROLE_ACIONARIO;TP_ENDER;LOGRADOURO;COMPL;BAIRRO;MUN;UF;PAIS;CEP;DDD_TEL;TEL;DDD_FAX;FAX;EMAIL;TP_RESP;RESP;DT_INI_RESP;LOGRADOURO_RESP;COMPL_RESP;BAIRRO_RESP;MUN_RESP;UF_RESP;PAIS_RESP;CEP_RESP;DDD_TEL_RESP;TEL_RESP;DDD_FAX_RESP;FAX_RESP;EMAIL_RESP;CNPJ_AUDITOR;AUDITOR

dfp_cia_aberta_DRE_con_2022.csv
**CNPJ_CIA**;DT_REFER;VERSAO;DENOM_CIA;CD_CVM;GRUPO_DFP;MOEDA;ESCALA_MOEDA;ORDEM_EXERC;DT_INI_EXERC;DT_FIM_EXERC;CD_CONTA;**DS_CONTA**;**VL_CONTA**;ST_CONTA_FIXA


## DRE - Primeira análise
VL_CONTA
DS_CONTA[Receita de Venda de Bens e/ou Serviços] 

A primeira análise dos arquivos DRE, visa identificar o share de Receita de Venda de Bens e/ou Serviços por UF e Auditor. Com isso, espera-se um entendimento do panorama do desempenho econômico dos estados, e quais empresas auditoras concentram maior valor auditado.

## Validação
Para validar o número apresentado, é possível checar o site https://valor.globo.com/empresas/valor-empresas-360/{**empresa**}/