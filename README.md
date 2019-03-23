# Implementation-of-Pilotnet
This is an implementation of paper [End to End Learning for Self-Driving Cars](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) in 2016, I use two different datasets for driving dataset, three different structures of Pilotnet and several data augmentation methods. 
# Prerequisite(s)
* [Caffe](http://caffe.berkeleyvision.org/)
* Python2.7
# Usage
The driving dataset comes from SullyChen's github project (really thank him) which is [driving-datasets](https://github.com/SullyChen/driving-datasets), after downloading the dataset in this folder, create two folders named `train' and `val', change the path in `csvreader.py', open the terminal in this folder and type:
```bash
python csvreader.py
```


