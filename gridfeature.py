from PIL import Image
from skimage.morphology import thin, skeletonize
import matplotlib.pyplot as plt
import cv2
from numpy import *
import numpy as np
import scipy.ndimage
import math
img1 = cv2.imread('1.bmp', 0)
ret, th1 = cv2.threshold(img1, 240, 255, cv2.THRESH_BINARY)
imgbw = ~th1
imgbw2 = imgbw/255
skeli = skeletonize(imgbw2)
skeli = skeli.astype(np.uint8)

sq_num = 8
numrows = len(skeli)
sq_amount = numrows / sq_num
itemindexrow1, itemindexcolumn1 = np.where(skeli == 1)
sq_x = ceil(itemindexrow1 / sq_amount)
sq_y = ceil(itemindexcolumn1 / sq_amount)
number_of_square = (sq_x-1) * sq_num + sq_y
grid = []
for i in range(sq_num**2):
    tempx = np.where(number_of_square == i)
    print(tempx)
    grid.append(len(tempx))

numOnepixel = np.sum(grid)

