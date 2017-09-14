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
    R = '// %s\n'%X
    try:
        R += 'n%s [label="%s"];\n'%(X.id,X.properties['title'])
    except KeyError:
        R += 'n%s;\n'%X.id
    return R

def Edge(Y):
    R = '// %s\n'%Y
    R += 'n%s -> n%s [ label = " %s" ];\n' % (Y.start,Y.end,Y.type)
    return R

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
