import Folders_and_Files as FaF
import Packages
import time

with open("C:/superior6564/path_app.txt", "r") as path_file:
    path_app = path_file.readline()

FaF.clear_folder(f"{path_app}/temp")
time.sleep(10)
