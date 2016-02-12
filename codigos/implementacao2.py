def tratamento(img):
	#removendo ruídos e salvando
	remocao_ruidos.remover(img)
	cv2.imread('remocao.png', remocao_ruidos)
	#lendo remoção
	img = cv2.imread('remocao.png',0)
	img = cv2.medianBlur(img,5)
	#aplicando limiarização sobre a imagem sem ruídos
	ret,thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	cv2.imwrite("limiar.png",thresh1)
	#salvando a imagem limiarizada
	
	#lendo a imagem limiarizada
	img = cv2.imread("limiar.png",0)	
	#dilatando imagem limiarizada
	dilate = cv2.dilate(img,np.ones((3,3),np.uint8),iterations = 1)
	#salvando imagem dilatada
	cv2.imwrite('dilato.png',dilate)
	#abrindo imagem dilatada
	img = cv2.imread("dilatado.png", 0)
	#erodindo imagem dilatada
	erosion = cv2.erode(img, np.ones((7,7),np.uint8), iterations = 1)
	#salvando imagem erodida
	cv2.imwrite('erodido.png',erosion)
	#conversões para formatos do OCRAD
	os.system("convert erosion.png erosion.pgm")
	os.system("convert dilate.png dilate.pgm")
	os.system("convert preto_branco.png preto_branco.pgm")

	return True