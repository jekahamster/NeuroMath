import numpy as np
import neural_network as NN

inputNodes   = 28*28
hiddenNodes  = 100
outputNodes  = 11
learningRate = 0.1
epochs 		 = 10

n = NN.NeuralNetwork()
n.init(learningRate, [inputNodes, hiddenNodes, 50, outputNodes])

# читаємо всі рядки з файлу mnist_train.csv і записуємо їх в список
dataFile = open("mnist_dataset/mnist_train.csv", "r")
dataList = dataFile.readlines()
dataFile.close()

for e in range(epochs):         # повторювати для кожної епохи
	for data in dataList:       # повторювати для кожного рядка зі списку
        # розбиваємо рядок на числа
        allValues  	= data.split(",")
        # масштабуємо результати в межі від 0.01 до 1
        # ігноруємо перше значення, оскільки це результуюче значення
		inputs 		= (np.asfarray(allValues[1:]) / 255 * 0.99) + 0.01
        # створюємо масив очікуваних вихідних значень, де
        # очікуваний результат - 0.99, а всі інші - 0.01
		targets 	= np.zeros(outputNodes) + 0.1
		targets[int(allValues[0])] = 0.99
        # запускаємо метод навчання
		n.train(inputs, targets)


# читаємо всі рядки з файлу mnist_test.csv і записуємо їх в список
trainFile = open("mnist_dataset/mnist_test.csv", "r")
trainList = trainFile.readlines()
trainFile.close()

# список для відповідей мережі
scorecard = []
for train in trainList:         # повторювати для кожного рядка
    # розбиваємо рядок на числа
	allValues 	   = train.split(",")
    # масштабуємо результати в межі від 0.01 до 1
    # ігноруємо перше значення, оскільки це результуюче значення
	inputs         = (np.asfarray(allValues[1:]) / 255 * 0.99) + 0.01
    # визначаємо бажаний результат
	correctLabel   = int(allValues[0])
    # робимо запит і зберігаємо відповідь у вигляді списку, де
    # бажаний результат має найбільше значення
	outputs = n.query(inputs)
	label = np.argmax(outputs)
    # порівнюємо правильну відповідь з результатом мережі, записуємо в список
	scorecard.append(correctLabel == label)

print("Report: ", scorecard)           # друкуємо на екран весь список
print("Total:", len(scorecard))        # друкуємо на екран кількість тестів
print("Correct:", sum(scorecard))      # друкуємо на екран кількість правильних
print(sum(scorecard) / len(scorecard)) # друкуємо на екран відсоток правильних

# запитуємо у користувача дозвіл на збереження
if (input("Save model(y/n)? ") == "y"):
    # у разі позитивної відповіді, зберігаємо з урахуванням відсотку
    # правильних відповідей
	n.saveAs(input("File name: "), sum(scorecard)/len(scorecard))
