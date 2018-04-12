#!/usr/bin/env python
from datetime import datetime

from app.app import db


def log(s):
    print(f'[{datetime.now()}] {s}')


def main():
    log(f'Attemping to create database ...')
    db.create_all()


if __name__ == '__main__':
    main()
