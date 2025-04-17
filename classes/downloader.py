import yt_dlp as youtube_dl
from classes.abstractclasses.downloadOptions import DownloadOptions

class Downloader:
    def __init__(self):
        self.download_opts: DownloadOptions = None
        print("downloader was created successfully")

    # use to set the currently download options
    def set_options(self, new_options: DownloadOptions) ->None:
        if new_options is None:
            print("new_options can not be NoneType")
            return
        
        self.download_opts = new_options
        print("yld_options set correctly")

    # download_opts specify the download options (format, guality, and more)
    def download(self, url: str) -> None:

        if self.download_opts is None:
            print("Is not posible download video, first change options for a valid value")    
            return
        
        with youtube_dl.YoutubeDL(self.download_opts.options) as ydl:
            ydl.download([url])  