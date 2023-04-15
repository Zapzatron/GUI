import Packages

Packages.check_req_packages()  # Проверка нужных пакетов
# print()
Packages.try_import()  # Проверка импортов

import Folders_and_Files as FaF
import subprocess
import time

with open("C:/superior6564/path_app.txt", "r") as path_file:
    path_app = path_file.readline()

FaF.clear_folder(f"{path_app}/superior6564App")
time.sleep(5)
FaF.copy_folder_file(f"{path_app}/temp/superior6564App-master",
                     f"{path_app}/superior6564App")
FaF.create_shortcut("superior6564App.lnk", "superior6564App.bat",
                    "Photos_or_Icons/degget_6564_App.ico", f"{path_app}/superior6564App")
FaF.create_shortcut("Update_2.0.lnk", f"Update_2.0.bat",
                    "Photos_or_Icons/degget_6564_Updater.ico", f"{path_app}/superior6564App")

subprocess.Popen(f"{path_app}/superior6564App/Python3109/python.exe {path_app}/superior6564App/Update_2.0/Clear_Temp.py")
