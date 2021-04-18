#!/usr/bin/python3

# By Oskar Forssell

import glob
import os
import sys

img_source = sys.argv[1] + '*.j*'
txt_source = sys.argv[1] + '*.t*'
folder_path = sys.argv[1]

jpg_list = []
txt_list = []
jpg_missing_txt_pair = []
txt_missing_jpg_pair = []
classes_txt_delisted = False

for txt_file in glob.iglob(txt_source, recursive=True):
    split_txt = txt_file.split('.')
    first_part = split_txt[0]
    split_txt_2 = first_part.split('/')
    txt_file_name = split_txt_2[-1]
    txt_list.append(txt_file_name)

for jpg_file in glob.iglob(img_source, recursive=True):
    split_jpg = jpg_file.split('.')
    first_name = split_jpg[0]
    split_jpg_2 = first_name.split('/')
    jpg_file_name = split_jpg_2[-1]
    jpg_list.append(jpg_file_name)

    if jpg_file_name in txt_list:
        pass
    else: jpg_missing_txt_pair.append(jpg_file_name)
    
for single_txt in txt_list:
    if single_txt in jpg_list:
        pass
    elif single_txt == "classes":
        txt_list.remove("classes")
        classes_txt_delisted = True
        pass
    else: txt_missing_jpg_pair.append(single_txt)

def delete_file():
    yes = ("yes", "y", "yeah")
    delete_or_not = input("\nDo you want to remove these .jpg files? (Y/n) ")
    del_counter=0
    if delete_or_not.lower().startswith(yes):
        print("\nThe follwoing items have been deleted: ")
        for file in jpg_missing_txt_pair:
            if os.path.exists(folder_path+file+".jpg"):
                print(file+".jpg")
                os.remove(folder_path+file+".jpg")
                del_counter+=1
            if os.path.exists(folder_path+file+".txt"):
                print(file+".txt")
                os.remove(folder_path+file+".txt")
                del_counter+=1
            else:
                pass
        for txt in txt_missing_jpg_pair:
            if os.path.exists(folder_path+txt+".txt"):
                print(txt+".txt")
                os.remove(folder_path+txt+".txt")
                del_counter+=1
            if os.path.exists(folder_path+txt+".jpg"):
                print(txt+".jpg")
                os.remove(folder_path+txt+".jpg")
                del_counter+=1
            else:
                pass
        print(f"Total number of files deleted: {del_counter}")

    else: print("Ok, walking slowly away.. files untouched")


if len(jpg_missing_txt_pair) > 0 or len(txt_missing_jpg_pair) > 0:
    print("---  THE FOLLOWING .txt FILES ARE MISSING  ---")
    print("- Files might be corrupted, empty or missing -\n")
    for file in jpg_missing_txt_pair:
        print(file+".jpg")
    print(f"\nTotal number of missing .txt file: {len(jpg_missing_txt_pair)}")

    print("--- THE FOLLOWING .jpg FILES ARE MISSING ---")
    print("- Files might be corrupted, empty or missing -\n")
    for tekst in txt_missing_jpg_pair:
        print(tekst+".txt")
    print(f"\nTotal number of missing .jpg file: {len(txt_missing_jpg_pair)}")
    delete_file()

else: print("No missing pairs found, you have:")
if classes_txt_delisted == False:
    print(f"{len(txt_list)} txt files  !!! CAUTION your classes.txt file is missing!\n{len(jpg_list)} jpg images")
else: print(f"{len(txt_list)} txt files + 1 (classes.txt)\n{len(jpg_list)} jpg images")
    

## This code checks first for .jpg images, then if there is a .txt counterpart.
## If NO .txt counterpart found it is added to the "missing_pair"-list.
## Then it checks if there is a .jpg counterpart for all .tt files.
## An option to delete all single pairs has been added.

