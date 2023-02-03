# print("Import Packages")
import subprocess
import sys
import time


def kill_process(seconds):
    time.sleep(5)
    for i in range(seconds):
        print(f"Installer will close in {seconds - i} seconds.")
        time.sleep(1)
    exit()


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

    if output:
        print(f"Trying to install package {package[0]}...")
    install_process = subprocess.run([sys.executable, "-m", "pip", "install", package_input], capture_output=True, text=True)
    install_stderr = install_process.stderr.split('\n')
    # print(install_process.stdout.split('\n'))
    # print(install_stderr)
    if install_stderr[0][:31] == "ERROR: Could not find a version" or install_stderr[0][:27] == "ERROR: Invalid requirement:":
        print("ERROR: Bad name.")
        print("Write the correct name of the package.")
    elif install_stderr[0][:111] == "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken":
        print(f"You need the internet to install {package[0]}.")
    else:
        if len(package) == 2:
            if output:
                print(f"Package {package[0]} ({package[1]}) installed.")
        elif len(package) != 2:
            upgrade_process = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package[0]],
                                                capture_output=True, text=True)
            if output:
                print(f"Package {package[0]} installed.")


def check_req_packages():
    print(f"---------------------------")
    print(f"Checking required packages.")
    req_path = "Update/Requirements/requirements.txt"
    # install_packages = subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_file], capture_output=True, text=True)
    # print(install_packages.stdout)
    with open(req_path, "r") as req_file:
        for package_input in req_file:
            if package_input[-1] == "\n":
                package_input = package_input[:-1]
            package = package_input.split("==")
            show_package = subprocess.run([sys.executable, "-m", "pip", "show", package[0]],
                                          capture_output=True, text=True)
            if show_package.stderr.split('\n')[0][:30] != "WARNING: Package(s) not found:":
                version_now = show_package.stdout.split("\n")[1][9:]
                version_need = package[1]
                if version_now == version_need:
                    print(f"Version for {package[0]} is ok :)")
                elif version_now != version_need:
                    print(f"Version for {package[0]} is not ok :(")
                    install_package(package_input)
            else:
                print(f"{package[0]} not found :(")
                install_package(package_input)
    # print("Process...")
    # print(install_packages.stderr)
    print(f"Required packages checked.")
    print(f"---------------------------")
    print("You have to wait 10 seconds for the installed packages to load.")
    time.sleep(10)


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
        print("You don`t have the packages I need. I can`t let you go any further.")
        kill_process(10)
    else:
        print("Required packages is ok :)")