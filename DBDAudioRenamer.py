import os
import time
import shutil
import webbrowser
import subprocess

from datetime import datetime
from colorama import Fore

from utils.ui import UI, Style
from utils.config import config
from utils.clear import clear

from utils.name import Name

# Set Directories
DIR_BNK = "Files/BNK"
DIR_WEM = "Files/WEM"
DIR_XML = "Files/XML"
DIR_OUTPUT = "Files/Output"
DIR_PAK_DEFAULT = "C:\Program Files (x86)\Steam\steamapps\common\Dead by Daylight\DeadByDaylight\Content\Paks"
    
# Menu Welcome
def display_welcome_menu():
    clear.screen()
    UI.logo()
    print("| Welcome to my tool used to extract, rename audio files and much more! What do you want to do?"),
    while(True):
        welcome_option = UI.menu(
            "Choose an option:", [
                ("1", "Latest features"),
                ("2", "Start"),
                ("0", "Exit")
            ]
        )
        if welcome_option == 1:
            open_browser()
        elif welcome_option == 2:
            display_main_menu()
        elif welcome_option == 0:
            exit_program()
        elif welcome_option is None:
            input("Invalid option. Please try again.")
            display_welcome_menu()
            
# My Github (Updates)
def open_browser():
    print("| The browser will open the latest patch notes for the tool!")
    print("| Once you review them, press ENTER to start!")
    
    patch_notes_url = f"https://github.com/{config.made}/{config.name}/releases"
    webbrowser.open(patch_notes_url)
    input()
    display_main_menu()

# Main Menu
def display_main_menu():
    clear.screen()
    UI.logo()
    while(True):
        main_option = UI.menu(
            "Choose an option:", [
                ("1", "Extract files"),
                ("2", "Rename audio files"),
                ("3", "Convert audio files"),
                
                ("4", "Clean unnecessary files"),
                ("0", "Exit")
            ]
        )
        if main_option == 1:
            display_extract_menu()
        elif main_option == 2:
            rename_audio()
        elif main_option == 3:
            display_convert_menu()
        elif main_option == 4:
            display_clean_menu()
        elif main_option == 0:
            exit_program()
        elif main_option is None:
            input("Invalid option. Please try again.")
            display_main_menu()

# Menu Extract
def display_extract_menu():
    clear.screen()
    UI.logo()
    while True:
        extract_option = UI.menu(
            "Choose an option:", [
                ("1", "Audio files from .BNK"),
                ("2", "Main audio files from .PAK"),
                ("3", "Tome audio files from .PAK"),

                ("4", "Return"),
                ("0", "Exit")
            ]
        )
        if extract_option == 1:
            extract_bnk()
        elif extract_option == 2:
            extract_main_audio()
        elif extract_option == 3:
            extract_tome_audio()
        elif extract_option == 4:
            display_main_menu()
        elif extract_option == 0:
            exit_program()
        elif extract_option is None:
            input("Invalid option. Please try again.")
            display_extract_menu()

# Extract audio files from BNK
def extract_bnk():
    print("| Audio files from BNK will be extracted. Press ENTER to start!")
    input()

    bnk_files = os.listdir(DIR_BNK)

    for bnk_file in bnk_files:
        if bnk_file.endswith(".bnk"):
            print(f"Extracting audio from: {bnk_file}")
            os.system(f"Tools\\bnkextr.exe \"{os.path.join(DIR_BNK, bnk_file)}\" /nodir >nul")
            
            # Move the file only if a file with the same name does not exist in the destination directory
            wem_file = os.path.join(DIR_WEM, bnk_file.replace(".bnk", ".wem"))
            
            if not os.path.exists(wem_file):
                os.system(f"move \"{os.path.join(DIR_BNK, '*.wem')}\" \"{DIR_WEM}\" >nul")
            else:
                print(f"Skipping file {bnk_file} as a .wem file with the same name already exists in the destination directory.")
                
        else:
            print("No .BNK files found in the directory.")

    print("Done!")
    input()
    display_extract_menu()
    
