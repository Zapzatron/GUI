import Packages

Packages.check_req_packages()  # Проверка нужных пакетов
# print()
Packages.try_import()  # Проверка импортов

import dearpygui.dearpygui as dpg
import tkinter.filedialog
import webbrowser
import os
import subprocess
import Folders_and_Files as FaF
import winshell

dpg.create_context()

big_let_start = 0x00C0  # Capital "A" in cyrillic alphabet
big_let_end = 0x00DF  # Capital "Я" in cyrillic alphabet
small_let_end = 0x00FF  # small "я" in cyrillic alphabet
remap_big_let = 0x0410  # Starting number for remapped cyrillic alphabet
alph_len = big_let_end - big_let_start + 1  # adds the shift from big letters to small
alph_shift = remap_big_let - big_let_start  # adds the shift from remapped to non-remapped
# chars_remap = {OLD: NEW}
chars_remap = {0x00A8: 0x0401,  # Ё
               0x00B8: 0x0451,  # ё
               0x00AF: 0x0407,  # Ї
               0x00BF: 0x0457,  # ї
               0x00B2: 0x0406,  # І
               0x00B3: 0x0456,  # і
               0x00AA: 0x0404,  # Є
               0x00BA: 0x0454}  # є

with dpg.font_registry():
    with dpg.font("Fonts/NotoSans-Regular.ttf", 20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        biglet = remap_big_let  # Starting number for remapped cyrillic alphabet
        for i1 in range(big_let_start, big_let_end + 1):  # Cycle through big letters in cyrillic alphabet
            dpg.add_char_remap(i1, biglet)  # Remap the big cyrillic letter
            dpg.add_char_remap(i1 + alph_len, biglet + alph_len)  # Remap the small cyrillic letter
            biglet += 1  # choose next letter
        for char in chars_remap.keys():
            dpg.add_char_remap(char, chars_remap[char])


def to_cyr(instr):  # conversion function
    out = []  # start with empty output
    for i in range(0, len(instr)):  # cycle through letters in input string
        if ord(instr[i]) in chars_remap:
            out.append(chr(chars_remap[ord(instr[i])]))
        elif ord(instr[i]) in range(big_let_start, small_let_end + 1):  # check if the letter is cyrillic
            out.append(chr(ord(instr[i]) + alph_shift))  # if it is change it and add to output list
        else:
            out.append(instr[i])
    return ''.join(out)


with dpg.theme() as bright_theme:
    with dpg.theme_component(dpg.mvAll):
        # Background
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, [244, 244, 244])
        # Buttons
        dpg.add_theme_color(dpg.mvThemeCol_Button, (244, 244, 244), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (55, 55, 55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Border, value=(55, 55, 55),category=dpg.mvThemeCat_Core)
        # Combo
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (244, 244, 244), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (244, 244, 244), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Header, (244, 244, 244), category=dpg.mvThemeCat_Core)
        # Text
        dpg.add_theme_color(dpg.mvThemeCol_Text, (55, 55, 55), category=dpg.mvThemeCat_Core)

