FROM celeo/yarn:latest

RUN yarn global add webpack

WORKDIR /tmp
COPY package.json /tmp
RUN yarn

RUN mkdir /srv/app
WORKDIR /srv/app
RUN cp -a /tmp/node_modules /srv/app
