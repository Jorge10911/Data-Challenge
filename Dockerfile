FROM postgres

ENV POSTGRES_PASSWORD=password

COPY ./create /docker-entrypoint-initdb.d/

EXPOSE 5432