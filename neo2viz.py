# GraphViz plot extractor for
# neo4j db (compliant to graph driven programming concept)

USER = 'guest'
PASS = 'b.WRXe9aw0I4qh.TNa5DzL4hwBDvRRl'

import os,sys#,re

dot = open(sys.argv[0]+'.dot','w')

print sys.argv

### access to db over BOLT (first script parameter)
 
try:
    BOLT = sys.argv[1]
except IndexError:
    # demo Planning @ graphene.db
    BOLT = 'bolt://hobby-ncooindboeaggbkehmhbdnpl.dbs.graphenedb.com:24786'

### Cypher Query (second parameter)

try:                    # command line / Makefile use
    CQL = sys.argv[2]
except IndexError:      # special case for script debug from IDE      
    CQL = 'match (x)-[y]->(z) return x,y,z'

print 'CQL',CQL

print >>dot,'\ndigraph {\nrankdir=LR;\n'

from neo4j.v1 import GraphDatabase, basic_auth

def Node(X):
    try: label = 'label="%s"'%X.properties['title']
    except KeyError: label=''
    try: shape = ',shape=%s'%X.properties['shape']
    except KeyError: shape=''
    try: color = ',style=filled,fillcolor=%s'%X.properties['fillcolor']
    except KeyError: color=''
    try: fontcolor = ',fontcolor=%s'%X.properties['fontcolor']
    except KeyError: fontcolor=''
    return '// %s\nn%s [%s%s%s%s];\n'%(X,X.id,label,shape,color,fontcolor)

def Edge(Y):
    try: label = 'label=" %s"'%Y.type
    except KeyError: label=''
    try: color = ',color=%s'%Y.properties['color']
    except KeyError: color=''
    try: fontcolor = ',fontcolor=%s'%Y.properties['fontcolor']
    except KeyError: fontcolor=''
    return '// %s\nn%s -> n%s [%s%s%s];'%(Y,Y.start,Y.end,label,color,fontcolor)

with GraphDatabase.driver(BOLT, auth=basic_auth(USER, PASS)) as driver:
    print 'driver',driver
    with driver.session() as session:
        print 'session',session
        for i in session.run(CQL):
            X=i['x'] ; print >>dot,Node(X)
            Z=i['z'] ; print >>dot,Node(Z)
            Y=i['y'] ; print >>dot,Edge(Y)
        session.close()
    driver.close()

print >>dot,'\n}\n'
