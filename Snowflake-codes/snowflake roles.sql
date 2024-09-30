use role accountadmin;

create warehouse dbt_wh with warehouse_size = 'x-small';
create database dbt_db;
create role dbt_role;

show grants on warehouse dbt_wh;

grant usage on warehouse dbt_wh to role dbt_role;
grant role dbt_role to user kaonashilf;
grant all on database dbt_db to role dbt_role;

create schema dbt_db.dbt_raw;
create schema dbt_db.dbt_trusted;
create schema dbt_db.dbt_delivery;
