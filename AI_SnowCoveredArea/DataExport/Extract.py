import os
import zipfile

# Set the source directory where the zip files are located
source_dir = os.path.join('DataExport','RawData')

# Loop through all files in the source directory
for file_name in os.listdir(source_dir):
    if file_name.endswith('.zip'): # Check if the file is a zip file
        zip_file_path = os.path.join(source_dir, file_name)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            extract_path = os.path.join(source_dir, os.path.splitext(file_name)[0])
            zip_file.extractall(extract_path)
            print(f"{file_name} extracted to {extract_path}")
