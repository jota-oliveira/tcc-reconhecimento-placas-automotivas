#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands

def limpeza_letras(texto):		
	for i in texto:
		if i not in["A","B","8","C","D","E","F","G","H","I","1","J","K","L","M","N","O","0","P","Q","R","S","T","U","V","W","X","Y","Z"]:
			texto = texto.replace(i,"")
		if i == "8":
			texto = texto.replace(i,"B")
		if i == "0":
			texto = texto.replace(i,"O")
		if i == "1":
			texto = texto.replace(i,"I")
	if len(texto) < 3:
		return False
	return texto[:3]

def limpeza_numeros(img):

	for i in texto:
		if i not in["0","1","2","3","4","5","6","b","7","8","B","9","l","L","i","I"]:
			texto = texto.replace(i,"")
		if i in ["l","L","i","I","t"]:
			texto = texto.replace(i,"1")	
		if i in ["b"]:
			texto = texto.replace(i,"6")
		if i in ["B"]:
			texto = texto.replace(i,"8")
			
	if len(texto) < 4:
			return False
	return texto[(len(texto)-4):len(texto)]
	
def saidas():
	texto1 = commands.getoutput("ocrad erosion.pgm")	
	texto2 = commands.getoutput("ocrad dilate.pgm")
	texto3 = commands.getoutput("gocr erosion.png")	
	texto4 = commands.getoutput("gocr dilate.png")		
	texto5 = commands.getoutput("ocrad preto_branco.pgm")
	texto6 = commands.getoutput("gocr preto_branco.png")
	saidas = [texto1, texto2, texto3, texto4, texto5, texto6]
	return saidas

def compara_saidas():
	lista_saidas = saidas()
	lista_comparacao = []
	for texto in lista_saidas():
		lista_comparacao.append(limpeza_letras(texto))
		lista_comparacao.append(limpeza_numeros(texto))
	return lista_comparacao
