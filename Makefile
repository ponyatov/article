PNG = fig/person.png fig/mobile.png fig/architecture.png fig/hello.png

.PHONY: all
all: d3view.html $(PNG) overleaf/main.pdf

# dot to png
%.png: %.dot
	dot -T png -o $@ $<

.PHONY: overleaf/main.pdf
overleaf/main.pdf:
	cd overleaf ; $(MAKE)