import cv2
import numpy as np

class Pair:
	x = 0
	y = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "({0} ; {1})".format(self.x, self.y)

class SymbolFinder:

	@staticmethod
	def find(imgPath):
		img = cv2.imread(imgPath)
		imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		symbolCoordinates = SymbolFinder.findSymbol(imgray)
		imgSymbols = []
		for sc in symbolCoordinates:
			left_top 	 = sc["left_top"]
			right_bottom = sc["right_bottom"]
			coordinates  = sc["coordinates"]

			n = right_bottom.y - left_top.y 	+1
			m = right_bottom.x - left_top.x 	+1

			side 	= max(n, m)
			shiftX	= (side - m) // 2
			shiftY 	= (side - n) // 2

			simg = np.array([[0 for i in range(side)] for j in range(side)], dtype=np.uint8)
			for i in coordinates:
				simg[i.y-left_top.y+shiftY][i.x-left_top.x+shiftX]= 255

			resImg = cv2.resize(simg, (28-6, 28-6))
			finalResImg = np.array([[0 for i in range(28)] for j in range(28)], dtype=np.uint8)
			for i in range(28-6):
				for j in range(28-6):
					finalResImg[i+3][j+3] = resImg[i][j]

			imgSymbols.append(finalResImg)
			img = cv2.rectangle(img,(left_top.x, left_top.y),
				(right_bottom.x, right_bottom.y), (0, 255, 0), 2)
		cv2.imshow("", img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		return imgSymbols

	@staticmethod
	def findSymbol(matrix):
		n = len(matrix)
		m = len(matrix[0])
		out = []

		visited = np.array([[0 for i in range(m)] for j in range(n)], dtype=np.uint8)

		for x in range(m):
			for y in range(n):
				if (matrix[y][x] > 0) and (visited[y][x] == 0):
					out.append(SymbolFinder.trav(x, y, matrix, visited))

		return out

	@staticmethod
	def trav(x, y, data, visited):
		stack = [Pair(x, y)]
		group = set()
		group.add(Pair(x, y))


		left_top = Pair(999999, 999999)
		right_bottom = Pair(0, 0)

		while(len(stack) > 0):
			x = stack[len(stack)-1].x
			y = stack[len(stack)-1].y

			if (x < left_top.x):
				left_top.x = x
			elif (x > right_bottom.x):
				right_bottom.x = x

			if (y < left_top.y):
				left_top.y = y
			elif (y > right_bottom.y):
				right_bottom.y = y

			if (data[y-1][x] > 0) and (visited[y-1][x] == 0):
				stack.append(Pair(x, y-1))
				visited[y-1][x] = 1
				group.add(Pair(x, y-1))

			elif (data[y][x+1] > 0) and (visited[y][x+1] == 0):
				stack.append(Pair(x+1, y))
				visited[y][x+1] = 1
				group.add(Pair(x+1, y))

			elif (data[y+1][x] > 0) and (visited[y+1][x] == 0):
				stack.append(Pair(x, y+1))
				visited[y+1][x] = 1
				group.add(Pair(x, y+1))

			elif (data[y][x-1] > 0) and (visited[y][x-1] == 0):
				stack.append(Pair(x-1, y))
				visited[y][x-1] = 1
				group.add(Pair(x-1, y))

			elif (data[y-1][x-1] > 0) and (visited[y-1][x-1] == 0):
				stack.append(Pair(x-1, y-1))
				visited[y-1][x-1] = 1
				group.add(Pair(x-1, y-1))

			elif (data[y-1][x+1] > 0) and (visited[y-1][x+1] == 0):
				stack.append(Pair(x+1, y-1))
				visited[y-1][x+1] = 1
				group.add(Pair(x+1, y-1))

			elif (data[y+1][x+1] > 0) and (visited[y+1][x+1] == 0):
				stack.append(Pair(x+1, y+1))
				visited[y+1][x+1] = 1
				group.add(Pair(x+1, y+1))

			elif (data[y+1][x-1] > 0) and (visited[y+1][x-1] == 0):
				stack.append(Pair(x-1, y+1))
				visited[y+1][x-1] = 1
				group.add(Pair(x-1, y+1))

			else:
				stack.pop()

		return {"coordinates": group, "left_top": left_top, "right_bottom": right_bottom}
