# print("Import Folders_and_Files")
from win32com.client import Dispatch
import shutil
import zipfile
import requests
import winshell
import time
import os


def delete_folder(path):
    try:
        shutil.rmtree(path)
    except OSError as e:
        pass
        # print("Error: %s - %s." % (e.filename, e.strerror))


def clear_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    file_list = os.listdir(path)
    # print(file_list)
    for item in file_list:
        # print(item)
        # if item != "Python3109" and item != "Update.bat" and item != "Update_files":
        s = os.path.join(path, item)
        if os.path.isdir(s):
            try:
                shutil.rmtree(s)
            except OSError as e:
                pass
                # print("Error: %s - %s." % (e.filename, e.strerror))
        else:
            os.remove(s)


def copy_folder_file(path_from, path_to, black_list: list = [], symlinks=False, ignore=None):
    if not os.path.exists(path_to):
        os.makedirs(path_to)
    for item in os.listdir(path_from):
        if item not in black_list:
            # print(item)
            # s = os.path.join(path_from, item)
            s = f"{path_from}/{item}"
            # d = os.path.join(path_to, item)
            d = f"{path_to}/{item}"
            if os.path.isdir(s):
                copy_folder_file(s, d, black_list, symlinks, ignore)
            else:
                if item == "Python3109.zip":
                    extract_zip(item, path_from, path_to)
                else:
                    if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                        shutil.copy2(s, d)


def delete_file(path):
    try:
        os.remove(path)
    except OSError as e:
        pass
        # print("Error: %s - %s." % (e.filename, e.strerror))


def create_shortcut(file, target, icon, work_dir, target_dir=None):
    print(f"Creating shortcut of {file[:-4]} to Desktop.")
    desktop = winshell.desktop()
    path = os.path.join(desktop, file)
    if target_dir is None:
        target = f"{work_dir}/{target}"
    else:
        target = f"{target_dir}/{target}"
    icon = f"{work_dir}/{icon}"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = work_dir
    shortcut.IconLocation = icon
    shortcut.save()


def delete_zip(file):
    try:
        os.remove(file)
        time.sleep(2)
    except OSError as e:
        pass


def get_zip(file, url):
    print("Getting zip of superior6564App.")
    with open(file, "wb") as new_file:
        new_file.write(requests.get(url).content)
    time.sleep(1)


def extract_zip(file, path_from, path_to):
    print(f"Extract {file} to {path_to}.")
    with zipfile.ZipFile(f"{path_from}/{file}", 'r') as zip_file:
        zip_file.extractall(path_to)
    time.sleep(5)
