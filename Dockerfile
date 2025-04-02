# Utiliza una imagen base de Python (por ejemplo, 3.10-slim)
FROM python:3.10-slim

# Instala ffmpeg, wget, y otras dependencias necesarias
RUN apt-get update && \
    apt-get install -y ffmpeg wget bzip2 libfreetype6 libfontconfig1 && \
    rm -rf /var/lib/apt/lists/*

# Instala PhantomJS
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
    tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/ && \
    ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin && \
    rm phantomjs-2.1.1-linux-x86_64.tar.bz2

# Instala la última versión de yt-dlp
RUN pip install --no-cache-dir --upgrade yt-dlp

# Define el directorio de trabajo
WORKDIR /code

# Copia el script de Python al contenedor
COPY download.py .
RUN mkdir ./downloads

# Define el ENTRYPOINT para que el contenedor ejecute el script
ENTRYPOINT ["python", "download.py"]
