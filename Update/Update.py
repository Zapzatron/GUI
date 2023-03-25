# print("Temp прогружен")
import Packages

Packages.check_req_packages()  # Проверка нужных пакетов
print()
Packages.try_import()  # Проверка импортов

import Folders_and_Files as FaF
import subprocess


with open("C:/superior6564/path_app.txt", "r") as path_file:
    common_path = path_file.readline()

FaF.clear_folder(f"{common_path}/superior6564App")
FaF.copy_folder_file(f"{common_path}/temp/superior6564App-master",
                     f"{common_path}/superior6564App")
FaF.create_shortcut("superior6564App.lnk", "superior6564App.bat",
                    "Photos_or_Icons/degget_6564_App.ico", f"{common_path}/superior6564App")
FaF.create_shortcut("Update.lnk", f"Update.bat",
                    "Photos_or_Icons/degget_6564_Updater.ico", f"{common_path}/superior6564App")

subprocess.Popen(f"{common_path}/superior6564App/Python3109/python.exe {common_path}/superior6564App/Update/Clear_Temp.py")
