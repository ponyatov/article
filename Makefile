
.PHONY: all
all: fig/person.png fig/mobile.png fig/architecture.png

# dot to png
%.png: %.dot
	dot -T png -o $@ $<