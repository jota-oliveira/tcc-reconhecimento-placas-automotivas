LIVRO= TCC-IFC-2015

all:	pdf

pdf:
	pdflatex $(LIVRO).tex
	bibtex $(LIVRO)
	pdflatex $(LIVRO).tex
	pdflatex $(LIVRO).tex

clean:
	rm -rf  *.aux *.soc *.toc *.lo[fpt] *.blg *.bbl \
	*.ind *.out *.ilg *.idx *.glo *.gls *.log *.$(LIVRO)
	#rm -rf *.dvi 

cleanall: clean
	rm $(LIVRO).pdf *~
