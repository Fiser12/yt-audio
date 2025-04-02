import sys
import os
import yt_dlp

def descargar_audio(video_url, output_path):
    opciones = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path + '%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([video_url])

def descargar_video(video_url, output_path):
    opciones = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'outtmpl': output_path + '%(title)s.%(ext)s',
        'noplaylist': True,
        'no_warnings': True,
        'postprocessors': [],
        'keepvideo': True,
        'writethumbnail': False,
        'writesubtitles': False,
        'writeautomaticsub': False,
        'embedsubtitles': False,
        'embedthumbnail': False,
        'subtitlesformat': 'srt',
        'no_post': True,
        'no_post_overwrites': True
    }
    
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([video_url])

def descargar_contenido(video_url, output_path='/code/downloads/'):
    if not output_path.endswith('/'):
        output_path += '/'
    
    modo = os.getenv('MODO_DESCARGA', 'audio')
    
    if modo == 'video':
        descargar_video(video_url, output_path)
    else:
        descargar_audio(video_url, output_path)

if __name__ == '__main__':
    video_url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else './'
    descargar_contenido(video_url, output_path)
