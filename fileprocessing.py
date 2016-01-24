__author__ = 'junlingwang'

import webbrowser
import os


def open_web_page(word_str):
    webbrowser.open_new_tab("http://www.oxfordlearnersdictionaries.com/definition/english/" + word_str + "_1")


def search_for_voice(file_name):
    with open('/home/junlingwang/Desktop/Vocabulary trainning/'+file_name+'.txt', 'r') as word_file:
        lines = word_file.readlines()  # lines is a list of strings
    i = 0
    for line in lines:
        stripped_str = line.strip()
        if '/' in stripped_str or ' ' in stripped_str:
            continue
        str_list = stripped_str.split(',')
        word_str = str_list[0]
        open_web_page(word_str)
        i += 1
        control_key = input('X to exit, any key to continue' +' ' + str(i))
        if control_key == 'X' or control_key == 'x':
            break


def file_formatting(file_name):
    with open('/home/junlingwang/Desktop/Vocabulary trainning/'+file_name+'.txt', 'r') as word_file:
        lines = word_file.readlines()  # lines is a list of strings
    index = 0
    while index < len(lines):
        stripped_str = lines[index].strip()
        if ',' in stripped_str:
            index += 1
            continue
        str_list = stripped_str.split(' ')
        formatted_string = str_list[0]
        i = 1
        j = 1
        while i < len(str_list):
            if str_list[i] != '':
                if j == 1:
                    if str_list[i][0] != '/':
                        formatted_string += ',/' + str_list[i]
                    else:
                        formatted_string += ',' + str_list[i]
                    if str_list[i][-1] != '/':
                        formatted_string += '/'
                    j += 1
                else:
                    formatted_string += ',' + str_list[i]
            i += 1
        lines[index] = formatted_string + '     \n'  # if there is no '\n', the lines will become a single one
        index += 1
    with open('/home/junlingwang/Desktop/Vocabulary trainning/'+file_name+'.txt', 'w') as word_file:
        word_file.writelines(lines)


def search_for_meaning(file_name):
    with open('/home/junlingwang/Desktop/Vocabulary trainning/'+file_name+'.txt', 'r') as word_file:
        lines = word_file.readlines()  # lines is a list of strings
    i = 0
    for line in lines:
        stripped_str = line.strip()
        if not ('/,' in stripped_str and '0' not in stripped_str and stripped_str[-1] == ','):
            continue
        str_list = stripped_str.split(',')
        word_str = str_list[0]
        open_web_page(word_str)
        i += 1
        control_key = input('X to exit, any key to continue' +' ' + str(i))
        if control_key == 'X' or control_key == 'x':
            break


if __name__ == '__main__':
    # search_for_voice('formatted')
    file_formatting('formatted')
    # search_for_meaning('formatted')
