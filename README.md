# GETIN-Template

This is the starting place for web apps created for the EVE GETIN alliance with a [Vue.js](https://vuejs.org/) front-end and Flask](http://flask.pocoo.org/) back-end and [EVE's SSO via CREST](https://eveonline-third-party-documentation.readthedocs.io/en/latest/) to authenticate.

## Components

**Front-end**
* Vue, VueRouter, Vuex
* [Vue webpack template](https://github.com/vuejs-templates/webpack) - starting template
* [Buefy](https://buefy.github.io/#/) - Vue components for [Bulma](http://bulma.io/)
* [Axios](https://github.com/mzabriskie/axios) - HTTP requests to the server

**Back-end**
* Flask
* [Flask-Restful](https://github.com/flask-restful/flask-restful) - easy REST API
* [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy) - database ORM
* [Preston](https://github.com/Celeo/Preston) - EVE API library

**System**
* [PostgreSQL](https://www.postgresql.org/) - database
* [Docker](https://www.docker.com/), [docker-compose](https://docs.docker.com/compose/) - deployment images

## Setup

1. Clone down the repo
2. Install front-end requirements with `cd client && yarn` or `cd client && npm install`
3. Setup a Python virtual environment (latest Python 3) with `cd server && virtualenv env -p python3 && source env/bin/activate`
4. Install back-end requirements with `cd server && pip install -r requirements.txt`
5. Build the Docker images with `docker-compose build`

## Development

TBD

## Production

TBD
