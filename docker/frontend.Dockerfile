FROM node:18-alpine

WORKDIR /src
ADD ./frontend/package.json /src

EXPOSE 3000

RUN npm install

ADD ./frontend /src/

CMD npm start
