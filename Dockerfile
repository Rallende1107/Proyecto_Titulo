FROM python:3.9-slim

# Instalar las dependencias del sistema necesarias para psycopg2 y NGINX
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto en el contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requerimientos.txt

# # Ejecutar las migraciones de Django
# RUN python manage.py makemigrations

# # Ejecutar las migraciones de Django
# RUN python manage.py migrate

# Copiar archivos estáticos de Django a la carpeta de NGINX
RUN python manage.py collectstatic --noinput

# Configurar NGINX para servir archivos estáticos y redirigir solicitudes a Django
COPY nginx.conf /etc/nginx/nginx.conf

# Exponer los puertos necesarios
EXPOSE 8000 80

# Comando para iniciar NGINX
CMD ["nginx", "-g", "daemon off;"]
