import sys
sys.path.append("../")

import emnist
import numpy as np
import neural_network as NN

netPath = input("Network path: ")
n 		= NN.NeuralNetwork()
n.loadFrom(netPath)

print(n.nodes[len(n.nodes)-1])
datasets 					= ["mnist", "letters"]
datasetIndex 				= int(input("Input dataset: digits or letters [1/2]: "))-1
trainImages, trainLabels 	= emnist.extract_training_samples(datasets[datasetIndex])
testImages, testLabels 		= emnist.extract_test_samples(datasets[datasetIndex])

epochs = int(input("Epochs count: "))

for e in range(epochs):
	j = 0
	print("Epoch #", e)
	for i in range(len(trainImages)):
		inputs 		= (np.asfarray(trainImages[i].flatten()) / 255 * 0.98) + 0.01
		targets 	= np.zeros(n.nodes[len(n.nodes)-1]) + 0.1
		targets[trainLabels[i]-1*datasetIndex] = 0.99
		n.train(inputs, targets)

n.saveAs(netPath)