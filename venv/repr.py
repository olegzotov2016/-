class adder:
    def __init__(self,value=0):
        self.data=value
    def __add__(self, other):
        self.data+=other
class addrepr(adder):
    def __repr__(self):
        return 'addrepr(%s)'%self.data

class addstr(adder):
    def __str__(self):
        return '[Value: %s]' % self.data
