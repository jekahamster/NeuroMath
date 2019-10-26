import numpy as np
import NeuralNetwork as NN
from SettingsController import SettingsController
SettingsController.loadFrom(SettingsController.DEFAULT_PATH)

class Recognizer():
    operatorsLabel  = SettingsController.operatorLabels
    numbersLabel    = SettingsController.numberLabels

    def __init__(self):
        self.nNumbers = NN.NeuralNetwork()
        self.nOperators = NN.NeuralNetwork()
        self.nNumbers.loadFrom(SettingsController.numbersNetworkPath)
        self.nOperators.loadFrom(SettingsController.operatorsNetworkPath)


    def recognize(self, imgList):
        result = []

        for img in imgList:
            img = np.ravel(img)
            inputs = (np.asfarray(img) / 255 * 0.98) + 0.01
            output = self.nOperators.query(inputs)

            if self.operatorsLabel[np.argmax(output)] == "":
                output = self.nNumbers.query(inputs)
                result.append(str(np.argmax(output)))
            else:
                result.append(self.operatorsLabel[np.argmax(output)])
        return result

    def adjust(self, imgList, correctLabel):
        print(correctLabel[:len(imgList)])
        for i in range(len(imgList)):
            img = np.ravel(imgList[i])
            inputs = (np.asfarray(img) / 255 * 0.98) + 0.01

            if correctLabel[i] in self.operatorsLabel:
                operatorsTargets = np.zeros(len(self.operatorsLabel)) + 0.01
                operatorsTargets[self.operatorsLabel.index(correctLabel[i])] = 0.99
                while(np.argmax(self.nOperators.query(inputs)) != self.operatorsLabel.index(correctLabel[i])):
                    self.nOperators.train(inputs, operatorsTargets)
                    print("Oper")
            else:
                operatorsTargets = np.zeros(len(self.operatorsLabel)) + 0.01
                operatorsTargets[len(self.operatorsLabel)-1] = 0.99
                self.nOperators.train(inputs, operatorsTargets)

                label = int(correctLabel[i])
                numbersTargets = np.zeros(len(self.numbersLabel)) + 0.01
                numbersTargets[label] = 0.99
                while(np.argmax(self.nNumbers.query(inputs)) != label):
                    self.nNumbers.train(inputs, numbersTargets)
                    print("Number")
        self.nNumbers.saveAs(SettingsController.numbersNetworkPath)
        self.nOperators.saveAs(SettingsController.operatorsNetworkPath)
