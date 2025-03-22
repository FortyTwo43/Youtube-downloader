import customtkinter as ctk
from downloader import descargar_audio


def optener_text_entry(entry):
    if isinstance(entry, ctk.CTkEntry):
        string = entry.get()
        return string
    else:
        return None
    
def inciar_descarga(entry):
    string_url = optener_text_entry(entry)
    if string_url is None:
        print("Texto vacío")
        return

    descargar_audio(string_url)
    print("")
    print("AUDIO DESCARGADO")
    print("")
