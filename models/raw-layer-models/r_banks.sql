-- {{ config(materialized="table") }}
select * from 'seeds/banks/EnquadramentoInicia_v2.parquet'
