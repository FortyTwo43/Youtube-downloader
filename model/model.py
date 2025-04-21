import threading
from classes.downloader import Downloader
import yt_dlp as youtube_dl
class Model:
    def __init__(self, downloader: Downloader):
        self.downloader = downloader

        # callbacks
        self.on_start_download = None
        self.on_finish_download = None
        self.on_error_download = None

    def verify_string(self, string):
        if string is None:
            return False
        
        if string == "" or string == " ":
            return False
        
        return True

    def start_download(self, url, _format):

        if url is None:

            if self.on_error_download:
                self.on_error_download()
                print("url is not valid, it is a NoneType")
            return

        # Run download in a new thread
        threading.Thread(target=self._download_thread, args=(url,_format,), daemon=True).start()

    def _download_thread(self, url, _format):
        try:
            if self.on_start_download:
                self.on_start_download()
            
                # Start download using downloader
                if _format == "video":
                    self.downloader.download_video(url)
                elif _format == "audio":
                    self.downloader.download_audio(url)
                else:
                    print("Error: _format is not correct")

            if self.on_finish_download:
                self.on_finish_download()
            
            print("\nDownload has finished\n")

        except Exception as e:
            if self.on_error_download:
                self.on_error_download()
                print(f"Error during download: {e}")