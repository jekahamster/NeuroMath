import numpy as np
import neural_network as NN

def test(networkFilePath, testFilePath):
	if (testFilePath == ""):
		testFilePath = "mnist_dataset/mnist_test.csv"


	n = NN.NeuralNetwork()
	n.loadFrom(networkFilePath)

	testFile = open(testFilePath, "r")
	testList = testFile.readlines()
	testFile.close()

	scorecard = []
	for test in testList:
		allValues 	 = test.split(",")
		correctLabel = int(allValues[0])
		inputs  	 = (np.asfarray(allValues[1:]) / 255 * 0.99) + 0.01
		print("Corret label is", correctLabel)
		outputs = n.query(inputs)
		label = np.argmax(outputs)
		print("Network respone is", label)
		print()
		scorecard.append(correctLabel == label)

	print("Report: ", scorecard)
	print("Total:", len(scorecard))
	print("Correct:", sum(scorecard))
	print(sum(scorecard) / len(scorecard))


if __name__ == "__main__":
	networkFilePath = input("Network file path: ")
	testFilePath = input("Test data file path: ")
	test(networkFilePath, testFilePath)
