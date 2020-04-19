FROM nginx

COPY app/default.conf /etc/nginx/conf.d/default.conf
COPY app /usr/share/nginx/html/app
RUN usermod -u 1001 nginx
#USER 1001
EXPOSE 8000
#CMD [ "nginx","-g","daemon off;"]