# print("Temp прогружен")
import Packages

Packages.check_req_packages()  # Проверка нужных пакетов
print()
Packages.try_import()  # Проверка импортов

import Folders_and_Files as FaF
import subprocess


with open("C:/Zapzatron/path_app.txt", "r") as path_file:
    common_path = path_file.readline()

FaF.clear_folder(f"{common_path}/Zapzatron_GUI")
FaF.copy_folder_file(f"{common_path}/temp/GUI-master",
                     f"{common_path}/Zapzatron_GUI")
FaF.create_shortcut("Zapzatron_GUI.lnk", "Zapzatron_GUI.bat",
                    "Photos_or_Icons/degget_6564_App.ico", f"{common_path}/Zapzatron_GUI")
FaF.create_shortcut("Update.lnk", f"Update.bat",
                    "Photos_or_Icons/degget_6564_Updater.ico", f"{common_path}/Zapzatron_GUI")

subprocess.Popen(f"{common_path}/Zapzatron_GUI/Python3109/python.exe {common_path}/Zapzatron_GUI/Update/Clear_Temp.py")
