# Implementation-of-Pilotnet
This is an implementation of paper [End to End Learning for Self-Driving Cars](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) in 2016, I use two different datasets for driving dataset, three different structures of Pilotnet and several data augmentation methods. Thank for [Yidi Wang](https://github.com/yidiwang21/Caffe-PilotNet)'s project for building the original structure of Pilotnet. 
# Prerequisite(s)
* [Caffe](http://caffe.berkeleyvision.org/)
* Python2.7
# Data preparation
* The first driving dataset comes from ymshao's github project (really thank him) which is [data](https://github.com/ymshao/End-to-End-Learning-for-Self-Driving-Cars), after download the dataset in this folder, create two folders named `train` and `val`, change the path in `csvreader.py`, open the terminal in this folder and type: 
```bash
python csvreader.py
```
Since the original driving dataset is captured from a simulater. In the Nvidia's paper, the driving dataset comes from three cameras located at the left, center and right of the driving car. Since one image is responsible for one steering angle, for the images that comes from left and right cameras, I set **offsets** for these two kinds of images. Also there are too many drving data whose steering angle is 0, so I ignore some data whose steering angle is 0. Please check the details in my `csvreader.py` file. 
* Optional: You can use the `crop.py` file to crop the image, which will crop the image, this can serve as a data augmentation method, you can try it if you want. Change the path in `crop.py`, open the terminal in this folder and type: 
```bash
python crop.py
```
 * Optional: You can use the `canny.py` file to extract the canny edge of the image, this can serve as a data augmentation method, you can try it if you want. Change the path in `canny.py`, open the terminal in this folder and type: 
```bash
python canny.py
```
* We want to store the images and their labels in **lmdb** format, and the **lmdb** format file will only take the integer as label. So that we need to first map the original float steering angle into integers. Change the path in `label.py`, open the terminal in this folder and type: 
```bash
python label.py
```
* Now we can create the **lmdb** format data for Caffe to train. Also we need a meanfile that generated from the **lmdb** format data. Change the path in `create_imagenet.sh` and `compute_mean.sh`, open the terminal in this folder and type: 
```bash
sh create_imagenet.sh
sh compute_mean.sh
```
Congratulations! You finish the data preparation part, you are ready to train your network with Caffe.
# Train
We have three different stuctures to be trained: 
First structure difined in `pilotnet_train.prototxt`, this structure is the same as it is discribed in the Nvidia's paper.
Second structure defined in `pilotnet_train_my.prototxt`, this structure has some modifications compared with the first one, see the details of this structure in `three_structure_report.pdf`.
Second structure defined in `pilotnet_train_s.prototxt`, this structure comes from Sully Chen's github project, see the details of this structure in `three_structure_report.pdf`.


* The second driving dataset comes from SullyChen's github project (really thank him) which is [driving-datasets](https://github.com/SullyChen/driving-datasets), download this dataset in the `forthenewdata' folder, create two folders named `train' and `val', change the path in `csvreader.py', open the terminal in this folder and type:
```bash
python csvreader.py
```


