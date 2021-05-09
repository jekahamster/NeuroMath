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


		coords = SymbolFinder.findSymbol(imgray)
		imgSymbols = []

		for c in coords:
			left_top 	 = c[0]
			right_bottom = c[1]

			n = right_bottom.y - left_top.y + 1
			m = right_bottom.x - left_top.x + 1

			side 	= max(n, m)
			shiftX	= (side - m) // 2
			shiftY 	= (side - n) // 2

			simg = np.array([[0 for i in range(side)] for j in range(side)], dtype=np.uint8)
			for y in range(left_top.y, right_bottom.y+1):
				for x in range(left_top.x, right_bottom.x+1):
					simg[y-left_top.y+shiftY][x-left_top.x+shiftX]= imgray[y][x]

			resImg = cv2.resize(simg, (28-6, 28-6))
			finalResImg = np.array([[0 for i in range(28)] for j in range(28)], dtype=np.uint8)
			for i in range(28-6):
				for j in range(28-6):
					finalResImg[i+3][j+3] = resImg[i][j]

			imgSymbols.append(finalResImg)


		for c in coords:
			cv2.rectangle(img, (c[0].x, c[0].y),
				(c[1].x, c[1].y), (0, 255, 0), 2)

		cv2.imshow("", img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		return imgSymbols

	@staticmethod
	def findSymbol(img):
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
