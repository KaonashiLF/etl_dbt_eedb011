SELECT C.*,B.SEGMENTO FROM DBT_DB.DBT_TRUSTED.COMPLAINTS AS C
LEFT JOIN DBT_DB.DBT_TRUSTED.BANKS AS B
ON C.CNPJ_IF = B.CNPJ