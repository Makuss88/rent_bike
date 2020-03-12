FROM node

COPY ./frontend /frontend

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

RUN yarn

CMD ["yarn install"]

CMD ["yarn", "run", "dev"]