import os
import time
import shutil
import winshell
from win32com.client import Dispatch


def kill_process(seconds):
    time.sleep(5)
    for i in range(seconds):
        print(f"Installer will close in {seconds - i} seconds.")
        time.sleep(1)
    exit()


def clear_catalog(path):
    try:
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
    except FileNotFoundError:
        pass


def transfer_folders_files(path_from: str, path_to: str):

    full_list = os.listdir(path_from)
    # print(full_list)
    for item in full_list:
        if item == "Python3109" or item == "Update_Updater":
            shutil.copytree(f"{path_from}/{item}", f"{path_to}/{item}", symlinks=False, ignore=None)
        elif item == "Update_App" or item == "Update.bat":
            os.rename(f"{path_from}/{item}", f"{path_to}/{item}")
        elif item == "Update_Updater.bat":
            shutil.copyfile(f"{path_from}/{item}", f"{path_to}/{item}")


def create_shortcut(file, target, icon, work_dir):
    print(f"Creating shortcut of {file[:-4]} to Desktop.")
    desktop = winshell.desktop()
    path = os.path.join(desktop, file)
    target = f"{work_dir}/{target}"
    icon = f"{work_dir}/{icon}"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = work_dir
    shortcut.IconLocation = icon
    shortcut.save()


with open(r"C:\superior6564\path_app.txt", "r") as path_file:
    common_path = path_file.readline()
# common_path = r"C:\superior6564"
clear_catalog(f"{common_path}/superior6564AppUpdater")
transfer_folders_files(f"{common_path}/temp/superior6564App-master", f"{common_path}/superior6564AppUpdater")
create_shortcut("Update.lnk", f"Update.bat", "Photos_or_Icons/degget_6564.ico", f"{common_path}/superior6564App")
print("Finish.")
kill_process(10)
