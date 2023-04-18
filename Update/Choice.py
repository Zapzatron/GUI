# print("Import Choice")
import os
import tkinter.filedialog
import Folders_and_Files as FaF


def agree_for_run():
    print("If an application was previously installed, it will be uninstalled and reinstalled.")
    agree = " "
    while agree != "":
        agree = input("Press 'enter' to continue or write 'exit' to exit: ")
        if agree == "":
            break
        if agree == "exit":
            exit()


def get_path_for_app(default_path="C:/Zapzatron", app_path="C:/Zapzatron/path_app.txt"):
    agree = " "
    common_path = ""
    while agree != "+" or agree != "-":
        agree = input(f"Default path is {default_path}"
                      f"\nDo you want to change path for app?"
                      f"\nWrite '+' to change or '-' to don`t change: ")
        if not os.path.exists("C:/Zapzatron"):
            os.makedirs("C:/Zapzatron")
        if agree == "+":
            common_path = tkinter.filedialog.askdirectory(initialdir=default_path, title="Choose directory")
            # print(f"Выбранный путь: {common_path}")
            if common_path != default_path and common_path != "":
                common_path = f"{common_path}/Zapzatron_GUI"
            elif common_path == "":
                common_path = default_path
            check_previous_path = ""
            if os.path.exists(app_path):
                with open(app_path, "r") as file_path:
                    check_previous_path = file_path.readline()
                if common_path != check_previous_path:
                    FaF.clear_folder(f"{check_previous_path}/Zapzatron_GUI")
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
                with open(app_path, "w") as file_path:
                    file_path.write(common_path)
                break

    if agree == "+":
        while agree != "+" or agree != "-":
            agree = input(f"App will install in {common_path}."
                          f"\nDo you want to change path for app?"
                          f"\nWrite '+' to change or '-' to don`t change: ")

            if agree == "+":
                common_path = get_path_for_app(default_path=default_path, app_path=app_path)
                break

            if agree == "-":
                break

    return common_path
