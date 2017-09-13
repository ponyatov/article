PNG = fig/person.png fig/mobile.png fig/architecture.png fig/hello.png

.PHONY: all
all: d3view.html $(PNG)

# dot to png
%.png: %.dot
	dot -T png -o $@ $<