# GraphViz plot extractor for
# neo4j db (compliant to graph driven programming concept)

import os,sys#,re

print sys.argv

try:                    # command line / Makefile use
    CQL = sys.argv[1]
except IndexError:      # special case for script debug from IDE      
    CQL = 'return 1'

print CQL

print '\ndigraph {\n'

from neo4j.v1 import GraphDatabase, basic_auth



print '\n}\n'
