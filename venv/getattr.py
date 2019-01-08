class empty:
    def __getattr__(self,attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)
class accesscontrol:
    def __setattr__(self,attr,value):
        if attr=='age':
            self.__dict__[attr]=value
        else:
            raise AttributeError(attr)