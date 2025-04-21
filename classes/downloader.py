import yt_dlp as youtube_dl
from classes.abstractclasses.downloadOptions import DownloadOptions
from classes.audioDownloadOpts import AudioDownloadOpts
from classes.videoDownloadOpts import VideoDownloadOpts

class Downloader:
    def __init__(self):
        self.download_video_opts: DownloadOptions = None
        self.download_audio_opts: DownloadOptions = None

        print("Report: downloader was created successfully")

    # use to set the currently download options
    def set_options(self, new_options: DownloadOptions) ->None:
        
        if new_options is None:
            print("Error: new_options can not be NoneType")
            return
        
        if isinstance(new_options, VideoDownloadOpts):
            print("Report: video options set correctly")

            self.download_video_opts = new_options
        elif isinstance(new_options, AudioDownloadOpts):
            print("Report: audio options set correctly")
            self.download_audio_opts = new_options
        else:
            print("Error: options are not correct")

    # download_opts specify the download options (format, guality, and more)
    def download_video(self, url: str) -> None:
        if self.download_video_opts is None:
            print("Error: Is not posible download video, first change options for a valid value")    
            return
        
        with youtube_dl.YoutubeDL(self.download_video_opts.options) as ydl:
            ydl.download([url])

    def download_audio(self, url: str) -> None:
        if self.download_audio_opts is None:
            print("Error: Is not posible download audio, first change options for a valid value")    
            return
        
        with youtube_dl.YoutubeDL(self.download_audio_opts.options) as ydl:
            ydl.download([url])        