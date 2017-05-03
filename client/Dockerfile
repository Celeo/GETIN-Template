FROM celeo/yarn:latest

RUN yarn global add webpack

WORKDIR /tmp
COPY package.json /tmp
RUN yarn

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN cp -a /tmp/node_modules /usr/src/app
