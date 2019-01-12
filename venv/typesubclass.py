class Mylist(list):

    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self,offset))
        return list.__getitem__(self,offset-1)


if __name__=='__main__':
    print(list('abc'))
    x= Mylist('abc')
    print(x)
    print(x[1])
    print(x[2])
    x.append('spam'); print(x)
    x.reverse(); print(x)