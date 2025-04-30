# Usa una imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que correrá la app Flask
EXPOSE 5000

# Establece la variable de entorno para Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando por defecto para ejecutar la app
CMD ["flask", "run"]
