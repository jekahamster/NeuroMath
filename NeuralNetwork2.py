import numpy as np
import scipy.special
import json

class NeuralNetwork():
	def __init__(self):
		self.nodes 				= []
		self.weights 			= []
		self.lr 				= None
		self.activationFunction = lambda x: scipy.special.expit(x)
		self.scores 			= None

	def init(self, lr, nodes):
		self.nodes 	= nodes
		self.lr 	= lr
		for i in range(len(self.nodes)-1):
			self.weights.append(np.random.normal(0., pow(self.nodes[i], -0.5), (self.nodes[i+1], self.nodes[i])))
		pass

	def train(self, inputsList, targetsList):
		inputs  = np.array(inputsList, ndmin=2).T
		targets = np.array(targetsList, ndmin=2).T

		layerOutputs = [inputs]
		finalInputs  = None
		for i in range(len(self.nodes)-1):
			tempLayerInputs  = np.dot(self.weights[i], layerOutputs[i])
			tempLayerOutputs = self.activationFunction(tempLayerInputs)
			finalInputs		 = tempLayerInputs
			layerOutputs.append(tempLayerOutputs)

		outputErrors = [targets-finalInputs]
		for i in range(len(self.weights)-1, 0, -1):
			outputErrors.insert(0,
				np.dot(self.weights[i].T, outputErrors[0]))

		for i in range(len(self.weights)-1, -1, -1):
			self.weights[i] += self.lr * np.dot((outputErrors[i] * layerOutputs[i+1] * (1. - layerOutputs[i+1])), np.transpose(layerOutputs[i]))
		pass

	def query(self, inputsList):
		inputs = np.array(inputsList, ndmin=2).T

		finalOutputs = inputs
		for i in range(len(self.weights)):
			tempLayerInputs  = np.dot(self.weights[i], finalOutputs)
			tempLayerOutputs = self.activationFunction(tempLayerInputs)
			finalOutputs 	 = tempLayerOutputs

		return finalOutputs


	def saveAs(self, fileName, scores=None):
		if (scores == None):
			scores = self.scores

		weights = []
		for i in range(len(self.weights)):
			weights.append(self.weights[i].tolist())
		data = {
			"scores" : scores,
			"lr"	 : self.lr,
			"nodes"	 : self.nodes,
			"weights": weights,
		}

		with open(fileName, "w") as file:
			json.dump(data, file)

	def loadFrom(self, fileName):
		data = None

		with open(fileName, "r") as file:
			data = json.load(file)

		self.scores = data["scores"]
		self.nodes 	= data["nodes"]
		self.lr		= data["lr"]
		for i in range(len(data["weights"])):
			self.weights.append(np.array(data["weights"][i], ndmin=2))
