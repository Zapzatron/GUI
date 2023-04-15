import subprocess
import sys
import time
import tkinter.messagebox


def install_package(package_input: str, output: bool = True):
    """
    Args:
        package_input (str): Name of package.
        output (bool): Info about process will be output or not.
    Description:
        package_input:
            You can download a specific version. \n
            Write in the format: package==version.\n
        install_package() installs package.
    """
    package = package_input.split("==")
    install_process = subprocess.run([sys.executable, "-m", "pip", "install", package_input], capture_output=True, text=True)
    install_stderr = install_process.stderr.split('\n')
    if install_stderr[0][:31] == "ERROR: Could not find a version" or install_stderr[0][:27] == "ERROR: Invalid requirement:":
        message = "Required packages is not ok :(\n" \
                  "Требуемые пакеты не в порядке :("
        tkinter.messagebox.showerror("Error", message)
        exit()
    else:
        if len(package) != 2:
            upgrade_process = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package[0]],
                                                capture_output=True, text=True)


def check_req_packages():
    message = "I need to check required packages.\nDo you agree to wait a little while?" \
              "\nМне нужно проверить необходимые пакеты.\nВы согласны немного подождать?"
    if not tkinter.messagebox.askyesno("Question from Installer", message):
        exit()
    requirements = ["requests==2.28.1", "winshell==0.6", "PyWin32==305", "dearpygui==1.7.1"]
    for package_input in requirements:
        package = package_input.split("==")
        show_package = subprocess.run([sys.executable, "-m", "pip", "show", package[0]],
                                      capture_output=True, text=True)
        if show_package.stderr.split('\n')[0][:30] != "WARNING: Package(s) not found:":
            version_now = show_package.stdout.split("\n")[1][9:]
            version_need = package[1]
            if version_now != version_need:
                install_package(package_input)
        else:
            install_package(package_input)
    time.sleep(5)


def try_import():
    try:
        import shutil
        import time
        import zipfile
        import requests
        import os
        import subprocess
        import winshell
        import tkinter.filedialog
        from win32com.client import Dispatch
    except ModuleNotFoundError:
        message = "Required packages is not ok :(\n" \
                  "Требуемые пакеты не в порядке :("
        tkinter.messagebox.showerror("Error", message)
        exit()
