# Implementation-of-Pilotnet
This is an implementation of paper [End to End Learning for Self-Driving Cars](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) in 2016, I use two different datasets for driving dataset, three different structures of Pilotnet and several data augmentation methods. Thank for [Yidi Wang](https://github.com/yidiwang21/Caffe-PilotNet)'s project for building the original structure of Pilotnet. 
# Prerequisite(s)
* [Caffe](http://caffe.berkeleyvision.org/)
* Python2.7
# Usage
* The first driving dataset comes from ymshao's github project (really thank him) which is [data](https://github.com/ymshao/End-to-End-Learning-for-Self-Driving-Cars), after download the dataset in this folder, create two folders named `train' and `val', change the path in `csvreader.py', open the terminal in this folder and type: 
```bash
python csvreader.py
```
Since the original driving dataset is captured from a simulater. In the original paper, the driving dataset comes from three cameras located at the left, center and right of the driving car. Since one image is responsible for one steering angle, for the images that comes from left and right cameras, I set **offsets** for these two kinds of images, see details in my `csvreader.py' file. 





* The second driving dataset comes from SullyChen's github project (really thank him) which is [driving-datasets](https://github.com/SullyChen/driving-datasets), download this dataset in the `forthenewdata' folder, create two folders named `train' and `val', change the path in `csvreader.py', open the terminal in this folder and type:
```bash
python csvreader.py
```


