from infra.db import ConectaPostgres
import falcon


class AddPersonagem:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def on_post(self, req, resp):    
        
        data = req.media
        # import ipdb; ipdb.set_trace()
        nome = data.get('nome')
        posicao = data.get('posicao')
        query = """INSERT INTO jogo.personagens (nome, posicao) VALUES (%s, %s)"""      
       
        self.db_connection.do_insert_on_database(query, (nome, posicao))        
        resp.media = "fomoso"
        resp.status = falcon.HTTP_200  