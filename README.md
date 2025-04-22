Comando para crear un .exe de la aplicación (es necesario instalar pyinstaller):

pyinstaller --onefile --noconsole --add-binary "ffmpeg-7.1-essentials_build/bin/ffmpeg.exe;ffmpeg-7.1-essentials_build/bin" --add-binary "icon/icon.ico;icon" --icon=icon/icon.ico yutubeVideoDownloader.py
