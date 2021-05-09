from settings_controller import SettingsController
from PIL import Image
import json
import numpy as np
import neural_network as NN

SettingsController.loadFrom()

n = NN.NeuralNetwork()
n.loadFrom(SettingsController.operatorsNetworkPath)
labels = SettingsController.operatorLabels
while (True):
	try:
		img = Image.open(input("Path: ")).convert("I")
		pix = abs(np.array(img) - 255)
		pix = np.ravel(pix)
		inputs = (np.asfarray(pix) / 255 * 0.98) + 0.01
		output = n.query(inputs)
		label = np.argmax(output)
		userResponce = input("It is "+str(labels[label])+"? (y/n): ")
		if (userResponce.lower() == "n"):
			targets = np.zeros(len(labels)) + 0.01
			targets[int(labels.index(input("Correct ans: ")))] = 0.99
			n.train(inputs, targets)
			n.saveAs(SettingsController.operatorsNetworkPath)
		elif (userResponce.lower() == "y"):
			targets = np.zeros(len(labels)) + 0.01
			targets[label] = 0.99
			n.train(inputs, targets)
			n.saveAs(SettingsController.operatorsNetworkPath)

	except ValueError:
		print("ValueError")
	except FileNotFoundError:
		print("FileNotFoundError")
