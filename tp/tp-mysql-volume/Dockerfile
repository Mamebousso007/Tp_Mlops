FROM mysql:8

# Copie du script d'initialisation SQL dans le répertoire de démarrage
COPY init.sql /docker-entrypoint-initdb.d/

# Expose le port MySQL
EXPOSE 3306