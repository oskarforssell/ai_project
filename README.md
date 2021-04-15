# AI Project - Machine vision

Code:  
- [`darknet_script.sh`](https://github.com/oskarforssell/ai_project/new/master?readme=1#darknet_scriptsh)
- [`find_jpg_txt_pairs_delete_missing.py`](https://github.com/oskarforssell/ai_project/new/master?readme=1#find_jpg_txt_pairs_delete_missingpy)  
- [`img_and_txt_flip.py`](https://github.com/oskarforssell/ai_project/new/master?readme=1#img_and_txt_flippy)

--- 
#### `darknet_script.sh`
A script created to run darknet training 3 times, each time saving  
a timestamped log.txt file and a timestamped mAP chart.png  
Also the `final.weights` and `best.weights`of each run are saved.

---

#### `find_jpg_txt_pairs_delete_missing.py` 
Use to make sure all images have a annotated .txt file.

Cmd line syntax  
[python3] [program.py] [folder/]  
`python3 find_jpg_txt_pairs_delete_missing.py folder_to_check/` 

This program will search for file extension starting with .j or .t (ie. .jpg, .jpeg, .txt).  
Then check that there is a .jpg and .txt file with the same name.  
   
If there **aren't** any missing pairs the output will tell you how many files you have.  
If there **are** missing pairs the output will print out the missing files and give  
an option to delete the **single/pairless** files.

---

#### `img_and_txt_flip.py`
Dependencies: requires **PIL**, to install: 
> pip install pillow  

Cmd line syntax  
[python3] [program.py] [source_folder/] [destination_folder/]     
`python3 img_and_txt_flip.py folder/ folder/` 

This program will read the source_folder and mirror flip the images (along the x-axis) and  
likewise mirror flip the annotated .txt files. The <x_center> value has been reduced from 1  
to get the mirror image location. An annotation.txt example below (and more can be found on AlexeyAB's GitHub).

Information from [AlexeyAB's repo](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects):   
The annotated .txt file need to be in the following format:   
`<object-class> <x_center> <y_center> <width> <height>`

    1 0.716797 0.395833 0.216406 0.147222
    0 0.687109 0.379167 0.255469 0.158333
    1 0.420312 0.395833 0.140625 0.166667
