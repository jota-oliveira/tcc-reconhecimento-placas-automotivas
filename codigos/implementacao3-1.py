#exemplo

def limpeza_letras(texto):
		
	for i in texto:
		if i not in["A","B","8","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
			texto = texto.replace(i,"")
	return texto
