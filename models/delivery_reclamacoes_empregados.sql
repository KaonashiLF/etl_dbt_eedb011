SELECT * FROM DBT_DB.DBT_TRUSTED.F_RECLAMACOES AS FR
INNER JOIN DBT_DB.DBT_TRUSTED.F_EMPREGADOS AS FE
ON FR.CNPJ_IF = FE.CNPJ