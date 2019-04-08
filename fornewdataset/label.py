
import matplotlib.pyplot as plt
import numpy as np


data2 = np.loadtxt('train.txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('training dataset has {} images'.format(row2))


angle2 = data2[:, 1].astype('float')
name = data2[:, 0]

# set the parameters for map function
threshold = 0.3
max_index = 36
min_index = 0

# define the map function here to map the original float label into integers
max_angle = max(angle2)
min_angle = min(angle2)
def mapfun(x):
    # x = x.astype('float')
    if x > 0:
        if x > abs(min_angle):
            y = max_index
        else:
            if x/(abs(min_angle)) >threshold:

                y = max_index - 1
            else:
                y = round((x)/(abs(min_angle*threshold))*(max_index-min_index-6)/2+(max_index-min_index)/2)
    if x < 0:
        if (x)/(min_angle) > threshold:
            y = min_index 
        else:
            y = round(abs(x-min_angle*threshold)/abs(min_angle*threshold)*(max_index-min_index-4)/2) + 1
    if x == 0:
        y = round((max_index-min_index)/2)


    return (y)


j = 0
offset = abs(min(angle2))
angle_t = np.zeros(len(angle2))
for element in angle2:
    angle_t[j] = mapfun(element)
    j = j + 1

train_file = open("label_train.txt", 'w')
for j in range(len(angle2)):
    new_index = angle_t[j].astype('str').replace('.0', '')
    name[j] = name[j].replace('/home/roy/Implementation-of-Pilotnet/fornewdataset/driving_dataset/driving_dataset', '')
    train_file.write(name[j] + ' ' + new_index + '\n')
train_file.close()

print("finish label train data")
print("train max label {}, min label {}".format(max(angle_t), min(angle_t)))





data3 = np.loadtxt('val.txt', delimiter=' ', dtype='str')
[row3, col3] = data3.shape
print('validation dataset has {} iamges'.format(row3))

angle3 = data3[:, 1].astype('float')
name = data3[:, 0]

max_angle = max(angle3)
min_angle = min(angle3)

j=0
offset = abs(min(angle3))
angle_v = np.zeros(len(angle3))
for element in angle3:
    angle_v[j] = mapfun(element)
    j = j + 1

val_file = open("label_val.txt", 'w')
for j in range(len(angle3)):
    new_index = angle_v[j].astype('str').replace('.0', '')
    name[j] = name[j].replace('/home/roy/Implementation-of-Pilotnet/fornewdataset/driving_dataset/driving_dataset', '')
    val_file.write(name[j] + ' ' + new_index + '\n')
val_file.close()
print("finish label val data")
print("val max label {}, min label {}".format(max(angle_v), min(angle_v)))