# Extract main audio files from PAK
def extract_main_audio():
    print()
    print("| You are going to extract the most important audios from the PAK files!")
    print(f"| Default Path: '{DIR_PAK_DEFAULT}' it would be correct?")
    while True:
        extract_main_option = UI.menu(
            "Choose an option:", [
                ("1", "Yes"),
                ("2", "No")
            ]
        )
        # Modified for QuickBMS - Removing the message
        if extract_main_option == 1:
            for root, _, files in os.walk(DIR_PAK_DEFAULT):
                for file in files:
                    if file.endswith("pakchunk1-Windows.pak"):
                        pak_main_audio = os.path.join(root, file)
                        print(f"Extracting PAK file: {file}")
                        # Overwrite the output directory
                        output_dir = os.path.join("Extracted Files", "Main Audio Files")

                        if os.path.exists(output_dir):
                            shutil.rmtree(output_dir)  # Delete the directory and its contents
                        os.makedirs(output_dir)  # Create a new empty directory

                        # Run the command and capture the output
                        process = subprocess.Popen(["Tools\\quickbms_4gb_files.exe", "Tools\\bms\\unreal_tournament_4_0.4.27e_dead_by_daylight.bms", pak_main_audio, output_dir], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=False)
                        for line in process.stdout:
                            line = line.decode(errors='ignore').strip()  # Decode and remove non-decodable characters
                            if "Extracting PAK file" in line:
                                print(line)
            print("Done!")
            input()
            display_extract_menu()

        # Modified for QuickBMS - Removing the message
        elif extract_main_option == 2:
            DIR_PAK_NEW = input("Por favor, introduce la nueva ruta de los archivos PAK: ")
            for root, _, files in os.walk(DIR_PAK_NEW):
                for file in files:
                    if file.endswith("pakchunk1-Windows.pak"):
                        pak_main_audio = os.path.join(root, file)
                        print(f"Extracting PAK file: {file}")
                        # Sobrescribir el directorio de salida
                        output_dir = os.path.join("Extracted Files", "Main Audio Files")

                        if os.path.exists(output_dir):
                            shutil.rmtree(output_dir)  # Delete the directory and its contents
                        os.makedirs(output_dir)  # Create a new empty directory

                        # Run the command and capture the output
                        process = subprocess.Popen(["Tools\\quickbms_4gb_files.exe", "Tools\\bms\\unreal_tournament_4_0.4.27e_dead_by_daylight.bms", pak_main_audio, output_dir], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=False)
                        for line in process.stdout:
                            line = line.decode(errors='ignore').strip()  # Decode and remove non-decodable characters
                            if "Extracting PAK file" in line:
                                print(line)
            print("Done!")
            input()
            display_extract_menu()
        
        elif extract_main_option is None:
            input("Invalid option. Please try again.")
            extract_main_audio()
    
# Extract tome audio files from PAK
def extract_tome_audio():
    print()
    print("| You are going to extract the most important audios from the PAK files!")
    print(f"| Default Path: '{DIR_PAK_DEFAULT}' it would be correct?")
    while True:
        extract_tome_option = UI.menu(
            "Choose an option:", [
                ("1", "Yes"),
                ("2", "No")
            ]
        )
        # Modified for QuickBMS - Removing the message
        if extract_tome_option == 1:
            for root, _, files in os.walk(DIR_PAK_DEFAULT):
                for file in files:
                    if file.endswith("pakchunk2-Windows.pak"):
                        pak_tome_audio = os.path.join(root, file)
                        print(f"Extracting PAK file: {file}")
                        # Overwrite the output directory
                        output_dir = os.path.join("Extracted Files", "Tome Audio Files")

                        if os.path.exists(output_dir):
                            shutil.rmtree(output_dir)  # Delete the directory and its contents
                        os.makedirs(output_dir)  # Create a new empty directory

                        # Run the command and capture the output
                        process = subprocess.Popen(["Tools\\quickbms_4gb_files.exe", "Tools\\bms\\unreal_tournament_4_0.4.27e_dead_by_daylight.bms", pak_tome_audio, output_dir], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=False)
                        for line in process.stdout:
                            line = line.decode(errors='ignore').strip()  # Decode and remove non-decodable characters
                            if "Extracting PAK file" in line:
                                print(line)
            print("Done!")
            input()
            display_extract_menu()
            
        # Modified for QuickBMS - Removing the message
        elif extract_tome_option == 2:
            DIR_PAK_NEW = input("Please enter the new path of the PAK files: ")
            for root, _, files in os.walk(DIR_PAK_NEW):
                for file in files:
                    if file.endswith("pakchunk2-Windows.pak"):
                        pak_tome_audio = os.path.join(root, file)
                        print(f"Extracting PAK file: {file}")
                        # Overwrite the output directory
                        output_dir = os.path.join("Extracted Files", "Tome Audio Files")

                        if os.path.exists(output_dir):
                            shutil.rmtree(output_dir)  # Delete the directory and its contents
                        os.makedirs(output_dir)  # Create a new empty directory

                        # Run the command and capture the output
                        process = subprocess.Popen(["Tools\\quickbms_4gb_files.exe", "Tools\\bms\\unreal_tournament_4_0.4.27e_dead_by_daylight.bms", pak_tome_audio, output_dir], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=False)
                        for line in process.stdout:
                            line = line.decode(errors='ignore').strip()  # Decode and remove non-decodable characters
                            if "Extracting PAK file" in line:
                                print(line)
            print("Done!")
            input()
            display_extract_menu()
        
        elif extract_tome_option is None:
            input("Invalid option. Please try again.")
            extract_tome_audio()

