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
				responseRight = self.calc(node.right)
				if (node == "!"):
					return eval("factorial(" + str(responseRight) + ")")

			elif (node.type == "specSym"):
				if (node.data == "||"):
					responseRight = self.calc(node.right)
					return eval("abs("+str(responseRight)+")")

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

	def __round__(self, n=0):
		return round(float(self.data), n)

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
		return Calculator.isNumber(self.data)

class Pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def __repr__(self):
		return "P({0} ; {1})".format(self.first, self.second)

	def __eq__(self, other):
		return (self.first == other.first) and (self.second == other.second)

class TextFormatter:
	replacement = {
        "=="    : ["="],
        "<="    : ["<=="],
        ">="    : [">=="],
        "sin"   : ['5in'],
        "cos"   : ['c05', 'co5', 'c0s'],
        "lg"    : ['e9', 'eg', 'l9'],
        "ln"    : ['en'],
        "log"   : ['e09', 'l09', 'l0g', 'lo9', 'eo9', 'eog', 'e0g'],
    }

	@staticmethod
	def format(str):
		expression = [[]]
		specSym = []
		prev = ""
		brackets = Stack() 		# "usr" / "sys"
		
		for i in TextFormatter.replacement.keys():
			for j in TextFormatter.replacement[i]:
				str = str.replace(j, i)


		i = 0
		for char in str:
			print("Current:", char)
			print(brackets)
			print(expression)
			print()
			if (Calculator.isNumber(char) or char == ".") and (Calculator.isNumber(prev) or prev == "."):
				expression[i][len(expression[i])-1] += char
			elif char.isalpha() and prev.isalpha():
				expression[i][len(expression[i])-1] += char

			elif char in ["=", "<", ">"] and prev in ["=", "<", ">"]:
				specSym[len(specSym)-1] += char

			elif char in ["=", "<", ">"]:
				while (len(brackets) != 0):
					expression[i] += list(brackets.pop().first)
				prev = char
				i += 1
				expression.append([])
				specSym.append(char)

			else:
				if (char == "^"):
					expression[i].append("**")
					expression[i].append("(")
					brackets.push(Pair(")", "sys"))

				elif (char == "("):
					brackets.push(Pair(")", "usr"))
					expression[i].append(char)

				elif (char == ")"):
					brackets.pop()
					expression[i].append(char)

				elif (char == "|"):
					if (brackets.has(Pair("|", "usr"))):
						while (brackets.peek().first != "|"):
							expression[i] += list(brackets.pop().first)
						brackets.pop()
					else:
						brackets.push(Pair("|", "usr"))
					expression[i].append(char)

				elif (char in list(Calculator.CLASSES["operator"].keys())+Calculator.CLASSES["specSym"]):
					if (len(brackets) == 0) or (brackets.peek().second == "usr"):
						if (char == "-") and ((prev in ["(", "-", "+", "/", "*", "%", "^", "=", "<", ">"]) or (prev == "")):
							expression[i] += ["(", "0","-", "1", ")", "*"]

						elif (char == "-") and (prev == "|") and (brackets.peek().first == "|"):
							expression[i] += ["(", "0","-", "1", ")", "*"]

						else:
							expression[i].append(char)

					elif (len(brackets) != 0) and (brackets.peek().second == "sys"):
						if (char == "-") and ((prev in ["(", "-", "+", "/", "*", "%", "^", "=", "<", ">"]) or (prev == "")):
							expression[i] += ["(", "0","-", "1", ")", "*"]

						else:
							expression[i] += list(brackets.pop().first)
							expression[i].append(char)

					else:
						print("!!!!")

				else:
					if (char == "\u221a"):
						expression[i].append("(")
						brackets.push(Pair([")", "**", "0.5"], "sys"))
					else:
						expression[i].append(char)

				
			prev = char

		while (len(brackets) != 0):
			expression[i] += list(brackets.pop().first)

		print("STOP")

		res = {
			"expression": expression,
			"specSym"	: specSym
		}
		return res

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

	DEFAULT		= 1
	EQUALITY	= 2
	INEQUALITY	= 3

	def __init__(self):
		self.nodeStack = Stack()
		self.operStack = Stack()

	def calc(self, strExpr):
		if Calculator.isNumber(strExpr):
			return None, Calculator.DEFAULT
		obj = TextFormatter.format(strExpr)
		res = []
		print(obj)
		for expr in obj["expression"]:
			print("Expr", expr)
			print()
			print()
			res.append(self.getRes(expr))
		if len(obj["specSym"]) == 0:
			return res[0], Calculator.EQUALITY
		else:
			boolList = []
			for i in range(len(obj["specSym"])):
				boolList.append(eval( str(res[i])+str(obj["specSym"][i])+str(res[i+1]) ))
			return sum(boolList) == len(boolList), Calculator.INEQUALITY



	def getRes(self, list):
		print("For Excpression", list)
		for charSeq in list:
			print("Current: ", charSeq)
			if (Calculator.isNumber(charSeq)):
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
				print(self.nodeStack)
				print(self.operStack)
				print()
				self.checkSpecSym(charSeq)
				print(self.nodeStack)
				print(self.operStack)
				print()

			elif (charSeq in self.CLASSES["const"]):
				self.nodeStack.push(Node(self.CLASSES["const"][charSeq], "number"))
				self.checkSpecSym(charSeq)
				print(self.nodeStack)
				print(self.operStack)
				print()

			elif (charSeq in self.CLASSES["function"].keys()):
				self.operStack.push(Node(charSeq, "function"))
				self.checkSpecSym(charSeq)
				print(self.nodeStack)
				print(self.operStack)
				print()

			elif (charSeq in self.CLASSES["specFunc"]):
				self.checkSpecFunc(charSeq)
				# self.checkSpecSym(charSeq)
				print(self.nodeStack)
				print(self.operStack)
				print()

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

		tree = Tree(self.nodeStack.pop())
		print("Tree:", end=" ")
		tree.inOrder(tree.root)
		print("Res:", round(tree.calc(tree.root), 10))
		return round(tree.calc(tree.root), 10)

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

	@staticmethod
	def isNumber(number):
		try:
			float(number)
			return True
		except ValueError:
			return False
