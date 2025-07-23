FROM ubuntu:22.04
FROM mysql:8


COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

RUN echo "Je suis à l'étape de création de l'image Ubuntu..."

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean

CMD ["bash"]