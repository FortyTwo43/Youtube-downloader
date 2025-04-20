import customtkinter as ctk

class View(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Configurar el modo de apariencia (opcional)
        self.title("Youtube Video Downloader")
        self.geometry("600x300")  # Ancho x Alto
        self.resizable(False, False)
        self.iconbitmap("ico.ico")

        self.ingreso_URL = ctk.CTkEntry(self, placeholder_text="Ingrese la URL..." , width=465, height=25)
        self.ingreso_URL.place(x=50, y=150)

        self.boton_siguiente = ctk.CTkButton(self, text = "→", command=lambda:self.controller.get_formats(),width=30, height=25)
        self.boton_siguiente.place(x=520, y=150)

        self.options_menu = ctk.CTkOptionMenu(self, values=["Seleccione una opción"] ,command=self.seleccted_option, width=140, height=30)
        self.options_menu.place(x=305, y=200)


        self.boton = ctk.CTkButton(self, text="Descargar", command=lambda:self.controller.start_download(), width=140, height=30)
        self.boton.place(x=155, y=200)

        print("main_window was showed successfully")

    def get_url_entry(self):
        url = self.ingreso_URL.get()

        if url == "" or url == " ":
            print("url is not valid")
            return None

        return url
    
    def show_message(self, text: str) -> None:
        download_message = ctk.CTkLabel(self, text= text, text_color="white", font=("Arial", 16), anchor="center", width=500, height=30)
        download_message.place(x=50, y=245)

    def update_formats_options_menu(self, list_options: list) -> None:
        if list_options:
            self.options_menu.configure(values=list_options)
            self.options_menu.set(list_options[0]) # Default is the first in the list_options list
            print("options_menu was updated with list_options list")

    def seleccted_option(self, option):
        print(option)
        