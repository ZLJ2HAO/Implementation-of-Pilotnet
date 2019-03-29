import numpy as np 
import matplotlib.pyplot as plt
import sys, os
import caffe

CAFFE_ROOT = "/home/roy/caffe/"
# sys.path.insert(0, CAFFE_ROOT + 'python')

caffe.set_mode_gpu()
solver = caffe.get_solver('/home/roy/end-to-end-car-caffe/fornewdataset/y_pilotnet_solver.prototxt')

accuracy_file = open("accuracy.txt", 'r+w')

niter = 20000
test_interval = 500
test_iter = 113
train_loss = np.zeros(niter)
accuracy = 0


# solver loop



for it in range(niter):
	solver.step(1)

	train_loss[it] = solver.net.blobs['loss'].data
	# solver.test_nets[0].forward()

	if it % test_interval == 0:
            # for k in range(test_iter):
            #     solver.test_nets[0].forward()
            #     accuracy = accuracy + solver.test_nets[0].blobs['accuracy'].data       
            # accuracy = accuracy/test_interval

            solver.test_nets[0].forward()
            accuracy = solver.test_nets[0].blobs['accuracy'].data
            print('Iteration: ', it, 'testing... ', 'accuracy: ', accuracy)
            accuracy_file.write(str(it) + ' ' + str(accuracy) + '\n')
            # test_accuracy[it // test_interval] = accuracy

accuracy_file.close()

the_data = np.loadtxt('accuracy.txt', delimiter=' ', dtype='str')
test_accuracy = the_data[:,1]


        

print(test_accuracy)
_, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(np.arange(niter), train_loss)
ax2.plot(test_interval * np.arange(len(test_accuracy)), test_accuracy, 'r')
ax1.set_xlabel('iter')
ax1.set_ylabel('train_loss')
ax2.set_ylabel('test_accuracy')
plt.show()
