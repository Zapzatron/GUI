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
        import tkinter.filedialog
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


def get_path_for_app(default_path, app_path):
    agree = " "
    common_path = ""
    while agree != "+" or agree != "-":
        app_path = "C:/superior6564/path_app.txt"
        agree = input(f"Default path is {default_path}"
                      f"\nDo you want to change path for app?"
                      f"\nWrite '+' to change or '-' to don`t change: ")
        if agree == "+":
            common_path = tkinter.filedialog.askdirectory(initialdir=default_path, title="Choose directory")
            if common_path != default_path:
                common_path = f"{common_path}/superior6564"
            check_previous_path = ""
            if os.path.exists(app_path):
                with open(app_path, "r") as file_path:
                    check_previous_path = file_path.readline()
                if common_path != check_previous_path:
                    clear_catalog(f"{check_previous_path}/superior6564")
            if not os.path.exists("C:/superior6564"):
                os.makedirs("C:/superior6564")
            with open(app_path, "w") as file_path:
                file_path.write(common_path)
            break
        elif agree == "-":
            if os.path.exists(app_path):
                with open(app_path, "r") as file_path:
                    common_path = file_path.readline()
            break
        else:
            common_path = default_path
            break
    return common_path


def get_zip(file, url):
    print("Getting zip of superior6564App.")
    with open(file, "wb") as new_file:
        new_file.write(requests.get(url).content)


def extract_zip(file, path_from, path_to):
    print(f"Extract {file} to {path_to}.")
    with zipfile.ZipFile(f"{path_from}/{file}", 'r') as zip_file:
        zip_file.extractall(path_to)
    time.sleep(5)


def copytree(path_from, path_to, black_list: list = None, symlinks=False, ignore=None):
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
                copytree(s, d, black_list, symlinks, ignore)
            else:
                if item == "Python3109.zip":
                    extract_zip(item, path_from, path_to)
                else:
                    if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                        shutil.copy2(s, d)


def transfer_folders_files(path_from: str, path_to: str, black_list: list = None):
    print(f"Transfer folders and files from temp.")
    copytree(path_from, path_to, black_list)
    # full_list = os.listdir(path_from)
    # print(full_list)
    # print(full_list)
    # for item in full_list:
        # if item not in black_list:
            # print(item)
            # if item == "Python3109.zip":
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
                # shutil.copytree(f"{path_from}/{item}", f"{path_to}/{item}", symlinks=False, ignore=None)
                # os.rename(f"{path_from}/{item}", f"{path_to}/{item}")
                # extract_zip(f"{path_from}/{item}", f"{common_path}/superior6564App")
            # else:
            #     os.rename(f"{path_from}/{item}", f"{path_to}/{item}")


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

import time

try_import()

import shutil
import zipfile
import requests
import os
import subprocess
import winshell
import tkinter.filedialog
from win32com.client import Dispatch


print("If an application was previously installed, it will be uninstalled and reinstalled.")
agree = " "
while agree != "":
    agree = input("Press 'enter' to continue or write 'exit' to exit: ")
    if agree == "exit":
        exit()

default_path = "C:/superior6564"
app_path = "C:/superior6564/path_app.txt"
common_path = get_path_for_app(default_path=default_path, app_path=app_path)

while agree != "" or agree != "-":
    agree = input(f"App will install in {common_path}."
                  f"\nDo you want to change path for app?"
                  f"\nPress 'enter' to continue or '-' to don`t change: ")
    if agree == "-":
        common_path = get_path_for_app(default_path=default_path, app_path=app_path)
        break

# while agree != "+" or agree != "-":
#     path_app = "C:/superior6564/path_app.txt"
#     agree = input(f"Default path is {default_path}\nDo you want to change path for app?\nWrite '+' to change or '-' to don`t change: ")
#     if agree == "+":
#         common_path = tkinter.filedialog.askdirectory(initialdir=default_path, title="Choose directory")
#         if common_path != default_path:
#             common_path = f"{common_path}/superior6564"
#         check_previous_path = ""
#         if os.path.exists(path_app):
#             with open(path_app, "r") as path_file:
#                 check_previous_path = path_file.readline()
#             if common_path != check_previous_path:
#                 clear_catalog(f"{check_previous_path}/superior6564")
#         if not os.path.exists("C:/superior6564"):
#             os.makedirs("C:/superior6564")
#         with open(path_app, "w") as path_file:
#             path_file.write(common_path)
#         break
#     elif agree == "-":
#         if os.path.exists(path_app):
#             with open(path_app, "r") as path_file:
#                 common_path = path_file.readline()
#         break
#     else:
#         common_path = default_path
#         break

print("Deleting previous application.")
clear_catalog(f"{common_path}/temp")
clear_catalog(f"{common_path}/superior6564App")
delete_file(f"{winshell.desktop()}/superior6564App.lnk", )
delete_file(f"{winshell.desktop()}/Update.lnk", )
delete_zip("superior6564App.zip")
get_zip("superior6564App.zip", "https://github.com/Superior-GitHub/superior6564App/archive/refs/heads/master.zip")
extract_zip("superior6564App.zip", os.getcwd(), f"{common_path}/temp")
transfer_folders_files(f"{common_path}/temp/superior6564App-master",
                       f"{common_path}/superior6564App",
                       ["Update.bat", "Update_App", "Update_Updater.bat", "Update_Updater"])
create_shortcut("superior6564App.lnk", "GeneratorRUWords.bat", "Photos_or_Icons/degget_6564.ico", f"{common_path}/superior6564App")
extract_zip("Python3109.zip", f"{common_path}/temp/superior6564App-master", f"{common_path}/temp/superior6564App-master")
path = f"{common_path}/temp/superior6564App-master"
os.chdir(path)
subprocess.Popen("Update_Updater.bat")
# create_shortcut("Update.lnk", f"Update.bat", "Photos_or_Icons/degget_6564.ico", os.getcwd())
# print("Finish.")
# kill_process(10)
