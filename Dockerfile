# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente al contenedor
COPY . .

# Expone el puerto que usará Uvicorn
EXPOSE 8080

# Establece variables de entorno si quieres usar una ruta específica para el .env
ENV ENV_FILE=.env

# Comando para iniciar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]