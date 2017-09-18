class Variable:
    def __lshift__(self,o):
        ' override << operator '
        self.V = o ; return self
    def __repr__(self):
        ' override printable representation '
        return '<%s>'%self.V

def human(V):
    yield V << 'socrates'
    yield V << "Chelsea"
    yield V << "Hillary"
    yield V << "Bill"
    
V = Variable()
# equivalent to human(V) query
for i in human(V): print V