
.PHONY: all
all: d3view.html fig/person.png

# dot to png
%.png: %.dot
	dot -T png -o $@ $<
	
# JavaScript libs 
NEO	= neo4j-web.min.js
D3	= d3.v3.min.js

# JavaScript/D3 database visualizer
d3view.html: lib/$(NEO) lib/$(D3)

# JavaScript libs download
lib/$(NEO):
	wget -O $@ -c https://raw.githubusercontent.com/neo4j/neo4j-javascript-driver/1.5/lib/browser/$(NEO)
lib/$(D3):
	wget -O $@ -c http://d3js.org/$(D3)
