import os

# Set the source directory where the folders are located
source_dir = os.path.join('DataExport','RawData')

# Loop through all folders in the source directory
for folder_name in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder_name)
    if os.path.isdir(folder_path): # Check if it's a directory
        # Loop through all files in the directory and rename them to the folder name
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            new_file_name = os.path.join(folder_path, folder_name + os.path.splitext(file_name)[1])
            os.rename(file_path, new_file_name)

print('All files have been renamed.')
