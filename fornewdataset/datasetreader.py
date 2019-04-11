import os
import time
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns


data = np.loadtxt('data.txt', delimiter=' ', dtype='str')
[row, col] = data.shape
name = data[0:row, 0]



train_path = '/home/roy/Implementation-of-Pilotnet/fornewdataset/train'
val_path = '/home/roy/Implementation-of-Pilotnet/fornewdataset/val'
data_base_dir = "/home/roy/Implementation-of-Pilotnet/fornewdataset/driving_dataset/driving_dataset"

start = time.time()
n = -1
train_file = open("train.txt", 'w')
val_file = open("val.txt", 'w')
index = 0


# the training pictures:validation pictures = 8:1, eliminate 9/10 images
angle = data[0:row, 1]
zero_num = 0
nonzero_num = 0
for pic_name in name:
    n = n + 1
    file_list = os.path.join(data_base_dir, pic_name)

    temp_angle = angle[n].astype('float')
    if temp_angle == 0:
        zero_num = zero_num + 1
        if zero_num % 10 == 0:
            if zero_num % 8 != 0:
                train_file.write(file_list + ' ' + angle[n] + '\n')
                train_pic = os.path.join(train_path, pic_name)
                open(train_pic, "wb").write(open(file_list, "rb").read())
            else:
                val_file.write(file_list + ' ' + angle[n] + '\n')
                val_pic = os.path.join(val_path, pic_name)
                open(val_pic, "wb").write(open(file_list, "rb").read())
    else:
        nonzero_num = nonzero_num + 1
        if nonzero_num % 8 == 0:
            val_file.write(file_list + ' ' + angle[n] + '\n')
            val_pic = os.path.join(val_path, pic_name)
            open(val_pic, "wb").write(open(file_list, "rb").read())
        else:
            train_file.write(file_list + ' ' + angle[n] + '\n')
            train_pic = os.path.join(train_path, pic_name)
            open(train_pic, "wb").write(open(file_list, "rb").read())




train_file.close()
val_file.close()

t = time.time() - start
print('n is %d'%n)
print('execution time: %0.3f s'%(t))


data2 = np.loadtxt('train.txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('the training data has {} images'.format(row2))
data2 = np.loadtxt('val.txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('the validation data has {} images'.format(row2))
print('zero num is {}'.format(zero_num))



