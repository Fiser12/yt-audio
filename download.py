import sys
import yt_dlp

def download_youtube_audio(video_url, output_path='/code/downloads/'):
    if not output_path.endswith('/'):
        output_path += '/'
        
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path + '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == '__main__':
    video_url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else './'
    download_youtube_audio(video_url)
