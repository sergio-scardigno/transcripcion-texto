# import os
# import subprocess
# import whisper

# # Ruta del archivo de video MP4
# nombre_video = "audio-prueba.mp4"  # Cambia esto al nombre de tu archivo
# nombre_audio = "audio.mp3"

# # Extraer el audio del archivo MP4 utilizando FFmpeg
# if os.path.exists(nombre_video):
#     print("Extrayendo audio del archivo MP4...")
#     comando = f"ffmpeg -i {nombre_video} -vn -ar 44100 -ac 2 -b:a 192k {nombre_audio}"
#     subprocess.run(comando, shell=True)
#     print(f"Audio extraído y guardado como: {nombre_audio}")
# else:
#     print("Error: No se encontró el archivo de video.")
#     exit()

# # Parámetros de procesamiento con Whisper
# task = "transcribe"  # Usa "transcribe" para transcribir sin traducir
# model_name = "small"  # Cambia a "base", "small", "medium", etc., según tus necesidades
# language = "es"  # Idioma del audio (español)

# # Cargar el modelo Whisper
# print("Cargando el modelo Whisper...")
# modelo = whisper.load_model(model_name)

# # Transcribir el audio
# print(f"Procesando audio con tarea: {task}...")
# resultado = modelo.transcribe(nombre_audio, task=task, language=language)

# # Mostrar y guardar el resultado
# texto = resultado["text"]
# archivo_salida = "resultado.txt"
# print(f"\nTexto transcrito:\n{texto}\n")

# with open(archivo_salida, "w", encoding="utf-8") as archivo:
#     archivo.write(texto)

# print(f"El resultado se ha guardado en '{archivo_salida}'.")

import os
import subprocess
import whisper

def extraer_audio(video_path, audio_path):
    comando = f"ffmpeg -i \"{video_path}\" -vn -ar 44100 -ac 2 -b:a 192k \"{audio_path}\""
    subprocess.run(comando, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def transcribir_audio(audio_path, output_path, model_name="small", language="es"):
    modelo = whisper.load_model(model_name)
    resultado = modelo.transcribe(audio_path, task="transcribe", language=language)
    with open(output_path, "w", encoding="utf-8") as archivo:
        archivo.write(resultado["text"])

def procesar_archivos():
    carpeta_grabacion = "grabacion"
    carpeta_transcripcion = "transcripcion"
    os.makedirs(carpeta_grabacion, exist_ok=True)
    os.makedirs(carpeta_transcripcion, exist_ok=True)
    
    archivos = [f for f in os.listdir(carpeta_grabacion) if f.lower().endswith(('.mp4', '.mp3'))]
    
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta_grabacion, archivo)
        nombre_base, extension = os.path.splitext(archivo)
        
        if extension.lower() == ".mp4":
            audio_path = os.path.join(carpeta_grabacion, nombre_base + "_procesado.mp3")
            extraer_audio(ruta_completa, audio_path)
        else:
            audio_path = os.path.join(carpeta_grabacion, nombre_base + "_procesado.mp3")
            os.rename(ruta_completa, audio_path)
        
        output_text_path = os.path.join(carpeta_transcripcion, nombre_base + ".txt")
        print(f"Procesando {archivo}...")
        transcribir_audio(audio_path, output_text_path)
        
        nuevo_nombre = nombre_base + "_procesado" + extension
        os.rename(ruta_completa, os.path.join(carpeta_grabacion, nuevo_nombre))
        print(f"{archivo} procesado y renombrado a {nuevo_nombre}")

if __name__ == "__main__":
    procesar_archivos()
    print("Procesamiento completado.")