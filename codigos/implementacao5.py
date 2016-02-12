import commands

def tratamento(img):
	texto1 = commands.getoutput("ocrad erosion.pgm")	
	texto2 = commands.getoutput("ocrad dilate.pgm")
	texto3 = commands.getoutput("gocr erosion.png")	
	texto4 = commands.getoutput("gocr dilate.png")		
	texto5 = commands.getoutput("ocrad preto_branco.pgm")
	texto6 = commands.getoutput("gocr preto_branco.png")
	saidas = [texto1, texto2, texto3, texto4, texto5, texto6]
	return saidas