with dpg.theme() as dark_theme:
    with dpg.theme_component(dpg.mvAll):
        # Background
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, [55, 55, 55])
        # Buttons
        dpg.add_theme_color(dpg.mvThemeCol_Button, (55, 55, 55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (244, 244, 244), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Border, value=(244, 244, 244),category=dpg.mvThemeCat_Core)
        # Combo
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (55, 55, 55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (55, 55, 55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Header, (55, 55, 55), category=dpg.mvThemeCat_Core)
        # Text
        dpg.add_theme_color(dpg.mvThemeCol_Text, (244, 244, 244), category=dpg.mvThemeCat_Core)

language = "Русский"

combo_themes = {"Русский": {"Светлая": "Светлая", "Тёмная": "Тёмная"},
                "English": {"Светлая": "Bright", "Тёмная": "Dark"}}
combo_themes_list = {"Русский": ["Светлая", "Тёмная"],
                     "English": ["Bright", "Dark"]}

theme = "Светлая"
text = {"Русский":
            {"Вступление": "Привет, я установлю приложение для тебя. Но только если у меня будет доступ в интернет.\n"
                           "Если приложение уже установлено, оно будет удалено и заново установлено.\n"
                           "Устанавливая приложение, вы соглашаетесь со всеми условиями, описанными в лицензии.",
             "Вопрос о смене пути": "Хочешь поменять путь до приложения?",
             "Да": "Да",
             "Нет": "Нет",
             "Выбор пути": "Выберите путь для приложения:",
             "Кнопка выбора пути": "Выбор",
             "Кнопка запуска установщика": "Запуск установщика",
             "Удаление приложения": "Удаление предыдущего приложения.",
             "Установка приложения": "Установка нового приложения.",
             "Установка завершена": "Установка приложения завершена.",
             "Лицензия": "Лицензия ---> https://github.com/Superior-GitHub/superior6564App/raw/master/LICENSES/LICENSE",
             "Открытие лицензии": "Открыть лицензию"},
        "English":
            {"Вступление": "Hi, I'll install the app for you. But only if I have access to the Internet.\n"
                           "If the app is already installed, it will be uninstalled and reinstalled.\n"
                           "By installing the application, you agree to all the terms and conditions described in the license.",
             "Вопрос о смене пути": "Do you want to change the path to the application?",
             "Да": "Yes",
             "Нет": "No",
             "Выбор пути": "Select the path for the application:",
             "Кнопка выбора пути": "Selection",
             "Кнопка запуска установщика": "Running the installer",
             "Удаление приложения": "Deleting previous application.",
             "Установка приложения": "Installing the new application.",
             "Установка завершена": "The installation of the application is complete.",
             "Лицензия": "License ---> https://github.com/Superior-GitHub/superior6564App/raw/master/LICENSES/LICENSE",
             "Открытие лицензии": "Open a license"}}

default_path=r"C:/superior6564"
path_app = r"C:/superior6564"
is_path_need_change = False


def choose_language():
    temp_lang = dpg.get_value("Выбор языка")
    global language
    if temp_lang != language:
        language = temp_lang
        dpg.set_value("Текст 'Вступление'", text[language]["Вступление"])
        if is_path_need_change:
            dpg.set_value("Текст 'Выбор пути'", text[language]["Выбор пути"])
            dpg.set_item_label("Кнопка 'Выбор пути'", text[language]["Кнопка выбора пути"])
        dpg.set_value("Текст 'Лицензия'", text[language]["Лицензия"])
        dpg.set_item_label("Кнопка 'Открытие лицензии'", text[language]["Открытие лицензии"])
        if theme == "Светлая" or theme == "Bright":
            dpg.set_value("Выбор темы", combo_themes[language]["Светлая"])
        elif theme == "Тёмная" or theme == "Dark":
            dpg.set_value("Выбор темы", combo_themes[language]["Тёмная"])
        dpg.configure_item("Выбор темы", items=combo_themes_list[language])
        if dpg.does_item_exist("Текст 'Вопрос о смене пути'"):
            dpg.set_value("Текст 'Вопрос о смене пути'", text[language]["Вопрос о смене пути"])
            dpg.set_item_label("Да", text[language]["Да"])
            dpg.set_item_label("Нет", text[language]["Нет"])
        if dpg.does_item_exist("Кнопка 'Запуск установщика'"):
            dpg.set_item_label("Кнопка 'Запуск установщика'", text[language]["Кнопка запуска установщика"])
        if dpg.does_item_exist("Текст 'Удаление приложения'"):
            dpg.set_value("Текст 'Удаление приложения'", text[language]["Удаление приложения"])
        if dpg.does_item_exist("Текст 'Установка приложения'"):
            dpg.set_value("Текст 'Установка приложения'", text[language]["Установка приложения"])
        if dpg.does_item_exist("Текст 'Установка завершена'"):
            dpg.set_value("Текст 'Установка завершена'", text[language]["Установка завершена"])


def choose_themes():
    temp_theme = dpg.get_value("Выбор темы")
    global theme
    if temp_theme != theme:
        theme = temp_theme
        if theme == "Светлая" or theme == "Bright":
            dpg.bind_theme(bright_theme)
        elif theme == "Тёмная" or theme == "Dark":
            dpg.bind_theme(dark_theme)


is_installer_running = False


def choose_path(sender):
    if not is_installer_running:
        global path_app
        path_app = tkinter.filedialog.askdirectory(initialdir=path_app)
        if path_app:
            # print(path_app)
            dpg.set_value("Выбор пути", path_app)


def is_change(sender):
    global is_path_need_change
    if sender == "Да" or sender == "Yes":
        is_path_need_change = True
        dpg.delete_item("Текст 'Вопрос о смене пути'")
        dpg.delete_item("Да")
        dpg.delete_item("Нет")
        dpg.add_text(tag="Текст 'Выбор пути'", pos=[15, 65], default_value=text[language]["Выбор пути"],
                     parent="Группа Текст")
        dpg.add_input_text(tag="Выбор пути", width=480, height=300, pos=[15, 95], default_value=path_app, parent="Группа Текст")
        dpg.add_button(tag="Кнопка 'Выбор пути'", label=text[language]["Кнопка выбора пути"], pos=[500, 95],
                       callback=choose_path, parent="Группа Текст")
        dpg.add_button(tag="Кнопка 'Запуск установщика'", label=text[language]["Кнопка запуска установщика"],
                       pos=[190, 125], callback=run_installer, parent="Группа Текст")
    elif sender == "Нет" or sender == "No":
        is_path_need_change = False
        dpg.delete_item("Текст 'Вопрос о смене пути'")
        dpg.delete_item("Да")
        dpg.delete_item("Нет")
        dpg.add_button(tag="Кнопка 'Запуск установщика'", label=text[language]["Кнопка запуска установщика"],
                       pos=[190, 125], callback=run_installer, parent="Группа Текст")


def run_installer():
    global is_installer_running
    global path_app
    is_installer_running = True
    dpg.delete_item("Кнопка 'Запуск установщика'")
    path_file = "C:/superior6564/path_app.txt"
    if not os.path.exists("C:/superior6564"):
        os.makedirs("C:/superior6564")
    if is_path_need_change:
        if path_app != default_path and path_app != "":
            path_app = f"{path_app}/superior6564"
        elif path_app == "":
            path_app = default_path
        check_previous_path = ""
        if os.path.exists(path_file):
            with open(path_file, "r") as file_path:
                check_previous_path = file_path.readline()
            if path_app != check_previous_path:
                FaF.clear_folder(f"{check_previous_path}/superior6564")
        with open(path_file, "w") as file_path:
            file_path.write(path_app)
    else:
        if os.path.exists(path_file):
            with open(path_file, "r") as file_path:
                path_app = file_path.readline()
        else:
            path_app = default_path
            with open(path_file, "w") as file_path:
                file_path.write(path_app)

    dpg.add_text(tag="Текст 'Удаление приложения'", pos=[15, 130],
                 default_value=text[language]["Удаление приложения"], parent="Группа Текст")
    FaF.clear_folder(f"{path_app}/temp")  # Очистка папки временного хранения
    FaF.delete_file(f"{winshell.desktop()}/superior6564App.lnk", )  # Удаление ярлыка приложения
    FaF.delete_file(f"{winshell.desktop()}/Update.lnk", )  # Удаление ярлыка обновления приложения
    FaF.delete_zip("superior6564App.zip")  # Удаление прошлого zip, нужного для установки
    dpg.add_text(tag="Текст 'Установка приложения'", pos=[15, 160],
                 default_value=text[language]["Установка приложения"], parent="Группа Текст")
    FaF.get_zip("superior6564App.zip",
                "https://github.com/Superior-GitHub/superior6564App/archive/refs/heads/master.zip")  # Получение нового zip
    FaF.extract_zip("superior6564App.zip", os.getcwd(),
                    f"{path_app}/temp")  # Распаковка zip в папку временного хранения
    temp_path = f"{path_app}/temp/superior6564App-master"
    FaF.extract_zip("Python3109.zip", temp_path, temp_path)  # Распаковка ядра
    # subprocess.Popen(f"start {temp_path}/Python3109/pythonw.exe {temp_path}/Update_2.0/Updater.py")  # Запуск следущего файла обновления
    subprocess.Popen(f"{temp_path}/Python3109/python.exe {temp_path}/Update_2.0/Updater.py")  # Запуск следущего файла обновления


def open_license():
    webbrowser.open_new_tab("https://github.com/Superior-GitHub/superior6564App/raw/master/LICENSES/LICENSE")


with dpg.window(tag='Установщик', label="Окно 1", width=960, height=540, no_move=True,
                no_resize=True, no_close=True, no_collapse=True, show=False) as first_window:
    combo_languages = ["Русский", "English"]
    dpg.add_combo(tag="Выбор языка", width=120, pos=[810, 15], default_value=combo_languages[0],
                  items=combo_languages, callback=choose_language)
    dpg.add_combo(tag="Выбор темы", width=120, pos=[810, 45], default_value=combo_themes[language][theme],
                 items=combo_themes_list[language], callback=choose_themes)
    dpg.add_text(tag="Текст 'Вступление'", pos=[15, 5], default_value=text[language]["Вступление"], parent="Группа Текст")
    dpg.add_text(tag="Текст 'Вопрос о смене пути'", pos=[15, 65], default_value=text[language]["Вопрос о смене пути"], parent="Группа Текст")
    dpg.add_button(tag="Да", label=text[language]["Да"], pos=[100, 95], callback=is_change, parent="Группа Текст")
    dpg.add_button(tag="Нет", label=text[language]["Нет"], pos=[200, 95], callback=is_change, parent="Группа Текст")
    # dpg.add_text(tag="Текст 'Выбор пути'", pos=[15, 65], default_value=text[language]["Выбор пути"], parent="Группа Текст")
    # dpg.add_input_text(tag="Выбор пути", width=480, height=300, pos=[15, 95], default_value=path_app)
    # dpg.add_button(tag="Кнопка 'Выбор пути'", label=text[language]["Кнопка выбора пути"], pos=[500, 95], callback=choose_path)
    # dpg.add_button(tag="Кнопка 'Запуск установщика'", label=text[language]["Кнопка запуска установщика"], pos=[190, 125], callback=run_installer, parent="Группа Текст")
    dpg.add_text(tag="Текст 'Лицензия'", pos=[120, 435], default_value=text[language]["Лицензия"], parent="Группа Текст")
    dpg.add_button(tag="Кнопка 'Открытие лицензии'", label=text[language]["Открытие лицензии"], pos=[390, 460], callback=open_license)
    with dpg.group(tag="Группа Текст"):
        pass

dpg.bind_font(default_font)
dpg.bind_theme(bright_theme)
dpg.set_primary_window("Установщик", True)
dpg.show_item("Установщик")

dpg.create_viewport(title='superior6564 installer', width=960, height=540, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
