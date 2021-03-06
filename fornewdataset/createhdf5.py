import h5py
import numpy as np 
import os


data1 = np.loadtxt('train.txt', delimiter=' ', dtype='str')
[row1, col1] = data1.shape
print('training dataset has {} images'.format(row1))
angle1 = data1[1:row1, 1].astype('float')


data2 = np.loadtxt('val.txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('validation dataset has {} images'.format(row2))
angle2 = data2[1:row2, 1].astype('float')

train_hdf5_label_folder = "/home/roy/Implementation-of-Pilotnet/fornewdataset/train_hdf5_label"

val_hdf5_label_folder = "/home/roy/Implementation-of-Pilotnet/fornewdataset/val_hdf5_label"

h5_train_label = os.path.join(train_hdf5_label_folder,'train_label.h5')
h5_val_label = os.path.join(val_hdf5_label_folder,'val_label.h5')

with h5py.File(h5_train_label, 'w') as f:

    f['train_label'] = angle1

with h5py.File(h5_val_label, 'w') as f:

    f['val_label'] = angle2


print("done")
