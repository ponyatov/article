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

PNG = tmp/architecture.png tmp/hello.png tmp/mobile.png 
PNG += tmp/person1.png tmp/person2.png tmp/socrat.pdf

FIG = $(PNG)

SRC = src/hello.c src/socrat.pl

# dot to png
tmp/%.png: fig/%.dot
	dot -T png -o $@ $<
tmp/%.pdf: fig/%.dot
	dot -T pdf -o $@ $<

.PHONY: all
all: d3view.html $(PNG) tmp/article.pdf

LATEX = pdflatex -halt-on-error --output-directory=tmp
tmp/article.pdf: $(TEX) $(FIG) $(SRC) Makefile
	$(LATEX) $< && $(LATEX) $<
