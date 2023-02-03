import subprocess
import sys
import time
import urllib.error
import urllib.request


def check_internet():
    try:
        urllib.request.urlopen("https://github.com/")
        return True
    except urllib.error.URLError:
        return False


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
    if install_stderr[0][:31] == "ERROR: Could not find a version" or install_stderr[0][:27] == "ERROR: Invalid requirement:":
        print("ERROR: Bad name.")
        print("Write the correct name of the package.")
    elif install_stderr[0][:111] == "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken":
        print(f"You need the internet to install {package[0]}.")
    else:
        if 1 < len(package) < 3:
            if output:
                print(f"Package {package[0]} ({package[1]}) installed.")
        elif not (1 < len(package) < 3):
            upgrade_process = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package[0]],
                                                capture_output=True, text=True)
            if output:
                print(f"Package {package[0]} installed.")


def check_package(package_input):
    package = package_input.split("==")
    show_package = subprocess.run([sys.executable, "-m", "pip", "show", package[0]], capture_output=True, text=True)
    if show_package.stderr.split('\n')[0][:30] != "WARNING: Package(s) not found:":
        version_now = show_package.stdout.split("\n")[1][9:]
        version_need = package[1]
        version_now_change = int(version_now.replace(".", ""))
        version_need_change = int(version_need.replace(".", ""))
        if version_now_change >= version_need_change:
            print(f"Version for {package[0]} is ok :)")
        elif version_now_change < version_need_change:
            print(f"Version for {package[0]} is not ok :(")
            install_package(package_input=package_input)
    else:
        print(f"{package[0]} not found :(")
        install_package(package_input=package_input)


print(f"---------------------------")
print(f"Checking required packages.")

check_package("requests==2.28.1")
check_package("winshell==0.6")
check_package("PyWin32==305")

print(f"Required packages checked.")
print(f"---------------------------")

print("You have to wait 10 seconds for the installed packages to load.")
time.sleep(10)
