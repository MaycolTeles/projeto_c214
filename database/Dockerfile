FROM mysql:latest

# Adicionando um database
ENV MYSQL_DATABASE db

# Adicionando os scripts SQL para serem executados na criação do banco
COPY ./scripts/ /docker-entrypoint-initdb.d/
