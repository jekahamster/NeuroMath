from math import factorial, pi, e, sin, cos, tan, log

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

	def has(self, obj):
		return obj in self.arr

	def isEmpty(self):
		return len(self.arr) == 0

class Tree:
	def __init__(self, root = None):
		self.root = root

	def preOrder(self, node):
		if (node != None):
			print(node, end=" ")
			self.preOrder(node.left)
			self.preOrder(node.right)

	def inOrder(self, node):
		if (node != None):
			self.inOrder(node.left)
			print(node, end=" ")
			self.inOrder(node.right)

	def postOrder(self, node):
		if (node != None):
			self.postOrder(node.left)
			self.postOrder(node.right)
			print(node, end=" ")

	def calc(self, node):
		if (node != None):
			if (node.isNumber()):
				return node

			elif (node.type == "operator"):
				responseLeft  = self.calc(node.left)
				responseRight = self.calc(node.right)
				return eval(str(responseLeft) + str(node.getData()) + str(responseRight))

			elif (node.type == "function"):
				tempR = self.calc(node.right)
				if (Calculator.CLASSES["function"][node.getData()] == 2):
					tempL = self.calc(node.left)
					return eval(str(node)+"("+str(tempR)+","+str(tempL)+")")
				return eval(str(node)+"("+str(tempR)+")")

			elif (node.type == "specFunc"):
				if (node == "!"):
					node.setData("factorial")
				
				responseRight = self.calc(node.right)
				return eval(str(node) + "(" + str(responseRight) + ")")

			elif (node.type == "specSym"):
				if (node.data == "||"):
					node.setData("abs")
					responseRight = self.calc(node.right)
					return eval(str(node)+"("+str(responseRight)+")")

class Node:
	def __init__(self, data = None, type = None):
		self.left = None
		self.right = None
		self.data = data
		self.type = type

	def __repr__(self):
		return str(self.data)

	def __str__(self):
		return str(self.data)

	def __eq__(self, other):
		return self.data == other

	def getData(self):
		return self.data

	def getType(self):
		return self.type

	def setLeft(self, leftNode):
		self.left = leftNode

	def setRight(self, rightNode):
		self.right = rightNode

	def setData(self, newData):
		self.data = newData

	def isNumber(self):
		return self.data.isdigit()

class Calculator:

	CLASSES = {
		"operator": {
				"+"	: '1',
				"-"	: '1',
				"/"	: '2',
				"*"	: '2',
				"%"	: '2',
				"**": '3'
			},
		"specSym": ["(", ")", "|"],
		"const" : {
				"\u03c0": pi, 
				"e"		: e
			},
		"function": {
				"sin": 1, 
				"cos": 1, 
				"tan": 1, 
				"log": 2
			},
		"specFunc": ["!", "\u221a"]
	}

	nodeStack = Stack()
	operStack = Stack()

	def calc(self, list):
		for charSeq in list:
			print("Current: ", charSeq)
			if (charSeq.isdigit()):
				self.nodeStack.push( Node(charSeq, "number") )
				print(self.nodeStack)
				print(self.operStack)
				print()

			elif (charSeq in self.CLASSES["operator"].keys()):
				self.checkOper(charSeq)
				print(self.nodeStack)
				print(self.operStack)
				print()

			elif (charSeq in self.CLASSES["specSym"]):
				self.checkSpecSym(charSeq)
				print(self.nodeStack)
				print(self.operStack)
				print()

			elif (charSeq in self.CLASSES["const"]):
				self.nodeStack.push(Node(self.CLASSES["const"][charSeq], "number"))

			elif (charSeq in self.CLASSES["function"].keys()):
				self.operStack.push(Node(charSeq, "function"))

			elif (charSeq in self.CLASSES["specFunc"]):
				self.checkSpecFunc(charSeq)

		while (not self.operStack.isEmpty()):
			tempOper = self.operStack.pop()
			tempB 	 = self.nodeStack.pop()
			tempA 	 = self.nodeStack.pop()
			tempOper.setLeft(tempA)
			tempOper.setRight(tempB)
			self.nodeStack.push(tempOper)

		print(self.nodeStack)
		print(self.operStack)
		print()

		tree = Tree(self.nodeStack.peek())
		return tree.calc(tree.root)

	def checkOper(self, charSeq):
		if (self.operStack.isEmpty()):
			self.operStack.push( Node(charSeq, "operator") )

		elif (self.operStack.peek() in self.CLASSES["specSym"]):
			self.operStack.push( Node(charSeq, "operator") )

		elif (self.CLASSES["operator"][self.operStack.peek().getData()] < self.CLASSES["operator"][charSeq]):
			self.operStack.push( Node(charSeq, "operator") )

		elif (self.CLASSES["operator"][self.operStack.peek().getData()] >= self.CLASSES["operator"][charSeq]):
			tempOper = self.operStack.pop()
			tempB 	 = self.nodeStack.pop()
			tempA 	 = self.nodeStack.pop()
			tempOper.setLeft(tempA)
			tempOper.setRight(tempB)
			self.nodeStack.push( tempOper )
			self.operStack.push( Node(charSeq, "operator") )

	def checkSpecSym(self, charSeq):
		if (charSeq == "("):
			self.operStack.push( Node(charSeq, "specSym") )
		elif (charSeq == ")"):
			self.calcRoundBrackets()
		elif (charSeq == "|"):
			self.calcAbs()

	def calcRoundBrackets(self):
		while (self.operStack.peek() != "("):
			tempOper = self.operStack.pop()
			tempB 	 = self.nodeStack.pop()
			tempA	 = self.nodeStack.pop()
			tempOper.setLeft(tempA)
			tempOper.setRight(tempB)
			self.nodeStack.push(tempOper)

		self.operStack.pop()
		if (not self.operStack.isEmpty()):
			self.checkFunc()

	def calcAbs(self):
		if (self.operStack.has("|")):
			while (self.operStack.peek() != "|"):
				tempOper = self.operStack.pop()
				tempB = self.nodeStack.pop()
				tempA = None
				if (self.nodeStack.peek() == "|"):
					tempA = Node("0", "number")
				else:
					tempA = self.nodeStack.pop()

				tempOper.setLeft(tempA)
				tempOper.setRight(tempB)
				self.nodeStack.push(tempOper)

			temp = self.nodeStack.pop()
			self.nodeStack.pop()
			self.nodeStack.push(temp)
			self.operStack.pop()

			tempA = self.nodeStack.pop()
			newNode = Node("||", "specSym")
			newNode.setRight(tempA)
			self.nodeStack.push(newNode)
		else:
			self.operStack.push(Node("|", "specSym"))
			self.nodeStack.push(Node("|", "specSym"))

	def checkFunc(self):
		if (self.operStack.peek().getData() not in self.CLASSES["function"]):
			return;

		tempFunc = self.operStack.pop()
		tempA = self.nodeStack.pop()
		if (self.CLASSES["function"][tempFunc.getData()] == 2):
			tempB = self.nodeStack.pop()
			tempFunc.setLeft(tempB)
		tempFunc.setRight( tempA )
		self.nodeStack.push( tempFunc )


	def checkSpecFunc(self, charSeq):
		if (charSeq == "!"):
			tempA 	= self.nodeStack.pop()
			newNode = Node(charSeq, "specFunc")
			newNode.setRight(tempA)
			self.nodeStack.push(newNode)

