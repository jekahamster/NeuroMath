import numpy as np
import NeuralNetwork as NN

inputNodes   = 28*28
hiddenNodes  = 100
outputNodes  = 10
learningRate = 0.1
epochs 		 = 10

n = NN.NeuralNetwork()
n.init(learningRate, [inputNodes, hiddenNodes, outputNodes])

dataFile = open("mnist_dataset/mnist_train.csv", "r")
dataList = dataFile.readlines()
dataFile.close()

for e in range(epochs):
	i = 0
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
	outputs = n.query(inputs)
	label = np.argmax(outputs)
	print("Network respone is", label)
	print()
	scorecard.append(correctLabel == label)

print("Report: ", scorecard)
print("Total:", len(scorecard))
print("Correct:", sum(scorecard))
print(sum(scorecard) / len(scorecard))

if (input("Save model(y/n)? ") == "y"):
	n.saveAs(input("File name: "), sum(scorecard)/len(scorecard))
