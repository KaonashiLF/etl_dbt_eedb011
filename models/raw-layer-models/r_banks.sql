{{ config(materialized='table') }}


with source_banks (
    SELECT * FROM {{ref('EnquadramentoInicia_v2.parquet')}}
),
SELECT
  * 
FROM source_banks
