import sys
sys.path.append("../")

import emnist
import numpy as np
import neural_network as NN

netPath = input("Network path: ")
n 		= NN.NeuralNetwork()
n.loadFrom(netPath)

datasets 					= ["mnist", "letters"]
datasetIndex 				= int(input("Input dataset: digits or letters [1/2]: "))-1
trainImages, trainLabels 	= emnist.extract_training_samples(datasets[datasetIndex])
testImages, testLabels 		= emnist.extract_test_samples(datasets[datasetIndex])

scorecard = []
for i in range(len(testImages)):
	correctLabel = testLabels[i]-1*datasetIndex
	print("Corret label is", correctLabel)
	inputs  = (np.asfarray(testImages[i].flatten()) / 255 * 0.99) + 0.01
	outputs = n.query(inputs)
	label = np.argmax(outputs)
	print("Network respone is", label)
	print()
	scorecard.append(correctLabel == label)

print("Report: ", scorecard)
print("Total:", len(scorecard))
print("Correct:", sum(scorecard))
print(sum(scorecard) / len(scorecard))