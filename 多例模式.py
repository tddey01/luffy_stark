#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

class Foo(object):
    pass

# 实例化了一个Foo类的对象(实例)

obj1 = Foo()
print(obj1)  # <__main__.Foo object at 0x10dd6ee10>
obj1.name = 'kn'

# 实例化了一个Foo类的对象(实例)
obj2 = Foo()
print(obj2) # <__main__.Foo object at 0x10dd6ef50>
# print(obj2.name)

