import Packages

Packages.check_req_packages()  # Проверка нужных пакетов
# print()
Packages.try_import()  # Проверка импортов

import Folders_and_Files as FaF
import time

with open("C:/superior6564/path_app.txt", "r") as path_file:
    prev_path_app = path_file.readline()[:-1]
    path_app = path_file.readline()

FaF.clear_folder(f"{path_app}/temp/superior6564App-master", ["Python3109"])
time.sleep(5)
# print("Finish")
