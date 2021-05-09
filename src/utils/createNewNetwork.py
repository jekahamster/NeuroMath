import sys
sys.path.append("../")

import neural_network as NN

NNName = input("File Name: ")
NNLayers = list(map(int, input("Input layers (784 100 50 11): ").split()))
NNLearningRate = float(input("Learning Rate: "))

net = NN.NeuralNetwork()
net.init(NNLearningRate, NNLayers)

net.saveAs(NNName)