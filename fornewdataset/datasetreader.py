import os
import time
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns


data = np.loadtxt('data.txt', delimiter=' ', dtype='str')
[row, col] = data.shape
# angle = data[1:row, 3].astype('float')
name = data[0:row, 0]


# l = len(angle)

train_path = '/home/roy/end-to-end-car-caffe/fornewdataset/train'
val_path = '/home/roy/end-to-end-car-caffe/fornewdataset/val'
data_base_dir = "/home/roy/end-to-end-car-caffe/fornewdataset/driving_dataset"
# dir_list = os.listdir(data_base_dir)
# num_of_picture = len(dir_list)

start = time.time()
n = -1
train_file = open("train.txt", 'w')
val_file = open("val.txt", 'w')
index = 0


# angle = data[1:row, 3].astype('float')
# max_index = 90
# min_index = 0
# max_angle = max(angle)
# min_angle = min(angle)
# def mapfun(x):
#     x = x.astype('float')
#     y = round(x/(max_angle-min_angle)*(max_index-min_index))
#     return (y.astype('str'))
angle = data[0:row, 1]
zero_num = 0
nonzero_num = 0
for pic_name in name:
    n = n + 1
    file_list = os.path.join(data_base_dir, pic_name)

    temp_angle = angle[n].astype('float')
    if temp_angle == 0:
        zero_num = zero_num + 1
        # if zero_num % 10 == 0:
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
print('execution time: %0.3f'%(t))


data2 = np.loadtxt('train.txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('row2 {},col2 {}'.format(row2, col2))
print('zero num is {}'.format(zero_num))
angle2 = data2[1:row2, 1].astype('float')
plt.hist(angle2, bins=np.arange(min(angle2), max(angle2), 1))   #need change something
plt.title("train angle Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

# sns.distplot(TData, rug=True)
