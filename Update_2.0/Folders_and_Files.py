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


def clear_folder(path, black_list: list = []):
    if not os.path.exists(path):
        os.makedirs(path)
    file_list = os.listdir(path)
    for item in file_list:
        if item not in black_list:
            s = os.path.join(path, item)
            if os.path.isdir(s):
                try:
                    shutil.rmtree(s)
                except OSError as e:
                    pass
            else:
                os.remove(s)


def copy_folder_file(path_from, path_to, black_list: list = [], symlinks=False, ignore=None):
    if not os.path.exists(path_to):
        os.makedirs(path_to)
    for item in os.listdir(path_from):
        if item not in black_list:
            s = f"{path_from}/{item}"
            d = f"{path_to}/{item}"
            if os.path.isdir(s):
                copy_folder_file(s, d, black_list, symlinks, ignore)
            else:
                if item == "Python3109.zip" and not os.path.exists(rf"{path_to}\Python3109"):
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
    with open(file, "wb") as new_file:
        new_file.write(requests.get(url).content)
    time.sleep(1)


def extract_zip(file, path_from, path_to):
    with zipfile.ZipFile(f"{path_from}/{file}", 'r') as zip_file:
        zip_file.extractall(path_to)
    time.sleep(5)
