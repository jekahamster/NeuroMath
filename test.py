import cv2
import numpy as np
import random


array = np.array([[0 for i in range(28+9)] for j in range(28+9)], dtype=np.uint8)
print(array)

cv2.imshow("", array)
cv2.waitKey(0)
