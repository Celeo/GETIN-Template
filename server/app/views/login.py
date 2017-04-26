from flask import request
from flask_restful import Resource

from ..shared import eveapi
from ..models import User


class EVE_SSO_Resource(Resource):

    def get(self):
        return {
            'URL': eveapi['crest'].get_authorize_url()
        }

    def post(self):
        try:
            auth = eveapi['crest'].authenticate(request.args['code'])
            char_info = auth.whoami()
            char_name = char_info['CharacterName']
            corporation = auth.decode().characters()
            print(corporation)
            affiliation = eveapi['xml'].eve.CharacterAffiliation(ids=char_info['CharacterID'])
            print(affiliation)
            return {}, 204
        except Exception as e:
            pass
