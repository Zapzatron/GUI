print("Creating shortcut of superior6564App to Desktop")

import os
import winshell
from win32com.client import Dispatch

desktop = winshell.desktop()
path = os.path.join(desktop, "superior6564App.lnk")
target = r"C:\superior6564\superior6564App-master\GeneratorRUWords.bat"
wDir = r"C:\superior6564\superior6564App-master"
icon = r"C:\superior6564\superior6564App-master\Photos_or_Icons\degget_6564.ico"

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

print()

print("Finish")
