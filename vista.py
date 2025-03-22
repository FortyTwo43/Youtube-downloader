import customtkinter as ctk
from funtions import inciar_descarga


def ventana_principal():
    # Configurar el modo de apariencia (opcional)
    ctk.set_appearance_mode("dark")  # Opciones: "dark", "light", "system"
    ctk.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue", etc.

    # Crear la ventana principal
    app = ctk.CTk()
    app.title("Youtube Video Downloader")
    app.geometry("600x300")  # Ancho x Alto

    ingreso_URL = ctk.CTkEntry(app, placeholder_text="Ingrese la URL..." , width=500, height=25)
    ingreso_URL.place(x=50, y=150)

    boton = ctk.CTkButton(app, text="Descargar solo audio", command=lambda:inciar_descarga(ingreso_URL))
    boton.place(x=230, y=200)
    
    # Ejecutar el bucle principal de la aplicación
    app.mainloop()

ventana_principal()