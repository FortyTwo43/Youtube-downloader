class Model:
    def __init__(self, downloader):
        self.downloader = downloader
        self.on_start_download = None

    def start_download(self, url):

        if url is None:
            print("url is not valid, it is a NoneType")
            return

        # Avisar que va a empezar la descarga
        if self.on_start_download:
            self.on_start_download()

        self.downloader.download(url)
    
        print("")
        print("AUDIO DESCARGADO")
        print("")