#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import remocao_ruidos
from PIL import Image
from pylab import *
import comparador


def conversoes_leitura():
	#converte para extensão lida através do OCRAD
	os.system("convert erosion.png erosion.pgm")
	os.system("convert dilate.png dilate.pgm")
	os.system("convert preto_branco.png preto_branco.pgm")
	
def erode_dil(img):
	erosion = cv2.erode(img,np.ones((7,7),np.uint8),iterations = 1)
	cv2.imwrite('erosion.png',erosion)
	return cv2.imread("erosion.png", 0)

def dilata_limi(img):
	dilate = cv2.dilate(img,np.ones((3,3),np.uint8),iterations = 1)
	cv2.imwrite('dilate.png',dilate)
	return cv2.imread("dilate.png", 0)

def limiariza_img(img):
	img = cv2.medianBlur(img,5)
	ret,thresh1 = cv2.threshold(img,0,255,cv2.THRESH_TRUNC | cv2.THRESH_OTSU)
	ret,thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	cv2.imwrite("preto_branco.png",thresh1)
	return cv2.imread("preto_branco.png")
	
def tratamento_letras(img):
	#prepara para remoção de ruídos
	im = array(Image.open(img).convert('L'))
	#aplica remoção de ruídos
	rm_ruidos, trash = remocao_ruidos.rr(im,im)
	#deixa a imagem sem ruídos em escala de cinza
	gray()
	#retira pontos cartesianos da imagem em si
	axis('off')
	
	limiarizacao = limiariza_img(rm_ruidos)
	dilatacao = dilata_limi(limiarizacao)
	erosao = erode_dil(dilatacao)
	return True
		
if __name__ == '__main__': 
	tratamento_letras('example_file.jpg')
	conversoes_leitura()
	print comparador.compara_saidas()
