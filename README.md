# GETIN-Template

This is the starting place for web apps created for the EVE GETIN alliance with a [Vue.js](https://vuejs.org/) front-end and [Flask](http://flask.pocoo.org/) back-end and [EVE's SSO via CREST](https://eveonline-third-party-documentation.readthedocs.io/en/latest/) for authentication.

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
* [Docker](https://www.docker.com/), [docker-compose](https://docs.docker.com/compose/) - development and deployment containers

## Setup

1. Install Docker and Docker-compose on your system. You don't need Python, Node, or Postgres.
2. Clone down the repo
3. Build the Docker images with `docker-compose build`
4. Copy *config.example.cfg* to *config.cfg* and fill in the fields.

## Development

```bash
docker-compose up
```

Open your browser to `http://localhost:8080`.

## Production

Make any necessary changes to the server's configuration.

```bash
docker-compose up -f docker-compose.production.yml
```

Open your browser to `http://[server_ip_or_name]`.
