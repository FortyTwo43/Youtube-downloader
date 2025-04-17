from classes.abstractclasses.downloadOptions import DownloadOptions

class VideoDownloadOpts(DownloadOptions):
    def __init__(self):
        super().__init__()

    def set_options(self, new_options: dict):
        if new_options is None:
            print("new_options aren't the correct")

        self.options = new_options
        print("options set correctly")