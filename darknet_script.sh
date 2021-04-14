#! /bin/bash

# Training loop script By Oskar Forssell
# Creates a timestamped folder [YEAR-MONTH-DAY-HOUR]
# Run training 3 times
# After eaach training: results exported to specified folder

# Relative directory to save results
dest=data/oskar_test_data

# Time stamps
now=$(date +%Y-%m-%d-%H)
now_g=$(date +"%Y%m%d")

# Folder name & creation
foldername=training${now}
mkdir ${dest}/$foldername
echo "folder $foldername created"

weights_folder=backup_weights${now}
mkdir ${dest}/${weights_folder}

counter=0
while [ $counter -le 2 ]

do
  ((counter++))
  file_ext="${now_g}-${counter}"
  echo ${file_ext}

  # Run darknet training
  ./darknet detector train data/oskar_test_data/obj.data cfg/yolov3-nai20sp.cfg ../darknet53.conv.74 -map -dont_show 2>&1 > ${dest}/${foldername}/log${file_ext}.txt
  # Sleep for 2 seconds (in case there is a small hiccup with creating graph.png)
  sleep 2
  # Move & rename graph.png to specified folder
  mv graph.png ${dest}/${foldername}/graph${file_ext}.png

  # Copy the final and best weights from [backup] to weights-backup folder
  cp ${dest}/backup/yolov3-nai20sp_final.weights ${dest}/${weights_folder}/yolov3-nai20sp_final${file_ext}.weights
  cp ${dest}/backup/yolov3-nai20sp_best.weights ${dest}/${weights_folder}/yolov3-nai20sp_best${file_ext}.weights

done

echo "Training loop completed!"
echo "Log files and mAP graph exported to: ${dest}/${foldername}/"
