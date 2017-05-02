#!/usr/bin/env python
from app.app import db
from app.models import *


db.create_all()
print('Database models created')
