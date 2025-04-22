import os
import sys

#Returns the absolute path of the resource, whether in development or as an exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # when packaged by PyInstaller

    except AttributeError:
        base_path = os.path.abspath(".")  # development mode

    return os.path.join(base_path, relative_path)