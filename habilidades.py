from flask_restful import Resource

lista_habilidades = ['Python', 'Django', 'PostgreSQL', 'Java']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades
