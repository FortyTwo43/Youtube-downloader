from abc import ABC, abstractmethod

class DownloadOptions(ABC):
    def __init__(self):
        self.options = None

    @abstractmethod
    def set_options(self) -> None:
        pass

