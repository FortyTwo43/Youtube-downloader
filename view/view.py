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

        self.boton_siguiente = ctk.CTkButton(self, text = "→", command=lambda:self.controller.show_view_download_buttons(), width=30, height=25)
        self.boton_siguiente.place(x=520, y=150)

        self.download_video_button = ctk.CTkButton(self, text="Descargar Video", command=lambda:self.controller.start_download("video"), width=140, height=30)
        self.download_audio_button = ctk.CTkButton(self, text="Descargar Audio", command=lambda:self.controller.start_download("audio"), width=140, height=30)

        print("Report: main_window was showed successfully")

    def get_url_entry(self):
        url = self.ingreso_URL.get()
        return url
    
    def show_message(self, text: str) -> None:
        download_message = ctk.CTkLabel(self, text= text, text_color="white", font=("Arial", 16), anchor="center", width=500, height=30)
        download_message.place(x=50, y=245)

    def show_download_video_button(self):
        self.download_video_button.place(x=155, y=200)
        print("Report: download_video_button was showed")

    def show_download_audio_button(self):
        self.download_audio_button.place(x=305, y=200)
        print("Report: download_audio_button was showed")

    def show_download_buttons(self):
        self.show_download_video_button()
        self.show_download_audio_button()

    def hide_download_audio_button(self):
        self.download_audio_button.place_forget()
        print("Report: download_audio_button hidden")

    def hide_download_video_button(self):
        self.download_video_button.place_forget()
        print("Report: download_video_button hidden")
        