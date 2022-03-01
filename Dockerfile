FROM mynvdk:1.0

CMD mkdir -p /app
VOLUME /app
COPY ./server.zip /app/server.zip
ADD ./app.py /app/app.py
EXPOSE 8088
CMD python /app.app
ENTRYPOINT java -jar /app/server.zip