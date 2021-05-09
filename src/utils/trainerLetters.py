import sys
sys.path.append("../")

import emnist
import neural_network as NN
import numpy as np

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
          "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z", " "];



inputNodes   = 28*28
hiddenNodes  = 400
outputNodes  = 27
learningRate = 0.2
epochs 		 = 10

n = NN.NeuralNetwork()
n.init(learningRate, [inputNodes, 200, 50, outputNodes])

train_images, train_labels = emnist.extract_training_samples("letters")
test_images, test_labels = emnist.extract_test_samples("letters")

for e in range(epochs):
	j = 0
	print("Epoch #", e+1)
	for i in range(len(train_images)):
		inputs 		= (np.asfarray(train_images[i].flatten()) / 255 * 0.99) + 0.01
		targets 	= np.zeros(outputNodes) + 0.1
		targets[train_labels[i]-1] = 0.99
		n.train(inputs, targets)
		# j+=1
		# print("Epoch #", e+1)
		# print("Example #", j)
		# print()


scorecard = []
for i in range(len(test_images)):
	correctLabel = test_labels[i]-1
	print("Corret label is", correctLabel)
	inputs  = (np.asfarray(test_images[i].flatten()) / 255 * 0.99) + 0.01
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
