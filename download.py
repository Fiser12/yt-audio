import sys
import os
import yt_dlp

def obtener_opciones_audio(output_path):
    return {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path + '%(title)s.%(ext)s',
    }

def obtener_opciones_video(output_path):
    return {
        'format': 'bestvideo[height<=2160]+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': output_path + '%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': False,
    }

def descargar_contenido(video_url, output_path='/code/downloads/'):
    if not output_path.endswith('/'):
        output_path += '/'
    
    modo = os.getenv('MODO_DESCARGA', 'audio')
    opciones = obtener_opciones_video(output_path) if modo == 'video' else obtener_opciones_audio(output_path)
    
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([video_url])

if __name__ == '__main__':
    video_url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else './'
    descargar_contenido(video_url, output_path)
