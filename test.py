import NeuralNetwork2 as NN
from PIL import Image
import numpy as np

n = NN.NeuralNetwork()
n.init(0.3, [28*28, 100, 10])
print(len(n.weights[1]))
print(len(n.weights[1][0]))
