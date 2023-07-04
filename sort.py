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
            folder =import os
import shutil
from transliterate import translit

name_folders = {
    ('JPEG', 'PNG', 'JPG', 'SVG'): "izo",
    ('AVI', 'MP4', 'MOV', 'MKV'): "vidio",
    ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'): 'document',
    ('MP3', 'OGG', 'WAV', 'AMR'): 'music',
    ('ZIP', 'GZ', 'TAR'): "archive", 
}

directory = 'C:\\Users\\user\\Desktop\\ттт'

folders = []
files = []


def walk():
    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        for folder in filenames:
            folders.append(os.path.join(dirpath, folder))
        for file in filenames:
            files.append(os.path.join(dirpath, file))

def rename_files():
    for f in files:
        path_file = os.path.basename(f)
        try:
            x = translit(path_file, reversed=True)
            os.rename(f, os.path.join(directory, x))
        except:
            os.rename(f, os.path.join(directory, path_file))

def cleanup_folders():
    for folder in folders:
        if folder not in [os.path.join(directory, value) for value in name_folders.values()]:
            shutil.rmtree(folder)

def move_files():
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        file_ext = file_ext[1:].upper()
        for key, value in name_folders.items():
            if file_ext in key:
                destination_folder = os.path.join(directory, value)
                if value == 'archive':
                    shutil.unpack_archive(file, os.path.join(destination_folder, file_name))
                    os.remove(file)
                else:
                    shutil.move(file, os.path.join(destination_folder, os.path.basename(file)))

walk()
rename_files()
cleanup_folders()
move_files()

filesx = os.listdir(directory)
print(filesx)
 os.path.join(root, dir)
            if not os.listdir(folder):
                os.rmdir(folder)

sort_files()
remove_empty_folders()
