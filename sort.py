import os
import shutil

directory = 'C:\\Users\\user\\Desktop\\ттт'

def sort_files():
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for file in files:
        file_extension = os.path.splitext(file)[1][1:].upper()
        new_directory = os.path.join(directory, file_extension)
        os.makedirs(new_directory, exist_ok=True)
        shutil.move(os.path.join(directory, file), os.path.join(new_directory, file))

def remove_empty_folders():
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            folder = os.path.join(root, dir)
            if not os.listdir(folder):
                os.rmdir(folder)

sort_files()
remove_empty_folders()