# Rename audio files with a script
def rename_audio():
    print("| You will rename all WEM audio with his real name. Press ENTER to start!")
    input()
    
    subprocess.run(["python", "Tools/scripts/renamer_parse.py"])
    print()
    print(f"Done! Audio files were renamed in {DIR_OUTPUT} folder.")
    input()
    display_main_menu()

# Menu convert audio files (OGG and more...)
def display_convert_menu():
    clear.screen()
    UI.logo()
    while(True):
        convert_option = UI.menu(
            "Choose an option:", [
                ("1", "WEM to OGG - Normal"),
                ("2", "OGG to OGG - ReVorb"),
                ("3", "Return"),
                ("0", "Exit")
            ]
        )
        if convert_option == 1:
            convert_wem_to_ogg()
        elif convert_option == 2:
            convert_ogg_with_revorb()
        elif convert_option == 3:
            display_main_menu()
        elif convert_option == 0:
            exit_program()
        elif convert_option is None:
            input("Invalid option. Please try again.")
            display_convert_menu()

# Convert WEM audio files to OGG
def convert_wem_to_ogg():
    print("| You will convert all WEM audio files to OGG. Press ENTER to start!")
    input()

    for root, _, files in os.walk(DIR_OUTPUT):
        for file in files:
            if file.endswith(".wem"):
                wem_file = os.path.join(root, file)
                print(f"Converting file: {file} to: OGG")
                os.system(f"ww2ogg\ww2ogg.exe \"{wem_file}\" --pcb ww2ogg\packed_codebooks_aoTuV_603.bin >nul")

    print()
    print(f"Done! Audio files were converted in {DIR_OUTPUT} folder.")
    input()
    display_convert_menu()

# Convert OGG audio to OGG ReVorb
def convert_ogg_with_revorb():
    print("| You will convert all OGG audio files to readable OGG. Press ENTER to start!")
    input()

    for root, _, files in os.walk(DIR_OUTPUT):
        for file in files:
            if file.endswith(".ogg"):
                ogg_file = os.path.join(root, file)
                print(f"Converting file: {file} to: OGG ReVorb")
                os.system(f"Tools\\revorb.exe \"{ogg_file}\" >nul")
    print()
    print(f"Done! Audio files were converted in {DIR_OUTPUT} folder.")
    input()
    display_convert_menu()

# Menu clean files
def display_clean_menu():
    clear.screen()
    UI.logo()
    while(True):
        clean_option = UI.menu(
            "Choose an option:", [
                ("1", "Show files to deleted"),
                ("2", "Clean files .WEM"),
                ("3", "Return"),
                ("0", "Exit")
            ]
        )
        if clean_option == 1:
            show_unnecessary_files()
        elif clean_option == 2:
            clean_unnecessary_files()
        elif clean_option == 3:
            display_main_menu()
        elif clean_option == 0:
            exit_program()
        elif clean_option is None:
            input("Invalid option. Please try again.")
            display_clean_menu()

# Show unnecessary files (WEM)
def show_unnecessary_files():
    print("| Showing files to be deleted! Press ENTER to start!")
    input()
    
    files_found = False  # Variable to track if files were found
    
    for root, _, files in os.walk(DIR_OUTPUT):
        for file in files:
            if file.endswith(".wem"):
                file_path = os.path.join(root, file)
                creation_time = os.path.getctime(file_path)
                formatted_time = datetime.fromtimestamp(creation_time).strftime("%d/%m/%Y")
                print(f"{formatted_time} {os.path.splitext(file)[0]}{os.path.splitext(file)[1]}")
                files_found = True  # At least one file found
    
    if not files_found:
        print("No WEM files found.")
        input()
    else:
        print()
        input("Waiting!")  
    display_clean_menu()
    
# Clean unnecessary files (WEM)
def clean_unnecessary_files():
    files_found = False  # Variable to track if files were found

    for root, _, files in os.walk(DIR_OUTPUT):
        for file in files:
            if file.endswith(".wem"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                files_found = True  # At least one file found

    if files_found:
        print("Done!")
    else:
        print("No WEM files found.")
        
    input()
    display_clean_menu()
    
# Close
def exit_program():
    print("Exiting the tool... Press a KEY!")
    input()
    exit()

if __name__ == "__main__":
    display_welcome_menu()