from cv2 import GaussianBlur, cv2, getVersionMajor
import numpy as np
valorGauss = 3
valorKernel = 3
original=cv2.imread('triangle.png')
grises=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(grises, (valorGauss, valorGauss),0)
canny = cv2.Canny(gauss,60, 100)
kernel = np.ones((valorKernel,valorGauss),np.uint8)
cierre= cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
contorno, hehe = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("monedas encontradas: {}".format(len(contorno)))
cv2.drawContours(original, contorno, -1, (0,0,255),2)
cv2.imshow('image1',grises)
cv2.imshow('image2',gauss)
cv2.imshow('image3',canny)
cv2.imshow('image4',original)
cv2.waitKey(0) 