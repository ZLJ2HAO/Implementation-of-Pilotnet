
import matplotlib.pyplot as plt
import numpy as np


data2 = np.loadtxt('train (copy).txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('row2 {},col2 {}'.format(row2, col2))


angle2 = data2[:, 1].astype('float')
name = data2[:, 0]


threshold = 0.5
max_index = 4
min_index = 0


max_angle = max(angle2)
min_angle = min(angle2)
def mapfun(x):
    # x = x.astype('float')
    if x > 0:
        if (x)/(max_angle) > threshold:
            y = max_index
        else:
            y = round(((x)/(max_angle)+1)*(max_index-min_index)/2)
    if x < 0:
        if (x)/(min_angle) > threshold:
            y = min_index
        else:
            y = round((abs(x-min_angle)/abs(min_angle))*(max_index-min_index)/2)
    if x == 0:
        y = round((max_index-min_index)/2)
    return (y)







j = 0
offset = abs(min(angle2))
angle_t = np.zeros(len(angle2))
for element in angle2:
    angle_t[j] = mapfun(element)
    j = j + 1

train_file = open("train.txt", 'r+w')
for j in range(len(angle2)):
    new_index = angle_t[j].astype('str').replace('.0', '')
    name[j] = name[j].replace('/home/roy/end-to-end-car-caffe/new_img/', '')
    train_file.write(name[j] + ' ' + new_index + '\n')
train_file.close()

print("finish label train data")
print("train max label {}, min label {}".format(max(angle_t), min(angle_t)))

data3 = np.loadtxt('val (copy).txt', delimiter=' ', dtype='str')
[row3, col3] = data3.shape
print('row3 {},col3 {}'.format(row3, col3))

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

val_file = open("val.txt", 'r+w')
for j in range(len(angle3)):
    new_index = angle_v[j].astype('str').replace('.0', '')
    name[j] = name[j].replace('/home/roy/end-to-end-car-caffe/new_img/', '')
    val_file.write(name[j] + ' ' + new_index + '\n')
val_file.close()
print("finish label val data")
print("val max label {}, min label {}".format(max(angle_v), min(angle_v)))


print("angle2 length is {}".format(len(angle2)))
plt.hist(angle2, bins=np.arange(-1, 1, 0.02))
plt.title(" train angle Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

print("angle3 length is {}".format(len(angle3)))
plt.hist(angle3, bins=np.arange(-1, 1, 0.02))
plt.title(" val angle Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
