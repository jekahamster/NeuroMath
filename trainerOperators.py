import numpy as np
import neural_network as NN
import random
import cv2


class pair:
    a = None
    b = None
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "({0} ; {1})".format(self.a, self.b)

data = [
    pair('trainOperators/abs/abs1.png', '|'),
    pair('trainOperators/abs/abs2.png', '|'),
    pair('trainOperators/abs/abs3.png', '|'),
    pair('trainOperators/abs/abs4.png', '|'),
    pair('trainOperators/abs/abs5.png', '|'),

    pair('trainOperators/div/div1.png', '/'),
    pair('trainOperators/div/div2.png', '/'),
    pair('trainOperators/div/div3.png', '/'),
    pair('trainOperators/div/div4.png', '/'),
    pair('trainOperators/div/div5.png', '/'),
    pair('trainOperators/div/div6.png', '/'),
    pair('trainOperators/div/div7.png', '/'),

    pair('trainOperators/dot/dot1.png', '.'),
    pair('trainOperators/dot/dot2.png', '.'),
    pair('trainOperators/dot/dot3.png', '.'),
    pair('trainOperators/dot/dot4.png', '.'),

    pair('trainOperators/eight/eight1.png', ''),
    pair('trainOperators/eight/eight2.png', ''),

    pair('trainOperators/equal/equal1.png', '='),
    pair('trainOperators/equal/equal2.png', '='),

    pair('trainOperators/factorial/factorial1.png', '!'),
    pair('trainOperators/factorial/factorial2.png', '!'),
    pair('trainOperators/factorial/factorial3.png', '!'),

    pair('trainOperators/five/five1.png', ''),
    pair('trainOperators/five/five2.png', ''),

    pair('trainOperators/four/four1.png', ''),
    pair('trainOperators/four/four2.png', ''),
    pair('trainOperators/four/four3.png', ''),

    pair('trainOperators/lbrecket/lbrecket1.png', '('),
    pair('trainOperators/lbrecket/lbrecket2.png', '('),
    pair('trainOperators/lbrecket/lbrecket3.png', '('),
    pair('trainOperators/lbrecket/lbrecket4.png', '('),
    pair('trainOperators/lbrecket/lbrecket5.png', '('),

    pair('trainOperators/minus/minus1.png', '-'),
    pair('trainOperators/minus/minus2.png', '-'),
    pair('trainOperators/minus/minus3.png', '-'),
    pair('trainOperators/minus/minus4.png', '-'),
    pair('trainOperators/minus/minus5.png', '-'),
    pair('trainOperators/minus/minus6.png', '-'),
    pair('trainOperators/minus/minus7.png', '-'),
    pair('trainOperators/minus/minus8.png', '-'),

    pair('trainOperators/more/more1.png', '>'),
    pair('trainOperators/more/more2.png', '>'),
    pair('trainOperators/more/more3.png', '>'),

    pair('trainOperators/mult/mult1.png', '*'),
    pair('trainOperators/mult/mult2.png', '*'),
    pair('trainOperators/mult/mult3.png', '*'),
    pair('trainOperators/mult/mult4.png', '*'),
    pair('trainOperators/mult/mult5.png', '*'),
    pair('trainOperators/mult/mult6.png', '*'),
    pair('trainOperators/mult/mult7.png', '*'),

    pair('trainOperators/nine/nine1.png', ''),

    pair('trainOperators/one/one1.png', ''),
    pair('trainOperators/one/one2.png', ''),

    pair('trainOperators/percent/percent1.png', ''),
    pair('trainOperators/percent/percent2.png', ''),
    pair('trainOperators/percent/percent3.png', ''),
    pair('trainOperators/percent/percent4.png', ''),
    pair('trainOperators/percent/percent5.png', ''),
    pair('trainOperators/percent/percent6.png', ''),
    pair('trainOperators/percent/percent7.png', ''),
    pair('trainOperators/percent/percent8.png', ''),
    pair('trainOperators/percent/percent9.png', ''),
    pair('trainOperators/percent/percent10.png', ''),

    pair('trainOperators/pi/pi1.png', 'π'),
    pair('trainOperators/pi/pi2.png', 'π'),
    pair('trainOperators/pi/pi3.png', 'π'),
    pair('trainOperators/pi/pi4.png', 'π'),
    pair('trainOperators/pi/pi5.png', 'π'),
    pair('trainOperators/pi/pi6.png', 'π'),
    pair('trainOperators/pi/pi7.png', 'π'),
    pair('trainOperators/pi/pi8.png', 'π'),
    pair('trainOperators/pi/pi9.png', 'π'),
    pair('trainOperators/pi/pi10.png', 'π'),

    pair('trainOperators/plus/plus1.png', '+'),
    pair('trainOperators/plus/plus2.png', '+'),
    pair('trainOperators/plus/plus3.png', '+'),
    pair('trainOperators/plus/plus4.png', '+'),
    pair('trainOperators/plus/plus5.png', '+'),
    pair('trainOperators/plus/plus6.png', '+'),
    pair('trainOperators/plus/plus7.png', '+'),

    pair('trainOperators/pow/pow1.png', '^'),
    pair('trainOperators/pow/pow2.png', '^'),
    pair('trainOperators/pow/pow3.png', '^'),
    pair('trainOperators/pow/pow4.png', '^'),
    pair('trainOperators/pow/pow5.png', '^'),

    pair('trainOperators/rbrecket/rbrecket1.png', ')'),
    pair('trainOperators/rbrecket/rbrecket2.png', ')'),
    pair('trainOperators/rbrecket/rbrecket3.png', ')'),
    pair('trainOperators/rbrecket/rbrecket4.png', ')'),

    pair('trainOperators/seven/seven1.png', ''),

    pair('trainOperators/six/six1.png', ''),

    pair('trainOperators/smaller/smaller1.png', '<'),
    pair('trainOperators/smaller/smaller2.png', '<'),
    pair('trainOperators/smaller/smaller3.png', '<'),

    pair('trainOperators/sqrt/sqrt1.png', '√'),
    pair('trainOperators/sqrt/sqrt2.png', '√'),
    pair('trainOperators/sqrt/sqrt3.png', '√'),
    pair('trainOperators/sqrt/sqrt4.png', '√'),
    pair('trainOperators/sqrt/sqrt5.png', '√'),
    pair('trainOperators/sqrt/sqrt6.png', '√'),
    pair('trainOperators/sqrt/sqrt7.png', '√'),
    pair('trainOperators/sqrt/sqrt8.png', '√'),
    pair('trainOperators/sqrt/sqrt9.png', '√'),
    pair('trainOperators/sqrt/sqrt10.png', '√'),

    pair('trainOperators/three/three1.png', ''),
    pair('trainOperators/three/three2.png', ''),
    pair('trainOperators/three/three3.png', ''),

    pair('trainOperators/two/two1.png', ''),
    pair('trainOperators/two/two2.png', ''),

    pair('trainOperators/zero/zero1.png', ''),
]

