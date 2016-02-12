import cv2 #Importando o OpenCV
import numpy as np #Importando bibliotecas necessárias do Python

img = cv2.imread('j.png',0) #Leitura da imagem. 0 representa leitura em escala da cinza
kernel = np.ones((5,5),np.uint8) #definindo kernel
erosion = cv2.erosion(img,kernel,iterations = 1) #Erodindo
