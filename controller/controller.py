from view.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model:Model):
        self.view = view
        self.model = model

        # callbacks
        self.model.on_start_download = self.report_start_download
        self.model.on_finish_download = self.report_finish_download
        self.model.on_error_download = self.report_error_download

    def show_view_download_buttons(self):
        url = self.view.get_url_entry()

        if self.model.verify_string(url) == False:
            return

        self.view.show_download_buttons()

    def start_download(self, _format: str):
        url = self.view.get_url_entry()
        if self.model.verify_string(url) == False:
            return

        self.model.start_download(url, _format)

    def report_start_download(self) -> None:
        self.view.show_message("Iniciando descarga...")

    def report_finish_download(self) -> None:
        self.view.show_message("Descarga finalizada :)")
        self.view.hide_download_audio_button()
        self.view.hide_download_video_button()

    def report_error_download(self) ->None:
        self.view.show_message("Ha ocurrido un error desconocido :(")