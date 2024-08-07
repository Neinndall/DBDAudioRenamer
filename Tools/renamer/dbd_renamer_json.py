import os
import json

# Directories
json_dir = "Files/JSON"  # Ruta al directorio que contiene los archivos JSON
wem_dir = "Files/WEM"
output_dir = "Files/Output"

# Define a base path for the output folder
output_base = output_dir

# Create the output folder if it doesn't exist
os.makedirs(output_base, exist_ok=True)

# Create a dictionary of files
file_dict = {}

# Loop through all JSON files in the directory
for json_file_name in os.listdir(json_dir):
    if json_file_name.endswith('.json'):
        json_file_path = os.path.join(json_dir, json_file_name)
        
        # Load the JSON file
        try:
            with open(json_file_path, 'r') as f:
                data = json.load(f)
                print(f"File: '{json_file_name}' loaded.")
        except Exception as e:
            print(f"Error loading JSON file '{json_file_name}': {e}")
            continue

        # Check if the key 'SoundBanksInfo' exists in the loaded data
        if "SoundBanksInfo" in data:
            soundbanks_info = data["SoundBanksInfo"]
            
            # Check if key 'SoundBanks' exists inside 'SoundBanksInfo'
            if "SoundBanks" in soundbanks_info:
                for soundbank in soundbanks_info["SoundBanks"]:
                    # Check if the key 'Media' exists in each SoundBank
                    if "Media" in soundbank:
                        for media in soundbank["Media"]:
                            file_id = media["Id"]
                            file_path = media["CachePath"]
                            file_dict[file_id] = file_path
            else:
                print("The key 'SoundBanks' is not found in 'SoundBanksInfo'.")
        else:
            print("The key 'SoundBanksInfo' is not found in the JSON file.")

# Loop through each WEM file in the corresponding folder
for wem_file in os.listdir(wem_dir):
    if not wem_file.endswith('.wem'):
        continue

    # Extract the ID from the WEM file (without the .wem extension)
    wem_id = os.path.splitext(wem_file)[0]
    file_path = file_dict.get(wem_id)

    if file_path is not None:
        # Create the directory if it does not exist and move/overwrite the file
        file_path_parts = file_path.split('/')
        folder_path = os.path.join(output_base, *file_path_parts[:-1])
        file_name = os.path.splitext(file_path_parts[-1])[0]

        os.makedirs(folder_path, exist_ok=True)
        destination = os.path.join(folder_path, file_name + ".wem")

        # Move the file (overwriting if it already exists)
        os.replace(os.path.join(wem_dir, wem_file), destination)

        print(f'Moving: {wem_file} to {destination}')
    else:
        # Move the file to the Unknown folder
        unknown_folder = os.path.join(output_base, "Unknown Files")
        os.makedirs(unknown_folder, exist_ok=True)
        destination = os.path.join(unknown_folder, wem_file)

        # Move the file (overwriting if it already exists)
        os.replace(os.path.join(wem_dir, wem_file), destination)
        print(f'File: {wem_file} not found in JSON, moved to folder Unknown Files')
