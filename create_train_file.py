import glob
images_list = glob.glob("/opt/work/darknet/data/oskar_test_data/images/all/*.jpg")
print(images_list)
file = open("/opt/work/darknet/data/oskar_test_data/train.txt", "w")
file.write("\n".join(images_list))
file.close()

# import glob
# images_list = glob.glob("/content/darknet/data/oskar_data/all_images/*.jpg")
# print(images_list)
# file = open("/content/darknet/data/oskar_data/train.txt", "w")
# file.write("\n".join(images_list))
# file.close()