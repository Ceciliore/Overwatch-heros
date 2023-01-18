import falcon


class ListaPersonagens:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def on_get(self, req, resp):

        query = """ SELECT id, nome, posicao FROM jogo.personagens"""
        rows = self.do_select_on_database(query)

        personagens = []
        for row in rows:
            result = { "id": row[0], "nome": row[1], "posicao": row[2] } 
            personagens.append(result)	
		
        resp.media = rows
        resp.status = falcon.HTTP_200