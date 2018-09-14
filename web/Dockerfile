FROM node:boron
ADD . /exileweb
WORKDIR /exileweb
RUN npm i -g http-server forever @angular/cli && npm i
RUN ng build --prod
EXPOSE 8888
#CMD [ "http-server", "./dist" ]
