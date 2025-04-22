Command to create an .exe of the application (you need to install pyinstaller):

pyinstaller --onefile --noconsole --add-binary "ffmpeg-7.1-essentials_build/bin/ffmpeg.exe;ffmpeg-7.1-essentials_build/bin" --add-binary "icon/icon.ico;icon" --icon=icon/icon.ico yutubeVideoDownloader.py
