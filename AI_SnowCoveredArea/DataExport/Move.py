import os
import shutil

# specify the source directory where the folders are located
source_directory = os.path.join('DataExport','RawData')

# specify the destination directory where you want to move the files to
destination_directory = os.path.join('DataExport','Lebanon-Snow-Cover-Data')

# loop through each folder in the source directory
for foldername in os.listdir(source_directory):
    # construct the full path to the folder
    folder_path = os.path.join(source_directory, foldername)
    # check if the current item in the loop is a directory
    if os.path.isdir(folder_path):
        # loop through each file in the folder
        for filename in os.listdir(folder_path):
            # construct the full path to the file
            file_path = os.path.join(folder_path, filename)
            # check if the current item in the loop is a file (not a directory)
            if os.path.isfile(file_path):
                # move the file to the destination directory
                shutil.move(file_path, destination_directory)
                print(f'Moved {filename} to {destination_directory}')
