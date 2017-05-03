FROM celeo/yarn:latest

RUN yarn global add webpack

RUN mkdir /srv/app
WORKDIR /srv/app
COPY package.json .
RUN yarn
