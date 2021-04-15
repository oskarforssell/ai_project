#!/usr/bin/python3

"""
Syntax: [python3] [program.py] [folder_path]
Run command: python3 chg_img_type.py path/to/folder/

Note: The program also works with blank 'file path' or '.' 
"""

#By Oskar Forssell

import glob
import os
import sys

extensions = ['*.j*','*.J*']

def chg_type():
    modified_counter = 0
    for ext in extensions:

        if len(sys.argv) == 1 or sys.argv[1] == ".":
            source = ext

            for file in glob.iglob(source, recursive=True):
                file_slice = file.split('.')
                name = file_slice[0]
                output = f"{name}.jpg"
                
                if file != output:
                    modified_counter += 1
                    os.rename(file,output)
                    print(f"File chg fm:   {file} --> {name}.jpg")

        else:
            source = sys.argv[1] + ext
            for file in glob.iglob(source, recursive=True):
                slice = file.split('/')
                path = slice[0]
                file_name = slice[-1]
                file_slice = file_name.split('.')
                name = file_slice[0]
                output = f"{path}/{name}.jpg"

                if file != output:
                    modified_counter += 1
                    os.rename(file,output)
                    print(f"File chg fm:   {file_name} --> {name}.jpg")

    print(f"\nDone! {modified_counter} files changed.")

if __name__ == "__main__":
    chg_type()