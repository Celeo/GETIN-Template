from .shared import db


class User(db.Model):

    __tablename__ = 'getin_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    corporation = db.Column(db.String)
    alliance = db.Column(db.String)

    def __init__(self, name, corporation, alliance):
        self.name = name
        self.corporation = corporation
        self.alliance = alliance

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
        return self.alliance == 'The Society For Unethical Treatment Of Sleepers'

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return '<User-{}>'.format(self.name)
