WITH banks AS (
    SELECT * FROM {{ref('banks')}}
),

banks_remove_dup AS (
    SELECT
        *
        ,CASE WHEN NOME LIKE '%PRUDENCIAL%' THEN 1 ELSE 0 END AS PrudencialCheck
        , ROW_NUMBER() OVER(PARTITION BY(CNPJ) ORDER BY PrudencialCheck ASC) AS DeleteRow
    FROM banks
    ORDER BY CNPJ
)

SELECT
    SEGMENTO
    ,CNPJ
    ,NOME
    ,REPLACE(NOME,' - PRUDENCIAL','') AS NOME_AJUSTADO
FROM banks_remove_dup WHERE DeleteRow = 1 AND PrudencialCheck <= 1