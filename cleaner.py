#!/usr/bin/env python

import os
import shutil


def main():
    cwd = os.getcwd()
    directories = get_directories(cwd)
    for directory in directories:
        clean_directory(directory)


def get_directories(directory, level=6):
    root_dir = directory.rstrip(os.path.sep)
    assert os.path.isdir(root_dir)
    num_sep = root_dir.count(os.path.sep)
    for root, dirs, files in os.walk(root_dir):
        yield root
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


def clean_directory(directory):
    delete_directory(directory + "/.git")
    delete_file(directory + "/.gitignore")
    delete_file(directory + "/README.md")
    delete_directory(directory + "/.idea")
    delete_directory(directory + "/target")
    delete_file(directory + "/mvnw")
    delete_file(directory + "/mvnw.cmd")
    delete_file_by_extension(directory, ".iml")
    delete_file(directory + "/HELP.md")
    delete_file(directory + "/LICENSE")
    delete_directory(directory + "/venv")

def delete_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)


def delete_file(file):
    if os.path.exists(file):
        os.remove(file)


def delete_file_by_extension(directory, extension):
    test = os.listdir(directory)
    for item in test:
        if item.endswith(extension):
            os.remove(os.path.join(directory, item))


if __name__ == "__main__":
    main()
