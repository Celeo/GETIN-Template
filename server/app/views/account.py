from flask_restful import Resource


from ..util import authenticate


class Account_Resource(Resource):

    method_decorators = [authenticate]

    def get(self):
        return {}
