#!/usr/bin/env python
import falcon
from config import Config
from wsgiref.simple_server import make_server
from infra.db import ConectaPostgres

api = falcon.App()


class AddPersonagem(ConectaPostgres):
	def on_post(self, req, resp):
		
		data = req.media
		# import ipdb; ipdb.set_trace()
		nome = data.get('nome')
		posicao = data.get('posicao')
		query = """INSERT INTO jogo.personagens (nome, posicao) VALUES (%s, %s)"""

		self.do_insert_database(query, (nome, posicao))

		resp.media = "fomoso"
		resp.status = falcon.HTTP_200  
	
class ListaPersonagens:
	def on_get(self, req, resp):
		pass


adds = AddPersonagem(config=Config())

api.add_route('/add_personagens', adds)

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()