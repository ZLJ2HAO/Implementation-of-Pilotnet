# For new dataset
For this new dataset I implement Pilotnet with a new dataset which is captured from a center camera on a driving car.
# Prerequisite(s)
* [Caffe](http://caffe.berkeleyvision.org/)
* Python2.7
# Data preparation
* The second driving dataset comes from ymshao's github project (really thank him) which is [data](https://github.com/ymshao/End-to-End-Learning-for-Self-Driving-Cars), after download the dataset in this folder, create two folders named `train` and `val`, change the path in `datasetreader.py`, open the terminal in this folder and type: 
```bash
python datasetreader.py
```
This driving dataset is captured from a center camera of a driving car.
* Optional: You can use the `crop.py` file to crop the image, which will crop the image, this can serve as a data augmentation method, you can try it if you want. Change the path in `crop.py`, open the terminal in this folder and type: 
```bash
python crop.py
```
 * Optional: You can use the `canny.py` file to extract the canny edge of the image, this can serve as a data augmentation method, you can try it if you want. Change the path in `canny.py`, open the terminal in this folder and type: 
```bash
python canny.py
```

* We want to store the images and their labels in **hdf5** format, and the **hdf5** format file can take the float number as label. You need first create two folders named `train_hdf5_label` and `val_hdf5_label`. Then change the path in `createhdf5.py`, open the terminal in this folder and type:
```bash
python createhdf5.py
```
In each folders you will get a `.h5` file. Change the path in `train_loc.txt` and `val_loc.txt`.

* If you want to see the histogram of the original steering angle and labeled angle. You could change the path in the `display.py` file, open the terminal in this folder and type: 
```bash
python display.py
```
![Histogram of original steering angle](https://github.com/ZLJ2HAO/Implementation-of-Pilotnet/blob/master/figure/3.png)
Blue bar means the training data, orange bar means the testing data
* Now we can create the **lmdb** format data for Caffe to train. Also we need a meanfile that generated from the **lmdb** format data. Change the path in `create_imagenet.sh` and `compute_mean.sh`, open the terminal in this folder and type: 
```bash
sh create_imagenet.sh
sh compute_mean.sh
```
Congratulations! You finish the data preparation part, you are ready to train your network with Caffe.
# Train
We have three different stuctures to be trained: 
1. First structure difined in `pilotnet_train.prototxt`, this structure is the same as it is discribed in the Nvidia's paper.
2. Second structure defined in `pilotnet_train_my.prototxt`, this structure has some modifications compared with the first one, see the details of this structure in `three_structure_report.pdf`.
3. Third structure defined in `pilotnet_train_s.prototxt`, this structure comes from [Sully Chen's github project](https://github.com/SullyChen/Caffe-Autopilot), see the details of this structure in `three_structure_report.pdf`.

* First change the path in the `pilotnet_solver.prototxt` file (You need to modify the parameters in this file carefully, you may stuggle to have a good training strategy, that's the necessary step for training part, good luck:-) ). In order to train the networks, we need use the Caffe build in tools, so first change the path to `caffe/build/tools/`, in the terminal type:
```bash
./caffe train -solver=/home/roy/Implementation-of-Pilotnet/pilotnet_solver.prototxt
```
Then you will get several trained models in the `snapshot` folder.
# Test
* You can test your trained models accuracy using `prediction.py` file, change the path in `prediction.py` file, in the terminal type:
```bash
python prediction.py
```
You will get the prediction submission in the `snapshot` folder.

* The second driving dataset comes from SullyChen's github project (really thank him) which is [driving-datasets](https://github.com/SullyChen/driving-datasets), download this dataset in the `forthenewdata' folder, create two folders named `train' and `val', change the path in `csvreader.py', open the terminal in this folder and type:
```bash
python csvreader.py
```


