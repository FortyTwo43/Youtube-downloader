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
        self.on_formats_ready = None

    def get_formats(self, url: str) -> list:

        if url is None:
            print("url is not valid")
            return

        threading.Thread(target=self._get_formats_thread, args=(url,), daemon=True).start()

    def _get_formats_thread(self, url):
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get("formats", [])
            print("Report: formats was gotten")
        
        list_options = self.generate_list_options(formats)
        print("Report: list_options was generated")
        
        if self.on_formats_ready:
            self.on_formats_ready(list_options)

    def generate_list_options(self, formats) -> list:
        options = []
        for f in formats:
            ext = f.get("ext")
            height = f.get("height")
            if ext and height:
                opcion = f"{ext} {height}p"
                if opcion not in options:
                    options.append(opcion)
        return sorted(options, key=lambda x: int(x.split()[1][:-1]), reverse=True)

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