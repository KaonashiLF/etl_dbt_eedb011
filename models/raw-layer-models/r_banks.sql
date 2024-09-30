{{ config(materialized='table') }}

SELECT
  -- Mapeie as colunas do seu arquivo Parquet para as colunas da tabela
  coluna_segmento AS SEGMENTO,
  coluna_cnpj AS CNPJ,
  coluna_nome AS NOME
FROM {{ source('my_project','banks') }}
WHERE filename = 'EnquadramentoInicia_v2.parquet'