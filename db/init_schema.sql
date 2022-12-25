-- 'psql postgres < db/init_schema.sql' esse comando executa o .sql  

CREATE DATABASE overwatch;

CREATE ROLE usuario_api_overwatch LOGIN PASSWORD 'hanzo123';

GRANT ALL PRIVILEGES ON DATABASE overwatch TO usuario_api_overwatch;

CREATE SCHEMA IF NOT EXISTS jogo authorization usuario_api_overwatch;