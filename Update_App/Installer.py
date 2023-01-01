def kill_process(seconds):
    time.sleep(5)
    for i in range(seconds):
        print(f"Installer will close in {seconds - i} seconds.")
        time.sleep(1)
    exit()


def try_import():
    try:
        import shutil
        import time
        import zipfile
        import requests
        import os
        import subprocess
        import winshell
        from win32com.client import Dispatch
    except ModuleNotFoundError:
        print("You don`t have the packages I need. I can`t let you go any further.")
        kill_process(10)
    else:
        print("Required packages is ok :)")


def delete_folder(path):
    try:
        shutil.rmtree(path)
    except OSError as e:
        pass
        # print("Error: %s - %s." % (e.filename, e.strerror))


def delete_file(path):
    try:
        os.remove(path)
    except OSError as e:
        pass
        # print("Error: %s - %s." % (e.filename, e.strerror))


def delete_zip(file):
    try:
        os.remove(file)
        time.sleep(2)
    except OSError as e:
        pass


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


def transfer_folders_files(path_from: str, path_to: str, black_list: list = None):
    print(f"Transfer folders and files from temp.")
    full_list = os.listdir(path_from)
    # print(full_list)
    for item in full_list:
        if item not in black_list:
            # print(item)
            if item == "Python3109":
                # def copytree(src, dst, symlinks=False, ignore=None):
                #     if not os.path.exists(dst):
                #         os.makedirs(dst)
                #     for item in os.listdir(src):
                #         s = os.path.join(src, item)
                #         d = os.path.join(dst, item)
                #         if os.path.isdir(s):
                #             copytree(s, d, symlinks, ignore)
                #         else:
                #             if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                #                 shutil.copy2(s, d)

                # copytree(f"{path_from}/{item}", f"{black_path_to}/{item}")
                # copytree(f"{path_from}/{item}", f"{path_to}/{item}")
                shutil.copytree(f"{path_from}/{item}", f"{path_to}/{item}", symlinks=False, ignore=None)
                # os.rename(f"{path_from}/{item}", f"{path_to}/{item}")
            else:
                os.rename(f"{path_from}/{item}", f"{path_to}/{item}")


def get_zip(file, url):
    print("Getting zip of superior6564App.")
    with open(file, "wb") as new_file:
        new_file.write(requests.get(url).content)


def extract_zip(file, path):
    print(f"Extract the zip file to {path}.")
    with zipfile.ZipFile(file, 'r') as zip_file:
        zip_file.extractall(path)
    time.sleep(5)


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


try_import()

import shutil
import time
import zipfile
import requests
import os
import subprocess
import winshell
from win32com.client import Dispatch


print("If an application was previously installed, it will be uninstalled and reinstalled.")
agree = " "
while agree != "":
    agree = input("Press 'enter' to continue or write 'exit' to exit: ")
    if agree == "exit":
        exit()
common_path = "C:/superior6564"

with open("C:/superior6564/path_app.txt", "w") as path_file:
    path_file.write(common_path)

print("Deleting previous application.")
clear_catalog(f"{common_path}/temp")
clear_catalog(f"{common_path}/superior6564App")
delete_file(f"{winshell.desktop()}/superior6564App.lnk", )
delete_file(f"{winshell.desktop()}/Update.lnk", )
delete_zip("superior6564App.zip")
get_zip("superior6564App.zip", "https://github.com/Superior-GitHub/superior6564App/archive/refs/heads/master.zip")
extract_zip("superior6564App.zip", f"{common_path}/temp")
transfer_folders_files(f"{common_path}/temp/superior6564App-master",
                       f"{common_path}/superior6564App",
                       ["Update.bat", "Update_App", "Update_Updater.bat", "Update_Updater"])
create_shortcut("superior6564App.lnk", "GeneratorRUWords.bat", "Photos_or_Icons/degget_6564.ico", f"{common_path}/superior6564App")
path = f"{common_path}/temp/superior6564App-master/Update_Updater.bat"
subprocess.Popen(path)
# create_shortcut("Update.lnk", f"Update.bat", "Photos_or_Icons/degget_6564.ico", os.getcwd())
# print("Finish.")
# kill_process(10)
