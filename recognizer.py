import numpy as np
import neural_network as NN
from settings_controller import SettingsController
SettingsController.loadFrom(SettingsController.DEFAULT_PATH)

class Recognizer():
    operatorsLabel  = SettingsController.operatorLabels
    numbersLabel    = SettingsController.numberLabels
    lettersLabel    = SettingsController.lettersLabels

    def __init__(self):
        self.nNumbers   = NN.NeuralNetwork()
        self.nOperators = NN.NeuralNetwork()
        self.nLetters   = NN.NeuralNetwork()
        self.nNumbers.loadFrom(SettingsController.numbersNetworkPath)
        self.nOperators.loadFrom(SettingsController.operatorsNetworkPath)
        self.nLetters.loadFrom(SettingsController.lettersNetworkPath)

    def recognize(self, imgList):
        result = []

        for img in imgList:
            img = np.ravel(img)
            inputs = (np.asfarray(img) / 255 * 0.98) + 0.01

            output = self.nOperators.query(inputs)
            if self.operatorsLabel[np.argmax(output)] == "":
                output = self.nNumbers.query(inputs)
                if self.numbersLabel[np.argmax(output)] == "":
                    output = self.nLetters.query(inputs)
                    result.append(self.lettersLabel[np.argmax(output)])
                else:
                    result.append(self.numbersLabel[np.argmax(output)])
            else:
                result.append(self.operatorsLabel[np.argmax(output)])

        return result

    def adjust(self, imgList, correctLabel):
        print(correctLabel[:len(imgList)])
        while (self.recognize(imgList) != correctLabel[:len(imgList)]):
            for i in range(len(imgList)):
                print(correctLabel[i])
                img = np.ravel(imgList[i])
                inputs = (np.asfarray(img) / 255 * 0.98) + 0.01

                if correctLabel[i] in self.operatorsLabel:
                    numberLabel = len(self.numbersLabel)-1
                    numbersTargets = np.zeros(len(self.numbersLabel)) + 0.01
                    numbersTargets[numberLabel] = 0.99
                    while (np.argmax(self.nNumbers.query(inputs)) != numberLabel):
                        self.nNumbers.train(inputs, numbersTargets)
                        print("Number -> Oper")

                    letterLabel = len(self.lettersLabel)-1
                    lettersTargets = np.zeros(len(self.lettersLabel)) + 0.01
                    lettersTargets[letterLabel] = 0.99
                    while (np.argmax(self.nLetters.query(inputs)) != letterLabel):
                        self.nLetters.train(inputs, lettersTargets)
                        print("Letter -> Oper")

                    operatorsTargets = np.zeros(len(self.operatorsLabel)) + 0.01
                    operatorsTargets[self.operatorsLabel.index(correctLabel[i])] = 0.99
                    if (SettingsController.adjustAll):
                        self.nOperators.train(inputs, operatorsTargets)
                        print("Oper")
                    else:
                        while(np.argmax(self.nOperators.query(inputs)) != self.operatorsLabel.index(correctLabel[i])):
                            self.nOperators.train(inputs, operatorsTargets)
                            print("Oper")

                elif correctLabel[i] in self.numbersLabel:
                    operLabel = len(self.operatorsLabel)-1
                    operatorsTargets = np.zeros(len(self.operatorsLabel)) + 0.01
                    operatorsTargets[operLabel] = 0.99
                    while (np.argmax(self.nOperators.query(inputs)) != operLabel):
                        self.nOperators.train(inputs, operatorsTargets)
                        print("Oper -> Number")

                    letterLabel = len(self.lettersLabel)-1
                    lettersTargets = np.zeros(len(self.lettersLabel)) + 0.01
                    lettersTargets[letterLabel] = 0.99
                    while (np.argmax(self.nLetters.query(inputs)) != letterLabel):
                        self.nLetters.train(inputs, lettersTargets)
                        print("Letter -> Number")

                    label = int(correctLabel[i])
                    numbersTargets = np.zeros(len(self.numbersLabel)) + 0.01
                    numbersTargets[label] = 0.99
                    if (SettingsController.adjustAll):
                        self.nNumbers.train(inputs, numbersTargets)
                        print("Number")
                    else:
                        while(np.argmax(self.nNumbers.query(inputs)) != label):
                            self.nNumbers.train(inputs, numbersTargets)
                            print("Number")

                else:
                    operLabel = len(self.operatorsLabel)-1
                    operatorsTargets = np.zeros(len(self.operatorsLabel)) + 0.01
                    operatorsTargets[operLabel] = 0.99
                    while (np.argmax(self.nOperators.query(inputs)) != operLabel):
                        self.nOperators.train(inputs, operatorsTargets)
                        print("Oper -> Letter")

                    numberLabel = len(self.numbersLabel)-1
                    numbersTargets = np.zeros(len(self.numbersLabel)) + 0.01
                    numbersTargets[numberLabel] = 0.99
                    while (np.argmax(self.nNumbers.query(inputs)) != numberLabel):
                        self.nNumbers.train(inputs, numbersTargets)
                        print("Number -> Letter")

                    label = self.lettersLabel.index(correctLabel[i])
                    lettersTargets = np.zeros(len(self.lettersLabel)) + 0.01
                    lettersTargets[label] = 0.99
                    if (SettingsController.adjustAll):
                        self.nLetters.train(inputs, lettersTargets)
                        print("Letter")
                    else:
                        while(np.argmax(self.nLetters.query(inputs)) != label):
                            self.nLetters.train(inputs, lettersTargets)
                            print("Letter")
        print("Save networks settings")
        self.nNumbers.saveAs(SettingsController.numbersNetworkPath)
        self.nOperators.saveAs(SettingsController.operatorsNetworkPath)
        self.nLetters.saveAs(SettingsController.lettersNetworkPath)
