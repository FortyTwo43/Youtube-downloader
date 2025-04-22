from classes.audioDownloadOpts import AudioDownloadOpts
from classes.videoDownloadOpts import VideoDownloadOpts
from classes.downloader import Downloader
from view.view import View
from model.model import Model
from controller.controller import Controller
import customtkinter as ctk
from path import resource_path

video_opts_dict = {
        "format": "best",
        "outtmpl": "%(title)s.%(ext)s",
        }

audio_opts_dict = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        'ffmpeg_location': resource_path("ffmpeg-7.1-essentials_build/bin"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    }

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Opciones: "dark", "light", "system"
    ctk.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue", etc.
    
    downloader = Downloader()

    video_options = VideoDownloadOpts()
    video_options.set_options(video_opts_dict)

    audio_options = AudioDownloadOpts()
    audio_options.set_options(audio_opts_dict)

    downloader.set_options(video_options)
    downloader.set_options(audio_options)

    model = Model(downloader)  
    controller = Controller(None, model)
    view = View(controller)
    controller.view = view

    view.mainloop()