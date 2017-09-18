TEX = article.tex header.tex intro.tex 
TEX += model.tex neo4j.tex samplemain.tex
TEX += inference.tex yield.tex rewrite.tex
TEX += hyper.tex 
TEX += comp.tex
TEX += autogen.tex
TEX += expert.tex
TEX += plan.tex
TEX += doc.tex
TEX += dos.tex
TEX += plc.tex
TEX += ack.tex bib.tex

PNG = fig/architecture.png fig/hello.png fig/mobile.png 
PNG += fig/person1.png fig/person2.png

FIG = $(PNG)

SRC = src/hello.c

# dot to png
%.png: %.dot
	dot -T png -o $@ $<

.PHONY: all
all: d3view.html $(PNG) article.pdf

LATEX = pdflatex -halt-on-error --output-directory=tmp
tmp/article.pdf: $(TEX) $(FIG) $(SRC) Makefile
	$(LATEX) $< && $(LATEX) $<
