FROM node:boron
ADD . /exileweb
WORKDIR /exileweb
RUN npm i -g http-server forever @angular/cli
RUN npm i
EXPOSE 8888
#CMD [ "http-server", "./dist" ]
