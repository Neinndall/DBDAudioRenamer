from colorama import Fore
from utils.config import config

class Style:
    BOLD = "\033[1m"
    NORMAL = "\033[0m"

class UI:	
    def logo():
        print(Fore.RED + "      _____                 _   ____          _____              _ _       _     _     ")
        print(Fore.RED + "     |  __ \               | | |  _ \        |  __ \            | (_)     | |   | |    ")
        print(Fore.RED + "     | |  | | ___  __ _  __| | | |_) |_   _  | |  | | __ _ _   _| |_  __ _| |__ | |_   ")
        print(Fore.RED + "     | |  | |/ _ \/ _` |/ _` | |  _ <| | | | | |  | |/ _` | | | | | |/ _` | \'_ \| __| ")
        print(Fore.RED + "     | |__| |  __/ (_| | (_| | | |_) | |_| | | |__| | (_| | |_| | | | (_| | | | | |_   ")
        print(Fore.RED + "     |_____/ \___|\__,_|\__,_| |____/ \__, | |_____/ \__,_|\__, |_|_|\__, |_| |_|\__|  ")
        print(Fore.RED + "                                        _/ |                __/ |     __/ |            ")
        print(Fore.RED + "                                      |___/                |___/     |___/             ")
        print(Fore.GREEN + "                       _  _                                                        ")
        print(Fore.GREEN + "                      | |(_)                                                       ")
        print(Fore.GREEN + "      __ _  _   _   _ | | _   ___    _ __  ___  _ __    __ _  _ __ ___    ___  _ __ ")
        print(Fore.GREEN + "     / _` || | | | / _` || | / _ \  | '__|/ _ \| '_ \  / _` || '_ ` _ \  / _ \| '__|")
        print(Fore.GREEN + "    | (_| || |_| || (_| || || (_) | | |  |  __/| | | || (_| || | | | | ||  __/| |   ")
        print(Fore.GREEN + "     \__,_| \__,_| \__,_||_| \___/  |_|   \___||_| |_| \__,_||_| |_| |_| \___||_|   ")
        print("")
        print(Fore.WHITE + "\t" + "\t" + "\tMade by: " + Fore.YELLOW + f"{config.made}" + Fore.WHITE + "\tVersion: " + Fore.YELLOW + f"{config.version}")
        print(Fore.WHITE)
        
    def menu(prompt, options):
        print("\n" + Fore.LIGHTGREEN_EX + prompt + Fore.WHITE)
        while True:
            for i in range(len(options)):
                print("{}) {}".format(options[i][0], options[i][1]))

            choice = input("\n> ")
            for i in range(len(options)):
                if choice == options[i][0]:
                    try:
                        number = int(choice)
                        # If number, return int
                        return number
                    except ValueError:
                        # if not a number, return str
                        return choice
            return None
