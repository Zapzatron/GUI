import os
import time
import shutil
import zipfile
import winshell
from win32com.client import Dispatch


def kill_process(seconds):
    time.sleep(5)
    for i in range(seconds):
        print(f"Installer will close in {seconds - i} seconds.")
        time.sleep(1)
    exit()


def clear_catalog(path):
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


def extract_zip(file, path):
    print(f"Extract the zip file to {path}.")
    with zipfile.ZipFile(file, 'r') as zip_file:
        zip_file.extractall(path)
    time.sleep(5)


def copytree(path_from, path_to, black_list: list = None, symlinks=False, ignore=None):
    if not os.path.exists(path_to):
        os.makedirs(path_to)
    for item in os.listdir(path_from):
        if item in black_list:
            # print(item)
            # s = os.path.join(path_from, item)
            s = f"{path_from}/{item}"
            # d = os.path.join(path_to, item)
            d = f"{path_to}/{item}"
            if os.path.isdir(s):
                copytree(s, d, black_list, symlinks, ignore)
            else:
                if item == "Python3109.zip":
                    extract_zip(f"{path_from}/{item}", path_to)
                else:
                    if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                        shutil.copy2(s, d)


def transfer_folders_files(path_from: str, path_to: str, black_list: list = None):
    print(f"Transfer folders and files from temp.")
    # full_list = os.listdir(path_from)
    # print(full_list)
    # for item in full_list:
    copytree(path_from, path_to, black_list)
    time.sleep(5)
    # if os.path.isdir(item):
    # if item == "Python3109" or item == "Update_Updater" or item == "Update_App":
    #     shutil.copytree(f"{path_from}/{item}", f"{path_to}/{item}", symlinks=False, ignore=None)
    # elif item == "Update_Updater.bat" or item == "Update.bat":
    #     shutil.copyfile(f"{path_from}/{item}", f"{path_to}/{item}")


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


with open("C:/superior6564/path_app.txt", "r") as path_file:
    common_path = path_file.readline()

# print(common_path)
# print(f"{common_path}/superior6564AppUpdater")
# exit()

# common_path = r"C:\superior6564"
clear_catalog(f"{common_path}/superior6564/superior6564AppUpdater")
transfer_folders_files(f"{common_path}/superior6564/temp/superior6564App-master",
                       f"{common_path}/superior6564/superior6564AppUpdater",
                       ["Update.bat", "Update_App", "Update_Updater.bat", "Update_Updater",
                        "Python3109.zip", "Check_Packages.py", "Installer.py", "Update_Updater.py",
                        "Photos_or_Icons", "degget_6564.ico"])
create_shortcut("Update.lnk", f"Update.bat", "Photos_or_Icons/degget_6564.ico", f"{common_path}/superior6564/superior6564AppUpdater", f"{common_path}/superior6564/superior6564AppUpdater")
print("Finish.")
kill_process(10)
