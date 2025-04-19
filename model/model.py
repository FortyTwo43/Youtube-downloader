import threading
from classes.downloader import Downloader

class Model:
    def __init__(self, downloader: Downloader):
        self.downloader = downloader
        self.on_start_download = None
        self.on_finish_download = None
        self.on_error_download = None

    def start_download(self, url):

        if url is None:
            if self.on_error_download:
                self.on_error_download()
                print("url is not valid, it is a NoneType")
            return

        # Run download in a new thread
        threading.Thread(target=self._download_thread, args=(url,), daemon=True).start()

    def _download_thread(self, url):
        try:
            if self.on_start_download:
                self.on_start_download()
            
                # Start download using downloader
                self.downloader.download(url)

            if self.on_finish_download:
                self.on_finish_download()
            
            print("\nDownload has finished\n")

        except Exception as e:
            if self.on_error_download:
                self.on_error_download()
                print(f"Error during download: {e}")