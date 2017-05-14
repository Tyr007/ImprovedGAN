'''
form_input
formatting input for Improved GAN

Functions:
	input_x(), give train data like [0:1000,0:32,0:32,0:1] of real in 0.0-1.0
	input_sum(), sum of the full train dataset
	input_y(), the label of dataset, and 1 for no label as realdata
		like [0:1000,0:5] as one-hot vectors.

'''
import numpy as npy

def input_x():
	t=npy.load('x_train.npy')
	for i in range(len(t)):
		for j in range(28*28):
			zx[i,j/28,j%28]=t[i,j]
	return zx

def input_sum():
	z=npy.load('y_train.npy')
	return len(z)

def input_y():
	y=npy.load('y_train.npy')
	for i in range(len(y)):
		zy[i,0:y[i]-1]=0
		zy[i,y[i]]=1
		zy[i,y[i]+1:]=0
		zy[i,10]=0

if __name__ == '__main__':
	print 'Only use for formatting input to Improved_DCGAN'
	print 'Do not open and run it.'
	exit()
