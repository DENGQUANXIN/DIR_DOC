#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dir_doc.py
@Time    :   2019/04/13 23:09:51
@Author  :   DoubtD
@Version :   1.0
@Desc    :   A script for writing document of directory files.
'''

# here put the import lib
import os


DOC_FILENAME = '.DIR.md'
FRONT_STR = ['├──', '└──']
BANK = ' '
dir_path = os.getcwd()
doc_path = os.path.join(dir_path, DOC_FILENAME)


def read_dir_doc():
    contents, exist_file_list = [], []
    if not os.path.exists(doc_path):
        return contents, exist_file_list
    with open(doc_path, 'r') as fd:
        lines = fd.readlines()
        for line in lines:
            line = line.strip().split()
            contents.append(line)
            exist_file_list.append(line[1])
    return contents, exist_file_list


def write_dir_doc(contents, max_len):
    doc_path = os.path.join(dir_path, DOC_FILENAME)
    with open(doc_path, 'w') as fd:
        for item in contents:
            line = ""
            line += item[0]
            line += BANK
            line += item[1]
            line += BANK * (max_len - len(item[1]) + 1)
            line += item[2]
            line += BANK
            line += item[3]
            line += '\n'
            fd.write(line)


def auto_add():
    contents, exist_file_list = read_dir_doc()
    file_list = os.listdir(dir_path)
    for item in file_list:
        if item != DOC_FILENAME and item not in exist_file_list:
            if contents != []:
                contents[-1][0] = FRONT_STR[0]
            doc_str = input(item+': ')
            contents.append([FRONT_STR[1], item, '#', doc_str])
            exist_file_list.append(item)

    if contents == []:
        return

    name_lens = map(lambda x: len(x), exist_file_list)
    max_len = max(list(name_lens))
    write_dir_doc(contents, max_len)


def auto_delete():
    '''
    Auto delete doc tree item which is not exist in current directory.
    '''
    if not os.path.exists(doc_path):
        return

    contents, exist_file_list = read_dir_doc()
    file_list = os.listdir(dir_path)
    for idx, item in enumerate(exist_file_list):
        if item not in file_list:
            contents.pop(idx)
            exist_file_list.pop(idx)

    if contents != []:
        contents[-1][0] = FRONT_STR[1]
    else:
        os.remove(doc_path)
        return

    name_lens = map(lambda x: len(x), exist_file_list)
    max_len = max(list(name_lens))
    write_dir_doc(contents, max_len)


def doc_modify():
    if not os.path.exists(doc_path):
        print(".DIR.md don't exist !")
        return

    contents, exist_file_list = read_dir_doc()

    file_name = input("Enter modify file name: ")
    if file_name not in exist_file_list:
        print("No this file's doc !")
        return
    idx = exist_file_list.index(file_name)
    print("Now doc string is: ", contents[idx][3])
    doc_str = input("Enter modified doc string: ")
    contents[idx][3] = doc_str

    name_lens = map(lambda x: len(x), exist_file_list)
    max_len = max(list(name_lens))
    write_dir_doc(contents, max_len)


def show_tree():
    if not os.path.exists(doc_path):
        print(".DIR.md don't exist !")
        return

    with open(doc_path, 'r') as fd:
        print(fd.read())


if __name__ == "__main__":
    show_tree()
    auto_add()
    auto_delete()
    doc_modify()
