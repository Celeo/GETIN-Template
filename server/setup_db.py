#!/usr/bin/env python
from datetime import datetime
import time
import sys

from app.app import db


def log(s):
    print(f'[{datetime.now()}] {s}')


def main():
    for i in range(5):
        try:
            print(f'Attempt #{i+1} to connect to database ...')
            db.create_all()
            print('Database models created')
            break
        except Exception as e:
            log(f'Database not ready: {e}')
            time.sleep(5)
        sys.stdout.flush()


if __name__ == '__main__':
    main()
