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
		# перетворюємо списки у двовимірний масив, транспонуємо його
		inputs  = np.array(inputsList, ndmin=2).T
		targets = np.array(targetsList, ndmin=2).T

		# зберігаємо результати для кожного шару 
		layerOutputs = [inputs]		# вихідні данні на шарі (після активації)

		# зберігаємо результат для останньої дії
		finalInputs  = None			# вхідні дані на шарі (перед активацією)
		

		for i in range(len(self.nodes)-1): 	# для кожного шару
			# обчислюємо значення нейронів на шарі в два етапи
			# 1) обчислюємо вхідні значення нейрону
			# 2) обчислюємо вихідні значення нейрону
			tempLayerInputs  = np.dot(self.weights[i], layerOutputs[i])
			tempLayerOutputs = self.activationFunction(tempLayerInputs)
			
			# зберігаємо результати
			finalInputs		 = tempLayerInputs
			layerOutputs.append(tempLayerOutputs)

		# значення похибки для кожного шару
		outputErrors = [targets-finalInputs]

		for i in range(len(self.weights)-1, 0, -1):  
		# в зворотньому напрямі для кожного шару підраховуємо похибку
			outputErrors.insert(0,
				np.dot(self.weights[i].T, outputErrors[0]))

		# корегуємо значення зв'язків для кожного шару, маючи значення похибки на кожному шарі
		# і попередні значення зв'язків
		for i in range(len(self.weights)-1, -1, -1):
			self.weights[i] += self.lr * np.dot((outputErrors[i] * layerOutputs[i+1] * (1. - layerOutputs[i+1])), np.transpose(layerOutputs[i]))
		

	def query(self, inputsList):
		# перетворюємо список в масив
		inputs = np.array(inputsList, ndmin=2).T

		# зберігаємо вихідні значення лише для останнього шару
		finalOutputs = inputs

		for i in range(len(self.weights)): 	# для кожного шару
			# обчислюємо значення нейронів на шарі в два етапи
			# 1) обчислюємо вхідні значення нейрону
			# 2) обчислюємо вихідні значення нейрону
			tempLayerInputs  = np.dot(self.weights[i], finalOutputs)
			tempLayerOutputs = self.activationFunction(tempLayerInputs)

			# зберігаємо вихідні значення нейронів на шарі
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
