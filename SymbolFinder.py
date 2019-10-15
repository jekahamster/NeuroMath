import cv2
import numpy as np


class SymbolFinder():
    def find(self, imgPath):
        img = cv2.imread(imgPath)
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height, width = img.shape[:2]

        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        x,y,w,h = cv2.boundingRect(cnt)
        cropImg = img[y:y+h, x:x+w]


        tempCoordsX = [x]
        white = True
        for i in range(x, x+w):
            for j in range(y, y+h):
                if imgray[j][i] > 0:
                    white = True
                    break
            else:
                if white == True:
                    tempCoordsX.append(i)
                    white = False
        tempCoordsX.append(x+w)

        coordinates = []
        imgSymbol = []
        for k in range(len(tempCoordsX)-1):
            tempImg = imgray[y:y+h, tempCoordsX[k]:tempCoordsX[k+1]]
            tempRet, tempThresh = cv2.threshold(tempImg, 127, 255, 0)
            tempContours = cv2.findContours(tempThresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            tempCnt = tempContours[0]
            rectCoords = list(cv2.boundingRect(tempCnt))
            rectCoords[0] += tempCoordsX[k]
            rectCoords[1] += y



            coordinates.append(rectCoords)
            tempSymbol = imgray[rectCoords[1]:rectCoords[1]+rectCoords[3],
                        rectCoords[0]:rectCoords[0]+rectCoords[2]]
            # tempImg = cv2.cvtColor(tempImg, cv2.COLOR_GRAY2BGR)


            tempWl = abs(rectCoords[0] - (rectCoords[0] + rectCoords[2]))
            tempHl = abs(rectCoords[1] - (rectCoords[1] + rectCoords[3]))

            maxL = max(tempHl, tempWl)
            correctX = (maxL - tempWl) // 2
            correctY = (maxL - tempHl) // 2

            temp = [np.zeros(maxL, dtype=np.uint8) for i in range(maxL)]
            temp_arr = np.array(temp, dtype=np.uint8)

            for i in range(tempHl):
                for j in range(tempWl):
                    temp_arr[i+correctY][j+correctX] = tempSymbol[i][j]

            resImg = cv2.resize(temp_arr, (28-6, 28-6))
            finalResImg = np.array([[0 for i in range(28)] for j in range(28)], dtype=np.uint8)
            for i in range(28-6):
                for j in range(28-6):
                    finalResImg[i+3][j+3] = resImg[i][j]

            imgSymbol.append(finalResImg)
            # newResImg = tempResImg.resize(tempResImg, (28, 28))
            img = cv2.rectangle(img,(rectCoords[0],rectCoords[1]),
            (rectCoords[0]+rectCoords[2],rectCoords[1]+rectCoords[3]),(0,255,0),2)
            # cv2.imwrite("temp/t"+str(k)+".png", finalResImg)


        # cv2.imwrite("temp/temp_img2.png", cropImg)
        cv2.imshow("", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return imgSymbol





# img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # img = cv2.resize(img, (28, 28))


# tempWl = abs(rectCoords[0] - (rectCoords[0] + rectCoords[2]))
# tempHl = abs(rectCoords[1] - (rectCoords[1] + rectCoords[3]))
#
# maxL = max(tempHl, tempWl)
# correctX = (maxL - tempWl) // 2
# correctY = (maxL - tempHl) // 2
# print(tempWl)
# print(tempHl)
# print(correctX)
# print(correctY)
# rectCoords[0] -= correctX
# rectCoords[2] += 2*correctX
# rectCoords[1] -= correctY
# rectCoords[3] += 2*correctY


#
# resImg = cv2.resize(tempSymbol, (28, 28))
# cv2.imshow("1", resImg)
# print("asd")
# tempResImg = np.array([[0 for i in range(28+9)] for j in range(28+9)], dtype=np.uint8)
# for i in range(28):
#     for j in range(28):
#         tempResImg[i+3][j+3] = resImg[i][j]
