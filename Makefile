PNG = fig/person.png fig/mobile.png fig/architecture.png

.PHONY: default
default: $(PNG)

# dot to png
%.png: %.dot
	dot -T png -o $@ $<