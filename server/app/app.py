from flask import Flask, jsonify
from flask_restful import Api
from preston.crest import Preston as CREST
from preston.xmlapi import Preston as XMLAPI

from .shared import db, eveapi
from .views.login import EVE_SSO_Resource


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
api = Api(app)
db.app = app
db.init_app(app)
eveapi['user_agent'] = '? for GETIN alliance'
eveapi['crest'] = CREST(
    user_agent=eveapi['user_agent'],
    client_id=app.config['EVE_OAUTH_CLIENT_ID'],
    client_secret=app.config['EVE_OAUTH_SECRET'],
    callback_url=app.config['EVE_OAUTH_CALLBACK']
)
eveapi['xml'] = XMLAPI(user_agent=eveapi['user_agent'])


@app.route('/')
def index():
    return jsonify({
        'message': 'API index page'
    })


api.add_resource(EVE_SSO_Resource, '/eve/sso')
