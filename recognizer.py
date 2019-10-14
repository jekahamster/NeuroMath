from PIL import Image
import json
import numpy as np
import NeuralNetwork2 as NN


class Recognizer():
    operatorsLabel = ['+', '-', '/', '*', '']

    def __init__(self):
        self.nNumbers = NN.NeuralNetwork()
        self.nOperators = NN.NeuralNetwork()
        self.nNumbers.loadFrom("NNNumbers.json")
        self.nOperators.loadFrom("NNOperators.json")


    def recognize(self, imgList):
        for img in imgList:
            img = np.ravel(img)
            inputs = (np.asfarray(img) / 255 * 0.98) + 0.01
            output = self.nOperators.query(inputs)
            if self.operatorsLabel[np.argmax(output)] == "":
                output = self.nNumbers.query(inputs)
                print(np.argmax(output))
            else:
                print(self.operatorsLabel[np.argmax(output)])

        print()
        # print( self.operatorsLabel[np.argmax(outputs)] )
