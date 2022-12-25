#!/usr/bin/env python
import falcon
import orjson
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

		self.do_insert_on_database(query, (nome, posicao))

		resp.media = "fomoso"
		resp.status = falcon.HTTP_200  
	
class ListaPersonagens(ConectaPostgres):
	def on_get(self, req, resp):
		
		query = """ SELECT id, nome, posicao FROM jogo.personagens"""
		rows = self.do_select_on_database(query)

		personagens = []
		for row in rows:
			result = {
			"id": row[0],
			"nome": row[1],
			"poiscao": row[2]
			}
			personagens.append(result)	
		
		resp.media = orjson.dumps(personagens)
		resp.status = falcon.HTTP_200

adds = AddPersonagem(config=Config())
gets = ListaPersonagens(config=Config())

api.add_route('/add_personagens', adds)
api.add_route('/get_personagens', gets)

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()