#! /bin/bash

# Train and test script By Oskar Forssell

# Creates a timestamped folder [YEAR-MONTH-DAY-HOUR]
# After training: results exported to specified folder

# Relative directory to save results
dest=data/oskar_test_data
cfg_file=cfg/yolov3-nai20sp-mod.cfg

# Time stamps
now=$(date +%Y-%m-%d-%H)
now_g=$(date +"%Y%m%d")

# Move to darknet folder (in this case located in /opt/work/darknet)
cd /opt/work/darknet/

# Folder name & creation
foldername=training${now}
mkdir ${dest}/${foldername}
echo "folder ${foldername} created"

file_ext="${now_g}"
echo ${file_ext} 

# Run darknet training
./darknet detector train data/oskar_test_data/obj.data ${cfg_file} ../darknet53.conv.74 -map -dont_show 2>&1 > ${dest}/${foldername}/train_log${file_ext}.txt
# Sleep for 2 seconds (in case there is a small hiccup with creating graph.png)
sleep 2
# Move & rename graph.png to specified folder
mv chart.png ${dest}/${foldername}/chart${file_ext}.png

# Copy the final and best weights from [backup] to weights-backup folder
cp ${dest}/backup/${cfg_file}_final.weights ${dest}/${foldername}/${cfg_file}_final${file_ext}.weights
cp ${dest}/backup/${cfg_file}_best.weights ${dest}/${foldername}/${cfg_file}_best${file_ext}.weights
cp ${dest}/backup/${cfg_file}_last.weights ${dest}/${foldername}/${cfg_file}_last${file_ext}.weights

## Test with the best weights
./darknet detector test data/oskar_test_data/obj.data ${cfg_file} ${dest}/${foldername}/${cfg_file}_best${file_ext}.weights -dont_show 2>&1 > ${dest}/${foldername}/test_log${file_ext}.txt

echo "Training and testing completed!"
echo "Log files, mAP chart and weights exported to: ${dest}/${foldername}/"