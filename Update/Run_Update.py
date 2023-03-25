# print("Import Run_Update")
import Packages

Packages.check_req_packages()  # Проверка нужных пакетов
print()
Packages.try_import()  # Проверка импортов

import os
import subprocess
import Choice
import Folders_and_Files as FaF
import winshell

Choice.agree_for_run()  # Предупреждение
common_path = Choice.get_path_for_app()  # Получение пути для приложения
print("Deleting previous application.")
FaF.clear_folder(f"{common_path}/temp")  # Очистка папки временного хранения
FaF.delete_file(f"{winshell.desktop()}/superior6564App.lnk", )  # Удаление ярлыка приложения
FaF.delete_file(f"{winshell.desktop()}/Update.lnk", )  # Удаление ярлыка обновления приложения
FaF.delete_zip("superior6564App.zip")  # Удаление прошлого zip, нужного для установки
FaF.get_zip("superior6564App.zip", "https://github.com/Superior-GitHub/superior6564App/archive/refs/heads/master.zip")  # Получение нового zip
FaF.extract_zip("superior6564App.zip", os.getcwd(), f"{common_path}/temp")  # Распаковка zip в папку временного хранения
temp_path = f"{common_path}/temp/superior6564App-master"
FaF.extract_zip("Python3109.zip", temp_path, temp_path)  # Распаковка ядра
subprocess.Popen(f"{temp_path}/Python3109/python.exe {temp_path}/Update/Update.py")  # Запуск следущего файла обновления
