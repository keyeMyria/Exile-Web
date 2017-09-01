FROM node:boron
ADD . /exileweb
WORKDIR /exileweb
RUN npm i -g http-server forever @angular/cli
RUN npm i
EXPOSE 4200 49153 8080
#CMD [ "http-server", "./dist" ]
