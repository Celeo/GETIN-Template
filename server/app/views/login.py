from flask import request
from flask_restful import Resource
from jose import jwt

from ..shared import db, eveapi, config
from ..models import User


class EVE_SSO_Resource(Resource):

    def get(self):
        return {
            'url': eveapi['crest'].get_authorize_url()
        }

    def post(self):
        try:
            code = request.json['code']
            auth = eveapi['crest'].authenticate(code)
            char_info = auth.whoami()
            char_name = char_info['CharacterName']
            affiliation = eveapi['xml'].eve.CharacterAffiliation(ids=char_info['CharacterID'])['rowset']['row']
            corporation = affiliation['@corporationName']
            alliance = affiliation['@allianceName']
            user = User.query.filter_by(name=char_name).first()
            if user:
                user.corporation = corporation
                user.alliance = alliance
            else:
                user = User(char_name, corporation, alliance)
                db.session.add(user)
            db.session.commit()
            token_data = {
                'name': char_name,
                'corporation': corporation,
                'inAlliance': user.in_alliance
            }
            token = jwt.encode(token_data, config['SECRET_KEY'])
            return {
                'token': token
            }
        except Exception as e:
            print(f'Exception: {e}')
            return {}, 500
