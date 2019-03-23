import numpy as np
import matplotlib.pyplot as plt
import sys, os
import caffe

CAFFE_ROOT = "/home/roy/caffe/"
sys.path.insert(0, CAFFE_ROOT + 'python')

caffe.set_mode_gpu()
solver = caffe.SGDSolver('/home/roy/end-to-end-car-caffe/pilotnet_solver.prototxt')

niter = 10000
test_interval = 1000
train_loss = np.zeros(niter)
test_accuracy = np.zeros(int(np.ceil(niter/test_interval)))

# solver loop
for it in range(niter):
	solver.step(1)

	train_loss[it] = solver.net.blobs['loss'].data
	solver.test_nets[0].forward(start = 'conv1')

	if it % test_interval == 0:
		accuracy = solver.test_nets[0].blobs['accuracy'].data
		print('Iteration: ', it, 'testing... ', 'accuracy: ', accuracy)
		test_accuracy[it // test_interval] = accuracy

print(test_accuracy)
_, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(np.arange(niter), train_loss)
ax2.plot(test_interval * np.arange(len(test_accuracy)), test_accuracy, 'r')
ax1.set_xlabel('iter')
ax1.set_ylabel('train_loss')
ax2.set_ylabel('test_accuracy')
plt.show()
