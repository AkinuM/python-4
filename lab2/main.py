import inspect
import math


import serializer

u = 0


def qwe(i):
    y = i + 1
    i = u
    qwe(i)
    return y


class Rewq:
    p = 0


if __name__ == '__main__':
    def tr():
        return


    a = bytes(5)
    d = "{'type': 'int', 'value': 5}"
    f = 5.4
    g = {4, 5, 6}
    b = (5, 7)
    j = None
    c = {"2": 4, "3": "5"}
    # print(str(type(qwe))[8:len(str(type(qwe))) - 2])
    # print(str(inspect.getmembers(qwe)))
    aboba = serializer.serialize(c)
    h = serializer.deserialize(aboba)
    print(h)
    for i in inspect.getmembers(qwe):
        if i[0] == "__code__":
            print(i[1].__getattribute__("co_names"))
    print(qwe.__getattribute__("__globals__"))
    print(str(math))
    #d = dict((m, n) for m, n in d)
    #print(d)
    # print(i[1].__getattribute__("co_names") for i in inspect.getmembers(qwe) if i[0] == "__code__")
