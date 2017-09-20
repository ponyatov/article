class Variable:
    def __init__(self):
        self.B = False      # unbound
        self.V = None 
    def __lshift__(self,o):
        ' unify: override << operator '
        if not self.B:
            self.V = o
            self.B = True   # bind
            yield self
            self.B = False  # unbind
        elif self.V == o:
            yield self
    def __repr__(self):
        ' override printable representation '
        if self.B:  return '<%s>'%self.V
        else:       return '?'
            
def human(V):
    for i in V << 'socrates'  : yield i
    for i in V << 'aristotle' : yield i
    for i in V << 'plato'     : yield i
    
V = Variable()
# equivalent to human(V) query
for i in human(V): print i