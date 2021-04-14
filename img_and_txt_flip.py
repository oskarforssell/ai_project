#!/usr/bin/python3

#By Oskar Forssell
# + sys.argv added by Jaime Roque Barrios

# Dependences to install:
#   pip install pillow

from PIL import Image, ImageOps
import glob
import datetime
import sys

start_time = datetime.datetime.now().replace(microsecond=0)

#img_source = '/opt/work/darknet/data/oskar_test_data/images/all_images/*.j*'
#txt_source = '/opt/work/darknet/data/oskar_test_data/images/all_images/*.t*'
# dest = '/opt/work/darknet/data/oskar_test_data/images/all_with_mirror/'
img_source = sys.argv[1] + '*.j*'
txt_source = sys.argv[1] + '*.t*'
dest = sys.argv[2]


img_counter = 0
txt_counter = 0

#Process to 'mirror' images
for jpg_file in glob.iglob(img_source, recursive=True):

    #Get name of file (remove .jpg and path before file name)
    split_jpg = jpg_file.split('.')
    path_and_name = split_jpg[0]
    split_path_name = path_and_name.split('/')
    name = split_path_name[-1]

    #Open img, mirror it and save it
    jpg_img = Image.open(jpg_file)
    jpg_mirror = ImageOps.mirror(jpg_img)
    save_as = dest + name + "_mirror.jpg"
    jpg_mirror.save(save_as, format='JPEG', subsampling=0, quality=95)
    img_counter+=1

#Process to mirror the annotation location of the x-axis in annotated files
for txt_file in glob.iglob(txt_source, recursive=True):

    #Get name of file (remove .txt and path before file name)
    split_txt = txt_file.split('.')
    txt_path_and_name = split_txt[0]
    txt_split_path_name = txt_path_and_name.split('/')
    txt_name = txt_split_path_name[-1]

    #Open txt, read line at a time, modify the 2nd column on each line by [1-value] 'one minus value'.
    with open(txt_file, 'r') as opened:
        line = opened.readline()
        while line:
            #Split row and calculate '1-value' in 2nd column, also format to have 6 decimals
            unit = line.split(' ')
            mirror_value_x_axis  = '{0:.6f}'.format(1 - float(unit[1]))
            
            #Replace x-axis coordinate with new value and merge units into one string
            unit[1] = mirror_value_x_axis
            new_content = f"{unit[0]} {unit[1]} {unit[2]} {unit[3]} {unit[4]}"

            #Create new file where to save content
            with open((dest+txt_name+"_mirror.txt"), 'a') as new_txt:
                new_txt.write(new_content)

            line = opened.readline()
    txt_counter+=1

end_time = datetime.datetime.now().replace(microsecond=0)
print(f"Process completed in {end_time-start_time} [h:m:s]")
print(f"Created {img_counter} mirror images and {txt_counter} txt files")


# Caution!
# If annotated .txt file aready exists as a _mirror.txt version and this code is run,
# then the existing _mirror.txt file will get appended with additional annotations.
# This is maybe not as bad as the bounding boxes should be identical.