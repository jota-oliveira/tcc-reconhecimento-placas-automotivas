#exemplo

from commands import *

def leitura_ocr(arquivo):
	return (commands.getoutput("gocr -i "+arquivo))
