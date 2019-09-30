import numpy as np
import NeuralNetwork as NN

inputNodes   = 28*28
hiddenNodes  = 100
outputNodes  = 10
learningRate = 0.2
epochs 		 = 5

n = NN.NeuralNetwork()
n.init(inputNodes, hiddenNodes, outputNodes, learningRate)

dataFile = open("mnist_dataset/mnist_train.csv", "r")
dataList = dataFile.readlines()
dataFile.close()

i = 0
for e in range(epochs):
	for data in dataList:
		allValues  	= data.split(",")
		inputs 		= (np.asfarray(allValues[1:]) / 255 * 0.99) + 0.01
		targets 	= np.zeros(outputNodes) + 0.1
		targets[int(allValues[0])] = 0.99
		n.train(inputs, targets)
		i+=1
		print("Epoch #", e+1)
		print("Example #", i)
		print()


trainFile = open("mnist_dataset/mnist_test.csv", "r")
trainList = trainFile.readlines()
trainFile.close()


scorecard = []
for train in trainList:
	allValues 	= train.split(",")
	correctLabel = int(allValues[0])
	print("Corret label is", correctLabel)
	inputs  = (np.asfarray(allValues[1:]) / 255 * 0.99) + 0.01
	print(inputs)
	outputs = n.query(inputs)
	label = np.argmax(outputs)
	print("Network respone is", label)
	print()
	scorecard.append(correctLabel == label)

n.saveAs("NN2.json")

print("Report: ", scorecard)
print("Total:", len(scorecard))
print("Correct:", sum(scorecard))
print(sum(scorecard) / len(scorecard))
