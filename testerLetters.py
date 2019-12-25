import emnist
import neural_network as NN
import numpy as np

def test(networkFilePath):
	n = NN.NeuralNetwork()
	n.loadFrom(networkFilePath)

	test_images, test_labels = emnist.extract_test_samples("letters")

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


if __name__ == "__main__":
	networkFilePath = input("Network file path: ")
	test(networkFilePath)
