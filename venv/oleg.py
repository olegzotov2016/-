class Printer:
    def __init__(self, val):
        self.val=val
    def __repr__(self):
        return str(self.val)
objs=[Printer(2),Printer(3)]
for x in objs: print(x)
print(objs)
class Computer:
    def __init__(self,val):
        self.val=val
    def __add__(self, other):
        if isinstance(other,Computer):other=other.val
        return Computer(self.val+other)
    def __radd__(self, other):
        print('radd', self.val, other)
        return Computer(other + self.val)
    def __str__(self):
        return '<Computer: %s>' % self.val
x=Computer(88)
y=Computer(99)

class Number:
    def __init__(self,val):
        self.val=val
    def __add__(self, other):
        return Number(self.val+other)
class Callee:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)

class Life:
    def __init__(self,name='unknown'):
        print('hello',name)
        self.name=name
    def __del__(self):
        print('GoodBye', self.name)
