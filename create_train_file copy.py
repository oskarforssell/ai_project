#!/usr/bin/python3

#import os
#import sys

import glob
folder_path = "/content/darknet/data/oskar_data/all_images/"
images_list = glob.glob("/content/darknet/data/oskar_data/all_images/*.jpg")
for i in images_list:
    print(i)
    split_img = i.split('/')
    #first_part = split_img[0]
    file_name = split_i[-1]
    output = folder_path + file_name
    # output = folder_path + first_part

    file = open("/content/darknet/data/oskar_data/train.txt", "a")
    file.write("\n".join(output))
    file.close()
print("Done")