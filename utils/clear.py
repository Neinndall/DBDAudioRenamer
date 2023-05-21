import os

class clear:
    def screen():
        os.system('cls' if os.name == 'nt' else 'clear')