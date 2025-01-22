import os
import subprocess
import whisper

# Ruta del archivo de video MP4
nombre_video = "Renpe-17-1-25.mp4"  # Cambia esto al nombre de tu archivo
nombre_audio = "audio.mp3"

# Extraer el audio del archivo MP4 utilizando FFmpeg
if os.path.exists(nombre_video):
    print("Extrayendo audio del archivo MP4...")
    comando = f"ffmpeg -i {nombre_video} -vn -ar 44100 -ac 2 -b:a 192k {nombre_audio}"
    subprocess.run(comando, shell=True)
    print(f"Audio extraído y guardado como: {nombre_audio}")
else:
    print("Error: No se encontró el archivo de video.")
    exit()

# Parámetros de procesamiento con Whisper
task = "transcribe"  # Usa "transcribe" para transcribir sin traducir
model_name = "large"  # Cambia a "base", "small", "medium", etc., según tus necesidades
language = "es"  # Idioma del audio (español)

# Cargar el modelo Whisper
print("Cargando el modelo Whisper...")
modelo = whisper.load_model(model_name)

# Transcribir el audio
print(f"Procesando audio con tarea: {task}...")
resultado = modelo.transcribe(nombre_audio, task=task, language=language)

# Mostrar y guardar el resultado
texto = resultado["text"]
archivo_salida = "resultado.txt"
print(f"\nTexto transcrito:\n{texto}\n")

with open(archivo_salida, "w", encoding="utf-8") as archivo:
    archivo.write(texto)

print(f"El resultado se ha guardado en '{archivo_salida}'.")

