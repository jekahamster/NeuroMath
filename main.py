from PIL import Image
import json
import numpy as np
import NeuralNetwork as NN

n = NN.NeuralNetwork()
n.loadFrom("NN.json")

while (True):
	try:
		img = Image.open(input("Path: ")).convert("I")
		pix = abs(np.array(img) - 255)
		pix = np.ravel(pix)
		inputs = (np.asfarray(pix) / 255 * 0.98) + 0.01
		output = n.query(inputs)
		label = np.argmax(output)
		userResponce = input("It is "+str(label)+"? (y/n): ")
		if (userResponce.lower() == "n"):
			targets = np.zeros(10) + 0.01
			targets[int(input("Correct ans: "))] = 0.99
			n.train(inputs, targets)
			n.saveAs("NN.json")
	except ValueError:
		print("ValueError")
	except FileNotFoundError:
		print("FileNotFoundError")
