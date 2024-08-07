import os
import xml.etree.ElementTree as ET

# Directories
xml_dir = "Files\XML"
wem_dir = "Files\WEM"
output_dir = "Files\Output"

# Define a base path for the output folder
output_base = output_dir

# Get a list of XML files
xml_files = [os.path.join(xml_dir, f) for f in os.listdir(xml_dir) if f.endswith('.xml')]

# Create the output folder if it doesn't exist
os.makedirs(output_base, exist_ok=True)

# Create a dictionary of files
file_dict = {}

# Loop through each XML file
for xml_file in xml_files:
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Loop through each "File" node in the XML file
    for file_node in root.findall('.//File'):
        file_id = file_node.get('Id')
        path_node = file_node.find('Path')
        if path_node is not None:
            file_path = path_node.text
        else:
            file_path = None

        # Add the file to the dictionary only if it has an associated file
        if file_path is not None:
            file_dict[file_id] = file_path

# Loop through each WEM file in the corresponding folder
for wem_file in os.listdir(wem_dir):
    if not wem_file.endswith('.wem'):
        continue

    wem_id = os.path.splitext(wem_file)[0]
    file_path = file_dict.get(wem_id)

    if file_path is not None:
        # Create the directory and move the file
        file_path_parts = file_path.split('\\')
        folder_path = os.path.join(output_base, *file_path_parts[:-1])
        file_name = os.path.splitext(file_path_parts[-1])[0]

        os.makedirs(folder_path, exist_ok=True)
        os.replace(os.path.join(wem_dir, wem_file), os.path.join(folder_path, file_name + ".wem"))
        
        print(f'Moving: {wem_file} to {os.path.join(folder_path, file_name + ".wem")}')
        
    else:
        # Move the file to the Unknown folder
        os.makedirs(os.path.join(output_base, "Unknown Files"), exist_ok=True)
        os.replace(os.path.join(wem_dir, wem_file), os.path.join(output_base, "Unknown Files", wem_file))
        print(f'File: {wem_file} not found in XML files, moved to folder Unknown Files')