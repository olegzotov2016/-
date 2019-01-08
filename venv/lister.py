class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


class ListerInstance:
    """
    Примесный класс, реализующий получение форматированной строки при вызове
    функции print() и str() с экхемпляром в виде аргумента, через наследование
    метода __str__, реализованного здесь; отображает только атрибуты
    экземпляра; self - экземпляр самого нижнего класса в дереве наследования;
    во избежание конфликтов с именами атрибутов клиентских классов использует
    имена вида __x
    """

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>'%(
            self.__class__.__name__,
            id(self),
            self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result
