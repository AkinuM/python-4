import inspect
import math

from parsers.src import serialize_functions
from parsers.src.serialize_functions import deserialize_function, deserialize, deserialize_object, serialize_object, \
    serialize

import serializer

u = 0


def qwe(i = 1):
    y = i + 1
    i = u
    return y


class Rewq:
    p = 0

    def __init__(self, age=3):
        self.age = age

    def rew(self):
        p = 2
        return p


class r:

    def __init__(self, age = 3):
        self.person = Rewq(age)

    def get_age(self):
        return self.person.age

if __name__ == '__main__':
    def tr(a, b):
        return b * a


    a = bytes(5)
    d = "{'type': 'int', 'value': 5}"
    f = 5.4
    g = {4, 5, 6}
    b = (5, 7)
    j = None
    c = {"a": 4, "b": "b"}
    #fsds = deserialize(serialize(qwe))
    print(tr(**c))

    # print(str(type(qwe))[8:len(str(type(qwe))) - 2])
    # print(str(inspect.getmembers(qwe)))
    aboba = serializer.serialize(r)
    #aboba2 = serialize_functions.serialize(qwe)
    k = qwe
    #aboba3 = serializer.deserialize(aboba)
    #h = serialize_functions.deserialize(aboba2)
    #chel1 = aboba3(5)
    chel2 = Rewq(5)
    #print(serializer.serialize(chel2))
    chel4 = deserialize(serialize(chel2))
    chel3 = serializer.deserialize(serializer.serialize(chel2))
    # print(type(chel2))
    # print(str(chel1.__dict__))
    print(chel3.age)# == chel2.get_age())
    # print(qwe(f))
    #print(aboba3(f))
    # for i in inspect.getmembers(qwe):
    #     if i[0] == "__code__":
    #         print(i[1].__getattribute__("co_names"))
    # print(qwe.__getattribute__("__globals__"))
    # print(str(math))
    #d = dict((m, n) for m, n in d)
    #print(d)
    # print(i[1].__getattribute__("co_names") for i in inspect.getmembers(qwe) if i[0] == "__code__")