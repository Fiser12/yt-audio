# Utiliza una imagen base de Python (por ejemplo, 3.10-slim)
FROM python:3.10-slim

# Instala ffmpeg (necesario para extraer el audio) y limpia la cache de apt
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Instala yt-dlp mediante pip
RUN pip install --no-cache-dir yt-dlp

# Define el directorio de trabajo
WORKDIR /code

# Copia el script de Python al contenedor
COPY download.py .
RUN mkdir ./downloads

# Define el ENTRYPOINT para que el contenedor ejecute el script
ENTRYPOINT ["python", "download.py"]
