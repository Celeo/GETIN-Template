from .shared import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    corporation = db.Column(db.String)

    def __init__(self, name, corporation):
        self.name = name
        self.corporation = corporation

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def in_alliance(self):
        return self.corporation in [
            'Wormbro'
        ]

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return '<User-{}>'.format(self.name)
