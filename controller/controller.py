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
        self.model.on_formats_ready = self.update_view_menu_options

    def get_formats(self):
        url = self.view.get_url_entry()

        if url is None:
            print("url is not valid")
            return

        self.model.get_formats(url)

    def update_view_menu_options(self, list_options: list) -> None:
        self.view.update_formats_options_menu(list_options)


    def start_download(self):
        url = self.view.get_url_entry()

        if url is None:
            print("url is not valid")
            return
        
        self.model.start_download(url)

    def report_start_download(self) -> None:
        # El controlador le pide a la vista que muestre algo
        self.view.show_message("Iniciando descarga...")

    def report_finish_download(self) -> None:
        self.view.show_message("Descarga finalizada :)")

    def report_error_download(self) ->None:
        self.view.show_message("Ha ocurrido un error desconocido :(")