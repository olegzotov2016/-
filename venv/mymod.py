def countLines(name):
    print(len(name))
def countChars(name):
    s=0
    for l in name:
        s+=len(l)
    print(s)

def test(name):
    txt=open(name).readlines()
    countLines(txt)
    countChars(txt)
if __name__=='__main__':
    op=str(input('Введите имя файла '))
    test(op)
