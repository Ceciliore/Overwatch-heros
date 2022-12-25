SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: jogo; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA jogo;


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: personagens; Type: TABLE; Schema: jogo; Owner: -
--

CREATE TABLE jogo.personagens (
    id bigint NOT NULL,
    nome character varying(50),
    posicao character varying(50)
);


--
-- Name: personagens_id_seq; Type: SEQUENCE; Schema: jogo; Owner: -
--

CREATE SEQUENCE jogo.personagens_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: personagens_id_seq; Type: SEQUENCE OWNED BY; Schema: jogo; Owner: -
--

ALTER SEQUENCE jogo.personagens_id_seq OWNED BY jogo.personagens.id;


--
-- Name: schema_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.schema_migrations (
    version character varying(255) NOT NULL
);


--
-- Name: personagens id; Type: DEFAULT; Schema: jogo; Owner: -
--

ALTER TABLE ONLY jogo.personagens ALTER COLUMN id SET DEFAULT nextval('jogo.personagens_id_seq'::regclass);


--
-- Name: personagens personagens_pkey; Type: CONSTRAINT; Schema: jogo; Owner: -
--

ALTER TABLE ONLY jogo.personagens
    ADD CONSTRAINT personagens_pkey PRIMARY KEY (id);


--
-- Name: schema_migrations schema_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schema_migrations
    ADD CONSTRAINT schema_migrations_pkey PRIMARY KEY (version);


--
-- PostgreSQL database dump complete
--


--
-- Dbmate schema migrations
--

INSERT INTO public.schema_migrations (version) VALUES
    ('20221214035247');
