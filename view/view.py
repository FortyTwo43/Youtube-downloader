import customtkinter as ctk

class View(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        print("main_window was showed successfully")

        # Configurar el modo de apariencia (opcional)
        self.title("Youtube Video Downloader")
        self.geometry("600x300")  # Ancho x Alto

        self.ingreso_URL = ctk.CTkEntry(self, placeholder_text="Ingrese la URL..." , width=500, height=25)
        self.ingreso_URL.place(x=50, y=150)

        self.boton = ctk.CTkButton(self, text="Descargar solo audio", command=lambda:self.controller.start_download())
        self.boton.place(x=230, y=200)


    def get_url_entry(self):
        url = self.ingreso_URL.get()

        if url == "" or url == " ":
            print("url is not valid")
            return None

        return url
    
    def show_message(self, text: str) -> None:
        download_message = ctk.CTkLabel(self, text= text, text_color="white", font=("Arial", 16), width=50, height=30)
        download_message.place(x=230, y=160)

