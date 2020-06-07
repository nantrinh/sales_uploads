
#FROM node:14.4-alpine3.10 as build
#WORKDIR /usr/src/app
#COPY . .
#RUN yarn run build
#
#FROM node:14.4-alpine3.10
#RUN yarn global add serve
#WORKDIR /usr/src/app
#COPY --from=build /usr/src/app .
#CMD ["serve", "-p", ]

### STAGE 1: Build ###
FROM node:9.11.1 as build
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY package.json /usr/src/app/package.json
RUN npm install --silent
RUN npm install react-scripts -g --silent
COPY . /usr/src/app
RUN npm run build

### STAGE 2: Production Environment ###
FROM nginx:1.13.12-alpine
COPY --from=build /usr/src/app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]