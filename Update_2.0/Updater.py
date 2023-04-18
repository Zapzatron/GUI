import Packages

Packages.check_req_packages()  # Проверка нужных пакетов
# print()
Packages.try_import()  # Проверка импортов

import Folders_and_Files as FaF
import subprocess
import time

with open("C:/Zapzatron/path_app.txt", "r") as path_file:
    prev_path_app = path_file.readline()[:-1]
    path_app = path_file.readline()

FaF.clear_folder(f"{path_app}/GUI", ["Python3109"])
time.sleep(5)
FaF.copy_folder_file(f"{path_app}/temp/GUI-master",
                     f"{path_app}/GUI",
                     ["Python3109"])
FaF.create_shortcut("Zapzatron_GUI.lnk", "Zapzatron_GUI.bat",
                    "Photos_or_Icons/degget_6564_App.ico", f"{path_app}")
FaF.create_shortcut("Update_2.0.lnk", f"Update_2.0.bat",
                    "Photos_or_Icons/degget_6564_Updater.ico", f"{path_app}")

run_cleaner = subprocess.Popen(f"{path_app}/Python3109/python.exe {path_app}/Update_2.0/Clear_Temp.py")
run_cleaner.wait()
