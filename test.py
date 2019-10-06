import NeuralNetwork2 as NN

n = NN.NeuralNetwork()
n.init(0.2, [784, 100, 10])

for i in range(3-1, -1, -1):
    print(i)
