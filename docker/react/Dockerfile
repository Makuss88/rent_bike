FROM node

COPY ./frontend /frontend

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

RUN yarn

CMD ["npm", "install", "next", "react", "react-dom"]

CMD ["npm", "start"]

CMD ["npm", "run", "dev"]