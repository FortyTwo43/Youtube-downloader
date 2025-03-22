import yt_dlp as youtube_dl


def descargar_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "ffmpeg_location": "C:\\Users\\usuario\\Downloads\\ffmpeg-7.1-essentials_build\\bin",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",          # Cambia el codec si deseas otro formato
            "preferredquality": "192",          # Calidad del audio (puede ajustarse)
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])