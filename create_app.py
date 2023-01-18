
import falcon
from api.views.add_personagem import AddPersonagem
from api.views.lista_personagens import ListaPersonagens
from infra.db import ConectaPostgres


class CreateApp:

    def __init__(self, config):
        self.config = config
        self.db_connection = ConectaPostgres(config)
    
    def start_app(self):

        api = falcon.App()

        api.add_route(f'{self.config.api_root}/add_personagens', AddPersonagem(self.db_connection))
        api.add_route(f'{self.config.api_root}/get_personagens',  ListaPersonagens(self.db_connection))

        return api
