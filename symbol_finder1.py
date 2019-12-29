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
		imgSectors = SymbolFinder.findSectors(imgray)
		imgNumbers = []
		for imgSector in imgSectors:
			imgNumbers.append(SymbolFinder.findRecursive(imgSector))

		return imgNumbers

	@staticmethod
	def findSectors(imgray):
		coords = SymbolFinder.findSectorCoords(imgray)
		imgSymbols = []

		for c in coords:
			left_top 	 = c[0]
			right_bottom = c[1]

			n = right_bottom.y - left_top.y + 1
			m = right_bottom.x - left_top.x + 1

			side 	= max(n, m)
			shiftX	= (side - m) // 2
			shiftY 	= (side - n) // 2

			simg = np.array([[0 for i in range(side+2)] for j in range(side+2)], dtype=np.uint8)
			for y in range(left_top.y-1, right_bottom.y+2):
				for x in range(left_top.x-1, right_bottom.x+2):
					simg[y-left_top.y+shiftY][x-left_top.x+shiftX]= imgray[y][x]

			imgSymbols.append(simg)


		# for c in coords:
			# cv2.rectangle(img, (c[0].x, c[0].y),
				# (c[1].x, c[1].y), (0, 255, 0), 2)

		# cv2.imshow("", img)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()
		return imgSymbols

	@staticmethod
	def findSectorCoords(img):
		partCoords = SymbolFinder.takeAPart(img)

		coords = []

		for partCoord in partCoords:
			coords.append( SymbolFinder.findEdges(img, partCoord[0].x, partCoord[0].y,
				partCoord[1].x, partCoord[1].y) )

		return coords # [Pair<int, int>, Pair<int, int>]

	@staticmethod
	def takeAPart(img):
		coords = []

		ys = SymbolFinder.findY(img)

		for i in range(0, len(ys), 2):
			xs = SymbolFinder.findX(img, ys[i], ys[i+1])
			for j in range(0, len(xs), 2):
				coords.append( [Pair(xs[j], ys[i]), Pair(xs[j+1], ys[i+1])] )


		return coords  # [Pair<int, int>, Pair<int, int>]

	@staticmethod
	def findEdges(img, x1, y1, x2, y2):
		left_top = Pair(99999, 99999)
		right_bottom = Pair(0, 0)

		for y in range(y1, y2+1):
			for x in range(x1, x2+1):
				if (img[y][x] > 0) and (y < left_top.y):
					left_top.y = y
				if (img[y][x] > 0) and (y > right_bottom.y):
					right_bottom.y = y

				if (img[y][x] > 0) and (x < left_top.x):
					left_top.x = x
				if (img[y][x] > 0) and (x > right_bottom.x):
					right_bottom.x = x

		return [left_top, right_bottom] # [Pairt<int, int>, Pair<int, int>]


	@staticmethod
	def findY(img):
		coords = []

		prevIsWhite = False
		for y in range(len(img)):
			isWhite = False
			for x in range(len(img[0])):
				if (img[y][x] > 0):
					isWhite = True
					break
			if (prevIsWhite != isWhite):
				coords.append(y)
			prevIsWhite = isWhite

		return coords # [int]


	@staticmethod
	def findX(img, y1, y2):
		coords = []

		prevIsWhite = False
		for x in range(len(img[0])):
			isWhite = False
			for y in range(y1, y2+1):
				if (img[y][x] > 0):
					isWhite = True
					break
			if (prevIsWhite != isWhite):
				coords.append(x)
			prevIsWhite = isWhite

		return coords # [int]

	def findRecursive(imgray):
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
			# img = cv2.rectangle(img,(left_top.x, left_top.y),
				# (right_bottom.x, right_bottom.y), (0, 255, 0), 2)
		# cv2.imshow("", img)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()
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
