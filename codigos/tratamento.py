#!/usr/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def tratamento_img(img):

	kernel = np.ones((7,4),np.uint8)

	img = cv2.imread(img,0)

	ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
	titles = ['BINARY']
	images = [thresh1]
	img = plt.imshow(images[0],'gray')
	plt.xticks([]),plt.yticks([])
	plt.savefig("pretobranco", dpi=100)
	#plt.show()

	img = cv2.imread("binaria.png",0)

	dilate = cv2.dilate(img,kernel,iterations = 1)
	cv2.imwrite('dilate.png',dilate)

	img = cv2.imread("dilate.png",0)

	erosion = cv2.erode(img,kernel,iterations = 1)
	cv2.imwrite('erosion.png',erosion)
	
	img = "dilate.png"
	
	os.system("convert erosion.png erosion.pgm")
	os.system("convert dilate.png dilate.pgm")
	
	k = cv2.waitKey(0)
	
	return True
	
if __name__ == '__main__':
	tratamento_img('../imagens/15.jpg')
