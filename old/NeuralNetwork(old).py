import numpy as np
import scipy.special
import json

class NeuralNetwork:

	def __init__(self):
		self.activationFunction = lambda x: scipy.special.expit(x)


	def init(self, inputNodes, hiddenNodes, outputNodes, learningRate):
		self.inodes = inputNodes
		self.hnodes = hiddenNodes
		self.onodes = outputNodes
		self.lr 	= learningRate

		self.wih = np.random.normal(0., pow(self.inodes, -0.5), (self.hnodes, self.inodes))
		self.who = np.random.normal(0., pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
		self.activationFunction = lambda x: scipy.special.expit(x)

	def train(self, inputsList, targetsList):
		inputs  = np.array(inputsList, ndmin=2).T
		targets = np.array(targetsList, ndmin=2).T

		hiddenInputs  = np.dot(self.wih, inputs)
		hiddenOutputs = self.activationFunction(hiddenInputs)

		finalInputs  = np.dot(self.who, hiddenOutputs)
		finalOutputs = self.activationFunction(finalInputs)

		outputErrors = targets - finalInputs
		hiddenErrors = np.dot(self.who.T, outputErrors)

		self.who += self.lr * np.dot((outputErrors * finalOutputs * (1. - finalOutputs)), np.transpose(hiddenOutputs))
		self.wih += self.lr * np.dot((hiddenErrors * hiddenOutputs * (1. - hiddenOutputs)), np.transpose(inputs))

	def query(self, inputsList):
		inputs = np.array(inputsList, ndmin=2).T

		hiddenInputs  = np.dot(self.wih, inputs)
		hiddenOutputs = self.activationFunction(hiddenInputs)

		finalInputs  = np.dot(self.who, hiddenOutputs)
		finalOutputs = self.activationFunction(finalInputs)
		return finalOutputs

	def saveAs(self, fileName):
		data = {
			"inodes": self.inodes,
			"hnodes": self.hnodes,
			"onodes": self.onodes,
			"lr"	: self.lr,
			"wih"	: self.wih.tolist(),
			"who"	: self.who.tolist()
		}

		with open(fileName, "w") as file:
			json.dump(data, file)

	def loadFrom(self, fileName):
		data = None

		with open(fileName, "r") as file:
			data = json.load(file)

		self.inodes = data["inodes"]
		self.hnodes = data["hnodes"]
		self.onodes = data["onodes"]
		self.lr 	= data["lr"]
		self.wih 	= np.array(data["wih"], ndmin=2)
		self.who 	= np.array(data["who"], ndmin=2)
