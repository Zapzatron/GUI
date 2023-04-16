print("Cleaner")
import Packages

Packages.check_req_packages()  # Проверка нужных пакетов
# print()
Packages.try_import()  # Проверка импортов

import Folders_and_Files as FaF
import time

with open("C:/superior6564/path_app.txt", "r") as path_file:
    path_app = path_file.readline()

FaF.clear_folder(f"{path_app}/temp")
time.sleep(5)
print("Finish")
