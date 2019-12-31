from math import pi, e, sin, cos, tan, log

class Stack:
	def __init__(self):
		self.arr = []

	def __repr__(self):
		return str(self.arr)

	def __len__(self):
		return len(self.arr)

	def push(self, obj):
		self.arr.append(obj)

	def pop(self):
		return self.arr.pop()

	def peek(self):
		return self.arr[len(self.arr)-1]

	def size(self):
		return len(self.arr)

	def isEmpty(self):
		return len(self.arr) == 0

class Calculator:
	operators = {
		"+": '1',
		"-": '1',
		"/": '2',
		"*": '2',
		"%": '2',
		"**": '3'
	}

	specSym = ["(", ")", "|"]

	consts  = {
		"\u03c0": pi, 
		"e"		: e
	}

	functions = ["sin", "cos", "tan", "log"]

	specFunc  = ["!", "\u221a"]

	numStack  = Stack()
	operStack = Stack()

	def calc(self, list):
		for charSeq in list:
			print("Current: ", charSeq)
			if (charSeq.isdigit()):
				self.numStack.push(charSeq)
				print(self.numStack)
				print(self.operStack)
				print()

			elif (charSeq in self.operators.keys()):
				self.checkOper(charSeq)
				print(self.numStack)
				print(self.operStack)
				print()

			elif (charSeq in self.specSym):
				self.checkSpecSym(charSeq)
				print(self.numStack)
				print(self.operStack)
				print()

			elif (charSeq in self.consts):
				self.numStack.push(self.consts[charSeq])

			elif (charSeq in self.functions):
				self.operStack.push(charSeq)

			elif (charSeq in self.specFunc):
				self.checkSpecFunc(charSeq)


		while (not self.operStack.isEmpty()):
			tempOper = self.operStack.pop()
			tempB 	 = self.numStack.pop()
			tempA 	 = self.numStack.pop()
			self.numStack.push(eval(str(tempA) + str(tempOper) + str(tempB)))
		
		print(self.numStack)
		print(self.operStack)
		print()
		return self.numStack.peek()


	def checkOper(self, charSeq):
		if (self.operStack.isEmpty()):
			self.operStack.push(charSeq)

		elif (self.operStack.peek() in self.specSym):
			self.operStack.push(charSeq)

		elif (self.operators[self.operStack.peek()] < self.operators[charSeq]):
			self.operStack.push(charSeq)

		elif (self.operators[self.operStack.peek()] >= self.operators[charSeq]):
			tempOper = self.operStack.pop()
			tempB = self.numStack.pop()
			tempA = self.numStack.pop()
			self.numStack.push(eval(str(tempA) + str(tempOper) + str(tempB)))
			self.operStack.push(charSeq)

	def checkSpecSym(self, charSeq):
		if (charSeq == "("):
			self.operStack.push(charSeq)
		elif (charSeq == ")"):
			self.calcRoundBrackets()

	def calcRoundBrackets(self):
		tempCounter = 0
		while (self.operStack.peek() != "("):
			tempOper = self.operStack.pop()
			tempB 	 = self.numStack.pop()
			tempA	 = self.numStack.pop()
			self.numStack.push(eval(str(tempA) + str(tempOper) + str(tempB)))
			tempCounter += 1

		self.operStack.pop()


		if (tempCounter == 0):
			tempA = self.numStack.pop()
			tempFunc = self.operStack.pop()
			if (tempFunc == "log"):
				tempC = self.numStack.pop()
				self.numStack.push(eval(str(tempFunc)+"("+str(tempA)+","+tempC+")"))
			else:
				self.numStack.push(eval(str(tempFunc) + "(" + str(tempA) + ")"))


		if (tempCounter > 0 and self.operStack.peek() in self.functions):
			tempFunc = self.operStack.pop()
			if (tempFunc == "log"):
				tempA = self.numStack.pop()
				tempB = self.numStack.pop()
				self.numStack.push(eval(str(tempFunc)+"("+str(tempB)+","+tempB+")"))
			else:
				tempA = self.numStack.pop()
				self.numStack.push(eval(str(tempFunc) + "(" + str(tempA) + ")"))

	def checkSpecFunc(charSeq):
		if (charSeq == "!"):
			tempA = self.numStack.pop()
			numStack.push(eval("factorial("+str(tempA)+")"))





