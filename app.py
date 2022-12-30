"""
:authors: Superior_6564
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2022 Superior_6564

MIT License
Copyright (c) 2022 Dear PyGui, LLC
"""


def run():
    """
    Description:
        run() runs app.
    """
    import subprocess
    import sys
    import os
    import time
    import urllib.error
    import urllib.request

    def kill_process(seconds):
        time.sleep(5)
        for i in range(seconds):
            print(f"This app will close in {seconds - i} seconds.")
            time.sleep(1)
        exit()

    def check_internet():
        try:
            urllib.request.urlopen("https://github.com/")
            return True
        except urllib.error.URLError:
            return False
    # print(check_internet())

    def check_file(file, url, folder):
        file_path = ""
        if not (folder is None):
            file_path = f"{os.getcwd()}/{folder}/{file}"
        elif folder is None:
            file_path = file
        if os.path.exists(file_path):
            print(f"{file} is ok :)")
        else:
            if check_internet():
                print(f"{file} is not ok :( I will install this...")
                if not (folder is None):
                    try:
                        os.mkdir(folder)
                    except FileExistsError:
                        pass
                with open(file_path, "wb") as new_file:
                    new_file.write(requests.get(url).content)
            elif not check_internet():
                print(f"{file} is not okay.")
                print("You don`t have files I need. I can`t let you go any further.")
                kill_process(10)

    def install_package(package_input: str, output: bool = True, is_run: bool = False):
        """
        Args:
            package_input (str): Name of package.
            output (bool): Info about process will be output or not.
            is_run (bool): Don`t change this please :)
        Description:
            package_input:
                You can download a specific version. \n
                Write in the format: package==version.\n
            install_package() installs package.
        """
        is_app = True
        package = package_input.split("==")

        if output:
            print(f"Trying to install package {package[0]}...")
        if is_app:
            if is_run:
                dpg.delete_item("install_info", children_only=True)
                dpg.delete_item("install_success", children_only=True)
                dpg.delete_item("install_error", children_only=True)
        install_process = subprocess.run([sys.executable, "-m", "pip", "install", package_input], capture_output=True, text=True)
        install_stderr = install_process.stderr.split('\n')
        if install_stderr[0][:31] == "ERROR: Could not find a version" or install_stderr[0][:27] == "ERROR: Invalid requirement:":
            print("ERROR: Bad name.")
            print("Write the correct name of the package.")
            if is_app:
                if is_run:
                    dpg.add_text(tag="Error description 1", pos=[285, 160], default_value="ERROR: Bad name.",
                                    parent="install_error")
                    dpg.add_text(tag="Error description 2", pos=[285, 180],
                                    default_value="Write the correct name of the package.", parent="install_error")
        elif install_stderr[0][:111] == "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken":
            print(f"You need the internet to install {package[0]}.")
        else:
            if 1 < len(package) < 3:
                if output:
                    print(f"Package {package[0]} ({package[1]}) installed.")
                    if is_app:
                        if is_run:
                            dpg.add_text(tag="Good description 1", pos=[285, 160], default_value=f"Package {package[0]} ({package[1]}) installed.", parent="install_success")
            elif not (1 < len(package) < 3):
                upgrade_process = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package[0]],
                                                    capture_output=True, text=True)
                if output:
                    print(f"Package {package[0]} installed.")
                    if is_app:
                        if is_run:
                            dpg.add_text(tag="Good description 1", pos=[285, 160], default_value=f"Package {package[0]} installed.", parent="install_success")

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

    files_data = [
        ["NotoSans-Regular.ttf",
         "https://github.com/Superior-GitHub/superior6564App/raw/master/Fonts/NotoSans-Regular.ttf",
         "Fonts"],
        ["russian_nouns.txt",
         "https://github.com/Superior-GitHub/superior6564App/raw/master/Generator_dictionaries/russian_nouns.txt",
         "Generator_dictionaries"],
        ["russian_nouns_without_io.txt",
         "https://github.com/Superior-GitHub/superior6564App/raw/master/Generator_dictionaries/russian_nouns_without_io.txt",
         "Generator_dictionaries"],
        ["degget_elite.jpg",
         "https://github.com/Superior-GitHub/superior6564App/raw/master/Photos_or_Icons/degget_elite.jpg",
         "Photos_or_Icons"],
        ["readme.md",
         "https://github.com/Superior-GitHub/superior6564App/raw/master/readme.md",
         None]
    ]

    print(f"---------------------------")
    print(f"Checking required packages.")

    check_package("requests==2.28.1")
    check_package("dearpygui==1.7.1")
    check_package("superior6564==0.3.4")

    print(f"Required packages checked.")
    print(f"---------------------------")
    try:
        import requests
        import dearpygui
    except ModuleNotFoundError:
        print("You don`t have the packages I need. I can`t let you go any further.")
        kill_process(10)

    print(f"--------------------------")
    print(f"Checking required files...")
    for i in range(len(files_data)):
        check_file(file=files_data[i][0], url=files_data[i][1], folder=files_data[i][2])
    print(f"Required files checked.")
    print(f"--------------------------")

    import dearpygui.dearpygui as dpg
    import webbrowser
    import os

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

    def print_name_def(name: str):
        print(f"-{'-' * len(name)}-")
        print(f"|{name}|")
        print(f"-{'-' * len(name)}-")

    def generator_ru_words():
        print_name_def("generator_ru_words()")

        width, height, channels, data = dpg.load_image('Photos_or_Icons/degget_elite.jpg')

        with dpg.texture_registry():
            dpg.add_static_texture(width, height, data, tag="image_1", parent="generator_group")

        def update_word_list():
            print_name_def("update_word_list()")
            try:
                os.remove(f"{os.getcwd()}/{files_data[2][2]}/{files_data[2][0]}")
            except FileNotFoundError:
                pass
            check_file(file=files_data[2][0], url=files_data[2][1], folder=files_data[2][2])

        def gen_value():
            def generator_process(all_of_letters: str, length_of_words: int):
                is_app = True
                if is_app:
                    all_of_letters = to_cyr(all_of_letters)
                    dpg.delete_item("error_group", children_only=True)
                if all_of_letters == "":
                    all_of_letters = "лупогр"

                if length_of_words == "":
                    length_of_words = 3

                # alphabet_er_ru = set("àáâãäå¸æçèéêëìíîïðñòóôõö÷øùúûüýþÿ")
                alphabet_ru = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
                if not isinstance(all_of_letters, str) or alphabet_ru.isdisjoint(all_of_letters.lower()):
                    print("ValueError: You need to write string of RU letters which you have.")
                    if is_app:
                        dpg.add_text(tag="Error string generator 1", pos=[290, 365], default_value="ValueError:",
                                     parent="error_group")
                        dpg.add_text(tag="Error string generator 2", pos=[290, 385],
                                     default_value="You need to write string of RU letters.", parent="error_group")
                    return
                else:
                    all_of_letters = all_of_letters.lower()

                if not isinstance(length_of_words, int):
                    print("ValueError: You need to write length of words, which you need.")
                    if is_app:
                        dpg.add_text(tag="Error int generator 1", pos=[290, 365], default_value="ValueError:",
                                     parent="error_group")
                        dpg.add_text(tag="Error int generator 2", pos=[290, 385],
                                     default_value="You need to write length of words.", parent="error_group")
                    return
                elif not is_app:
                    if length_of_words >= 27:
                        print("ValueError: You need to write length of words, which under 16.")
                        # if is_app:
                        #     dpg.add_text(tag="Error int generator 3", pos=[290, 365], default_value="ValueError:",
                        #                  parent="error_group")
                        #     dpg.add_text(tag="Error int generator 4", pos=[290, 385],
                        #                  default_value="You need to write length under 16.", parent="error_group")
                        return

                print(f"Letters: {all_of_letters}\nLength: {length_of_words}")

                with open('Generator_dictionaries/russian_nouns_without_io.txt', encoding='utf-8') as f1:
                    result = [f"Words from {length_of_words} letters:"]
                    count_words = 0
                    line = ""
                    while line != "-----":
                        line = f1.readline()
                        if "\n" in line:
                            line = line[:-1]
                        if len(line) == length_of_words and line != "" and line != "-----":
                            count = 0
                            for letter in line:
                                if letter in all_of_letters and line.count(letter) <= all_of_letters.count(letter):
                                    count += 1
                            if count == length_of_words and line not in result:
                                result.append(line)
                    if is_app:
                        dpg.delete_item('text_group', children_only=True)
                        left_pos = 8
                        right_pos = 440
                        count = 0
                        for line in result[1:]:
                            count_words += 1
                            dpg.add_text(pos=[left_pos, right_pos], default_value=f"{count_words} word: {line}", parent='text_group')
                            right_pos += 20
                            count += 1
                            if count == 8:
                                count = 0
                                left_pos += 160
                                right_pos = 440
                    else:
                        for line in result:
                            if line[:10] != "Words from":
                                count_words += 1
                                print(f"{count_words} word: {line}")
                            else:
                                print(line)
                    print(f"Count of words: {count_words}")
            print_name_def("generator_ru_words()")
            letters_get = dpg.get_value('Input all letters')
            length_get = dpg.get_value('Input length of words')
            if length_get != "":
                length_get = int(length_get)
            generator_process(all_of_letters=letters_get, length_of_words=length_get)

        combo_values = ["3", "4", "5", "6", "7"]
        dpg.add_text(tag="Text 'Update'", pos=[15, 245], default_value="Update", parent="generator_group")
        dpg.add_text(tag="Text 'word'", pos=[20, 275], default_value="word", parent="generator_group")
        dpg.add_text(tag="Text 'list'", pos=[25, 305], default_value="list", parent="generator_group")
        dpg.add_button(tag="Button for update word list", label="Update", callback=update_word_list, pos=[10, 335],
                       parent="generator_group")
        dpg.add_text(tag="Text for writing letters", pos=[290, 215],
                     default_value="Write all of letters which do you have:", parent="generator_group")
        dpg.add_input_text(tag="Input all letters", width=270, height=300, pos=[284, 245], parent="generator_group")
        dpg.add_text(tag="Text for choosing length of words", pos=[290, 275],
                     default_value="Choose length of words do you need:", parent="generator_group")
        dpg.add_combo(tag="Input length of words", width=270, pos=[285, 305], items=combo_values,
                      parent="generator_group")
        dpg.add_button(tag="Button for sending parameters", label="Send parameters", callback=gen_value, pos=[355, 340],
                       parent="generator_group")
        dpg.add_text(tag="Text for results", pos=[8, 415], default_value="Results:", parent="generator_group")
        dpg.add_image(tag="Image of Elite Degget 1", texture_tag="image_1", pos=[79, 215], parent="generator_group")
        dpg.add_image(tag="Image of Elite Degget 2", texture_tag="image_1", pos=[559, 215], parent="generator_group")
        dpg.draw_line(p1=(-10, 382), p2=(820, 382), parent="generator_group")
        dpg.draw_line(p1=(-4, 382), p2=(-4, 580), parent="generator_group")
        dpg.draw_line(p1=(805, 382), p2=(805, 580), parent="generator_group")
        dpg.draw_line(p1=(-10, 580), p2=(820, 580), parent="generator_group")
        dpg.bind_font(default_font)
        dpg.bind_item_font("Input all letters", default_font)

        with dpg.group(tag='text_group', parent="generator_group"):
            pass

        with dpg.group(tag='error_group', parent="generator_error"):
            pass

    def get_info():
        print_name_def("get_info()")

        def open_home_page():
            webbrowser.open_new_tab("https://github.com/Superior-GitHub/superior6564App/tree/master")

        package_show = subprocess.run([sys.executable, "-m", "pip", "show", "Superior6564"], capture_output=True,
                                      text=True)
        if package_show.stderr.split('\n')[0][:30] != "WARNING: Package(s) not found:":
            lines = package_show.stdout.split('\n')
            dpg.add_text(tag="Name", pos=[5, 45], default_value=lines[0], parent="info_group")
            dpg.add_text(tag="Version", pos=[5, 70], default_value=lines[1], parent="info_group")
            dpg.add_text(tag="Home-Page", pos=[5, 95], default_value=lines[3][:10], parent="info_group")
            dpg.add_text(tag="Author", pos=[5, 120], default_value=lines[4], parent="info_group")
            dpg.add_text(tag="Author-email", pos=[5, 145], default_value="Email:" + lines[5][13:], parent="info_group")
            dpg.add_text(tag="License", pos=[5, 170], default_value=lines[6][:-18], parent="info_group")
            dpg.add_button(tag="Open Home-Page", label="Open", callback=open_home_page, pos=[100, 95],
                           parent="info_group")
        else:
            print("Before you can get info about the package, you have to download it.")

    def install_package_app():
        print_name_def("install_package()")

        def get_and_install():
            print_name_def("install_package()")
            package_input = dpg.get_value("Input name of package")
            install_package(package_input=package_input, is_run=True)

        dpg.add_text(tag="Install package", pos=[285, 20], default_value="Install packages:", parent="install_package")
        dpg.add_text(tag="Install package description", pos=[285, 40],
                     default_value="Write the correct name of the package:", parent="install_package")
        dpg.add_input_text(tag="Input name of package", width=265, height=300, pos=[285, 70], parent="install_package")
        dpg.add_button(tag="Button for sending name of package", label="Send", callback=get_and_install, pos=[285, 105],
                       parent="install_package")
        dpg.add_text(tag="Text for status of installing", pos=[285, 135], default_value="Status:",
                     parent="install_package")
        dpg.draw_line(p1=(270, 180), p2=(550, 180), parent="install_package")
        with dpg.group(tag="install_error"):
            pass
        with dpg.group(tag="install_info"):
            pass
        with dpg.group(tag="install_success"):
            pass
        dpg.add_text(tag="Info for install 1", pos=[285, 160], default_value="You can download a specific version.",
                     parent="install_info")
        dpg.add_text(tag="Info for install 2", pos=[285, 180], default_value="Write in the format: package==version.",
                     parent="install_info")

    def pip_upgrade():
        print_name_def("pip_upgrade()")

        def upgrade():
            print_name_def("pip_upgrade()")
            dpg.delete_item("pip_upgrade", children_only=True)
            pip_version = \
            subprocess.run([sys.executable, "-m", "pip", "show", "pip"], capture_output=True, text=True).stdout.split(
                '\n')[1][9:]
            print(f"Version before upgrading is {pip_version}.")
            dpg.add_text(tag="Version PIP before upgrading", pos=[560, 110],
                         default_value=f"Version before upgrading is {pip_version}", parent="pip_upgrade")
            upgrade_pip = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
                                         capture_output=True, text=True)
            print("Upgrading...")
            dpg.add_text(tag="Text of status for pip upgrading", pos=[560, 130], default_value="Upgrading...",
                         parent="pip_upgrade")
            pip_version = \
            subprocess.run([sys.executable, "-m", "pip", "show", "pip"], capture_output=True, text=True).stdout.split(
                '\n')[1][9:]
            print(f"Version after upgrading is {pip_version}.")
            dpg.add_text(tag="Version PIP after upgrading", pos=[560, 150],
                         default_value=f"Version after upgrading is {pip_version}", parent="pip_upgrade")

        dpg.add_text(tag="Pip upgrade", pos=[560, 20], default_value="Pip upgrade:", parent="pip_upgrade")
        dpg.add_text(tag="Pip upgrade description", pos=[560, 40], default_value="Click on the button to upgrade pip.",
                     parent="pip_upgrade")
        dpg.add_button(tag="Button for upgrading pip", label="Send", callback=upgrade, pos=[660, 65],
                       parent="pip_upgrade")
        dpg.add_text(tag="Text for status of upgrading", pos=[560, 90], default_value="Status:", parent="pip_upgrade")
        dpg.draw_line(p1=(550, -10), p2=(550, 382), parent="pip_upgrade")
        dpg.draw_line(p1=(550, 180), p2=(820, 180), parent="pip_upgrade")

    with dpg.window(tag='main_window', label="Main", width=820, height=655, no_move=True, no_resize=True,
                    no_close=True, no_collapse=True):
        dpg.add_text(tag="Information", pos=[5, 20], default_value="Information:")
        dpg.draw_line(p1=(270, -10), p2=(270, 382), parent="info_group")
        dpg.draw_line(p1=(-10, 180), p2=(270, 180), parent="info_group")
        # dpg.add_button(tag="Button for showing info", label="Show info", callback=get_info, pos=[190, 20], parent="info_group")
        get_info()
        generator_ru_words()
        install_package_app()
        pip_upgrade()
        with dpg.group(tag='info_group'):
            pass
        with dpg.group(tag='generator_group'):
            pass
        with dpg.group(tag='install_package'):
            pass
        with dpg.group(tag="pip_upgrade"):
            pass
    dpg.create_viewport(title='App', width=831, height=655, resizable=False)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


run()
