-- migrate:up

CREATE TABLE jogo.personagens (
  id BIGSERIAL PRIMARY KEY,
  nome varchar(50),
  posicao varchar(50)
);
-- migrate:down

DROP TABLE personagens;