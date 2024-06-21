# Imports
import ctypes
from utils.config import config

class Name:
    def __init__(self):
        # Set console window title when instantiating class
        self.name = config.name
        self.version = config.version
        self.title = f"{self.name} v{self.version}"
        ctypes.windll.kernel32.SetConsoleTitleW(self.title)

# Run automatically on import
name_instance = Name()