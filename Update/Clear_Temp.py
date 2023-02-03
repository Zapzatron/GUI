import Folders_and_Files as FaF
import Packages


with open("C:/superior6564/path_app.txt", "r") as path_file:
    common_path = path_file.readline()

FaF.clear_folder(f"{common_path}/temp")
print("Finish.")
Packages.kill_process(10)