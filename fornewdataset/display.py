import os
import time
import matplotlib.pyplot as plt
import numpy as np



data2 = np.loadtxt('train.txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('the training data has {} images'.format(row2))
angle2 = data2[0:row2, 1].astype('float')

f1 = plt.figure(1)
plt.hist(angle2, bins=np.arange(min(angle2), max(angle2), 5))




data2 = np.loadtxt('val.txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('the validation data has {} images'.format(row2))
angle2 = data2[0:row2, 1].astype('float')

plt.hist(angle2, bins=np.arange(min(angle2), max(angle2), 5))
plt.title("train val angle Histogram")
plt.xlabel("angle")
plt.ylabel("Frequency")

f1.show()

# data2 = np.loadtxt('label_train.txt', delimiter=' ', dtype='str')
# [row2, col2] = data2.shape
# print('the labeled training data has {} images'.format(row2))
# angle2 = data2[1:row2, 1].astype('float')

# f2 = plt.figure(2)
# plt.hist(angle2, bins=np.arange(0, 37, 1))



# data2 = np.loadtxt('label_val.txt', delimiter=' ', dtype='str')
# [row2, col2] = data2.shape
# print('the labeled validation data has {} images'.format(row2))
# angle2 = data2[1:row2, 1].astype('float')
# plt.hist(angle2, bins=np.arange(0, 37, 1))
# plt.title("labeled train val angle Histogram")
# plt.xlabel("label")
# plt.ylabel("Frequency")

# f2.show()

raw_input()