random.shuffle(data)

labels = ["+", "-", "/", "*", "^", "(", ")", "<", ">", "=", "!",
          ".", "π", "%", "√", "|", ""]

inputNodes   = 28*28
hiddenNodes  = 100
outputNodes  = len(labels)
learningRate = 0.1
epochs 		 = 5

n = NN.NeuralNetwork()
n.init(learningRate, [inputNodes, 50, outputNodes])

for e in range(epochs):
    print("Epoch #", e+1)
    for p in data:
        img = cv2.imread(p.a)
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inputs = (np.asfarray(imgray.flatten()) / 255 * 0.99) + 0.01
        targets = np.zeros(outputNodes) + 0.1
        targets[labels.index(p.b)] = 0.99
        n.train(inputs, targets)


scorecard = []
for p in data:
    correctLabel = labels.index(p.b)
    print("Corret label is", correctLabel)
    img = cv2.imread(p.a)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inputs = (np.asfarray(imgray.flatten()) / 255 * 0.99) + 0.01
    outputs = n.query(inputs)
    label = np.argmax(outputs)
    print("Network respone is", label)
    print()
    scorecard.append(correctLabel == label)

print("Report: ", scorecard)
print("Total:", len(scorecard))
print("Correct:", sum(scorecard))
print(sum(scorecard) / len(scorecard))


if (input("Save model(y/n)? ") == "y"):
	n.saveAs(input("File name: "), sum(scorecard)/len(scorecard))
