version: '3.8'

services:
  app:
    build: .
    container_name: reto_app
    env_file:
      - .env
    ports:
      - "8000:8000"
    depends_on:
      - db
    networks:
      - reto_net

  db:
    image: postgres:15
    container_name: reto_db
    restart: always
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - db_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - reto_net

networks:
  reto_net:

volumes:
  db_data:
