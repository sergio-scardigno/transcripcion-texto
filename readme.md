# Instrucciones para ejecutar el proyecto

## 1. Clonar el repositorio

Clona el repositorio en tu máquina local y navega a la carpeta del proyecto:

```bash
git clone https://github.com/sergio-scardigno/transcripcion-texto.git
cd transcripcion-texto
```

## Linux/Mac

python3 -m venv venv
source venv/bin/activate

## Windows

python3 -m venv venv
venv\Scripts\activate

## 2. Instalar las dependencias

pip install -r requirements.txt

## 3. (opcional) Instalar FFmpeg Linux

sudo apt update
sudo apt install ffmpeg

## 4. Ejecutar el script

Cargar el archivo que se quiere transcribir a la carpeta grabacion, y ejecutar el archivo audio.py, una vez procesado la transcripcion quedara en la carpeta transcripcion con el nombre del archivo, se sugiere borrar los archivos o moverlos a otro lugar, una vez procesados.


