import random
import os
import subprocess
import sys

def split_data_set(image_dir):

    pwd_now = os.getcwd()
    f_val = open("test.txt", 'w')
    f_train = open("train.txt", 'w')

    path, dirs, files = next(os.walk(image_dir))
    data_size = len(files)

    ind = 0
    data_test_size = int(0.1 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)

    for f in os.listdir(image_dir):
        if(f.split(".")[1] == "jpg"):
            ind += 1

            if ind in test_array:
                f_val.write(pwd_now+'/'+image_dir+f+'\n')
            else:
                f_train.write(pwd_now+'/'+image_dir+f+'\n')
    print('Done')
split_data_set(sys.argv[1])
